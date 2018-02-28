

'''
Kiran: 2/25/2018

Data:

movies.dat
MovieID::Title::Genres

users.dat
UserID::Gender::Age::Occupation::Zip-code

ratings.dat
UserID::MovieID::Rating::Timestamp

#/home/kiran/km/km_hadoop/data/ml-1m

spark submit in local (AND use py3.5 because 3.6 gives error with Spark<=2.1.0):
source activate py35
spark-submit --master local ~/km/km_py/uc_spark_moviedb_analysis.py
deactivate


'''

#import pandas as pd

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType

#def main():
    #using Spark session (in spark-submit only)
spark = SparkSession.builder \
    .master("local") \
    .appName("MovieDB Analysis") \
    .getOrCreate()


#1

#storesDF = spark.read.option("header","true").csv("/home/kiran/km/km_hadoop/data/data_rtl_stores.csv")

#spark.read.format('json').load('python/test_support/sql/people.json')

#dfMovies = spark.read.format("csv").option("delimiter", "::").load("/home/kiran/km/km_hadoop/data/ml-1m/movies.dat")
#=>Gives error pyspark.sql.utils.IllegalArgumentException: 'Delimiter cannot be more than one character: ::'

dfMovies = spark.sparkContext.textFile("/home/kiran/km/km_hadoop/data/ml-1m/movies.dat").map(lambda x: x.split("::")).toDF(["MovieID", "Title", "Genres"])
dfMovies.show(20, False)
dfMovies.dtypes
dfMovies.count() #EXPENSIVE FOR HUGE DATASET
#=>3883

dfRatings = spark.sparkContext.textFile("/home/kiran/km/km_hadoop/data/ml-1m/ratings.dat").map(lambda x: x.split("::")).toDF(["UserID", "MovieID", "Rating", "Timestamp"])
dfRatings.show()
dfRatings.dtypes
dfRatings.count() #EXPENSIVE FOR HUGE DATASET
#=>1000209

dfUsers = spark.sparkContext.textFile("/home/kiran/km/km_hadoop/data/ml-1m/users.dat").map(lambda x: x.split("::")).toDF(["UserID", "Gender", "Age", "Occupation", "Zip-code"])
dfUsers.show()
dfUsers.dtypes
dfUsers.count() #EXPENSIVE FOR HUGE DATASET
#=>6040


#2

dfRatingsUsers = dfRatings.join(dfUsers, ["UserID"])
#OR: dfRatingsUsers = dfRatings.join(dfUsers, dfUsers.UserID==dfRatings.UserID) #This creates duplicate key columns (UserID)
dfRatingsUsers.show(20, False)
dfRatingsUsers.count()
#=>1000209

dfRatingsUsers = dfUsers.join(dfRatings, ["UserID"])
dfRatingsUsers.show(20, False)
dfRatingsUsers.count()
#=>1000209

dfRatingsUsersMovies = dfRatingsUsers.join(dfMovies, ["MovieID"])
dfRatingsUsersMovies.show(20, False)
dfRatingsUsersMovies.count()
#=>1000209

dfRatingsUsersMovies.cache()

#3
from pyspark.sql.functions import col

dfRatingsUsersMoviesMale = dfRatingsUsersMovies.filter(col("Gender")=="M").groupBy('MovieID').count().withColumnRenamed('count', 'Male')
dfRatingsUsersMoviesMale.show(10)
#=>3671

dfRatingsUsersMoviesFemale = dfRatingsUsersMovies.filter(col("Gender")=="F").groupBy('MovieID').count().withColumnRenamed('count', 'Female')
dfRatingsUsersMoviesFemale.show(10)
#=> 3481

dfRatingsUsersMoviesAllMale = dfMovies.select('MovieID').join(dfRatingsUsersMoviesMale, ["MovieID"], 'outer')
#Male didnt give ratings
dfRatingsUsersMoviesAllMale.where(col("Male").isNull()).count()
#=>212

dfRatingsUsersMoviesAllMF = dfRatingsUsersMoviesAllMale.join(dfRatingsUsersMoviesFemale, ["MovieID"], 'outer')
dfRatingsUsersMoviesAllMF.where(col("Female").isNull()).count()
#=>402

dfRatingsUsersMoviesAllMF.where(col("Female").isNull() | col("Male").isNull()).count()
#=>437

#Movies with no reviews
dfRatingsUsersMoviesAllMF.where(col("Female").isNull() & col("Male").isNull()).show(5)
dfRatingsUsersMoviesAllMF.where(col("Female").isNull() & col("Male").isNull()).count()
#=>177



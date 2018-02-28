

'''
Kiran: 2/25/2017

Data:

movies.dat
MovieID::Title::Genres

users.dat
UserID::Gender::Age::Occupation::Zip-code

ratings.dat
UserID::MovieID::Rating::Timestamp

#/home/kiran/km/km_hadoop/data/ml-1m
'''

import pandas as pd

#1
#dfMovies = pd.read_csv("C:\\Users\\kiran\\Downloads\\assignment\\ml-1m\\movies.dat",
dfMovies = pd.read_csv("/home/kiran/km/km_hadoop/data/ml-1m/movies.dat",
                       header = None, delimiter="::", names=["MovieID", "Title", "Genres"])
#dfMovies.dtypes

#dfRatings = pd.read_csv("C:\\Users\\kiran\\Downloads\\assignment\\ml-1m\\ratings.dat",
dfRatings = pd.read_csv("/home/kiran/km/km_hadoop/data/ml-1m/ratings.dat",
                        header = None, delimiter="::", names=["UserID", "MovieID", "Rating", "Timestamp"])

#dfUsers = pd.read_csv("C:\\Users\\kiran\\Downloads\\assignment\\ml-1m\\users.dat",
dfUsers = pd.read_csv("/home/kiran/km/km_hadoop/data/ml-1m/users.dat",
    header = None, delimiter="::", names=["UserID", "Gender", "Age", "Occupation", "Zip-code"])


#2
dfRatingsUsers = dfRatings.merge(dfUsers)
dfRatingsUsersMovies = dfRatingsUsers.merge(dfMovies)


#3
#mvRatingPivot = dfRatingsUsersMovies.groupby(['MovieID'])['UserID'].count()

from pandas import pivot_table
mvRatingPivot = pd.pivot_table(dfRatingsUsersMovies[['MovieID', 'UserID']],  index='MovieID', values='UserID', aggfunc="count").rename(columns={'UserID': 'total_reviews'})

mvRatingPivot[mvRatingPivot['total_reviews'] >= 250]

#4
dfRatingsUsersMovies[dfRatingsUsersMovies['Gender'] == "F"]

mvRatingPivotFem = pd.pivot_table(dfRatingsUsersMovies.loc[dfRatingsUsersMovies['Gender'] == "F", ['MovieID', 'UserID']], index='MovieID', values='UserID', aggfunc="count").rename(columns={'UserID': 'total_reviews_f'})

mvRatingPivotFem.sort(['total_reviews'], ascending=[1, 0]).head(10)



#5
#Male total reviews
mvRatingPivotMale = pd.pivot_table(dfRatingsUsersMovies.loc[dfRatingsUsersMovies['Gender'] == "M", ['MovieID', 'UserID']], index='MovieID', values='UserID', aggfunc="count").rename(columns={'UserID': 'total_reviews_m'})
mvRatingPivotMale.reset_index()
mvRatingPivotMaleFemale = mvRatingPivotMale.merge(mvRatingPivotFem)
mvRatingPivotMaleFemale = mvRatingPivotMale.set_index('MovieID').join(mvRatingPivotFem.set_index('MovieID')).reset_index()


mvRatingPivotFm = pd.pivot_table(dfRatingsUsersMovies.loc[dfRatingsUsersMovies['Gender'] == "F", ['MovieID', 'UserID']], index='MovieID', values='UserID', aggfunc="mean").rename(columns={'UserID': 'total_reviews_f'})
mvRatingPivotMale = pd.pivot_table(dfRatingsUsersMovies.loc[dfRatingsUsersMovies['Gender'] == "M", ['MovieID', 'UserID']], index='MovieID', values='UserID', aggfunc="mean").rename(columns={'UserID': 'total_reviews_m'})




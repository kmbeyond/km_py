


spark.createDataFrame([("a", 10), ("b", 10), ("c", 7), ("d", 16)]) \
 .toDF("id", "rec_count") \
 .show(200, False)
 

spark.createDataFrame([("111")], StringType()) \
  .toDF("id").show()


---------------------insert in Hive table --------------
from pyspark.sql.types import IntegerType, StringType
import pyspark.sql.functions as F
from datetime import datetime, date

#Ext table
create external table vivid.test_ext (id STRING) LOCATION '/vivid/common/test_ext';
spark.createDataFrame([("111")], StringType()).write.insertInto("{}.test_ext".format(sDBName), overwrite=True)


#partitioned table
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

create external table vivid.test_ext_prtn (id STRING) PARTITIONED BY (extract_date string) LOCATION '/vivid/common/test_ext_prtn';

#df.write.mode("overwrite") :-> is not working
spark.createDataFrame([("2020030202")], StringType()) \
 .withColumn("extract_date", F.lit('2020-03-02')) \
 .write.insertInto("{}.test_ext_prtn".format(sDBName), overwrite=True)


spark.createDataFrame([("2020030301")], StringType()) \
 .withColumn("extract_date", F.lit(datetime.today().strftime('%Y-%m-%d'))) \
 .write.insertInto("{}.test_ext_prtn".format(sDBName), overwrite=True)




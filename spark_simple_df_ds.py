


spark.createDataFrame([("a", 10), ("b", 10), ("c", 7), ("d", 16)]) \
 .toDF("id", "rec_count") \
 .show(200, False)
 
 
 
 

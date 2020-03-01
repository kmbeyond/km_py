
import pyspark.sql.functions as F

sDBName="pdw"
mx_ext_mrch=spark.table("{}.mrch_mast_bin".format(sDBpdw)).select("extract_date") \
 .filter(f.col("extract_date")==(date.today()-timedelta(36)).strftime('%Y-%m-%d') ) \
 .agg(F.max("extract_date")) \
 .collect()[0][0]
 
 
 
 

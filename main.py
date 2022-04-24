from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FHIR conversoin").getOrCreate()

df = spark.read.json("./data")

df.show(10)

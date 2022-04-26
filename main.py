from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, from_json
from pyspark.sql.types import ArrayType, StringType, StructField, StructType

spark = SparkSession.builder.appName("FHIR conversoin").getOrCreate()

data = spark.read.option("multiline", "true").json("./data").rdd

mappedLines = data.map(lambda x: x.asDict())

entryLines = mappedLines.map(lambda x: x["entry"])

flattendEntries = entryLines.flatMap(lambda x: x)

requiredData = flattendEntries.map(lambda x: (x["fullUrl"], x["resource"]["id"]))

requiredData.saveAsTextFile("./output")

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FHIR conversoin").getOrCreate()

data = spark.read.option("multiline", "true").json("./data").rdd

mappedLines = data.map(lambda x: x.asDict())

entryLines = mappedLines.map(lambda x: x["entry"])

flattendEntries = entryLines.flatMap(lambda x: x)

requiredData = flattendEntries.map(lambda x: (x["fullUrl"], x["resource"]["id"]))

requiredData.saveAsTextFile("./output")

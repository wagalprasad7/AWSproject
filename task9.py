df = spark.read.text("s3://wagal/bigdata/sportify.txt")
df.show()
df.head(10)

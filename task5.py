df =spark.read.text("s3://wagal/bigdata/shakespeare.txt")
df.head(10)
df.show()
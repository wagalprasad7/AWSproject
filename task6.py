from pyspark.sql import functions as F
df =spark.read.text("s3://wagal/bigdata/shakespeare.txt")
textLowerDf = df.select(F.lower(F.col("value")).alias("words_lower"))
textSplitDf = textLowerDf.select(F.split(F.col("words_lower"), " ").alias("words_split"))
textExplodedDf = textSplitDf.select(F.explode(F.col("words_split")).alias("word"))
textExplodedDf = textExplodedDf.where(F.ltrim(F.col("word")) != "")
textExplodedDf = textExplodedDf.select(F.regexp_extract(F.col("word"), "[a-z]+", 0).alias("word"))
textWordCounts = textExplodedDf.groupBy("word").count().orderBy(F.col("count").desc())
textWordCounts.show()

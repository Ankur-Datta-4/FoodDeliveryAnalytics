from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, count

# Create a Spark session
spark = SparkSession.builder.appName("OrderTracker").getOrCreate()

# Define the schema for the Kafka messages
schema = "orderId STRING, status STRING, hotelId INT, hotelName STRING, customerId STRING"

# Read from the Kafka topic
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ORDER_UPDATE") \
    .load()

# Parse the message value as a JSON string
df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data"))

# Group by status and count the number of orders for each status
agg_df = df.groupBy("data.status") \
    .agg(count("*").alias("count"))

# Start the query
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Wait for the query to finish
query.awaitTermination()

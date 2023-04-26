from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, count

# import os
# os.environ["HADOOP_HOME"] = "C:/hadoop"
# os.environ["HADOOP_HOME_BIN"] = os.path.join(os.environ["HADOOP_HOME"], "bin")
# Create a Spark session
# spark = SparkSession.builder.appName("OrderTracker").getOrCreate()


scala_version = "2.12"
spark_version = "3.4.0"
# TODO: Ensure match above values match the correct versions
packages = [
    f"org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}",
    "org.apache.kafka:kafka-clients:3.4.0",
]

# spark = (
#     SparkSession.builder.master("local")
#     .appName("kafka")
#     .config("spark.jars.packages", ",".join(packages))
#     .getOrCreate()
# )


spark = (
    SparkSession.builder.master("local")
    .appName("kafka")
    .config("spark.jars", "/home/pes1ug20cs537/Downloads/postgresql-42.6.0.jar")  # Replace x.y.z with the actual version number
    .config("spark.jars.packages", ",".join(packages))
    .config('spark.local.dir', '/home/tmp')
    .getOrCreate()
)

# spark.conf.set("spark.local.dir", "C:/Users/DARSHAN NA/AppData/Local/Temp")
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


# from pyspark.sql import SparkSession
# from pyspark.sql.functions import (
#     col, from_json, window, count, sum, desc, when, lit, approx_count_distinct
# )

# # Rest of the initial script
# # ...

# # Define the JSON schema for your data
# json_schema = (
#     StructType([
#         StructField("eventType", StringType(), True),
#         StructField("orderId", StringType(), True),
#         StructField("createdAt", TimestampType(), True),
#         StructField("netPrice", FloatType(), True),
#         StructField("category", StringType(), True),
#         StructField("hotelId", IntegerType(), True),
#         StructField("hotelName", StringType(), True),
#         StructField("orderStatus", StringType(), True),
#     ])
# )

# # Deserialize the Kafka value column
# kafka_df = kafka_df.select(from_json(col("value").cast("string"), json_schema).alias("data")).select("data.*")

# # Filter order received events for hotels
# order_received = kafka_df.filter(col("eventType") == "order_received")

# # Compute pending orders per hotel
# pending_orders = order_received.groupBy("hotelId").agg(count("orderId").alias("pending_orders"))

# # Compute top-selling items today
# top_selling_today = (
#     order_received.groupBy("category")
#     .agg(sum("netPrice").alias("total_sales"))
#     .sort(desc("total_sales"))
# )

# # Compute top-selling items in a 60-second window
# top_selling_60_sec = (
#     order_received.groupBy(window("createdAt", "60 seconds"), "category")
#     .agg(sum("netPrice").alias("total_sales"))
#     .sort(desc("total_sales"))
# )

# # Write the computed DataFrames to the console
# pending_orders_query = (
#     pending_orders.writeStream.outputMode("complete")
#     .format("console")
#     .trigger(processingTime="1 minute")
#     .start()
# )

# top_selling_today_query = (
#     top_selling_today.writeStream.outputMode("complete")
#     .format("console")
#     .trigger(processingTime="1 minute")
#     .start()
# )

# top_selling_60_sec_query = (
#     top_selling_60_sec.writeStream.outputMode("complete")
#     .format("console")
#     .trigger(processingTime="1 minute")
#     .start()
# )

# # # Wait for the queries to terminate
# pending_orders_query.awaitTermination()
# top_selling_today_query.awaitTermination()
# top_selling_60_sec_query.awaitTermination()

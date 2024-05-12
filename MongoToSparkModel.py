from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import monotonically_increasing_id, col
from pyspark.sql.types import IntegerType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Music Recommendation") \
    .getOrCreate()

# Connect to MongoDB and load the DataFrame
mongo_uri = "mongodb://localhost:27017"
mongo_db = "audio"
mongo_collection = "songs"
df = spark.read.format("mongo") \
    .option("uri", mongo_uri) \
    .option("database", mongo_db) \
    .option("collection", mongo_collection) \
    .load()

# Print the schema to inspect the column names and types
df.printSchema()

# Convert double array columns to integers if possible
df = df.withColumn("userId", col("user_id").cast(IntegerType()))  # Assuming "user_id" is the correct column for user ID
df = df.withColumn("itemId", col("id").cast(IntegerType()))       # Assuming "id" is the correct column for item ID

# Add a dummy "rating" column using monotonically_increasing_id()
df = df.withColumn("rating", monotonically_increasing_id())

# Drop rows with null values in userId or itemId columns
df = df.dropna(subset=["userId", "itemId"])

# Print the schema to inspect the column names and types
df.printSchema()

# Split the data into training and test sets
(training, test) = df.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS on the training data
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="itemId",
          ratingCol="rating", coldStartStrategy="drop")
model = als.fit(training)

# Predictions for the test data
predictions = model.transform(test)

# Stop the SparkSession
spark.stop()


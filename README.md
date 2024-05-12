# Faizan_1946_Ziyan_1998_Tasmiya_2060_BDA_Project


# Fundamentals Of Big Data Analytics

# Semester Project

# Group Members:

Faizan Aziz			i221946

Tasmiya Asad		i222060

Ziyan Murtaza		i221998

# Submitted On:

12th May, 24

# Project Statement:

Create an audio recommendation system given the dataset.

# Process:

# 1. Conversion from Audio to MFCC:

Utilizing librosa’s mfcc feature to convert the audio files into a numerical vector.
Flattening the vector for further utilization.

# 2. Storing MFCC’s into a MongoDB:

Using MongoDB to store the vast dataset processed for ease in access and usage for further model training.

# 3. Connection with PySpark:

Connecting the MongoDB with PySpark to form and Resilient Distributed Dataset (RDD) for further and easy processing and model training.


# 4. Model Training – ALS:

Utilization of ALS model to build the recommendation system and storing the data into a MongoDB.

# 5. Web Application Using Flask and Kafka:

Utilization of Kafka to stream data from MongoDB as per need to display recommendations based on the listening.

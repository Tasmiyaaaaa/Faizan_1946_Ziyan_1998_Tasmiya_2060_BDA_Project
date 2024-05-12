import zipfile
import librosa
import numpy as np
from pymongo import MongoClient
from pyspark import SparkContext
from pyspark.sql import SparkSession

zip_file_path = "sample.zip"
num = 1
final_list = []

# Open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    
    # List all files in the zip file
    file_list = zip_ref.namelist()
    
    # Read the contents of each file in the zip file
    for file_name in file_list:
        if file_name.endswith('.mp3'):
            
            dictionary = {}
            
            try:
                with zip_ref.open(file_name) as audio_file:
                    
                    audio_data, sr = librosa.load(audio_file, sr=None)
                    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr)
                    mfccs_flat = np.ndarray.flatten(mfccs)

                    mfccs_flat = mfccs_flat.tolist()
                    mfccs_flat = [float(value) for value in mfccs_flat]
                    dictionary[str(num)] = mfccs_flat
                    num += 1
                    final_list.append(dictionary)
                    
            except:
                continue

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['audio']
collection = db['songs']

# Select/Create collection (similar to a table)
collection.insert_many(final_list)

data = collection.find()

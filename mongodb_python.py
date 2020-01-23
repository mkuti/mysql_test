import os
import pymongo

from os import path
if path.exists("env.py"):
    import env

MONGO_URL = os.getenv("MONGO_URl")
DBS_NAME = "myOwnDB"
COLLECTION_NAME = "myOwnMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo!")
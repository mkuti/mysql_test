import os
import pymongo

from os import path
if path.exists("env.py"):  # import file where username and password of MongoDB is saved
    import env

MONGO_URL = os.environ.get("MONGO_URL")  # variable with secret MONGO_URL
DBS_NAME = "myOwnDB"  # variable with name of DB
COLLECTION_NAME = "myOwnMDB"  # variable with name of collection inside DB


def mongo_connect(url):  # function to connect to Mongo with url argument passed in
    try:   # start try/except block
        conn = pymongo.MongoClient(url)  # variable to connect to mongo client db
        print("Mongo is connected")  # print in console if connected
        return conn  # return variable for connection
    except pymongo.errors.ConnectionFailure as e:  # catch error if connection fails
        print("Could not connect to MongoDB: %s") % e  # print error message which has been defined as 'e' alias


conn = mongo_connect(MONGO_URL)  # calling function with MONGOBDB url

coll = conn[DBS_NAME][COLLECTION_NAME]  # set collection name

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'pink'}})

documents = coll.find()  # print everything that's in the database = returns MongoDB object

for doc in documents:
    print(doc)

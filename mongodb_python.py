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

new_docs = [{'first': 'janis', 'last': 'joplin', 'occupation': 'singer', 'dob': '12/04/1950', 'hair': 'blond', 'nationality': 'american'}, {'first': 'nina', 'last': 'simone', 'occupation': 'singer', 'dob': '23/07/1948', 'hair': 'black', 'nationality': 'american'}]

coll.insert_many(new_docs)  # add new doc variable in database collection

documents = coll.find()  # print everything that's in the database = returns MongoDB object

for doc in documents:
    print(doc)

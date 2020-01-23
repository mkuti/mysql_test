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
        return conn  # return variable for connection
    except pymongo.errors.ConnectionFailure as e:  # catch error if connection fails
        print("Could not connect to MongoDB: %s") % e  # print error message which has been defined as 'e' alias


def show_menu():
    print("")
    print("1. Add record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    print("")
    option = input("Enter your option: ")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URL)  # calling function with MONGOBDB url

coll = conn[DBS_NAME][COLLECTION_NAME]  # set collection name

main_loop()

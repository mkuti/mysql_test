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


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error, no record found")

    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter dob > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {"first": first.lower(), "last": last.lower(), "dob": dob.lower(), "gender": gender.lower(), "hair_colour": hair_colour.lower(), "occupation": occupation.lower(), "nationality": nationality.lower()}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + "[" + v + "] > ")  # show current value of k

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing database")


def delete_record():  # be careful with indent!!!

    doc = get_record()  # user choose record in get_record function

    if doc:  # if record found, automatic error message if no record found
        print("")
        for k, v in doc.items():  # interate through and print all values
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())  # show all keys and values of doc chosen by user

        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")  # based on above doc, confirm if ok to delete
        print("")

        if confirmation.lower() == "y":

            try:
                coll.remove(doc)
                print("")
                print("Document deleted")
            except:
                print("Error accessing database")
            
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URL)  # calling function with MONGOBDB url

coll = conn[DBS_NAME][COLLECTION_NAME]  # set collection name

main_loop()

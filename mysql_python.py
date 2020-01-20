import os
import pymysql

# Get username from GitPod
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try: #RUN QUERY
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;" # mysql commands inside python variable
        cursor.execute(sql) # execute sql variable
        result = cursor.fetchall() # get data back
        print(result) # print result
finally: # CLOSE CONNECTION
    connection.close()

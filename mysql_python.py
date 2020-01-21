import os
import pymysql
import datetime

# Get username from GitPod
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try: 
    # RUN QUERY
    with connection.cursor() as cursor:
        list_of_names = ['jack', 'mark']
        format_string = ",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name IN ({});".format(format_string), list_of_names)
        connection.commit()
finally: 
    # CLOSE CONNECTION
    connection.close()

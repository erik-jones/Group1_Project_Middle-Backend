from cgi import test
import mysql.connector

#setup the connections to a MySQL site
mydb= mysql.connector.connect(
    host = "localhost",     #this is the server address
    user = "root",          #this user, for a localhost this is typically "root"
    password = "",          #no password was defined so I didn't set up one
    database = "testsite"   #Name of the database you are tying to access, typically the name of the website
)

#create and run the query
mycursor = mydb.cursor() #setting up an SQL statement
test_query = "SELECT * FROM wp_fluentform_entry_details" #Gets information from fluent forms
mycursor.execute(test_query) #Executes the query

#displays the query
for x in mycursor:
    print(x[5])
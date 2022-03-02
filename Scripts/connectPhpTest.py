from cgi import test
import mysql.connector

mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testsite"
)

mycursor = mydb.cursor()
test_query = "SELECT * FROM wp_fluentform_entry_details"

mycursor.execute(test_query)

for x in mycursor:
    print(x[5])
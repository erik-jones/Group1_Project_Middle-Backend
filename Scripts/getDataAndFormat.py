import mysql.connector

#TODO:
#Move away from fluent forms

#connects to a MySQL database and retrieves data
def getFieldThing():
    #establishes a MySQL connection
    mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mysite"
    )

    mycursor = mydb.cursor()
    #submission_id is connected to a specific form that a user submits. Will increase with each submission
    test_query = "SELECT * FROM wp_fluentform_entry_details where submission_id = 10;"
    mycursor.execute(test_query)

    # Pull the data from the form and store in an array
    # x[3] is the field name, x[5] is the field value
    fieldArray = []
    for x in mycursor:
        # location is a special case where x[3] = location and x[4] is the specific field (city, state, country)
        if x[3] == "location":
            fieldArray.append([x[4],x[5]])
        else:
            fieldArray.append([x[3],x[5]])

    return(fieldArray)
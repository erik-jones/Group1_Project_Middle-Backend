from cgi import test
import mysql.connector

#TODO:
#Move away from fluent forms
#If using fluent forms, figure out a way to automate the fieldArray process (looking into it)
#Look into automating the if-block section

#This is an array that will store the row identifiers
fieldArray =    [   ["Project Name"],
                    ["College"],
                    ["Department"],
                    ["Class Level"],
                    ["Primary Focus Area"],
                    ["Participant Type"],
                    ["Number of Participants"],
                    ["Start Date"],
                    ["End Date"],
                    ["Semester"],
                    ["Year"],
                    ["Status"],
                    ["Compensation"],
                    ["Opportunity Type"],
                    ["University Partner"],
                    ["Working with a community partner?"],
                    ["Association"],
                    ["Type"],
                    ["Contact"],
                    ["Website"],
                    ["Address"],
                    ["Mode"],
                    ["Financing"],
                    ["Cost to Student"],
                    ["Cost to UA Partner"],
                    ["Cost to Community Partner"],
                    ["Time Commitment"],
                    ["Admission Type"],
                    ["Impact"],
                    ["Outreach"],
                    ["Project Description"]
                ]

#couldn't be bothered to choose a better name for this
#connects to a MySQL database and retrieves data
def getFieldThing():
    #establishes a MySQL connection
    mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "testsite"
    )

    mycursor = mydb.cursor()
    #submission_id is connected to a specific form that a user submits. Will increase with each submission
    test_query = "SELECT * FROM wp_fluentform_entry_details where submission_id = 7;"
    mycursor.execute(test_query)

    #make this better
    for x in mycursor:
        if(x[3] == "input_text"):
            fieldArray[0].append(x[5])
        elif(x[3] == "dropdown"):
            fieldArray[1].append(x[5])
        elif(x[3] == "dropdown_1"):
            fieldArray[2].append(x[5])    
        elif(x[3] == "checkbox"):
            fieldArray[3].append(x[5])
        elif(x[3] == "dropdown_2"):
            fieldArray[4].append(x[5])
        elif(x[3] == "checkbox_1"):
            fieldArray[5].append(x[5])
        elif(x[3] == "numeric-field"):
            fieldArray[6].append(x[5])
        elif(x[3] == "datetime"):
            fieldArray[7].append(x[5])
        elif(x[3] == "datetime_1"):
            fieldArray[8].append(x[5])
        elif(x[3] == "dropdown_3"):
            fieldArray[9].append(x[5])
        elif(x[3] == "numeric-field_4"):
            fieldArray[10].append(x[5])
        elif(x[3] == "input_radio"):
            fieldArray[11].append(x[5])
        elif(x[3] == "input_radio_1"):
            fieldArray[12].append(x[5])
        elif(x[3] == "dropdown_4"):
            fieldArray[13].append(x[5])
        elif(x[3] == "dropdown_5"):
            fieldArray[14].append(x[5])
        elif(x[3] == "input_radio_2"):
            fieldArray[15].append(x[5])
        elif(x[3] == "input_radio_3"):
            fieldArray[16].append(x[5])
        elif(x[3] == "input_text_1"):
            fieldArray[17].append(x[5])
        elif(x[3] == "input_text_2"):
            fieldArray[18].append(x[5])
        elif(x[3] == "input_text_3"):
            fieldArray[19].append(x[5])
        elif(x[3] == "address_1"):
            fieldArray[20].append(x[5])
        elif(x[3] == "checkbox_2"):
            fieldArray[21].append(x[5])
        elif(x[3] == "dropdown_6"):
            fieldArray[22].append(x[5])
        elif(x[3] == "numeric-field_1"):
            fieldArray[23].append(x[5])
        elif(x[3] == "numeric-field_2"):  
            fieldArray[24].append(x[5])
        elif(x[3] == "numeric-field_3"):  
            fieldArray[25].append(x[5])
        elif(x[3] == "dropdown_7"): 
            fieldArray[26].append(x[5])
        elif(x[3] == "dropdown_8"): 
            fieldArray[27].append(x[5])
        elif(x[3] == "dropdown_9"): 
            fieldArray[28].append(x[5])
        elif(x[3] == "description"): 
            fieldArray[29].append(x[5])
        elif(x[3] == "description_1"): 
            fieldArray[30].append(x[5])
        else:
            print("Not found")

    for i in range(len(fieldArray)):
        print(fieldArray[i])

    return(fieldArray)

getFieldThing()
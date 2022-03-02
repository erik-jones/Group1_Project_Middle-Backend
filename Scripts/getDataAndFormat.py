from cgi import test
import mysql.connector

fieldArray =    [   ["Project Name"],
                    ["College"],
                    ["Department"],
                    ["Class Level"],
                    ["Primary Focus Area"],
                    ["Academic Level"],
                    ["Start Date"],
                    ["End Date"],
                    ["Project Description"],
                    ["Semester"],
                    ["Status"],
                    ["Compensation"],
                    ["Opportunity Type"],
                    ["University Partner"],
                    ["Community Partner Internal/External"],
                    ["Community Partner Organization"],
                    ["Community Partner Type"],
                    ["Community Partner Contact"],
                    ["Community Partner Website"],
                    ["Number of Participants"],
                    ["City"],
                    ["State"],
                    ["Country"],
                    ["Mode"],
                    ["Impact"],
                    ["Outreach"],
                    ["Cost to Student"],
                    ["Time Commitment"],
                    ["Admission Type"]
                ]

mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testsite"
)

mycursor = mydb.cursor()
test_query = "SELECT * FROM wp_fluentform_entry_details where submission_id = 6"

mycursor.execute(test_query)

for x in mycursor:
    if(x[3] == "input_text"):
        fieldArray[0].append(x[5])
    elif(x[3] == "dropdown_1"):
        fieldArray[1].append(x[5])
    elif(x[3] == "input_text_1"):
        fieldArray[2].append(x[5])
    elif(x[3] == "checkbox"):
        fieldArray[3].append(x[5])
    elif(x[3] == "dropdown"):
        fieldArray[4].append(x[5])
    elif(x[3] == "checkbox_1"):
        fieldArray[5].append(x[5])
    elif(x[3] == "datetime"):
        fieldArray[6].append(x[5])
    elif(x[3] == "datetime_2"):
        fieldArray[7].append(x[5])
    elif(x[3] == "description"):
        fieldArray[8].append(x[5])
    elif(x[3] == "dropdown_2"):
        fieldArray[9].append(x[5])
    elif(x[3] == "input_radio"):
        fieldArray[10].append(x[5])
    elif(x[3] == "input_radio_1"):
        fieldArray[11].append(x[5])
    elif(x[3] == "dropdown_3"):
        fieldArray[12].append(x[5])
    elif(x[3] == "input_text_2"):
        fieldArray[13].append(x[5])
    elif(x[3] == "input_radio_2"):
        fieldArray[14].append(x[5])
    elif(x[3] == "input_text_3"):
        fieldArray[15].append(x[5])
    elif(x[3] == "dropdown_4"):
        fieldArray[16].append(x[5])
    elif(x[3] == "input_text_4"):
        fieldArray[17].append(x[5])
    elif(x[3] == "url"):
        fieldArray[18].append(x[5])
    elif(x[3] == "numeric-field"):
        fieldArray[19].append(x[5])
    elif(x[3] == "input_text_5"):
        fieldArray[20].append(x[5])
    elif(x[3] == "input_text_6"):
        fieldArray[21].append(x[5])
    elif(x[3] == "country-list"):
        fieldArray[22].append(x[5])
    elif(x[3] == "checkbox_2"):
        fieldArray[23].append(x[5])
    elif(x[3] == "dropdown_5"):
        fieldArray[24].append(x[5])
    elif(x[3] == "input_text_7"):
        fieldArray[25].append(x[5])
    elif(x[3] == "numeric-field_1"):  
        fieldArray[26].append(x[5])
    elif(x[3] == "dropdown_6"):  
        fieldArray[27].append(x[5])
    elif(x[3] == "dropdown_7"): 
        fieldArray[28].append(x[5])
    else:
        print("Not found")

# for i in range(len(fieldArray)):
#     print(fieldArray[i])

def getFieldThing():
    return(fieldArray)

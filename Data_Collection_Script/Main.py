# Main script that will delegate and call all other scripts
import Authorize, Courses, Groups, Impacts, Events
import WriteToExcel, Box
import json

# Constants
EXCEL_FILE_PATH = "Data_Collection_Script/BamaPulse_Data.xlsx"
INFO = json.load(open('Data_Collection_Script/Info.json'))

# Execution Starts Here
# First need to get an authorization token for bamapulse
token = Authorize.getAuthToken(INFO)

# Make other calls here and pass the token as a parameter
groupData = Groups.getGroups(token)
impactData = Impacts.getImpacts(token)
eventData = Events.getEvents(token)
#courseData = Courses.getCourses(token) --> getCourses request is returning a 500 internal server error

# Get the excel file from box
Box.downloadFile(EXCEL_FILE_PATH, INFO)

# Write the data to the excel file
WriteToExcel.writeData(groupData, impactData, eventData, None, EXCEL_FILE_PATH)

# Upload the file back to box
Box.uploadFile(EXCEL_FILE_PATH, INFO)
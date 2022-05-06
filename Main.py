# Main script that will delegate and call all other scripts
import Authorize, Courses, Groups, Impacts, Events
import WriteToExcel, Box

# Constants
EXCEL_FILE_PATH = "Scripts/givepulse_api/BamaPulse_Data.xlsx"

# Execution Starts Here
# First need to get an authorization token for bamapulse
token = Authorize.getAuthToken()

# Make other calls here and pass the token as a parameter
groupData = Groups.getGroups(token)
impactData = Impacts.getImpacts(token)
eventData = Events.getEvents(token)
#courseData = Courses.getCourses(token) --> getCourses request is returning a 500 internal server error

# Get the excel file from box
Box.downloadFile(EXCEL_FILE_PATH)

# Write the data to the excel file
WriteToExcel.writeData(groupData, impactData, eventData, None, EXCEL_FILE_PATH)

# Upload the file back to box
Box.uploadFile(EXCEL_FILE_PATH)
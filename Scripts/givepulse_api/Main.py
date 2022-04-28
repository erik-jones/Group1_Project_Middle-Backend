# Main script that will delegate and call all other scripts
import Authorize, Courses, Groups, Impacts, Events
import WriteToExcel

# Execution Starts Here
# First need to get an authorization token for bamapulse
token = Authorize.getAuthToken()
# Make other calls here and pass the token as a parameter
groupData = Groups.getGroups(token)
# WriteToExcel.writeData(groupData, None, None, None)

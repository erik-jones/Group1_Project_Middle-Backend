# Main script that will delegate and call all other scripts
import Authorize, Courses, Groups, Impacts

# Execution Starts Here
# First need to get an authorization token for bamapulse
# token = Authorize.getAuthToken()
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3LmdpdmVwdWxzZS5jb20iLCJhdWQiOiJUaGUgVW5pdmVyc2l0eSBvZiBBbGFiYW1hIiwidHlwZSI6Imdyb3VwIiwiY29uc3VtZXJfaWQiOiIxOTgiLCJ1aWQiOiIyMjY1MTk0IiwiZ3JvdXBfaWQiOiIxMTkwNDgiLCJpYXQiOjE2NTExNjk0NTIsImV4cCI6MTY1MTE3NjY1Mn0.wVRaifAJZhRO34J9wulkCm3CKmu3Wc7MPjCAFcD-r6M"
# Make other calls here and pass the token as a parameter
#groupData = Groups.getGroups(token)
# Courses are for some reason returning a 500 error through the Givepulse api
#courseData = Courses.getCourses(token)
# Add events
# Add impacts
impactData = Impacts.getImpacts(token)

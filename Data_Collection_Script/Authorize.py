# Before making any other API calls, you have to get an authorization token that will be valid for 2 hours
# This requires 4 values: Key, Secret, Email, Password
# Key, secret were given to us by someone with admin privilege. Email, password can be any valid givepulse account

import base64
import requests

key = ""
secret = ""
email = ""
password = ""

# Gets the bearer auth token needed for future calls
def getAuthToken():
    # Need to put the above values in the format: key:secret:email:password
    # Then base64 encode that string
    message = key + ':' + secret + ':' + email + ':' + password
    messageBytes = message.encode("ascii")
    base64Bytes = base64.b64encode(messageBytes)
    base64String = base64Bytes.decode("ascii")
    
    # Header that is passed in to the api call
    basicAuth = "Basic " + base64String
    header = {"Authorization": basicAuth}

    # This returns a response in JSON form, which in python is stored as a dictionary, which we can get the token from
    print("Call to auth")
    response = requests.get("https://api2.givepulse.com/auth", headers=header)
    token = response.json().get("token")
    return token
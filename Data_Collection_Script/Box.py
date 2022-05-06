# Methods for connecting to the excel file within Box, using the Box SDK
from boxsdk import Client, CCGAuth
import os

# Authorize with dev token
def __authorize(id, secret, token):
    # The dev token is only valid for 60 minutes, so can only be used for testing purposes
    # Moving foward we need to find a way to get a permanent token, but this seems to require a further level of authorization
    auth = CCGAuth(
        client_id=id,
        client_secret=secret,
        access_token=token,
        #user=""
    )
    # Client is used to call all other methods
    return Client(auth)

# Download the excel file using the file id
def downloadFile(excelFilePath, info):
    print("Downloading file from box")

    FILE_ID = info["box_file_id"]
    client = __authorize(info["box_client_id"], info["box_client_secret"], info["box_access_token"])

    output_file = open(excelFilePath, 'wb')
    client.file(FILE_ID).download_to(output_file)
    output_file.close()

# Upload the updated file back into box
def uploadFile(excelFilePath, info):
    print("Uploading file to box")

    FILE_ID = info["box_file_id"]
    client = __authorize(info["box_client_id"], info["box_client_secret"], info["box_access_token"])

    stream = open(excelFilePath, 'rb')
    client.file(FILE_ID).update_contents_with_stream(stream)
    stream.close()
    os.remove(excelFilePath)
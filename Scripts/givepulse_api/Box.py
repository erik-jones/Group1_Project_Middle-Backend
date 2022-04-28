# Methods for connecting to the excel file within Box, using the Box SDK
from boxsdk import Client, CCGAuth

# Can be obtained by opening the file within box and checking the url
FILE_ID = ""

# Authorize with dev token
def __authorize():
    # The dev token is only valid for 60 minutes, so can only be used for testing purposes
    # Moving foward we need to find a way to get a permanent token, but this seems to require a further level of authorization
    auth = CCGAuth(
        client_id='kmekvkq9zw2vobwr6psn3g4umf9o5u2g',
        client_secret='blTORvVwqm0V9v4VfNRdPY5mbzFARnvo',
        access_token='Bt8I52Y6vBqlPcAtMqM2dxKO6hTdwx4d',
        #user=""
    )
    # Client is used to call all other methods
    return Client(auth)

# Download the excel file using the file id
def downloadFile():
    client = __authorize()

    output_file = open('', 'wb')
    client.file(FILE_ID).download_to(output_file)
    output_file.close()

# Upload the updated file back into box
def uploadFile():
    client = __authorize()

    stream = open('testing.txt', 'rb')
    client.file(FILE_ID).update_contents_with_stream(stream)
    stream.close()
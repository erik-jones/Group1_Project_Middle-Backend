import requests
import base64
import json

username = "wordpress_python"
password = "IZ8b nkhn meJQ bPYZ WIJ4 r16M"

creds = username + ':' + password
cred_token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}

url = "https://uaelos.com/"

post = {
 'title' : 'This is WordPress Python Integration Testing',

 'content' : 'Hello, this content is published using WordPress Python Integration',
 'status' : 'publish', 
 'categories': 5, 
 'date' : '2021-12-05T11:00:00'
}

blog = requests.post(url + '/posts' , headers=header , json=post)
print(blog)
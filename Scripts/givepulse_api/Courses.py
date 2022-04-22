#get the courses
def getCourses(token, fields = None):
    # fields is a dictionary (fields : values)
    # used to filter output i.e group_id = 1002

    # Authentication Header that is passed in to the api call
    authenticationToken = "Bearer " + token
    headers = {"Authorization": authenticationToken}

    # Other fields are added to dictionary if they exist
    if fields:
        headers.update(fields)

    # This returns a response in JSON form, which in python is stored as a dictionary, which we can get the data from
    response = requests.get("https://api2.givepulse.com/courses", headers=headers)
    data = response.json().get("token")
    return data

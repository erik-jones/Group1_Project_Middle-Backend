import requests  

#get the impacts
def getImpacts(token, fields = None):
    # fields is a dictionary
    # used to filter output i.e group_id = 1002

    # Authentication Header that is passed in to the api call
    authenticationToken = "Bearer " + token
    headers = {"Authorization": authenticationToken}

    # List of dictionaries, where each one is one impact
    impactList = []

    # Bamapulse only returns up to 50 items at once, so need to make the call multiple times, using limit, offset as parameters
    limit = 50
    offset = 0
    params = {"limit": limit, "offset": offset}

    # Other fields are added to dictionary if they exist
    if fields:
        headers.update(fields)

    counter = 1
    print(f"Call to impacts: {counter}")
    response = requests.get("https://api2.givepulse.com/impacts", headers=headers, params=params)
    data = response.json()
    impactList.extend((data.get("results")))

    # Get the total from the first call, then make successive calls until you reach the total
    total = int(data.get('total'))
    while len(impactList) < total:
        counter += 1
        print(f"Call to impacts: {counter}")
        offset += 50
        params.update({"offset": offset})

        response = requests.get("https://api2.givepulse.com/impacts", headers=headers, params=params)
        data = response.json()
        impactList.extend(data.get("results"))

    return impactList

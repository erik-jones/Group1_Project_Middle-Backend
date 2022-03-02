# Python script that parses data sent by middle end script and writes it to the EL database

# Constants (may move to a seperate constants file later for organization, doesn't really matter now)
ELDB_FILE_PATH = "../Data/Example_DB.xlsx"

# imports

# Temporary fake data, will change later
# Store as a list of lists where each sublist is in form: [field, value]
exampleInput = [["Name", "Biology Outreach"], ["College", "Arts & Science"], ["Department", "Biology"],
                ["Academic Level", "Undergraduate"]]
                
# Edits a currently existing project in the excel database

#TODO: 
# Step 1: find the project within the database (find the row that's needed)

# Step 2: identify which column needs to change

# Step 3: using the row and column found in previous steps, change the field to the new value, save the excel file

# Constants
ELDB_FILE_PATH = "../Data/Example_DB.xlsx"

def editProject(projectName, field, value):
    # field is the column that needs to change, value is the new value you want to set it to
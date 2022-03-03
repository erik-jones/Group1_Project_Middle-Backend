# Python script that parses data sent by middle end script and writes it to the EL database
import openpyxl
from sqlalchemy import column
import ColumnTranslation

# Constants (may move to a seperate constants file later for organization, doesn't really matter now)
ELDB_FILE_PATH = "../Data/Example_DB.xlsx"

# Return the max number of rows that have data so we can append to the end
def __getMaxRows(sheet):
    rows = 0
    for max_row, row in enumerate(sheet, 1):
        if not all(col.value is None for col in row):
            rows += 1
    return rows

# 'Main Method' of script
def writeToExcel(dataFromForm):
    # Temporary fake data, will change later
    #exampleInput = [["Project Name", "Biology Outreach"], 
    #                ["College", "Arts & Science"], 
    #                ["Department", "Biology"],
    #                ["Academic Level", "Undergraduate"]]

    columns = ColumnTranslation.columnTranslate

    # Load the db and get the sheet the projects are in
    db = openpyxl.load_workbook(ELDB_FILE_PATH)
    projectSheet = db['Sheet1']

    newRow = __getMaxRows(projectSheet) + 1
    for field in dataFromForm:
        tempCell = projectSheet.cell(row=newRow, column=columns.get(field[0])).value = field[1]

    db.save(ELDB_FILE_PATH)

# Driver Code (move to different file later)
writeToExcel()

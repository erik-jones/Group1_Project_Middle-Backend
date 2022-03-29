# Writes the data pulled from the form to the excel database
import openpyxl
import ColumnTranslation

# Constants
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
    # Get the column from the excel file
    columns = ColumnTranslation.translateColumns(ELDB_FILE_PATH)

    # Load the db and get the sheet the projects are in
    db = openpyxl.load_workbook(ELDB_FILE_PATH)
    projectSheet = db['Sheet1']
    
    # Get the next empty row in the sheet
    newRow = __getMaxRows(projectSheet) + 1

    # Insert the value from the form into its respective column/row
    for field in dataFromForm:
        tempCell = projectSheet.cell(row=newRow, column=columns.get(field[0])).value = field[1]
        
    db.save(ELDB_FILE_PATH)

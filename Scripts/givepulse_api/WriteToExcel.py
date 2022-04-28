# Writes the data from each table to their respective excel sheet
import openpyxl
from openpyxl import Workbook

# Constants
EXCEL_FILE_PATH = "Scripts/givepulse_api/BamaPulse_Data.xlsx"
GROUP_SHEET = "Subgroup"
IMPACT_SHEET = "Impact"
EVENT_SHEET = "Event"
COURSE_SHEET = "Course"

# Return the max number of rows that have data so we can append to the end
def __getMaxRows(sheet):
    rows = 0
    for max_row, row in enumerate(sheet, 1):
        if not all(col.value is None for col in row):
            rows += 1
    return rows

# Write the list of groups to the excel file
def __writeToGroups(db: Workbook, group):
    sheet = db[GROUP_SHEET]

    # Add a check to see if this is already in the excel file
    
    # Get the next empty row in the sheet
    newRow = __getMaxRows(sheet) + 1
    for field in group:
        # Update this to have the actual column value
        tempCell = sheet.cell(row=newRow, column=1).value = field[1]

# Main function of this script
def writeData(groupData, impactData, eventData, courseData):
    db = openpyxl.load_workbook(EXCEL_FILE_PATH)
    
    for group in groupData:
        __writeToGroups(db, group)
        break

    db.save(EXCEL_FILE_PATH)



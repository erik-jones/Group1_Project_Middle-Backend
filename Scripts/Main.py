import getDataAndFormat
import WriteToDB

#TODO:
# 1) Loop through excel columns to build out the dictionary stored in columntranslation, so it doesn't have to be hardcoded

data = getDataAndFormat.getFieldThing()
print(data)
#WriteToDB.writeToExcel(data)
# If we stick with using our own form, these scripts will handle that flow of data. Execution begins in this file.

import getDataAndFormat
import WriteToDB

data = getDataAndFormat.getFieldThing()
#print(data)
WriteToDB.writeToExcel(data)
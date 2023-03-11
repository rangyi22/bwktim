import openpyxl

# New Excel File Creation
wb = openpyxl.Workbook()

# Choose the current activated sheet
ws = wb.active

# Change the sheet name
ws.title = "Something created by automation"

# Save the Excel file
wb.save('./StartCoding_Python_Automation/automated_excel.xlsx')
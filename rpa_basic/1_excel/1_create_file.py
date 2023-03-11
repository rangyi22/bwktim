from openpyxl import Workbook
wb = Workbook()  # Create the new workbook
ws = wb.active # Loading the current active sheet
ws.title = "NadoSheet" # Change the name of the sheet
wb.save("sample.xlsx")
wb.close()

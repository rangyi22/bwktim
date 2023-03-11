import openpyxl
import random

# Creat a new Excel file
wb = openpyxl.Workbook()

# Create the activated sheet 
ws = wb.active

# Change the sheet nmae
ws.title = "data"

# Add the header
ws.append(['Number', 'Product Name', 'Price', 'Quantity', 'Sum'])

# Add the data
name_list = ['Mechanical Keyboard', 'Gaming Mouse', '32 Inch Monitor', 'Mouse Pad']

for i in range(random.randint(5,10)): # Sales Data (row): 5 ~ 10ea
    name = random.choice(name_list)
    if name == "Mechanical Keyboard":
        price = 120000
    elif name == "Gaming Mouse":
        price = 40000
    elif name == "32 Inch Monitor":
        price = 350000
    elif name == "Mouse Pad":
        price = 20000
    ws.append([i+1, name, price, random.randint(1, 5), f'=C{i+2}*D{i+2}'])

# Save
wb.save("StartCoding_Python_Advanced/11street.xlsx")
wb.save("StartCoding_Python_Advanced/coopang.xlsx")
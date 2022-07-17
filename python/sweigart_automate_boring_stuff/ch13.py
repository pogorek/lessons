# 13 WORKING WITH EXCEL SPREADSHEETS

# Opening Excel Documents with OpenPyXL

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# print(type(wb))
# # <class 'openpyxl.workbook.workbook.Workbook'>
# print(wb)
# # <openpyxl.workbook.workbook.Workbook object at 0x7fb792b3ab20>
# # Getting Sheets from the Workbook

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# print(wb.sheetnames) # The workbook's sheets' names.
# # ['Sheet1', 'Sheet2', 'Sheet3']
# sheet = wb['Sheet3'] # Get a sheet from the workbook.
# print(sheet)
# # <Worksheet "Sheet3">
# print(type(sheet))
# # <class 'openpyxl.worksheet.worksheet.Worksheet'>
# print(sheet.title) # Get the sheet's title as a string.
# # 'Sheet3'
# anotherSheet = wb.active # Get the active sheet.
# print(anotherSheet)
# # <Worksheet "Sheet1">

# Getting Cells from the Sheets

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb['Sheet1']  # Get a sheet from the workbook.
# print(sheet['A1'])  # Get a cell from the sheet.
# # <Cell 'Sheet1'.A1>
# print(sheet['A1'].value)  # Get the value from the cell.
# # datetime.datetime(2015, 4, 5, 13, 34, 2)
# c = sheet['B1']  # Get another cell from the sheet.
# print(c.value)
# # 'Apples'
# # Get the row, column, and value from the cell.
# print('Row %s, Column %s is %s' % (c.row, c.column, c.value))
# # 'Row 1, Column B is Apples'
# print('Cell %s is %s' % (c.coordinate, c.value))
# # 'Cell B1 is Apples'
# print(sheet['C1'].value)
# # 73

# print(sheet.cell(row=1, column=2))
# # <Cell 'Sheet1'.B1>
# print(sheet.cell(row=1, column=2).value)
# # 'Apples'
# for i in range(1, 8, 2):  # Go through every other row:
#     print(i, sheet.cell(row=i, column=2).value)
# # 1 Apples # 3 Pears # 5 Apples # 7 Strawberries

# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb['Sheet1']
# print(sheet.max_row)  # Get the highest row number.
# # 7
# print(sheet.max_column)  # Get the highest column number.
# # 3

# Converting Between Column Letters and Numbers

# import openpyxl
# from openpyxl.utils import get_column_letter, column_index_from_string
# print(get_column_letter(1))  # Translate column 1 to a letter.
# # 'A'
# print(get_column_letter(2))
# # 'B'
# print(get_column_letter(27))
# # 'AA'
# print(get_column_letter(900))
# # 'AHP'
# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb['Sheet1']
# print(get_column_letter(sheet.max_column))
# # 'C'
# print(column_index_from_string('A'))  # Get A's number.
# # 1
# print(column_index_from_string('AA'))
# # 27

# Getting Rows and Columns from the Sheets

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb['Sheet1']
# print(tuple(sheet['A1':'C3']))  # Get all cells from A1 to C3.
# # ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell
# # 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>,
# # <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
# for rowOfCellObjects in sheet['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate, cellObj.value)
#     print('--- END OF ROW ---')

# # A1 2015-04-05 13:34:02
# # B1 Apples
# # C1 73
# # --- END OF ROW ---
# # A2 2015-04-05 03:41:23
# # B2 Cherries
# # C2 85
# # --- END OF ROW ---
# # A3 2015-04-06 12:46:51
# # B3 Pears
# # C3 14
# # --- END OF ROW ---

# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb.active
# list(sheet.columns)[1]  # Get second column's cells.
# # (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
# for cellObj in list(sheet.columns)[1]:
#     print(cellObj.value)

# # Apples Cherries Pears Oranges Apples Bananas Strawberries


#! Writing Excel Documents

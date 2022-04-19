import openpyxl

workbook = openpyxl.load_workbook("..//excel/testdata.xlsx")
sheet = workbook["Login Test"]


def getRowCount(path, sheetName):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    return sheet.max_row


def getColCount(path, sheetName):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    return sheet.max_column


def getCellData(path, sheetName, rowNum, colNum):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    return sheet.cell(row=rowNum, column=colNum).value


def setCelData(path, sheetName, rowNum, colNum, data):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    sheet.cell(row=rowNum, column=colNum).value = data
    workbook.save(path)


path = "..//excel/testdata.xlsx"
sheetName = "Login Test"
rows = getRowCount(path, sheetName)
cols = getColCount(path, sheetName)
setCelData(path, sheetName, 1, 4, "DOB")

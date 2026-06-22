import openpyxl

def getRowCount(file, sheetName):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    return(sheet.max_row)

def getRoColumnCount(file, sheetName):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    return(sheet.max_column)

def readData(file, sheetName, rownum, columnnum):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    return(sheet.cell(rownum, columnnum).value)

def writeData(file, sheetName, rownum, columnnum, data):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    sheet.cell(rownum, columnnum).value=data
    workbook.save(file)

import xlsxwriter
import webscrapping
import Projectmain

workbook=xlsxwriter.Workbook("ProjectData.xlsx")
worksheet=workbook.add_worksheet("My Worksheet")

for i range(0,100):
    worksheet.write(row,col,website)
    worksheet.write(row,col+1,keyword)
    row+=1

    workbook.close()
    

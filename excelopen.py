from openpyxl import Workbook
import os


book=Workbook()
sheet=book.active

sheet['A1']="s.no"
sheet['b1']="name"
sheet['c1']="date"
sheet['A2']=1
sheet['B2']="suganya"


book.save("openxlexam.xlsx")
os.system('start openxlexam.xlsx')


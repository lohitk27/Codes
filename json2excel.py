import sys
import json
import xlsxwriter
import pandas as pd
import numpy as np


class JSON2Excel:
    def __init__(self):
        self.jsonFle="Actual.JSON"
        self.excelFile="output.xlsx"
        
    def readFile(self):
        with open(self.jsonFle) as data:
            data=json.load(data)
            pprint.pprint(data)
    def savetoexcel(self):
        work= xlsxwriter.Workbook(self.excelFile)
        worksheet=work.add_worksheet()
        for majorkey, subdict in data.items():
            for subkey, value in subdict.items():
                    for index,sam in enumerate(value):
                        worksheet.write(index, 0,sam['type'])
                        worksheet.write(index, 1,sam['type1'])
                        worksheet.write(index, 2,sam['type2'])
                        worksheet.write(index, 3,sam['type3'])
                        worksheet.write(index, 4,sam['type4'])
                        worksheet.write(index, 5,sam['type5'])
                        worksheet.write(index, 6,sam['type6'])
                        worksheet.write_row(index, 7,sam['type7'])
                        
                    work.close()
    
if __name__=='__main__':
    flows=JSON2Excel()
    flows.readFile()
    flows.savetoexcel()

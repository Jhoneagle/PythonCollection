# coding=utf-8

import sys
from components.invoice import Invoice
from components.finvoice import Finvoice
from components.row import Row
from components.invoiceRow import InvoiceRow

'''
Solutions main. Only handles system variables and call for actual logic and ofcourse the printing for user.
First argument is filename of the xml-file and second argument is filename of csv-file but this one is optional as 
if second argument isn't given then it will automatically call it 'out.csv'.
'''
def main():
    if (len(sys.argv) < 2):
        print('you need to give atleast target XMLs filename!')
        return

    xmlPath = sys.argv[1]

    if (len(sys.argv) > 2):
        outPutPath = sys.argv[2]
    else:
        outPutPath = "out.csv"

#   collectiong names of columns in the invoice rows.
    InvoiceRowRecords = "fields/invoiceRowDetails.md"

    try:
        foo = Finvoice(xmlPath, InvoiceRowRecords)
        foo.writeCSV(outPutPath)
        print("successfully created a procountor csv file '" + outPutPath + "'")
    except ValueError:
        print("Oops! Somethings wrong...")

if __name__ == "__main__":
    main()

# coding=utf-8

from lxml import etree
from components.invoiceRow import InvoiceRow
from components.invoice import Invoice

'''
Reads the column names from the file thats name is given.
'''
def readRecordList(fileName):
    with open(fileName, 'r') as f:
        records = list(f)
#   maps each column name to be separate.
    cleanRecords = map(lambda x: x.rstrip(), records)
    return cleanRecords

'''
Class for the main logic of the program. Does the actual generating of the csv-file and also parsing for the xml-file.
It makes for the buyer and seller details own object and own for each row in the invoice after that.
'''
class Finvoice(object):
#   Gets xml-file as filename and makes it into xml tree.
    def __init__(self, xmlPath, InvoiceRowRecords):
        self._invoiceRecords = readRecordList("fields/invoiceDetails.md")
        self._invoiceRowRecords = InvoiceRowRecords
        parser = etree.XMLParser(encoding="ISO-8859-15")
        self._root = etree.parse(xmlPath, parser).getroot()
        self.__parseXML(xmlPath)

#   parses the xml tree.
    def __parseXML(self, xmlPath):
        self.invoice = Invoice(self._invoiceRecords, self._root)
        self.invoiceRows = self._root.findall("InvoiceRow")
    
    def writeCSV(self, outPutPath):
#       generates the list of csv-files rows.
        rows = []
        rows.append(self.invoice)
        for x in self.invoiceRows:
            temp = readRecordList(self._invoiceRowRecords)
            rows.append(InvoiceRow(temp, x))
        
        output = ""
        for x in rows:
            output += (x.toCSV() + '\n')

#       And for last writes the lines into the file which name was given.
        output = output.strip()
        with open(outPutPath, 'w') as f:
            f.write(output)



# coding=utf-8

from lxml import etree

'''
Super class for csv-files rows. Implemented child classes at the moment are Invoice and InvoiceRow classes.
'''
class Row(object):
    def __init__(self, records, xmlRoot):
        self._root = xmlRoot
        self.records = records
        self.fields = dict()
        self._parse()

    def toCSV(self):
        csvFields = map(self.__getRecord, self.records)
        output = ""
        
        for x in csvFields:
            output += (x + ';')
        
        return output

#   get the data of given column in the row this spesifies.
    def __getRecord(self, record):
        if (record in self.fields):
            return self.fields[record]
        return ''

#   Super method to parse the xml and make it ready to be printed into csv-file. 
#   This is supposed to be implemented by child classes.
    def _parse(self):
        pass

#   set data to given column.
    def _setElem(self, elemName, recordName):
        elem = self._root.find(elemName)
        if (elem is not None):
            self.fields[recordName] = elem.text



# coding=utf-8

from lxml import etree
from components.row import Row

'''
Class to make object out of each invoice row so that it is easier to make each product its own line.
'''
class InvoiceRow(Row):
    def _parse(self):
        self._setElem("ArticleName", "ArticleName")
        self._setElem("ArticleIdentifier", "ArticleIdentifier")
        self._setElem("OrderedQuantity", "OrderedQuantity")
        self._setElem("UnitPriceAmount", "UnitPriceAmount")
        self._setElem("RowVatRatePercent", "RowVatRatePercent")
        self.__setUnitCode()

    def __setUnitCode(self):
        quantity = self._root.find("OrderedQuantity")

        if (quantity is None):
            return

        unitCode = quantity.get("QuantityUnitCode")

        if (unitCode is None):
            return

        self.fields["QuantityUnitCode"] = unitCode


# coding=utf-8

from lxml import etree
import datetime
from components.row import Row

'''
CLass for invoice files main details like payment info.
'''
class Invoice(Row):
    def _parse(self):
        invoiceDetails = self._root.find("InvoiceDetails")
        self._setElem("BuyerPartyDetails/BuyerOrganisationName", "BuyerOrganisationName")
        self._setElem("BuyerPartyDetails/BuyerPartyIdentifier", "BuyerPartyIdentifier")
        self._setElem("InvoiceDetails/InvoiceFreeText", "InvoiceFreeText")
        self._setElem("InvoiceDetails/InvoiceTypeCode", "InvoiceTypeCode")
        self._setElem("InvoiceDetails/PaymentTermsDetails/PaymentOverDueFineDetails/PaymentOverDueFinePercent", "PaymentOverDueFinePercent")
        self.__setBuyerPostalAddr()
        self.__setCurrency()
        self.__setDeliveryPostalAddr()
        self.__setInvoiceDate()

#        this field cannot be read from the sample xml. We'll thus expect it to be '2'
        self.fields["InvoiceMethod"] = '2'

    def __setCurrency(self):
        vatExcluded = self._root.find("InvoiceDetails/InvoiceTotalVatExcludedAmount")
        vatAmount = self._root.find("InvoiceDetails/InvoiceTotalVatAmount")
        vatIncluded = self._root.find("InvoiceDetails/InvoiceTotalVatIncludedAmount")

        elements = [vatExcluded, vatAmount, vatIncluded]

        element = next((item for item in elements if item is not None), None)

        if (element is None):
            return

        currency = element.get("AmountCurrencyIdentifier")

        if (currency):
            self.fields["AmountCurrencyIdentifier"] = currency

    def __setInvoiceDate(self):
        elem = self._root.find("InvoiceDetails/InvoiceDate")

        if (elem is None):
            return

        dateFormat = elem.get("Format")

        if (dateFormat is None):
            return

#       Python's date libraries can't handle the date format in the xml
        try:
            dateFormat = dateFormat.replace('C', '').replace("YY", "%Y").replace("MM", "%m").replace("DD", "%d")
            self.fields["InvoiceDate"] = datetime.datetime.strptime(elem.text, dateFormat).strftime('%d.%m.%Y')
        except ValueError as e:
            return

    def __setBuyerPostalAddr(self):
        name = self._root.find("BuyerPartyDetails/BuyerOrganisationName").text
        addressDetails = self._root.find("BuyerPartyDetails/BuyerPostalAddressDetails")

        if (addressDetails is None):
            return

        countryCodeElem = addressDetails.find("CountryCode")

        if (countryCodeElem is None):
            return

        street = addressDetails.find("BuyerStreetName").text
        town = addressDetails.find("BuyerTownName").text
        postCode = addressDetails.find("BuyerPostCodeIdentifier").text
        countryCode = countryCodeElem.text

        self.fields["BuyerPostalAddress"] = '\\'.join([name, street, postCode, town, countryCode])

    def __setDeliveryPostalAddr(self):
        name = self._root.find("DeliveryPartyDetails/DeliveryOrganisationName").text
        addressDetails = self._root.find("DeliveryPartyDetails/DeliveryPostalAddressDetails")

        if (addressDetails is None):
            return

        countryCodeElem = addressDetails.find("CountryCode")

        if (countryCodeElem is None):
            return

        street = addressDetails.find("DeliveryStreetName").text
        town = addressDetails.find("DeliveryTownName").text
        postCode = addressDetails.find("DeliveryPostCodeIdentifier").text
        countryCode = countryCodeElem.text

        self.fields["DeliveryPostalAddress"] = '\\'.join([name, street, postCode, town, countryCode])


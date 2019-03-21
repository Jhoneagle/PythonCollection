# Python collection

Contains self made python scripts

## Scripts

multitasker: Simple code for doing some clean up to text-files. Example after pasteing the text from pdf-file. Also makes the text-files little bit more accessible to read because replaces non letter symbols with longer equivalent. Executable only from commandline. Excution can be done following way: _python3 Multitasker.py (text-files name/location)_.

finvoiceConverter: Simple XML -> SCV converter for finvoice formatted files. Standard bases on Procountors SCV imports acceptance criterias.

HTTPrequests: Commandline program to make HTTP-requests of GET, POST and PUT type. First command line param is url you want to make it, second is the type between GET, POST and PUT and after that in case not GET the filename/location of json file which to send and on GET file where the possibly needed params are as third commandline param. So basically the commandline executions is following. GET: _python3 HTTPrequests.py (url) (type of http request) (files name/location of possible params)_ and POST/PUT: _python3 HTTPrequests.py (url) (type of http request) (json-files name/location)_.
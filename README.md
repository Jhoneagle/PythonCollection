# Python collection

Contains self made python scripts

## Scripts

multitasker: simple code for doing some clean up to text-files. Example after pasteing the text from pdf-file. also makes the text-files little bit more accessible to read because replaces non letter symbols with longer equivalent. 

finvoiceConverter: Simple XML -> SCV converter for finvoice formatted files. Standard bases on Procountors SCV imports acceptance criterias.

HTTPrequests: commandline program to make HTTP-requests of GET, POST and PUT type. first command line param is url you want to make it, second is the type between GET, POST and PUT and after that in case not GET the filename/location of json file which to send and on GET the needed params as thrid commandline param. so basically the commandline executions is following. GET: _python3 HTTPrequests.py (url) (type of http request) (possible params)_ and POST/PUT: _python3 HTTPrequests.py (url) (type of http request) (json-files name/location)_.
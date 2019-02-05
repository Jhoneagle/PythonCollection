# Converter

Program to convert finvoice xml-files into csv files that procounter can accept.

## How to use

- Program contains 'requirements.txt' so basically if your using virtual python enviroment (like venv) then run it or just pass this if use global python. However it is recommented to have python 3.5 or newer. Run command 'pip install -r requirements.txt' to get needed librarys which in this case is lxml.

- After that you can just type '*spisification of python call* XMLtoCSV.py *filename of xml-file* *filename of csv-file*'. For me the first part is 'py' as I have made enviroment variable to connect that into python i have. the second and third are also mandatory but the csv filename is optional. If you don't give name for output file then it automatically generates 'out.csv'.

- Then it just responds with line telling if operation succeed or not.
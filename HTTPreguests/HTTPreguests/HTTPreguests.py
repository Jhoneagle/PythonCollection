import requests
import sys, os
import json

def main():
    if (len(sys.argv) < 3):
        print('you need to give atleast url and HTTP-reguest type!')
        return

    url = sys.argv[1]
    type = sys.argv[2]

    if (type == 'POST' or type == 'PUT'):
        if (len(sys.argv) < 4):
            print('you also need to give json filename!')
            return

        with open(sys.argv[3]) as json_file:  
            data = json.load(json_file)
            
            # sending post request and saving response as response object 
            r = requests.post(url, json = data) 
            
            text = r.text 
            print(text) 
    else:
        params = ''
        
        if (len(sys.argv) >= 4):
            f = open(sys.argv[3], "r")
            params = f.read()
        
        # sending get request and saving the response as response object 
        r = requests.get(url, params = params) 

        # extracting data in json format 
        data = r.json() 

        # printing the output 
        print(data) 

if __name__ == "__main__":
    main()
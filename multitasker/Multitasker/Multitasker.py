'''
Python code for cleaning text files so that it could be more accessable to read. 
Mostly able to fix only common mistakes like forced line changes, splitted words and uncommon symbols.

@author: Johneagle
'''

import sys, os

if __name__ == "__main__":
    path = sys.argv[2]

    name = path.split('.')[0]

    newPath = name + 'Done.md'
    newF = open(newPath, "w", encoding="utf-8")

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parse = list(line)
            length = len(parse)

            if (length == 1):
                newF.write(str('\n'))
                newF.write(str('\n'))
                continue

            if (parse[length - 3] == '.' or parse[length - 3] == '!' or parse[length - 3] == '?'):
                if (parse[length - 2] == ' ' or parse[length - 2] == '"'):
                    parse.append('\n')
                    parse.append('\n')

            if (parse[length - 3] == chr(45) or parse[length - 3] == chr(126) or parse[length - 3] == chr(172)):
                if (parse[length - 2] == ' '):
                    parse[length - 3] = ''
                    parse[length - 2] = ''

            if (parse[length - 2] != '.' and parse[length - 2] != '!' and parse[length - 2] != '?'):
                if (parse[length - 2] == chr(45) or parse[length - 2] == chr(126) or parse[length - 2] == chr(172)):
                    parse[length - 2] = ''
                    parse[length - 1] = ''
                else:
                    parse[length - 1] = ' '
            else:
                parse.append('\n')
            
            result = ''
            point = 0

            for char in parse:
                if (char == ' '):
                    if (0 <= (point - 1) and len(parse) > (point + 1)):
                        if (parse[point - 1].isupper() and parse[point + 1].isupper()):
                            char = ''
                        if (parse[point + 1] == ' '):
                            char = ''

                if (char == chr(189)):
                    char = '1/2'

                if (char == chr(188)):
                    char = '1/4'

                if (char == chr(190)):
                    char = '3/4'

                if (char == chr(8364)):
                    char = 'euroa'

                point += 1
                result += str(char)

            if ('ENITEN' in result):
                result = result[:6] + ' ' + result[6:]

            if ('VALMISTUSAIKA' in result):
                result = result[:13] + ' ' + result[13:]

            if ('TEKSTIJAKUVAT' in result and 'TEKSTI JA KUVAT:' not in result):
                result = result[:6] + ' ' + result[6:8] + ' ' + result[8:13] + ': ' + result[13:]

            if ('TEKSTIJATYYLI' in result and 'TEKSTI JA TYYLI:' not in result):
                result = result[:6] + ' ' + result[6:8] + ' ' + result[8:13] + ': ' + result[13:]

            if ('TEKSTI' in result and 'TEKSTI:' not in result and 'TEKSTI JA' not in result):
                result = result[:6] + ': ' + result[6:]

            if ('KUVAUS' in result and 'KUVAUS:' not in result):
                result = result[:6] + ': ' + result[6:]

            if ('KUVAT' in result and 'KUVAT:' not in result):
                result = result[:5] + ': ' + result[5:]

            if ('KUVA' in result and 'KUVA:' not in result and 'KUVAT:' not in result and 'KUVALEHTI' not in result):
                result = result[:4] + ': ' + result[4:]

            if ('KOONNUT' in result and 'KOONNUT:' not in result):
                result = result[:7] + ': ' + result[7:]

            if ('KOONNEET' in result and 'KOONNEET:' not in result):
                result = result[:8] + ': ' + result[8:]

            if ('TYYLIT' in result and 'TYYLIT:' not in result and 'TYYLI:' not in result):
                result = result[:6] + ': ' + result[6:]

            if ('TYYLI' in result and 'TYYLIT:' not in result and 'TYYLI:' not in result):
                result = result[:5] + ': ' + result[5:]

            newF.write(str(result))

    newF.close()

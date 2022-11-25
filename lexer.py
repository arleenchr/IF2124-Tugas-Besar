import re #regex
import sys
from token import list_token

def lexer(inputText,listToken):
    # Membuat lexer untuk parsing program js
    # Contoh:  "int a = 3;" di-split menjadi 5 lexemes: "int, a, =, 3, ;"
    currentChar = 0 #indeks yang menunjuk tiap karakter dalam input teks
    currentLine = 1 #indeks yang menunjuk baris dalam input teks
    lexemes = []
    
    while (currentChar<len(inputText)):
        if (inputText[currentChar]=='\n'):
            currentLine += 1 # jika baris baru, indeks penunjuk currentLine bertambah
        
        for tkn in listToken:
            # iterasi semua elemen di list_token
            regexPattern, token = tkn
            #print(regexPattern)
            regex = re.compile(regexPattern) # compile regex
            match = regex.match(inputText,currentChar) # cari token yang match
            if (match != None):
                if token:
                    lexemes.append(token)
                break
        if (match == None):
            print("Syntax Error")
            sys.exit()
        else:
            currentChar = match.end(0) # update currentChar menunjuk ke setelah suatu token
    #print(lexemes)
    return lexemes

def tokenToStr(filename):
    file = open(filename)
    text = file.read()
    file.close()
    lexemes = lexer(text,list_token)
    return " ".join(lexemes)

#print(tokenToStr('testing.js'))
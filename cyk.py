# Cocke Younger Kasami (CYK) Algorithm

from convert_to_cfg import *
from convert_to_cnf import *

def cyk(cnf,inputStr):
    # parameter input CNF (dicitonary) dan string input
    arrInputStr = inputStr.split() # stringnya ditulis dalam array
    cykTable = [[set([]) for j in range (len(arrInputStr))] for i in range (len(arrInputStr))]
    
    '''
    Misal CYK Table 5x5
      0 1 2 3 4
    0 1 2 3 4 5
    1   1 2 3 4
    2     1 2 3
    3       1 2
    4         1
    cykTable[0][1] cek dari [0][0]&[1][1]
    cykTable[1][2] cek dari [1][1]&[2][2]
    cykTable[2][3] cek dari [2][2]&[3][3]
    cykTable[3][4] cek dari [3][3]&[4][4]
    
    cykTable[0][2] cek dari [0][0]&[1][2] dan [0][1]&[2][2]
    cykTable[1][3] cek dari [1][1]&[2][3] dan [1][2]&[3][3]
    cykTable[2][4] cek dari [2][2]&[3][4] dan [2][3]&[4][4]
    
    cykTable[0][3] cek dari [0][0]&[1][3] dan [0][1]&[2][3] dan [0][2]&[3][3]
    cykTable[1][4] cek dari [1][1]&[2][4] dan [1][2]&[3][4] dan [1][3]&[4][4]
    
    cykTable[0][4] cek dari [0][0]&[1][4] dan [0][1]&[2][4] dan [0][2]&[3][4] dan [0][3]&[4][4]
    '''
    
    for i in range (len(arrInputStr)):
        for kiri,kanan in cnf.items():
            for var in kanan:
                if (len(var)==1) and (var[0]==arrInputStr[i]):
                    cykTable[i][i].add(kiri) # untuk input 1 string
    
        for x in range (i,-1,-1):
            for y in range (x,i):
                for kiri,kanan in cnf.items():
                    for prod in kanan:
                        if (len(prod)==2) and (prod[0] in cykTable[x][y]) and (prod[1] in cykTable[y+1][i]):
                            cykTable[x][i].add(kiri)
    
    '''
    for k in range(2, len(arrInputStr)+1):
        for i in range (0, (len(arrInputStr)-k+1)):
            j = i + k - 1
            for k in range (i,j):   
                for var,prods in cnf.items():
                    for prod in prods:
                        if (len(prod)==2):
                            if (prod[0] in cykTable[i][k]) and (prod[1] in cykTable[k+1][j]): 
                                cykTable[i][j].add(var)
    '''
    #print(cykTable[0][len(arrInputStr)-1])
    #print(cykTable)
    
    if ('0' not in cykTable[0][len(arrInputStr)-1]):
        return True # acceptable
    else:
        return False # rejected
    

#print(cyk(cfg_to_cnf(file_to_cfg("grammar.txt")),"LET ID EQ INT NEWLINE ID TAMBAH EQ INT"))
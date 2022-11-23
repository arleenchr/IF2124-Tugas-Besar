from convert_to_cfg import *

def cfg_to_cnf(cfg):
    '''
    Langkah CFG to CNF:
    0. Jika ada symbol S di kanan, buat start symbol baru S' dan production S'->S
    1. Hapus null productions
       - definisikan nullable variables, yaitu yang bisa diturunkan menjadi string kosong
       - contoh: A->e atau B->A, A->e
       - Hapus nullable variables, lalu ganti semua production yang mengandung nullable variables
    2. Hapus unit productions
       - unit productions adalah aturan produksi yang kanannya hanya terdiri dari satu variable
       - contoh: A->B
    3. Hapus useless variables (yang tidak dicapai start symbol)
    4. Ubah ke bentuk A->BC (minimal 2 variables) atau A->a (single terminal)
    '''
    # cfg berbentuk dictionary
    # Langkah 0: Jika ada symbol S di kanan, buat start symbol baru S' dan production S'->S
    arrHead = list(cfg.keys())
    arrBody = list(cfg.values())
    startSymbol = arrHead[0] # start symbol adalah elemen pertama pada head
    addProduction = False
    
    for production in arrBody:
        for prod in production:
            if (startSymbol in prod):
                # jika di "kanan" ada start symbol, maka buat production baru
                addProduction = True
                break
        if addProduction:
            break
    
    # buat production baru
    if addProduction:
        newVar = {"S0" : [[startSymbol]]} # S0->S
        newVar.update(cfg) # insert cfg
        cfg = newVar
    
    # Langkah 1 (pada program ini tidak ada kasus nullable variables)
    # Langkah 2: Hapus Unit Productions
    isUnitProd = True
    
    while isUnitProd:
        unitProd = {} # empty dictionary
        isUnitProd = False
        for kiri,kanan in cfg.items():
            for var in kanan:
                if (len(var)==1) and (is_variabel(var[0])):
                    isUnitProd = True # jika hanya 1 variabel, maka unit production
                    if (kiri not in unitProd.keys()):
                        unitProd[kiri] = [[var[0]]] # symbolnya ditambahkan ke unitProd
                    else:
                        unitProd[kiri].append([var[0]]) # append ke unitProd
        
        # salin unit production
        for kiriUnitProd, kananUnitProd in unitProd.items():
            for varUnitProd in kananUnitProd:
                for kiri,kanan in cfg.items():
                    if (len(varUnitProd)==1) and (kiri==varUnitProd[0]):
                        newVar = {kiriUnitProd : kanan} # salin unit production
                        if (kiriUnitProd in cfg.keys()):
                            for var in kanan:
                                if (var not in cfg[kiriUnitProd]):
                                    cfg[kiriUnitProd].append()(var)
                        else:
                            cfg[kiriUnitProd] = kanan
        
        # hapus unit production
        for kiriUnitProd, kananUnitProd in unitProd.items():
            for varUnitProd in kananUnitProd:
                if (len(varUnitProd)==1):
                    cfg[kiriUnitProd].remove(varUnitProd)
            
    # Langkah 3 (pada program ini tidak akan ada useless variables)
    # Langkah 4: Ubah ke bentuk A->BC (minimal 2 variables) atau A->a (single terminal)
    newProd = {}
    delProd = {}
    
    counter = 0
    for kiri,kanan in cfg.items():
        for var in kanan:
            symbol = kiri
            tempVar = [v for v in var]
            if (len(tempVar)>2):
                while (len(tempVar)>2):
                    newSymbol = "X"+str(counter) # buat symbol baru
                    if (symbol not in newProd.keys()):
                        newProd[symbol] = [[tempVar[0],newSymbol]]
                    else:
                        newProd[symbol].append()([tempVar[0],newSymbol])
                    symbol = newSymbol
                    tempVar.remove(tempVar[0])
                    counter += 1
                else:
                    if (symbol not in newProd.keys()):
                        newProd[symbol] = [tempVar]
                    else:
                        newProd[symbol].append(tempVar)
                    if (kiri not in delProd.keys()):
                        delProd[kiri] = [var]
                    else:
                        delProd[kiri].append(var)
    
    for newKiri, newKanan in newProd.items():
        if (newKiri not in cfg.keys()):
            cfg[newKiri] = newKanan
        else:
            cfg[newKiri].extend(newKanan)
    for delKiri, delKanan in delProd.items():
        for delVar in delKanan:
            cfg[delKiri].remove(delVar)
            
    # Ubah terminal jadi variabel
    newProd = {}
    delProd = {}
    counter1 = 0
    counter2 = 0
    
    for kiri,kanan in cfg.items():
        for var in kanan:
            if (len(var)==2) and is_terminal(var[0]) and is_terminal(var[1]):
                newSymbol1 = "Y"+str(counter1)
                newSymbol2 = "Z"+str(counter2)
                if (kiri not in newProd.keys()):
                    newProd[kiri] = [[newSymbol1,newSymbol2]]
                else:
                    newProd[kiri].append([newSymbol1,newSymbol2])
                
                newProd[newSymbol1] = [[var[0]]]
                newProd[newSymbol2] = [[var[1]]]
                
                if (kiri not in delProd.keys()):
                    delProd[kiri] = [var]
                else:
                    delProd[kiri].append(var)
                
                counter1 += 1
                counter2 += 1
                
            elif (len(var)==2) and is_terminal(var[0]):
                newSymbol1 = "Y"+str(counter1)
                if (kiri not in newProd.keys()):
                    newProd[kiri] = [[newSymbol1,var[1]]]
                else:
                    newProd[kiri].append([newSymbol1,var[1]])
                
                newProd[newSymbol1] = [[var[0]]]
                
                if (kiri not in delProd.keys()):
                    delProd[kiri] = [var]
                else:
                    delProd[kiri].append(var)
                
                counter1 += 1
            
            elif (len(var)==2) and is_terminal(var[1]):
                newSymbol2 = "Z"+str(counter2)
                if (kiri not in newProd.keys()):
                    newProd[kiri] = [[var[0],newSymbol2]]
                else:
                    newProd[kiri].append([var[0],newSymbol2])
                
                newProd[newSymbol2] = [[var[1]]]
                
                if (kiri not in delProd.keys()):
                    delProd[kiri] = [var]
                else:
                    delProd[kiri].append(var)
                
                counter2 += 1
    
    for newKiri, newKanan in newProd.items():
        if (newKiri not in cfg.keys()):
            cfg[newKiri] = newKanan
        else:
            cfg[newKiri].extend(newKanan)
    for delKiri, delKanan in delProd.items():
        for delVar in delKanan:
            cfg[delKiri].remove(delVar)
    
    return cfg

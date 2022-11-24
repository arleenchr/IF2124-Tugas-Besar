# Finite set of states (Q)
# Finite set of input symbols (Σ)
# Transition function (δ)

# Q = {start, dead, final}
# Σ = {
#   uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#   lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#   digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#   specialsign = ['_', '$']
# }

transition = [["start", "uppercase", "final"], 
            ["start", "lowercase", "final"], 
            ["start", "digits", "dead"],
            ["start", "specialsign", "final"],
            ["start", "specialsign", "final"],
            ["dead", "uppercase", "dead"],
            ["dead", "lowercase", "dead"],
            ["dead", "digits", "dead"],
            ["dead", "specialsign", "dead"],
            ["final", "uppercase", "final"],
            ["final", "lowercase", "final"],
            ["final", "digits", "final"],
            ["final", "specialsign", "final"]]

uppercase       = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase       = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits          = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialsign     = ['_', '$']
reservedwords   = ["break", "null", "public", "in", "eval", "continue", "true", "false", "boolean", "case", "catch", "debugger", "default", "delete", "do", "finally", "for", 
                "function", "if", "in", "instanceof", "new", "return", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with", 'abstract', 'arguments', 'byte', 'char', 'double', 'const', 'double', 'else']
operation       = ['-', '+', '*', '/', '%']

def startState(char):
    global state
    if (char in uppercase) or (char in lowercase) or (char in specialsign):
        state = "final"
    else :
        state = "dead"
    return state

def finalState(char):
    global state
    if (char not in uppercase) and (char not in lowercase) and (char not in specialsign):
        state = "dead"
    else :
        state = "final"
    return state

def deadState(char):
    global state
    state = "dead"
    return state

def check_variabel_name(str):
    global state
    state = "start"

    if (str in reservedwords):
        state = "dead"

    for i in range (len(str)):
        if (state == "start") :
            state = startState(str[i])
        elif (state == "final") :
            state = finalState(str[i])
        elif (state == "dead") :
            state = "dead"
            break

    if (state == "final") :
        return True
    elif (state == "dead") :
        return False

def startEquation(char, charnext):
    global stateEq

    if (char == '-') and ((charnext == '-') or (charnext == '+')):
        stateEq = "dead"
    elif (char == '-') or (char in digits):
        stateEq = "final"
    else :
        stateEq = "dead"
    return stateEq

def deadEquation(char):
    global stateEq
    stateEq = "dead"
    return stateEq

def finalEquation(char):
    global stateEq
    if (char not in digits) and (char not in operation):
        stateEq = "dead"
    else :
        stateEq = "final"
    return stateEq

def check_equation(str):
    global stateEq
    stateEq = "start"

    for i in range (len(str)):
        if (stateEq == "start") :
            stateEq = startEquation(str[i], str[i+1])
        elif (stateEq == "final") :
            if (str[len(str)-1] in operation):
                stateEq = "dead"
            else :
                stateEq = finalEquation(str[i])
        elif (stateEq == "dead") :
            stateEq = "dead"
            break

    if (stateEq == "final") :
        return True
    elif (stateEq == "dead") :
        return False
    
# testing

# var = "123dasda"
# if(check_variabel_name(var)) :
#     print ("Accepted")
# else :
#     print("Syntax Error")

eq = "55+"
if(check_equation(eq)) :
    print ("Accepted")
else :
    print("Syntax Error")
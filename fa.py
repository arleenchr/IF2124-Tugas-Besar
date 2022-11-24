# Finite set of states (Q)
# Finite set of input symbols (Σ)
# Transition function (δ)

# Q = {start, dead, final}
# Σ = {
#   uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#   lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#   digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#   specialsign = ['_', '$']
#   else = []
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

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialsign = ['_', '$']
reservedwords = ["break", "null", "public", "in", "eval", "continue", "true", "false", "boolean", "case", "catch", "debugger", "default", "delete", "do", "finally", "for", 
                "function", "if", "in", "instanceof", "new", "return", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with"]
others = [' ']

global state
state = ''

def startState(char):
    global state
    if (char in uppercase) or (char in lowercase) or (char in specialsign):
        state = "final"
        # print("YES")
    else :
        state = "dead"
    return state

def finalState(char):
    global state
    if (char in others):
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
        if (state == "final") :
            state = finalState(str[i])
        if (state == "dead") :
            state = "dead"
            break

    if (state == "final") :
        return True
    elif (state == "dead") :
        return False

# def check_operation():
    

# startState("A")
# testing
var = "austin"
if(check_variabel_name(var)) :
    print ("Accepted")
else :
    print("Syntax Error")


list_terminal = [
    "OP_ROUND_BRACKET",
    "CL_ROUND_BRACKET",
    "OP_SQUARE_BRACKET",
    "CL_SQUARE_BRACKET",
    "OP_CURLY_BRACKET",
    "CL_CURLY_BRACKET",

    "TITIKKOMA",
    "TITIKDUA",
    "TITIK",
    "KOMA",
    "PETIKSATU",
    "PETIKDUA",
    
    "TAMBAH",
    "KURANG",
    "KALI",
    "BAGI",
    "MOD",
    "PANGKAT",
    
    "TAMBAHSD",
    "KURANGSD",
    "KALISD",
    "BAGISD",
    "MODSD",
    "PANGKATSD",
    
    "INCREMENT",
    "DECREMENT",
    
    "LESS",
    "LEQ",
    "GREATER",
    "GEQ",
    "ISNEQ",
    "ISNEQTYPE",
    "EQ",
    "ISEQ",
    "ISEQTYPE",
    "TERNARY",
    
    "AND",
    "OR",
    "NOT",

    "LET",
    "VAR",
    "CONST",

    "TRUE",
    "FALSE",
    "NULL",
    "DELETE",

    "IF",
    "ELSE",
    "SWITCH",
    "CASE",
    "DEFAULT",

    "WHILE",
    "FOR",

    "CONTINUE",
    "BREAK",
    "FUNCTION",
    "RETURN",

    "TRY",
    "CATCH",
    "FINALLY",
    "THROW",

    "NULL",
    
    "ID",
    "TYPE",
    "INT",
    "STRING",
    "MULTILINE",
    "NEWLINE"
]


def file_to_cfg(filename):
    file = open(filename, 'r')
    cfg = {}

    row = file.readline()
    while (row != ''):
        head, body = row.replace('\n', '').split(' -> ')

        if (head not in cfg.keys()):
            cfg[head] = [body.split(' ')]
        else:
            cfg[head].append(body.split(' '))
        row = file.readline()

    file.close()
    # print(cfg)
    return cfg


def is_terminal(string):
    return string in list_terminal


def is_variabel(string):
    return string not in list_terminal


#file_to_cfg('ref.txt')
list_terminal = [
    "EQ",
    "ISEQ",
    "KBKI",
    "KBKA",
    "TITIKKOMA",
    "TITIKDUA",
    "ADD",
    "SUB",
    "MUL",
    "DIV",
    "MOD",
    "POW",
    "FLOORDIV",
    "LEQ",
    "L",
    "GEQ",
    "G",
    "NEQ",
    "SUBAS",
    "MULAS",
    "SUMAS",
    "DIVAS",
    "MODAS",
    "POWAS",
    "FLOORDIVAS",
    "AND",
    "OR",
    "NOT",
    "IF",
    "THEN",
    "ELSE",
    "ELIF",
    "WHILE",
    "RANGE",
    "FALSE",
    "TRUE",
    "NONE",
    "BREAK",
    "AS",
    "CLASS",
    "CONTINUE",
    "DEF",
    "FOR",
    "FROM",
    "FORMAT",
    "IMPORT",
    "IN",
    "IS",
    "RETURN",
    "RAISE",
    "PASS",
    "WITH",
    "COMMA",
    "KARTITIK",
    "TITIK",
    "PETIKSATU",
    "PETIKDUA",
    "KSKI",
    "KSKA",
    "KKKI",
    "KKKA",
    "INT",
    "STRING",
    "MULTILINE",
    "ID",
    "NEWLINE",
    "TYPE",
    "ARROW"
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


file_to_cfg('ref.txt')
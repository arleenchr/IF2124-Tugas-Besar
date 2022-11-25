global list_token
list_token = [
    (r'[ \t]+',      None),           # tab
    (r'\/\/[^\n]*',  None),           # comment single line
    (r'[\t]*\/\*[\w\W]*\*\/',  None), # comment multi lines

    # Integer and String
    (r'\"[^\"\n]*\"',           "STRING"), # pakai petik dua
    (r'\'[^\'\n]*\'',           "STRING"), # pakai petik satu
    (r'[\+\-]?[1-9]+',          "INT"),    # angka bulat
    (r'[\+\-]?[0-9]*\.[0-9]+',  "FLOAT"),  # angka desimal

    # Delimiter
    (r'\n', "NEWLINE"),
    (r'\(', "OP_ROUND_BRACKET"),
    (r'\)', "CL_ROUND_BRACKET"),
    (r'\[', "OP_SQUARE_BRACKET"),
    (r'\]', "CL_SQUARE_BRACKET"),
    (r'\{', "OP_CURLY_BRACKET"),
    (r'\}', "CL_CURLY_BRACKET"),

    (r'\;', "TITIKKOMA"),
    (r'\:', "TITIKDUA"),
    (r'\,', "KOMA"),
    (r'\.', "TITIK"),

    # Arithmetic Operators
    (r'\+',    "TAMBAH"),
    (r'\-',    "KURANG"),
    (r'\*',    "KALI"),
    (r'\/',    "BAGI"),
    (r'\%',    "MOD"),
    (r'\*\*',  "PANGKAT"),
    
    (r'\+=',   "TAMBAHSD"),  # tambah sama dengan -> +=
    (r'\-=',   "KURANGSD"),  # kurang sama dengan -> -=
    (r'\*=',   "KALISD"),    # kali sama dengan -> *=
    (r'\/=',   "BAGISD"),    # bagi sama dengan -> /=
    (r'\%=',   "MODSD"),     # mod sama dengan -> %=
    (r'\*\*=', "PANGKATSD"), # pangkat sama dengan -> **=

    (r'\+\+',  "INCREMENT"),
    (r'\-\-',  "DECREMENT"),
    
    # Comparison Operators
    (r'<',      "LESS"),      # less
    (r'<=',     "LEQ"),       # less equal
    (r'>',      "GREATER"),   # greater
    (r'>=',     "GEQ"),       # greater equal
    (r'!=',     "ISNEQ"),     # !=
    (r'!==',    "ISNEQTYPE"), # !==
    (r'=',      "EQ"),        # ==
    (r'==',     "ISEQ"),      # ==
    (r'===',    "ISEQTYPE"),  # ===
    (r'?',      "TERNARY"),   # ? ternary operator

    # Logical Operators
    (r'&&',     "AND"),
    (r'\|\|',   "OR"),
    (r'!',      "NOT"),

    # Keyword
    (r'\blet\b',        "LET"),
    (r'\bvar\b',        "VAR"),
    (r'\bconst\b',      "CONST"),

    (r'\btrue\b',       "TRUE"),
    (r'\bfalse\b',      "FALSE"),
    (r'\bnull\b',       "NULL"),
    (r'\bdelete\b',     "DELETE"),
    
    (r'\bif\b',         "IF"),
    (r'\belse\b',       "ELSE"),
    (r'\bswitch\b',     "SWITCH"),
    (r'\bcase\b',       "CASE"),
    (r'\bdefault\b',    "DEFAULT"),

    (r'\bwhile\b',      "WHILE"),
    (r'\bfor\b',        "FOR"),
    
    (r'\bcontinue\b',   "CONTINUE"),
    (r'\bbreak\b',      "BREAK"),

    (r'\bfunction\b',   "FUNCTION"),
    (r'\breturn\b',     "RETURN"),
    
    (r'\btry\b',        "TRY"),
    (r'\bcatch\b',      "CATCH"),
    (r'\bfinally\b',    "FINALLY"),
    (r'\bthrow\b',      "THROW"),
    
    (r'\bnull\b',       "NULL"),
    
    (r'\bobject\b',     "TYPE"),
    (r'\bint\b',        "TYPE"),
    (r'\bstr\b',        "TYPE"),
    (r'\bfloat\b',      "TYPE"),

    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),

    (r'\/\/[^\n]*',                   "SINGLELINE"),
    (r'\/\*[(?!(\"\"\"))\w\W]*\*\/',  "MULTILINE")
]


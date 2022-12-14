global list_token
list_token = [
    (r'[ \t]+',      None),           # tab
    (r'\/\/[^\n]*',  None),           # comment single line
    (r'[\t]*\/\*[\w\W]*\*\/',  None), # comment multi lines

    # Integer and String
    (r'\"[^\"\n]*\"',           "STRING"), # pakai petik dua
    (r'\'[^\'\n]*\'',           "STRING"), # pakai petik satu
    (r'[\+\-]?[0-9]*\.[0-9]+',  "FLOAT"),  # angka desimal
    (r'[\+\-]?[0-9]+',          "INT"),    # angka bulat

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
    
    # Comparison Operators
    (r'<=',     "LEQ"),       # less equal
    (r'<',      "LESS"),      # less
    (r'>=',     "GEQ"),       # greater equal
    (r'>',      "GREATER"),   # greater
    (r'!==',    "ISNEQTYPE"), # !==
    (r'!=',     "ISNEQ"),     # !=
    (r'===',    "ISEQTYPE"),  # ===
    (r'==',     "ISEQ"),      # ==
    (r'=',      "EQ"),        # ==
    (r'\?',      "TERNARY"),   # ? ternary operator
    
    (r'\+=',   "TAMBAHSD"),  # tambah sama dengan -> +=
    (r'\-=',   "KURANGSD"),  # kurang sama dengan -> -=
    (r'\*=',   "KALISD"),    # kali sama dengan -> *=
    (r'\/=',   "BAGISD"),    # bagi sama dengan -> /=
    (r'\%=',   "MODSD"),     # mod sama dengan -> %=
    (r'\*\*=', "PANGKATSD"), # pangkat sama dengan -> **=

    (r'\+\+',  "INCREMENT"),
    (r'\-\-',  "DECREMENT"),
    
    # Arithmetic Operators
    (r'\+',    "TAMBAH"),
    (r'\-',    "KURANG"),
    (r'\*',    "KALI"),
    (r'\/',    "BAGI"),
    (r'\%',    "MOD"),
    (r'\*\*',  "PANGKAT"),
    
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
    (r'\$[A-Za-z_][A-Za-z0-9_]*', "ID"),
    (r'\_[A-Za-z_][A-Za-z0-9_]*', "ID"),
    
    (r'\/\/[^\n]*',                   "SINGLELINE"),
    (r'\/\*[(?!(\"\"\"))\w\W]*\*\/',  "MULTILINE")
]
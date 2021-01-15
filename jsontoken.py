
ILLEGAL = "ILLEGAL"

COMMA = ','
COLON = ':'
LBRACE = '{'
RBRACE = '}'
LBRACKET = '['
RBRACKET = ']'
MINUS = "-"
STRING = "STRING"
INT = "INTEGER"
TRUE = "TRUE"
FALSE = "FALSE"
NULL = "NULL"
EOF = "EOF"

class Token:
    token = ""
    literal = ""
    def __init__(self, token, literal):
        self.token = token
        self.literal = literal

def lookup_literal(s):
    keywords = {
        "true": TRUE,
        "false": FALSE,
        "null": NULL,
    }
    t = keywords.get(s)
    if t != None:
        return t
    else:
        return ILLEGAL
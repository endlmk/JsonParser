
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
EOF = "EOF"

class Token:
    token = ""
    literal = ""
    def __init__(self, token, literal):
        self.token = token
        self.literal = literal
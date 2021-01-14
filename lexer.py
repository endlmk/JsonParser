import jsontoken

class Lexer:
    """
    Lexer for Json Parser
    """
    _input = ""
    _position = 0
    _read_position = 0
    _ch = ''

    def __init__(self, input):
        self._input = input
        self._read_char()

    def next_token(self):
        self._skip_whitespaces()

        if self._ch == '{':
            tok = jsontoken.Token(jsontoken.LBRACE, self._ch)
        elif self._ch == '}':
            tok = jsontoken.Token(jsontoken.RBRACE, self._ch)
        elif self._ch == '[':
            tok = jsontoken.Token(jsontoken.LBRACKET, self._ch)
        elif self._ch == ']':
            tok = jsontoken.Token(jsontoken.RBRACKET, self._ch)
        elif self._ch == ',':
            tok = jsontoken.Token(jsontoken.COMMA, self._ch)
        elif self._ch == ':':
            tok = jsontoken.Token(jsontoken.COLON, self._ch)
        elif self._ch == '-':
            tok = jsontoken.Token(jsontoken.MINUS, self._ch)
        elif self._ch == '"':
            s = self._read_string()
            tok = jsontoken.Token(jsontoken.STRING, s)
        elif self._ch == '\0':
            tok = jsontoken.Token(jsontoken.EOF, '')
        else:
            if self._ch.isdigit():
                n = self._read_number()
                return jsontoken.Token(jsontoken.INT, n)
            else:
                tok = jsontoken.Token(jsontoken.ILLEGAL, self._ch)
        
        self._read_char()
        return tok

    def _read_char(self):
        if self._read_position >= len(self._input):
            self._ch = '\0'
        else:
            self._ch = self._input[self._read_position]
        
        self._position = self._read_position
        self._read_position += 1
        return 

    def _skip_whitespaces(self):
        while self._ch in {' ', '\t', '\n', '\r'}:
            self._read_char()
    
    def _read_string(self):
        self._read_char()

        s = ""
        while self._ch != '"':
            s += self._ch
            self._read_char()
        
        return s
    
    def _read_number(self):
        s = ""
        while self._ch.isdigit():
            s += self._ch
            self._read_char()
        
        return s  
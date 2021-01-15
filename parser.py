import jsontoken
import lexer

class Parser:
    def __init__(self, lexer):
        self._lexer = lexer
        self._parser_dict = {
            jsontoken.TRUE: self._parse_boolean,
            jsontoken.FALSE: self._parse_boolean,
            jsontoken.NULL: self._parse_null,
            jsontoken.STRING: self._parse_string,
            jsontoken.INT: self._parse_integer,
            jsontoken.LBRACKET: self._parse_array,
        }

    def parse(self):
        tok = self._lexer.next_token()

        result = self._parser_dict[tok.token](tok)
        return result

    def _parse_boolean(self, token):
        return token.token == jsontoken.TRUE

    def _parse_null(self, token):
        return None
    
    def _parse_string(self, token):
        return token.literal
    
    def _parse_integer(self, token):
        return int(token.literal)

    def _parse_array(self, token):
        array = []

        tok = self._lexer.next_token()
        if tok.token == jsontoken.RBRACKET:
            return array

        while tok.token != jsontoken.EOF:
            val = self._parser_dict[tok.token](tok)
            array.append(val)
        
            tok = self._lexer.next_token()
            if tok.token == jsontoken.RBRACKET:
                return array
            
            if tok.token != jsontoken.COMMA:
                return None
            
            tok = self._lexer.next_token()





        
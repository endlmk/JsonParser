import jsontoken
import lexer

class Parser:
    def __init__(self, lexer):
        self._lexer = lexer
        self._parser_dict = {
            jsontoken.TRUE: self._parse_boolean,
            jsontoken.FALSE: self._parse_boolean,
            jsontoken.NULL: self._parse_null,
        }

    def parse(self):
        tok = self._lexer.next_token()

        result = self._parser_dict[tok.token](tok)
        return result

    def _parse_boolean(self, token):
        return token.token == jsontoken.TRUE

    def _parse_null(self, token):
        return None
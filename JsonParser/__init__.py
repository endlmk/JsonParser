from .lexer import Lexer
from .parser import Parser

def parse_json(s):
    l = Lexer(s)
    p = Parser(l)
    return p.parse()

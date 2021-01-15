import unittest

import lexer
import parser

class TestParser(unittest.TestCase):

    def test_parse_literal(self):
        l = lexer.Lexer("true")
        p = parser.Parser(l)
        self.assertEqual(True, p.parse())
        
        l = lexer.Lexer("false")
        p = parser.Parser(l)
        self.assertEqual(False, p.parse())
        
        l = lexer.Lexer("null")
        p = parser.Parser(l)
        self.assertEqual(None, p.parse())
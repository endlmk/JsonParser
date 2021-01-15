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

    def test_parse_string(self):
        l = lexer.Lexer('"test"')
        p = parser.Parser(l)
        self.assertEqual("test", p.parse())

    def test_parse_integer(self):
        l = lexer.Lexer("1")
        p = parser.Parser(l)
        self.assertEqual(1, p.parse())

    def test_parse_array(self):
        l = lexer.Lexer("[]")
        p = parser.Parser(l)
        self.assertEqual([], p.parse())

        l = lexer.Lexer('["array"]')
        p = parser.Parser(l)
        self.assertEqual(["array"], p.parse())

        l = lexer.Lexer("[1, 2, 3]")
        p = parser.Parser(l)
        self.assertEqual([1, 2, 3], p.parse())

        l = lexer.Lexer('[1, ["", "abc"], 3]')
        p = parser.Parser(l)
        self.assertEqual([1, ["", "abc"], 3], p.parse())

    def test_parse_object(self):
        l = lexer.Lexer("{ }")
        p = parser.Parser(l)
        self.assertEqual({}, p.parse())

        l = lexer.Lexer('{"a": []}')
        p = parser.Parser(l)
        self.assertEqual({"a": []}, p.parse())

        l = lexer.Lexer('{"abc": [1, 2, 3], "def": true, "ghi": "value"}')
        p = parser.Parser(l)
        self.assertEqual({"abc": [1, 2, 3], "def": True, "ghi": "value"}, p.parse())

        l = lexer.Lexer("""\
{
    "test1": {
        "abc": "def",
        "cde": 5
    }
}
""")
        p = parser.Parser(l)
        self.assertEqual({
                "test1": {
                    "abc": "def",
                    "cde": 5
                }
            }, p.parse())
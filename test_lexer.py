import unittest
import lexer
import jsontoken

class TestLexer(unittest.TestCase):

    def test_next_token_braces_brackets(self):
        l = lexer.Lexer("""\
{ [] }
 """)
        tests = [
            (jsontoken.LBRACE, '{'),
            (jsontoken.LBRACKET, '['),
            (jsontoken.RBRACKET, ']'),
            (jsontoken.RBRACE, '}'),
            (jsontoken.EOF, ''),
        ]

        for t in tests:
            expected_token = t[0]
            expected_literal = t[1]

            t = l.next_token()
            
            self.assertEqual(expected_token, t.token)
            self.assertEqual(expected_literal, t.literal)

    def test_next_token_string(self):
        l = lexer.Lexer("""\
["abc", "567", "444"]
 """)
        tests = [
            (jsontoken.LBRACKET, '['),
            (jsontoken.STRING, "abc"),
            (jsontoken.COMMA, ','),
            (jsontoken.STRING, "567"),
            (jsontoken.COMMA, ','),
            (jsontoken.STRING, "444"),
            (jsontoken.RBRACKET, ']'),
            (jsontoken.EOF, ''),
        ]

        for t in tests:
            expected_token = t[0]
            expected_literal = t[1]

            t = l.next_token()
            
            self.assertEqual(expected_token, t.token)
            self.assertEqual(expected_literal, t.literal)

    def test_next_token_integer(self):
        l = lexer.Lexer("""\
{"abc": 123, "567": 0, "444": -1 }
 """)
        tests = [
            (jsontoken.LBRACE, '{'),
            (jsontoken.STRING, "abc"),
            (jsontoken.COLON, ':'),
            (jsontoken.INT, "123"),
            (jsontoken.COMMA, ','),
            (jsontoken.STRING, "567"),
            (jsontoken.COLON, ':'),
            (jsontoken.INT, "0"),
            (jsontoken.COMMA, ','),
            (jsontoken.STRING, "444"),
            (jsontoken.COLON, ':'),
            (jsontoken.MINUS, "-"),
            (jsontoken.INT, "1"),
            (jsontoken.RBRACE, '}'),
            (jsontoken.EOF, ''),
        ]

        for t in tests:
            expected_token = t[0]
            expected_literal = t[1]

            t = l.next_token()
            
            self.assertEqual(expected_token, t.token)
            self.assertEqual(expected_literal, t.literal)

    def test_next_token_literal(self):
        l = lexer.Lexer("""\
{"abc": [true, null, false , "efg", 5] }
 """)
        tests = [
            (jsontoken.LBRACE, '{'),
            (jsontoken.STRING, "abc"),
            (jsontoken.COLON, ':'),
            (jsontoken.LBRACKET, '['),
            (jsontoken.TRUE, "true"),
            (jsontoken.COMMA, ','),
            (jsontoken.NULL, "null"),
            (jsontoken.COMMA, ','),
            (jsontoken.FALSE, "false"),
            (jsontoken.COMMA, ','),
            (jsontoken.STRING, "efg"),
            (jsontoken.COMMA, ','),
            (jsontoken.INT, "5"),
            (jsontoken.RBRACKET, ']'),
            (jsontoken.RBRACE, '}'),
            (jsontoken.EOF, ''),
        ]

        for t in tests:
            expected_token = t[0]
            expected_literal = t[1]

            t = l.next_token()
            
            self.assertEqual(expected_token, t.token)
            self.assertEqual(expected_literal, t.literal)
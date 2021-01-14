import unittest
import lexer
import jsontoken

class TestLexer(unittest.TestCase):

    def test_next_token(self):
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

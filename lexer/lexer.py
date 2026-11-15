from multilingual_keywords import MULTILINGUAL_KEYWORDS
# SUPL Lexer — النگو ڈویلپرز
try:
    from .tokens import KEYWORDS, TOKEN_IDENTIFIER, TOKEN_NUMBER, TOKEN_STRING, TOKEN_EOF
except ImportError:
    from tokens import KEYWORDS, TOKEN_IDENTIFIER, TOKEN_NUMBER, TOKEN_STRING, TOKEN_EOF

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def number(self):
        result = ''
        is_float = False
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_float:
                    break
                is_float = True
            result += self.current_char
            self.advance()
        return float(result) if is_float else int(result)

    def string(self):
        result = ''
        self.advance() # کوٹیشن مارک چھوڑیں
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance() # آخری کوٹیشن مارک چھوڑیں
        return result

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_' or ord(self.current_char) > 127):
            result += self.current_char
            self.advance()
        
        token_type = KEYWORDS.get(result, TOKEN_IDENTIFIER)
        return token_type, result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '#':
                self.skip_comment()
                continue

            if self.current_char == '"':
                val = self.string()
                return Token(TOKEN_STRING, val, self.line)

            if self.current_char.isdigit():
                val = self.number()
                return Token(TOKEN_NUMBER, val, self.line)

            if self.current_char.isalpha() or self.current_char == '_' or ord(self.current_char) > 127:
                token_type, val = self.identifier()
                return Token(token_type, val, self.line)

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('EQUALS', '==', self.line)
                return Token('ASSIGN', '=', self.line)

            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('GREATER_EQUAL', '>=', self.line)
                return Token('GREATER', '>', self.line)

            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('LESS_EQUAL', '<=', self.line)
                return Token('LESS', '<', self.line)

            char = self.current_char
            self.advance()
            return Token('SYMBOL', char, self.line)

        return Token(TOKEN_EOF, None, self.line)

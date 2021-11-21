from .token import TokenType, Token

class LexerException(Exception):
    pass

class Lexer():

    def __init__(self) -> None:
        self._pos: int = -1
        self._current_char: str = ''
        self._text: str = ''

    def next(self) -> Token:
        while self._current_char != None:
            if self._current_char == ' ':
                self._skip()
                continue

            char = self._current_char
         
            if self._current_char.isdigit():
                number = self._float()
                if '.' in number:
                    return Token(TokenType.FLOAT, number)
                else:
                    return Token(TokenType.INTEGER, number)
            elif self._current_char == '+':
                self._forward()
                return Token(TokenType.PLUS, char)
            elif self._current_char == '-':
                self._forward()
                return Token(TokenType.MINUS, char)
            elif self._current_char == '*':
                self._forward()
                return Token(TokenType.MUL, char)
            elif self._current_char == '/':
                self._forward()
                return Token(TokenType.DIV, char)
            elif self._current_char == '^':
                self._forward()
                return Token(TokenType.POW, char)
            elif self._current_char == '(':
                char = self._current_char
                self._forward()
                return Token(TokenType.LPAREN, char)
            elif self._current_char == ')':
                char = self._current_char
                self._forward()
                return Token(TokenType.RPAREN, char)
            raise LexerException(f"Undefined token: {char}")
        return Token(TokenType.EOS, None)

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]
        
    def _skip(self):
        while self._current_char == ' ':
            self._forward()

    def _integer(self) -> str:
        result: list = []
        while self._current_char and self._current_char.isdigit():
            result.append(self._current_char)
            self._forward()
        return ''.join(result)
    
    def _float(self) -> str:
        lhs_part = self._integer()
        if self._current_char == '.':
            self._forward()
            rhs_part = self._integer()
            return f"{lhs_part}.{rhs_part}"
        return lhs_part
    
    def init(self, text: str):
        self._text = text
        self._pos = -1
        self._forward()
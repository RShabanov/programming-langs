from .token import TokenType, Token

class InterpreterException(Exception):
    pass

class Interpreter():
    
    def __init__(self) -> None:
        self._pos: int = -1
        self._current_token: Token = None
        self._current_char: str = ''
        self._text: str = ''

    def interpret(self, text: str) -> int:
        self._text = text
        self._pos = -1
        self._forward()
        return self._expr()

    def _expr(self) -> int:
        self._current_token = self._next_token()
        lhs = self._current_token
        self._check_token_type(TokenType.INTEGER)
        
        op = self._current_token
        if op.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
        elif op.type_ == TokenType.MINUS:
            self._check_token_type(TokenType.MINUS)

        rhs = self._current_token
        self._check_token_type(TokenType.INTEGER)

        if op.type_ == TokenType.PLUS:
            return int(lhs.value) + int(rhs.value)
        elif op.type_ == TokenType.MINUS:
            return int(lhs.value) - int(rhs.value)
        else:
            raise InterpreterException(f"Undefined token: {op}")


    def __call__(self, text: str) -> int:
        return self.interpret(text)

    def _next_token(self) -> Token:
        while self._current_char != None:
            if self._current_char == ' ':
                self._skip()
                continue

            char = self._current_char
         
            if self._current_char.isdigit():
                return Token(TokenType.INTEGER, self._integer())
            elif self._current_char == '+':
                self._forward()
                return Token(TokenType.PLUS, char)
            elif self._current_char == '-':
                self._forward()
                return Token(TokenType.MINUS, char)

            raise InterpreterException(f"Undefined token: {char}")
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

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._next_token()
        else:
            raise InterpreterException(f"Invalid expression - expected token type: {type_}")

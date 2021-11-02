from .token import TokenType, Token
from .lexer import Lexer, LexerException

class InterpreterException(Exception):
    pass

class Interpreter():
    
    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def interpret(self, text: str) -> int:
        self._lexer.init(text)
        return self._expr()

    def _expr(self) -> int:
        self._current_token = self._lexer.next()
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

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise InterpreterException(f"Invalid expression - expected token type: {type_}")

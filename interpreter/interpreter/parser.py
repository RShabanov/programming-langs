from .token import TokenType, Token
from .lexer import Lexer, LexerException
from .node import Node, Number, BinOp

class ParserException(Exception):
    pass

class Parser:
    
    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def parse(self, text: str) -> Node:
        self._lexer.init(text)
        self._current_token = self._lexer.next()
        return self._expr()

    def __call__(self, text: str) -> Node:
        return self.parse(text)

    def _factor(self) -> Node:
        token = self._current_token
        
        if token.type_ == TokenType.INTEGER:
            self._check_token_type(TokenType.INTEGER)
            return Number(token)
        elif token.type_ == TokenType.LPAREN:
            self._check_token_type(TokenType.LPAREN)
            result = self._expr()
            self._check_token_type(TokenType.RPAREN)
            return result
        # unary minus
        # elif token.type_ == TokenType.MINUS:
        #     self._check_token_type(TokenType.MINUS)
        #     val = self._factor()
        #     return Number(-val)
        # # unary plus
        # elif token.type_ == TokenType.PLUS:
        #     self._check_token_type(TokenType.PLUS)
        #     val = self._factor()
        #     return Number(val)
        else:
            raise ParserException(f"Invalid factor - {token.type_}")

    def _term(self) -> Node:
        result = self._factor()
        ops = [TokenType.MUL, TokenType.DIV]

        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
            else:
                self._check_token_type(TokenType.DIV)
            result = BinOp(result, token, self._factor())
        return result

    def _expr(self) -> Node:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self._term()

        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
            else:
                self._check_token_type(TokenType.MINUS)              
            result = BinOp(result, token, self._term())
        return result

    def _check_token_type(self, type_: TokenType):
        # print(f"Token type: {type_}")
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise ParserException(f"Invalid expression - expected token type: {type_}")

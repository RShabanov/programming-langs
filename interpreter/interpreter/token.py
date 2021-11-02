from enum import Enum, auto
import typing

class TokenType(Enum):
    INTEGER = auto()
    FLOAT = auto()
    PLUS = auto()
    MINUS = auto()
    DOT = auto()
    EOS = auto()

class Token():
    
    def __init__(self, type_: TokenType, value: str) -> None:
        self.type_ = type_
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type_}, {self.value})"

    def __repr__(self) -> str:
        return str(self)

if __name__ == "__main__":
    print(list(TokenType))

    t = Token(TokenType.INTEGER, '2')
    print([t])
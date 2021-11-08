
from .token import Token


class Node:
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class Number(Node):
    def __init__(self, token: Token) -> None:
        super().__init__()
        self.token = token

    def __str__(self) -> str:
        return f"{super().__str__()}(<{self.token.type_}, {self.token.value}>)"


class BinOp(Node):
    def __init__(self, lhs: Node, op: Token, rhs: Node) -> None:
        super().__init__()
        self.lhs = lhs
        self.rhs = rhs
        self.op = op

    def __str__(self) -> str:
        return f"{super().__str__()} {self.op.value} ({self.lhs}, {self.rhs})"


class UnaryOp(Node):
    def __init__(self, op: Token, node: Node) -> None:
        super().__init__()
        self.op = op
        self.node = node

    def __str__(self) -> str:
        return f"{super().__str__()} {self.op.value}{self.node}"
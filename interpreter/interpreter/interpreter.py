
from interpreter.token import TokenType
from .node import Node, Number, BinOp, UnaryOp
import operator

class InterpreterException(Exception):
    pass

class Interpreter:
    def interpret(self, tree: Node) -> float:
        return self._visit(tree)
    
    def _visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_bin_op(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unary_op(node)
        
        raise InterpreterException(f"Invalid node: {node}")

    def _visit_number(self, node: Number) -> float:
        return float(node.token.value)

    def _visit_bin_op(self, node: BinOp) -> float:
        op = node.op
        binop = {
            TokenType.PLUS: operator.add,
            TokenType.MINUS: operator.sub,
            TokenType.MUL: operator.mul,
            TokenType.DIV: operator.truediv,
            TokenType.POW: operator.pow,
        }.get(op.type_)

        if binop:
            return binop(self._visit(node.lhs), self._visit(node.rhs))
        raise InterpreterException(f"Invalid node (bin_op): {node}")

    def _visit_unary_op(self, node: UnaryOp) -> float:
        op = node.op
        unary_op = {
            TokenType.PLUS: operator.pos,
            TokenType.MINUS: operator.neg,
        }.get(op.type_)
        
        if unary_op:
            return unary_op(self._visit(node.node))
        raise InterpreterException(f"Invalid node (bin_op): {node}")
        

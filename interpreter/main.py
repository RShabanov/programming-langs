from interpreter import Interpreter
import interpreter
from interpreter.parser import Parser
from interpreter import Interpreter

if __name__ == "__main__":
    parser = Parser()
    inter = Interpreter()
    print(inter.interpret(parser("1 * (2.54 + 3)")))
    print(inter.interpret(parser("1.5 * (2 + 3)")))
    print(inter.interpret(parser("1 * 2 + 3")))
    print(inter.interpret(parser("-1")))
    print(inter.interpret(parser("+1")))
    print(inter.interpret(parser("-(1 + 1)^3^2")))
    print(inter.interpret(parser("-1.5^2")))

from interpreter import Interpreter
import interpreter
from interpreter.parser import Parser
from interpreter import Interpreter

if __name__ == "__main__":
    parser = Parser()
    inter = Interpreter()
    print(inter.interpret(parser("1 * (2 + 3)")))
    print(inter.interpret(parser("1 * 2 + 3")))
    print(inter.interpret(parser("-1")))
    print(inter.interpret(parser("+1")))


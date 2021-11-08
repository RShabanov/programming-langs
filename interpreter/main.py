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

    # print(parser("2-7/2*3"))
    # print(parser.parse("(2   + 4) - ((4 + 2))*3"))
    # print(parser.parse("2- 4"))

from interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    print(interpreter("2+2"))
    print(interpreter.interpret("2   + 4"))
    print(interpreter.interpret("2- 4"))

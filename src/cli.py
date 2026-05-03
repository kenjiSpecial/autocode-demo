"""Interactive calculator CLI."""

from src.calculator import add, subtract, multiply, divide


def main():
    """Run interactive calculator REPL."""
    print("Interactive Calculator")
    print("Commands: add <a> <b>, subtract <a> <b>, multiply <a> <b>, divide <a> <b>, quit")
    while True:
        try:
            user_input = input("> ").strip()
        except EOFError:
            break
        if not user_input:
            continue
        if user_input == "quit":
            break
        parts = user_input.split()
        if len(parts) != 3:
            print("Usage: <operation> <a> <b>")
            continue
        op, a_str, b_str = parts
        try:
            a, b = float(a_str), float(b_str)
        except ValueError:
            print("Error: arguments must be numbers")
            continue
        ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
        }
        if op not in ops:
            print(f"Unknown operation: {op}")
            continue
        try:
            result = ops[op](a, b)
            print(result)
        except ZeroDivisionError:
            print("Error: division by zero")

if __name__ == "__main__":
    main()

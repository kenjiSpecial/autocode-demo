"""Interactive calculator CLI."""

from src.calculator import add, subtract


def main():
    """Run interactive calculator REPL."""
    print("Interactive Calculator (type 'quit' to exit)")
    while True:
        expr = input("> ").strip()
        if expr == "quit":
            break
        parts = expr.split()
        if len(parts) != 3:
            print("Usage: <num> <op> <num>  (ops: + -)")
            continue
        a, op, b = parts
        try:
            a, b = float(a), float(b)
        except ValueError:
            print("Invalid numbers")
            continue
        if op == "+":
            print(add(a, b))
        elif op == "-":
            print(subtract(a, b))
        else:
            print(f"Unknown operator: {op}")


if __name__ == "__main__":
    main()

"""Interactive calculator CLI."""

import sys
from src.calculator import add, subtract


def main():
    print("Welcome to Interactive Calculator")
    print("Available commands: add <a> <b>, subtract <a> <b>, quit")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]
        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "add":
            if len(parts) != 3:
                print("Usage: add <a> <b>")
                continue
            try:
                result = add(float(parts[1]), float(parts[2]))
            except ValueError:
                print("Error: arguments must be numbers")
                continue
            print(result)
        elif cmd == "subtract":
            if len(parts) != 3:
                print("Usage: subtract <a> <b>")
                continue
            try:
                result = subtract(float(parts[1]), float(parts[2]))
            except ValueError:
                print("Error: arguments must be numbers")
                continue
            print(result)
        else:
            print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()

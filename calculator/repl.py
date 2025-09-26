from typing import Callable, Optional

from .operations import OPS
from .parser import HELP_TEXT, parse_line

BANNER = "Welcome to calc-cli! Press Ctrl+C or Ctrl+D to quit."

def eval_once(line: str) -> str:
    """
    Single-step evaluator used by both the REPL and tests.
    Returns a user-facing string describing the result or the error/help text.
    """
    parsed = parse_line(line)

    if parsed.kind == "empty":
        return ""

    if parsed.kind == "help":
        return HELP_TEXT

    if parsed.kind == "quit":
        return "Goodbye!"

    if parsed.kind == "error":
        assert parsed.error is not None
        return f"Error: {parsed.error}"

    # calc
    assert parsed.op is not None and parsed.a is not None and parsed.b is not None
    try:
        result = OPS[parsed.op](parsed.a, parsed.b)
        # Display as int when possible (e.g., 5.0 -> 5)
        if result.is_integer():
            return str(int(result))
        return str(result)
    except ZeroDivisionError as e:
        return f"Error: {e}"

def run_repl(
    input_fn: Optional[Callable[[str], str]] = input,
    print_fn: Optional[Callable[[str], None]] = print,
) -> None:
    """
    Interactive calculator REPL (step-by-step input; exit with Ctrl+C / Ctrl+D).
    """
    print_fn(BANNER)

    while True:
        try:
            op = input_fn("Enter the operation you want to perform (+, -, *, /): ").strip()
            if op not in OPS:
                print_fn("Error: Unknown operation. Please choose from +, -, *, /")
                continue

            a = float(input_fn("Enter the first number: ").strip())
            b = float(input_fn("Enter the second number: ").strip())

            result = OPS[op](a, b)
            if result.is_integer():
                result = int(result)
            print_fn(f"Result: {result}")

        except ValueError:
            print_fn("Error: Operands must be valid numbers.")
        except ZeroDivisionError:
            print_fn("Error: Cannot divide by zero.")
        except (EOFError, KeyboardInterrupt):
            print_fn("\nGoodbye!")
            break

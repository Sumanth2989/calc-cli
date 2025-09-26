from typing import Optional, Callable

from .operations import OPS
from .parser import parse_line, HELP_TEXT

BANNER = "Welcome to calc-cli! Type 'help' for usage, 'quit' to exit."

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
    Interactive REPL. input_fn and print_fn are injectable for testing.
    """
    print_fn(BANNER)
    while True:
        try:
            line = input_fn("> ")
        except (EOFError, KeyboardInterrupt):
            print_fn("\nGoodbye!")
            break

        out = eval_once(line)
        if out:
            print_fn(out)
        if out == "Goodbye!":
            break

if __name__ == "__main__":  # pragma: no cover
    run_repl()               # pragma: no cover

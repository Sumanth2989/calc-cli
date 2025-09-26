from dataclasses import dataclass
from typing import Literal, Optional

from .operations import OPS

QuitCmd = Literal["quit", "exit"]
HelpCmd = Literal["help"]
ParsedKind = Literal["calc", "quit", "help", "empty", "error"]

@dataclass
class Parsed:
    kind: ParsedKind
    op: Optional[str] = None
    a: Optional[float] = None
    b: Optional[float] = None
    error: Optional[str] = None

HELP_TEXT = (
    "Usage:\n"
    "  <op> <a> <b>\n"
    "  where <op> is one of: +, -, *, /, add, sub, mul, div\n"
    "Commands:\n"
    "  help  - show this message\n"
    "  quit  - exit the calculator\n"
    "Examples:\n"
    "  + 2 3     -> 5\n"
    "  div 10 2  -> 5\n"
)

def parse_line(line: str) -> Parsed:
    if line is None:
        return Parsed(kind="error", error="No input provided.")
    parts = line.strip().split()
    if not parts:
        return Parsed(kind="empty")

    head = parts[0].lower()

    if head in ("quit", "exit"):
        return Parsed(kind="quit")

    if head == "help":
        return Parsed(kind="help")

    if head not in OPS:
        return Parsed(kind="error", error=f"Unknown operation '{head}'. Type 'help'.")

    if len(parts) != 3:
        return Parsed(kind="error", error="Expected format: <op> <a> <b>. Type 'help'.")

    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError:
        return Parsed(kind="error", error="Operands must be numbers. Type 'help'.")

    return Parsed(kind="calc", op=head, a=a, b=b)

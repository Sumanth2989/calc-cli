from typing import Callable

Number = float

def add(a: Number, b: Number) -> Number:
    return a + b

def sub(a: Number, b: Number) -> Number:
    return a - b

def mul(a: Number, b: Number) -> Number:
    return a * b

def div(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

OPS: dict[str, Callable[[Number, Number], Number]] = {
    "+": add,
    "add": add,
    "-": sub,
    "sub": sub,
    "*": mul,
    "x": mul,
    "mul": mul,
    "/": div,
    "div": div,
}

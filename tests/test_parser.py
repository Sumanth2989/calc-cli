from calculator.parser import parse_line, HELP_TEXT

def test_none_input_is_error():
    p = parse_line(None)  # type: ignore[arg-type]
    assert p.kind == "error"
    assert "No input" in (p.error or "")

def test_parse_empty():
    p = parse_line("   ")
    assert p.kind == "empty"

def test_parse_help():
    p = parse_line("help")
    assert p.kind == "help"

def test_parse_quit_aliases():
    assert parse_line("quit").kind == "quit"
    assert parse_line("exit").kind == "quit"

def test_parse_unknown_op():
    p = parse_line("pow 2 3")
    assert p.kind == "error"
    assert "Unknown operation" in (p.error or "")

def test_parse_wrong_arity():
    p = parse_line("+ 2")
    assert p.kind == "error"
    assert "Expected format" in (p.error or "")

def test_parse_non_numeric():
    p = parse_line("+ a 3")
    assert p.kind == "error"
    assert "Operands must be numbers" in (p.error or "")

def test_parse_ok_symbols():
    p = parse_line("+ 2 3")
    assert p.kind == "calc" and p.op == "+" and p.a == 2 and p.b == 3

def test_parse_ok_words():
    p = parse_line("div 10 2")
    assert p.kind == "calc" and p.op == "div" and p.a == 10 and p.b == 2

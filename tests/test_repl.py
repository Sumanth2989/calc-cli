from calculator.repl import eval_once, run_repl, BANNER

def test_eval_once_empty_returns_blank():
    assert eval_once("   ") == ""

def test_repl_suppresses_blank_output():
    inputs = iter(["   ", "quit"])
    lines = []
    run_repl(input_fn=lambda _ : next(inputs), print_fn=lambda s="": lines.append(s))
    # Should have banner, then no line printed for empty command, then Goodbye!
    assert lines[0] == BANNER
    assert "Goodbye!" in lines
    # ensure only 2 non-empty lines (banner + goodbye)
    non_empty = [ln for ln in lines if ln]
    assert len(non_empty) == 2

def test_eval_once_help():
    out = eval_once("help")
    assert "Usage:" in out

def test_eval_once_add_int_display():
    assert eval_once("+ 2 3") == "5"  # 5.0 printed as 5

def test_eval_once_div_float_display():
    assert eval_once("/ 2 4") == "0.5"

def test_eval_once_errors():
    assert eval_once("pow 2 3").startswith("Error:")
    assert "Unknown operation" in eval_once("pow 2 3")
    assert "Expected format" in eval_once("+ 2")
    assert "Operands must be numbers" in eval_once("+ a 2")

def test_eval_once_div_by_zero():
    out = eval_once("/ 1 0")
    assert out.startswith("Error:")
    assert "divide by zero" in out.lower()

def test_eval_once_quit():
    assert eval_once("quit") == "Goodbye!"

def test_repl_flow():
    inputs = iter(["help", "+ 2 3", "quit"])

    def fake_input(_):
        return next(inputs)

    lines = []
    def fake_print(s=""):
        lines.append(s)

    run_repl(input_fn=fake_input, print_fn=fake_print)

    # banner shown, help printed, result printed, goodbye printed
    assert lines[0] == BANNER
    assert any("Usage:" in ln for ln in lines)
    assert "5" in lines
    assert "Goodbye!" in lines

def test_repl_exits_on_eof():
    # Simulate Ctrl-D (EOF) to cover the except branch
    def fake_input(_):
        raise EOFError
    lines = []
    run_repl(input_fn=fake_input, print_fn=lambda s="": lines.append(s))
    assert lines[0] == BANNER
    assert lines[-1].strip() == "Goodbye!"

def test_repl_exits_on_keyboardinterrupt():
    # Simulate Ctrl-C to cover the except branch
    def fake_input(_):
        raise KeyboardInterrupt
    lines = []
    run_repl(input_fn=fake_input, print_fn=lambda s="": lines.append(s))
    assert lines[0] == BANNER
    assert lines[-1].strip() == "Goodbye!"

from calculator.repl import run_repl, BANNER, eval_once

def _run_with_inputs(inp_seq):
    """Helper to run the REPL with a finite sequence, then EOF."""
    it = iter(inp_seq)

    def fake_input(_prompt: str) -> str:
        try:
            return next(it)
        except StopIteration:
            # Simulate Ctrl-D to exit loop cleanly
            raise EOFError

    lines = []
    run_repl(input_fn=fake_input, print_fn=lambda s="": lines.append(s))
    return lines

def test_repl_happy_path_two_calculations_and_eof():
    # + 2 3 -> 5   and   / 10 2 -> 5
    lines = _run_with_inputs(["+", "2", "3", "/", "10", "2"])
    assert lines[0] == BANNER
    assert any("Result: 5" in ln for ln in lines)  # at least one result is 5
    # both results should be present
    assert sum(1 for ln in lines if "Result: 5" in ln) >= 2
    assert lines[-1].strip() == "Goodbye!"

def test_repl_unknown_operation_then_valid_calc():
    # unknown op -> error; then valid op -> result; then EOF
    lines = _run_with_inputs(["pow", "+", "1", "4"])
    assert "Unknown operation" in "\n".join(lines)
    assert "Result: 5" in "\n".join(lines)
    assert lines[-1].strip() == "Goodbye!"

def test_repl_non_numeric_operands_then_success():
    # non-numeric -> error; then valid numbers -> result; then EOF
    lines = _run_with_inputs(["*", "a", "3", "*", "7", "6"])
    joined = "\n".join(lines)
    assert "Operands must be valid numbers" in joined
    assert "Result: 42" in joined
    assert lines[-1].strip() == "Goodbye!"

def test_repl_divide_by_zero_then_success():
    # / 1 0 -> error; then / 10 2 -> 5; then EOF
    lines = _run_with_inputs(["/", "1", "0", "/", "10", "2"])
    joined = "\n".join(lines)
    assert "Cannot divide by zero" in joined
    assert "Result: 5" in joined
    assert lines[-1].strip() == "Goodbye!"

def test_repl_exits_on_keyboardinterrupt_immediately():
    # Simulate Ctrl-C on first prompt
    def fake_input(_prompt: str) -> str:
        raise KeyboardInterrupt

    captured = []
    run_repl(input_fn=fake_input, print_fn=lambda s="": captured.append(s))
    assert captured[0] == BANNER
    assert captured[-1].strip() == "Goodbye!"


from calculator.repl import eval_once

def test_eval_once_help():
    out = eval_once("help")
    assert "Usage:" in out

def test_eval_once_add_int_display():
    assert eval_once("+ 2 3") == "5"  # 5.0 -> "5"

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



def test_eval_once_empty_returns_blank():
    assert eval_once("   ") == ""


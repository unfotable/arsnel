"""Module 12 content: testing with pytest, fixtures, mocking and TDD."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=12,
    intro="Tests are executable documentation and a safety net for change. You will write pytest tests, share setup with fixtures, isolate code with mocks and practise test-driven development.",
    lessons=(
        Lesson(
            "Why test, and what makes a good test",
            """
A good test is **fast**, **deterministic**, **independent** and checks **one behaviour**. Structure it as
*arrange -> act -> assert*. Test behaviour through the public interface, not private details.
Start with the cases that scare you: empty input, boundaries, errors.
""",
        ),
        Lesson(
            "pytest essentials",
            """
```python
def test_add():
    assert add(2, 3) == 5

@pytest.mark.parametrize(("a", "b", "want"), [(1, 1, 2), (0, 0, 0)])
def test_many(a, b, want):
    assert add(a, b) == want

def test_error():
    with pytest.raises(ZeroDivisionError, match="zero"):
        divide(1, 0)

assert 0.1 + 0.2 == pytest.approx(0.3)
```

Name files `test_*.py` and functions `test_*`. Run with `pytest -q`; `-k name` selects, `-x` stops at the first failure.
""",
        ),
        Lesson(
            "Fixtures",
            """
```python
@pytest.fixture
def db(tmp_path):
    conn = connect(tmp_path / "x.db")
    yield conn            # test runs here
    conn.close()          # teardown
```

Request a fixture by naming it as a parameter. Built-ins: `tmp_path` (temp folder), `monkeypatch` (patch env/attrs),
`capsys` (capture output). Scope (`scope="module"`) trades isolation for speed; share via `conftest.py`.
""",
        ),
        Lesson(
            "Mocks and TDD",
            """
```python
notifier = Mock()
send_alert(notifier, "hot")
notifier.send.assert_called_once_with("hot")

with patch("module.requests.get", return_value=fake): ...
```

Inject dependencies (pass a clock or client in) so tests can substitute `Mock` objects and `side_effect`.
**TDD**: write a failing test (red), make it pass with the simplest code (green), clean up (refactor), repeat.
Do not mock what you own and can run cheaply; mock slow, flaky or external things.
""",
        ),
    ),
    examples=(
        Example(
            "pytest_basics.py",
            "pytest basics",
            "Asserts, parametrize, raises and approx.",
            False,
        ),
        Example(
            "pytest_fixtures.py",
            "Fixtures and built-ins",
            "tmp_path, monkeypatch, capsys and skipif.",
            False,
        ),
        Example("mocking.py", "unittest.mock", "Mock, side_effect and patch.", False),
        Example(
            "tdd_walkthrough.py",
            "Red, green, refactor",
            "Three versions of one function against one spec.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_slugify.py", "TDD: slugify", "satisfy the described test-suite.", 2
        ),
        Exercise(
            "ex_02_stack.py",
            "A tested Stack",
            "implement the class the tests describe.",
            2,
        ),
        Exercise(
            "ex_03_mock_notifier.py",
            "Dependency injection",
            "design code that is easy to mock.",
            3,
        ),
    ),
    quiz=(
        Question(
            "What do pytest test functions need to be discovered?",
            (
                "A decorator",
                "A name starting with test_ in a test_*.py file",
                "A class",
                "Docstrings",
            ),
            1,
            "Default discovery patterns are test_*.py and test_*.",
        ),
        Question(
            "Which compares floats safely?",
            ("==", "pytest.approx", "is", "assertTrue"),
            1,
            "approx allows a small tolerance.",
        ),
        Question(
            "What does a fixture with `yield` do after the test?",
            (
                "Nothing",
                "Runs the teardown code after yield",
                "Restarts the test",
                "Skips it",
            ),
            1,
            "Code after yield is the teardown.",
        ),
        Question(
            "What is `tmp_path`?",
            (
                "A global folder",
                "A fresh temporary directory per test",
                "A string",
                "A mock",
            ),
            1,
            "pytest creates and cleans it for you.",
        ),
        Question(
            "In TDD the first step is...",
            ("Write the code", "Write a failing test", "Refactor", "Deploy"),
            1,
            "Red comes before green.",
        ),
        Question(
            "What does `Mock(side_effect=[1, ValueError])` do?",
            (
                "Returns 1 forever",
                "Returns 1 then raises ValueError on the next call",
                "Raises first",
                "Nothing",
            ),
            1,
            "A list side_effect yields/raises one item per call.",
        ),
        Question(
            "Why inject a clock into a function instead of calling datetime.now() inside?",
            ("Speed", "So tests can control time", "Style", "Typing"),
            1,
            "Dependencies you control make tests deterministic.",
        ),
    ),
    cheatsheet=(
        "`pytest -q`, `-k expr`, `-x`, `-s`",
        "`@pytest.mark.parametrize`, `pytest.raises`, `pytest.approx`",
        "`@pytest.fixture` + `yield`; `tmp_path`, `monkeypatch`, `capsys`",
        "`Mock`, `MagicMock`, `patch`, `side_effect`, `assert_called_once_with`",
        "red -> green -> refactor",
        "inject dependencies; test behaviour",
    ),
    next_steps="Next: package your work for others in module 13.",
)

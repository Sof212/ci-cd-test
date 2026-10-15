from python_code import read_file
from pathlib import Path

def test_read_file():
    assert len(read_file(Path(__file__).parent / "test_hello_word.txt")) > 0

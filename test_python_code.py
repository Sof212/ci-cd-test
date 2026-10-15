from python_code import read_file


def test_read_file():
    assert len(read_file("/workspaces/ci-cd-test/test_hello_word.txt")) > 0

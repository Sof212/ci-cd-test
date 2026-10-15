def read_file(filename: str):
    with open(filename, "r") as f:
        return f.read()


print(read_file("/workspaces/ci-cd-test/test_hello_word.txt"))

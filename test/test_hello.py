from calculatortesting import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

# our saved tests in a folder now in a file called test_hello.py
# Pytest lets me to run this too but after do something else
# lets terminal "code test/__init__.py" , although the file is empty it tells python to treat the test folder as a package
# We can now just terminal "pytest test" or in my case "python -m pytest test" and run the entire folder for testing
# we can use this growing files in the test folder to test our codes
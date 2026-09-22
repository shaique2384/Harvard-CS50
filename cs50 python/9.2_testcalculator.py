# Lets test the square function
# We are now at the tester file and we will test the testee square() from the unittest.py


# if you wanna test a function for square our custom function should be about testing that custom function square()
# I don't dislike the idea of testing with the functioning of squaring like before
# In the real world it will be better to test the program automatically over and over with an automated process rather than doing it manually

if False:
    from calculatortesting import square
    def main():
        test_square()
    # we wrote it last, it's sole purpose is to make it a module as well

    def test_square():
        if square(2) != 4:                                              # It is only psossible when there is an error occured
            print("2 squared was not 4")
        if square(3) != 9:
            print("3 squared was not 9")


    # Now let's make it a library too
    if __name__ == "__main__":
        main()

# if the code doesn't show anything that means our anticipation of errors have been checked, the eroors did not happen. We are taking humans out of the calculation
# the challenge of this code is to find those anticipated errors
# No output is good
# let's go back and change the def square() black into return n+n from the testee
# side effect shows "3 squared was not 9"
# our code is brocken
# but we are writing 5 lines of codes to test a 2 lines of code which is not efficient
# To solve this let's use a python keyword assert, it's a boolean expression. It says true or falls for whatever is input

if False:
    from calculatortesting import square
    def main():
        test_square()
    # we wrote it last, it's sole purpose is to make it a module as well

    def test_square():
        assert square(2) == 4                                              # It is only psossible when there is an error occured
        assert square(3) == 9


    # Now let's make it a library too
    if __name__ == "__main__":
        main()

# if code is broken it will give AssertionError with the conditions broken
# if the code is okay, side effect clean
# we catch error with try and except block

if False:
    from calculatortesting import square
    def main():
        test_square()
    # we wrote it last, it's sole purpose is to make it a module as well

    def test_square():
        try:
            assert square(2) == 4                                             # It is only psossible when there is an error occured
        except:
            print("2 squared was not 4")
        try:
            assert square(3) == 9
        except:
            print("3 squared was not 9")
        try:
            assert square(-2) == 4                                             # It is only psossible when there is an error occured
        except:
            print("-2 squared was not 4")
        try:
            assert square(-3) == 9
        except:
            print("-3 squared was not 9")
        try:
            assert square(0) == 0
        except:
            print("0 squared was not 0")

    # Now let's make it a library too
    if __name__ == "__main__":
        main()

# our wrong code was return n+n
# Only 3 squared was not 9
# We might end up writing too many codes
# But hei i cant try an infinit number!
# We are just trying to find the corner cases
# Crazy cause not all of the assertionns are failing
# Still it would have been nicer if we didn't have to wright so many darn codes
# But hei i cant try an infinit number!
# We are just trying to find the corner cases
# So many assertions, why not we create tools to make easier to do so. We can do this with pytest. It's a third party program or library per say.
# There are also other libraries of testing unit tests but pytest is musch simpler
# Unit testing is a formal way of describing testing individual units of your programs, which are basically functions
# Let's see if we can distill the tests to their essence

if False:
    from calculatortesting import square
    def test_square():
        assert square(2) == 4
        assert square(3) == 9
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0
        # Wouldn't it be better something or someone else handles the tryb the except and printing al of these standardisations of actually running the test
        # You dont't need the documentation https://docs.pytest.org as pytest itself is very user friendly
        # We don't need main() and etc.
        # Just run on the terminal instead of python, pytest 10.1_test_calculator.py.py.
        # It's output is not userfriendly, it shows bunch of errors
        # I cross my fingers I hit enter, lol. For some reasons I can not add pytest to my path
        # So with a bit of help from my beloved copilot I'm calling python -m pytest 10.1_test_calculator.py.py ; -m flag in python stands for module and by python -m pytest you’re telling Python: “Run the module named pytest as if it were a script.”
        # It shows,

"""
=================== test session starts ===================
platform win32 -- Python 3.13.3, pytest-9.0.3, pluggy-1.6.0
rootdir: F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50
collected 1 item                                           

testcalculator.py F                                  [100%]                             # F stannds for fail, not very encouraging

======================== FAILURES =========================
_______________________ test_square _______________________                             # The function at issue

    def test_square():
        assert square(2) == 4
>       assert square(3) == 9                                                           # > means pytest did not like
E       assert 6 == 9                                                                   # It says I'm trying to assert 6==9 , what?. This is the assertion, the next line is the problem
E        +  where 6 = square(3)                                                         # According to our definition squared input of 3 gives us 6 but the assertion make the symbol == lose it's definition because 6==9 is not true

testcalculator.py:104: AssertionError                                                   # Then I go bacl an encounter a lightbulb moment, ooooh , I defined square with + instead of *
================= short test summary info =================
FAILED testcalculator.py::test_square - assert 6 == 9
==================== 1 failed in 0.09s ====================
"""
# After we correct the program with the clue from the pytest, we get this
"""
.                                                                   [100%]

==================================== 1 passed in 0.02s =====================================
"""
# We have passed

if False:
    from calculatortesting import square
    def test_square():
        assert square(2) == 4
        assert square(3) == 9
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0
    def user_input():
        # Let's walk in the shoes of the users, what mistakes can they make
        assert user_input() == "Cat"

# We can also run loops tho to test them manually

if False:
    from calculatortesting import square, user_input
    def test_square():
        for i in range(100):
            assert square(i) == i*i
            assert square(-i) == i*i
    def test_user_input():
        # Let's walk in the shoes of the users, what mistakes can they make
        assert user_input() == "Cat"




# We need a system or dataset to to test user input but user input is not a programmers fault
# It will flag the first problem it encounters, so abstracting the error concepts using loops is the key.
# Let's find other errors
# Let's first distribute between positive and negative numbers

if False:
    from calculatortesting import square
    def test_positive():
        for i in range(100):
            assert square(i+2) == (i+2)*(i+2)
    def test_negative():
        for i in range(100):
            assert square(-(i+2)) == (-(i+2))*(-(i+2))


# Let's now test funcctions that doesn't only take numbers as inputs but also strings
if False:
    from calculatortesting import hello
    # How the fuck do I test it?
    def test_hello():
        assert hello("David") == "hello, David" # [R.H.S. is the return value]
        # These are different than square() function, print does not return a value
        # hello("David") == "Hello, David" it can check the return value with == but it's just showing side effects on the terminal, it's not even traveling to R.H.S. 
        # As our programs start getting more and more sophisticated or complicated, it's best to use functions with side effects less and less
        # Let's assert hello() without any argument
        assert hello() == "hello, world"

# Let's make different functions for different scenarios

if False:
    from calculatortesting import hello
    def test_default():        
        assert hello() == "hello, world"
    def test_argument():
        assert hello("David") == "hello, David"

# We can also test recursive funtions i.e, function inside a function this way. Just assert and call the function

if False:
    from calculatortesting import hello
    def test_default():        
        assert hello() == "hello, world"
    def test_argument():
        for name in ["H", "I", "J", "K", "L"]:
            assert hello(name) == f"hello, [{name}]"

# Lets not write tests for our tests for our tests for our tests for our ........
# Suppose we don't have just one test but many different tests and we wanna organize our tests into a file or a folder
# type in the terminal "mkdir test" and enter and "code/test_hello.py"
# open test_hello.py to see furthur instructions
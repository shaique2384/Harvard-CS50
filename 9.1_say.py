if False:
    import sys
    from sayings import hello                               # sayings is a module file suggested by Cs50David. For some weird reasons numbering for the sake of lesson documentation for future reuse is creating problems while importing. So saying is devoid of the index numbeing.
    if len(sys.argv)==2:
        hello(sys.argv[1])
    else:
        sys.exit("kindly input one word for name")          # Shoytan abar iccha koira bhul korse -_-

# the bottom line is if the saying.py has a main() call at the end the importing of sayings will by default activate that
# Let's go back to the sayings.py file and assign __name__ == "__main__" ; this double underscore means that call the name of that main function only when it is called explicitly from the command line or terminal.
# __name__ is a special variable. 
# When __name__ != "__main__" which means saying.py is not called via command line then it will not be called like the traditional main() calling rather any custom functions of sayings.py will be called after importing sys as a module.
if False:
    import sys
    from sayings import goodbye
    if len(sys.argv)==2:
        goodbye(sys.argv[1])
    else:
        sys.exit

import sys,sayings
if len(sys.argv)==2:
    sayings.hello(sys.argv[1])
    sayings.goodbye(sys.argv[1])
else:
    sys.exit
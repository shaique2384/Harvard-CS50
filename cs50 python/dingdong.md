PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Type any number: 5
meow meow meow meow meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Type any number: 4
Traceback (most recent call last):
  File "F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra\3_meows.py", line 47, in <module>
    M(n)
    ~^^^
  File "F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra\3_meows.py", line 40, in M
    for _ in range(x):
             ~~~~~^^^
TypeError: 'str' object cannot be interpreted as an integer
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Type any number: 6
Traceback (most recent call last):
  File "F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra\3_meows.py", line 48, in <module>
    M(n)
    ~^^^
  File "F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra\3_meows.py", line 40, in M
    for _ in range(x):
             ~~~~~^^^
TypeError: 'str' object cannot be interpreted as an integer
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Type any number: 5
Traceback (most recent call last):
  File "F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra\3_meows.py", line 50, in <module>
    M(n)
    ~^^^
  File "F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra\3_meows.py", line 40, in M
    for _ in range(x):
             ~~~~~^^^
TypeError: 'str' object cannot be interpreted as an integer
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Type any number: 6
6 meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Type any number: 4
4meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:50: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:55: error: Name "n" already defined on line 47  [no-redef]
3_meows.py:56: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:57: error: Name "n" already defined on line 47  [no-redef]
3_meows.py:64: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:57: error: Name "n" already defined on line 47  [no-redef]
3_meows.py:64: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:58: error: Name "n" already defined on line 48  [no-redef]
3_meows.py:65: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meow
None
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:58: error: Name "n" already defined on line 48  [no-redef]
Found 1 error in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
Success: no issues found in 1 source file
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 4
meow
meow
meow
meow
None
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:84: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
3_meows.py:84: error: Incompatible types in assignment (expression has type "None", variable has type "str")  [assignment]
Found 2 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 5
meowmeowmeow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meow

PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meow

PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meow
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meowmeow

PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:95: error: Name "meow" already defined on line 75  [no-redef]
3_meows.py:104: error: Name "number" already defined on line 83  [no-redef]
3_meows.py:105: error: Name "meows" already defined on line 84  [no-redef]
3_meows.py:105: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
Found 4 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:95: error: Name "meow" already defined on line 75  [no-redef]
3_meows.py:104: error: Name "number" already defined on line 83  [no-redef]
3_meows.py:105: error: Name "meows" already defined on line 84  [no-redef]
3_meows.py:105: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
Found 4 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 3
meow
meow
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 4
meow
meow
meow
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 5
meow
meow
meow
meow
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 4
meow
meow
meow
meow
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:95: error: Name "meow" already defined on line 75  [no-redef]
3_meows.py:104: error: Name "number" already defined on line 83  [no-redef]
3_meows.py:105: error: Name "meows" already defined on line 84  [no-redef]
3_meows.py:105: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
Found 4 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:92: error: Name "meows" is used before definition  [used-before-def]
3_meows.py:95: error: Name "meow" already defined on line 75  [no-redef]
3_meows.py:105: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
3_meows.py:105: error: Incompatible types in assignment (expression has type "None", variable has type "str")  [assignment]
Found 4 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
3_meows.py:95: error: Name "meow" already defined on line 75  [no-redef]
3_meows.py:105: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
3_meows.py:105: error: Incompatible types in assignment (expression has type "None", variable has type "str")  [assignment]
Found 3 errors in 1 file (checked 1 source file)
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> mypy 3_meows.py
Success: no issues found in 1 source file
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 4
  ____
 /    \
| meow |
| meow |
| meow |
| meow |
 \    /
  ====
    \
     \
       ^__^
       (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra> python 3_meows.py
Number: 4
  ____
 /    \
| meow |
| meow |
| meow |
| meow |
 \    /
  ====
    \
     \
      \
       \
                      _ ___.--'''`--''//-,-_--_.
          \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
         /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
        /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
       /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
       `-'``/  /  |  // \\__/\\__  /  \\__/ \\
            `-'  /-\\/  | -|   \\__ \\   |-' |
              __/\\ / _/ \\/ __,-'   ) ,' _|'
             (((__/(((_.' ((___..-'((__,'
PS F:\PHD Prep\Harvard CS50\GitHub From Cloud\Harvard-CS50\cs50 python\cs50 python etcetra>
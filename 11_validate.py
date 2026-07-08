# At first let's prompt the user to write their email address
                                  
# if the user add something with the @ sign then it's valid.
if False:
    email = input('What is your email address? ').strip()                               # strip() will be applied to the returned strinng by input() and after input() means it will be applied afterwards like input().append()
    if '@' in email:                                                                    # we don't have to write is before in here because the in operator will return a boolean value True or False, so we can use it directly in the if statement. Let's see how we can do this.
        print('valid')
    else:
        print('invalid')
# well we also need a dot. and we can use it after the @ sign
    if '@' and '.' in email:
        print('valid')
    else:
        print('invalid')

# Problem is if we type in just @. it will be valid but it is not a valid email address. So we need to check if the @ sign comes before the dot. We can use the find() function of the string object to find the index of the @ sign and the dot in the email address. Let's see how we can do this.
# we need dot in the domain name specifically not just in the username
# Let's add a bit more logic here, let's split the email string dataset using split(@) and we can create two variables username, domains and assign split parts to them resepctively. This is basically what it is
    username, domain = email.split('@')
    if username and '.' in domain:                                                        # This meanins if username is something, anything but nothing, it will give a true boolean signal. We can also add another boolean question using and "." in domain.
    # Here (username) and ('.' in domain) are seperate expression to run boolean with
        print('valid')
    else:
        print('invalid')

# but it will also validate malan@harvard. 

    username, domain = email.split('@')
    if username and domain.endswith('edu'):
        print('valid')
    else:
        print('invalid')
# this way we have a username that has something, the split function worked and no flag there, and we have a domain name that ends with edu
# here input malan@.edu works as well
# In python there is a library for regular expression called Re. In the re library we have a lot of capabilities to define, and check for and even replace patterns.
# Regular expression is a pattern, re will let usdefine some of these patterns, like a pattern for an email address, and use some built in functions that actually validates a user's inputs against that pattern or even use these patterns to change these user's inputs, or extract partial expression therefrom.
# let's have fun with re.search(pattern, string, flags=0) [it reminds me of reaper plugins like reapitch, reatune, reaverb]. It is going to be a pattern that we are going to search for instance a string that came from an user , the string argument here is going to be the the actual string that you are going to search for that pattern.
# flags are parameters that we are passing in to modify the behavior of the function but initially we are not going to even use this, we are gonna pass in couple of arguments instead.
# Let's use the re library and solve the problems incrementally, first let's import the re library at the top,

if False:
    import re
    email = input('What is your email address? ').strip()
    # we are gonna use this function super trivially for now, let's search inside re library if it contains '@', in the email variable
    if re.search('@', email):
        print('valid')
    else:
        print('invalid')
# we are still in the problem where inputing only @ gives valid. To use the library we need a bit of vocabulary in the realm of regular expressions inorder to be able to express ourselves more precisely
# In the world of regular expression, there are certain symbols to define certain patterns. 

'''
.[any character except a newline]
*[0 or more repetitions]
+[1 or more repetitions]
?[0 or 1 repetitions]
{m}[m repetitions]
{m,n}[m-n repetitions]
^[matches the start of the string]
$[matches the end of the string or just before the newline at the end of the string]
[][set of characters]
[^][complementing the set, anything except the character after ^]
\d[decimal digit]
\D[not a decimal digit]
\s[whitespace character]
\S[not a whitespace character]
\w[word character as well as numbers and the underscore]
\W[not a word character]
A|B[either A or B]
(...)[a group]
(?:...)[non-capturing version]
'''

if False:
    import re
    email = input('What is your email address? ').strip()
    # Get rid of the white spaces but we gotta pass in white spaces so we don't need strip() function in the input, but let's include lower() to force the input to be lowercase
    # we want any character before @, so dot . then * to represent 0 or more repetations. Same for after. But it will accept nothing as well. So we will use + in the place of *.
    # if re.search('.+@.+', email):                                                     # in the email variable having a string we are searching for .+@.+. If the re can find it after search then boolean is yes, otherwise invalid
    # we could also use '..*@..*'
    # now let's add .edu, but the danger is we are facing with some overlaps. . means any character, . means period.
    # we can use backslash and . . But we don't want also python to misinterprete this as an escape sequence like newline. So like f"str" we are going to make raw string with an r
    # if re.search(r'^.+@.+\.edu$', email):
    # if we have more than @s it wont flag, so let's use [^] to specify everything except @
    # if re.search(r'^[^@]+@[^@]+\.edu$', email):
    # we gott use hashes here because the escape sequence will cause problems
    # If we want to use [] then we can use a-zA-Z0-9, we don't need to use any comma whitespace, or anything else. It will just accept those sets of string characters. Computer's gonna know we mean a through z, we don't have to type in all the letters
    # if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$', email):                      # We also wanna include _ so, now it should be okay
    # we can also get rid of [a-zA-Z0-9_] altogether and use \w, which means word numeric including _ , we need to use escape sequence or the computer will think it'a a str character
    # if re.search(r'^\w+@\w+\.edu$', email):
    # in the space of edu we can use parentheses and we can or them together with a |. Here each of the vertical bars means or
    # if somebody inputs all uppercase then .EDU will work as email address but our code will show invalid, so we can add .lower() anywhere with our variable email after the input function
    # if re.search(r'^\w+@\w+\.(com|edu|govt|org|net)$', email.lower()):
    # We can also use flags, the third parameter for argument into re.search(). Some of the flags that we can pass into this function are these, they are built in variables,
    '''
    re.IGNORECASE[re.search will ignore the case, both uppercase and lowercase]
    re.MULTILINE[maybe user input spans multiple lines and we wanna match with each line of the input paragraog]
    re.DORALL[we can make dots any character plus new line instead of any character except a new line]
    '''
    # again if we input malan@cs50.harvard.edu; because of the loopiong nature of the matching each character in the flow diagram, the dot string will be considered as \. and as there is no edu after that it will give invalid. We might also have malan@something.cs50.harvard.edu
    # if we want to tolerate a sub domain like cs50 or something we can use the group function, using r'^\w+@\w+\.\W+\.edu$' will not work. We can use ?[0 or 1 repetition] but how do we use it? we wrap around the group of pattern symbols using parentheses and it will stay as is. The ? will only work if we use it after the parentheses group i.e, (\w+\.)? . We can also use * where 0 or more repetitions are allowed
    # if re.search(r'^\w+@(\w+\.)*\w+\.(com|edu|govt|org|net)$', email, re.IGNORECASE):
    # if we have literal dots in the username we can also allow that, by grouping (\w|\.) before + which means, word character or literal dot with one or more repetitions,
    if re.search(r'^(\w|\.)+@(\w+\.)*\w+\.(com|edu|govt|org|net)$', email, re.IGNORECASE):
        print('valid')
    else:
        print('invalid')
    # we can also use re.match() which is same as re.search() but it comes up with this ^ symbol that we are using.
    # There is also re.fullmatch() where we also don't have to use the $ sign at the end

# Let's consider a situation where we store user input and clean up a little. We can use open save csv etc functions
# Let's create a function that will help us clean up data not manually, so lets code 11.1_format.py
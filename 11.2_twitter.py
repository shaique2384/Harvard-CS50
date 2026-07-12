# one final example where we very specifically extracting information in order to ansere some questions
# The goal of this excercise is to prompt users for the url of their twitter profile and extract from it, infer from the url what is the user's username
# we are canonicalizing, standardizing user inputs while being flexible with the user

if False:
    import re

    url = input('URL: ').strip()
    if matches := re.search(r'\w+[://]\w+\.(\w+)\.(\w+)[/](\w+|\.+)', url):
        print(f"your username for {matches.group(1)} under domain {matches.group(2)} is {matches.group(3)}")
    else:
        print("ERROR!")


if False:
    url = input('URL: ').strip()
    # replace() is a str method like strip() split() capitalize() etc
    # replace has two arguments, first one replacee second one replacer. Nothing is "" this str, not even whitesapce

    username = url.replace('https://twitter.com/', "")
    print(f'USERNAME: {username}')                               

if False:
    url = input('URL: ').strip()
    # removeprefix() is a str method like strip() split() capitalize() etc
    # replace has two arguments, first one replacee second one replacer. Nothing is "" this str, not even whitesapce

    username = url.removeprefix('https://twitter.com/')
    print(f'USERNAME: {username}') 

# now let's use re library

if False:
    import re
    url = input('URL: ').strip()
    # there is also a re.search(pattern, repl, string, count=0, flag=0) in the regular expression library. It means substitute
    # here pattern is the replacee string, repl is the replacer string and string is the string at issue
    # username = re.sub(r'https://twitter\.com/', "", url)
    # let's tolerate corner cases of all the valid user inputs.
    # let's make match the start, let's make s in https, (www\.) and the whole protocol (https://) optional with a question mark
    # the work that we are doing is also called parsing
    # we can also use (www\.|) in the place of (www\.)?
    # make things easy, like jeff miley
    username = re.sub(r'^(https?://)?(www\.)?twitter\.com/', "", url)
    print(f'USERNAME: {username}')

# now let's try and use re.search to create conditional for twitter.com specifically

if False:
    import re
    url = input('URL: ').strip()
    matches = re.search(r'^(https?://)?(www\.)?\w+\.com/([a-zA-Z0-9\.]+).*$', url, re.IGNORECASE)
    if matches:                                                             # without if matches: conditional re.search() won't return matches.group(n)
        username = matches.group(3)
    print(f'USERNAME: {username}')

# we can tighten things up further with the walrus conditional and non capturing groups, (?:...) i.e, these groups will not be returned
import re
url = input('URL: ').strip()
if matches := re.search(r'^(?:https?://)?(?:www\.)?\w+\.com/([a-zA-Z0-9_\.]+).*$', url, re.IGNORECASE):
    print(f'USERNAME: {matches.group(1)}')

# there is also re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flag=0) it will find for us multiple copies of the same pattern in the entire string


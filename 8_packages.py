# Lest's talk about packages that exists. There are a lot of third party packages that you can install using pip, which is a package manager for Python. Pip allows you to easily install and manage third-party packages that are not included in the standard library. You can use pip to install packages from the Python Package Index (PyPI), which is a repository of thousands of third-party packages that you can use in your Python projects. To install a package using pip, you can use the command "pip install package_name" in your terminal or command prompt. For example, if you want to install the requests package, which is a popular package for making HTTP requests, you can use the command "pip install requests". Once you have installed a package using pip, you can import it into your Python code and use its functions and features just like any other library or module.
# Strictly speaking pythen itself is a package, it is a collection of modules that are organized in a specific way. The standard library that comes with Python is also a package, it contains a collection of modules that provide various functions and features for Python programmers. When you import a module from the standard library, you are importing it from the Python package. For example, when you import the random module, you are importing it from the Python package. So in a way, we are all using packages when we use Python and its standard library.
# It is not a file but rather a folder. Let's download from pypi.org and have fun.
# There's a fun one out there, a throwback to a command that has been around for decades called cowsay. It is a fun package that allows you to create ASCII art of a cow saying something. You can install it using pip and then use it in your Python code to create fun messages with cows. For example, you can use the cowsay package to create a cow that says "Hello, World!". 
# Python has a package manager called pip which awfully sounds like a pimp but it is actually a package manager that allows you to easily install and manage third-party packages for Python. With pip, you can install packages from the Python Package Index (PyPI) and other sources, making it easy to add new functionality to your Python projects. To use pip, you can simply run the command "pip install package_name" in your terminal or command prompt, and pip will handle the installation process for you. Once you have installed a package using pip, you can import it into your Python code and start using its features right away.

if False:
    import cowsay
    import sys

    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])                         # According to defintion it's not like print, I can't use comma this comma that, I need to use + to catenate.


# It's an asky art package, it allows you to create fun messages with cows. You can install it using pip and then use it in your Python code to create fun messages with cows. For example, you can use the cowsay package to create a cow that says "Hello, World!".
# Let's do trex, I don't know what it is but let's do it. It is a fun package that allows you to create ASCII art of a T-Rex saying something. You can install it using pip and then use it in your Python code to create fun messages with T-Rex. For example, you can use the trex package to create a T-Rex that says "Hello, World!".

if False:
    import cowsay
    import sys

    if len(sys.argv) == 2:
        cowsay.trex("hello, " + sys.argv[1]) 

# It will not run tho, 'cause if conditional. When the conditional is not satisfied, the code inside the if block will not be executed. In this case, since the condition is False, the code inside the if block will not run, and therefore the cowsay.trex function will not be called. If you want to see the output of the cowsay.trex function, you can change the condition to True or remove the if statement altogether.
# It's a demonstration how you can package staffs into cows and trexes and share it via internet as open source. You can create your own packages and share them with others, or you can use packages created by other developers to add new functionality to your Python projects. The Python community is very active and there are many packages available for a wide range of purposes, so you can easily find packages that suit your needs and interests.

# API is an application programing interface, it is a set of rules and protocols that allows different software applications to communicate with each other. An API defines how different software components should interact and exchange data, and it provides a way for developers to access the functionality of a software application or service without needing to understand its internal workings. APIs can be used to access data, perform operations, or integrate with other software applications, and they are commonly used in web development, mobile app development, and other areas of software development.
# It can refer to python files and functions. For example, when you import a module in Python, you are using an API to access the functions and features of that module. The module provides a set of functions and classes that you can use in your code, and the API defines how you can access and use those functions and classes. Similarly, when you use a third-party package in Python, you are using an API to access the functionality provided by that package. The package provides a set of functions and features that you can use in your code, and the API defines how you can access and use those functions and features. So in a way, APIs are an important part of how we interact with software applications and libraries in Python and other programming languages.
# APIs are third party services that we can write code to interact with. For example, if you want to access data from a web service, you can use an API provided by that web service to retrieve the data and use it in your Python code. Many web services provide APIs that allow developers to access their data and functionality, and these APIs can be used to create powerful applications and integrations. For example, you can use the Twitter API to access tweets and user data from Twitter, or you can use the Google Maps API to access map data and geolocation services. By using APIs, you can leverage the functionality of other software applications and services in your own projects, making it easier to create complex and powerful applications.
# Many APIs, not all, live in the internet these days. They are web APIs that allow you to access data and functionality from web services. These APIs typically use HTTP requests to communicate with the web service, and they often return data in a format such as JSON or XML. By using web APIs, you can access a wide range of data and functionality from various web services, such as social media platforms, weather services, financial data providers, and more. This allows you to create powerful applications that can integrate with multiple web services and provide a rich user experience.
# So long as you have a browser, as you have some experience in code in any language, like python, you can wtite code that in effect tends to be a browser connects to that third party API on aserver and download some data that you can then incorporate into your own program.
# Python has a very popular package called requests that allows you to easily make HTTP requests to web APIs and retrieve data. With the requests package, you can send GET, POST, PUT, DELETE, and other types of HTTP requests to web APIs and receive responses in various formats, such as JSON or XML. This makes it easy to interact with web APIs and integrate their functionality into your Python projects. For example, you can use the requests package to access the Twitter API and retrieve tweets, or you can use it to access the OpenWeatherMap API and retrieve weather data for a specific location. By using the requests package, you can easily connect to web APIs and incorporate their data and functionality into your Python applications.
# You can download it via pip, using the command "pip install requests". Once you have installed the requests package, you can import it into your Python code and start making HTTP requests to web APIs. For example, you can use the following code to make a GET request to the OpenWeatherMap API and retrieve weather data for a specific location.
# The reuest library allows you to send HTTP requests to web APIs and receive responses in various formats, such as JSON or XML. This makes it easy to interact with web APIs and integrate their functionality into your Python projects. For example, you can use the requests package to access the Twitter API and retrieve tweets, or you can use it to access the OpenWeatherMap API and retrieve weather data for a specific location. By using the requests package, you can easily connect to web APIs and incorporate their data and functionality into your Python applications.
# For example web requests, internet requests using python code essentially as though you are a browser yourself. You can automate there for the retreival of urls that starts with http or https, you can automate the retrieval of data from web APIs, you can automate the submission of forms on websites, and much more. By using Python to automate web requests, you can save time and effort when working with web data and services, and you can create powerful applications that can interact with the web in various ways.
# In summary, packages are collections of modules that provide additional functionality to Python, and they can be easily installed using pip. APIs are sets of rules and protocols that allow different software applications to communicate with each other, and they can be used to access data and functionality from web services. By using packages and APIs, you can enhance your Python projects and create powerful applications that can interact with the web and other software applications.
# Documents for this pypi package: https://pypi.org/project/requests/ 
# This is one of the reason why python is so popular, because it has a vast ecosystem of packages and libraries that allow developers to easily add functionality to their projects and interact with web services and APIs. With the right packages and APIs, you can create powerful applications that can do almost anything you can imagine, from data analysis and machine learning to web development and automation. So if you're interested in learning more about Python and its ecosystem of packages and APIs, there are many resources available online that can help you get started.
# There are so solutions to problems that you can have and may invariably have in the future when we write projects of our own.
# There's just really a vibrant ecosystem, a vibrant community of open source softwares that's that easy for us to install.
# Let's talk about itunes for instance, which is an API for their itune services, the software that provides the services of streaming and downloading music.
# Let's click on this https://itunes.apple.com/search?entity=song&limit=1&term=weezer and download a text file that looks awfully similar to a list and dictionary dataset which is a json file.
# Fun time! Let's download my song coriander lol https://itunes.apple.com/search?entity=song&limit=1&term=shaique , I am getting bald! :'() 
# In the text file we have a 2nd bracket pair and inside a third bracket inside of which we have another second bracket with a whole lot of strings and arguements, keywords and what not!
# It is a standard text formate called JSON, called Java Script Obkect Notation which yes is technically realated to yet another language called javascript but json itself is typically used nowadays as a language agnostic format for exchanging data between cmputers. Language agnostic means we can use any language to read or write json and it's technically a text based formate which means if I visit that url with my browser which gets downloaded is just a bunch of texts but that text is formatted in a standard way using square and curly braces, quotation marks and colons yhat ultimatly contains all of the information in apple's database about the wheezer's songs at least the first one and that's an api. It's an API, a mechanism wherby I can access data on someone else's server and somehow integrate into my program.
# My browser chrome is not something that I wrote I should actualy write some python codes that perhaps pretends to be a browser to grab the same data.

if False:
    import requests                                         # To make those http or s requests
    import sys                                              # Importing sys library to input command line arguments like spacification of the band I want to search for

    if len(sys.argv) != 2:                                  # Running some error managements, the user must input name of the file and single name of the band
        sys.exit("What's wrong with you?")                  # Let's keep things simple and exit the program prematurely in case of errors
                                                            # Now it's finally time to use the request library. The get function will simply grab and get the shits from the url which is a string, because we are grabing through txts. Let's close the url early and let's append using a catanation symbol + argv[1].
                                                            # respnse is the variable that we are getting from the apple server out in the blue using requests library using the function get.
                                                            # So whatever we are getting using requests we are making it pass through json() .

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    print(response.json())

# We should be seeing exactly the text file that we downloaded and was in json formate into our side effects window in the terminal
# By the way python is converting it into a python dictionary.
# In the side effects we are seeing a dictionary with keys and their values with colon.
# Let's use another library in that will allow me to format my data a little more cleanly. So let't import json library.
# Json library < https://docs.python.org/3/library/json.html > lets us manipulate data and print it that is format in a way that will be more easy for us to understand.
# Now we will be doing some pretty printing using json.dumpstring and indent=2 of print function over the same set of information.

if False:
    import json
    import requests                                         # To make those http or s requests
    import sys                                              # Importing sys library to input command line arguments like spacification of the band I want to search for

    if len(sys.argv) != 2:                                  # Running some error managements, the user must input name of the file and single name of the band
        sys.exit("What's wrong with you?")                  # Let's keep things simple and exit the program prematurely in case of errors
                                                            # Now it's finally time to use the request library. The get function will simply grab and get the shits from the url which is a string, because we are grabing through txts. Let's close the url early and let's append using a catanation symbol + argv[1].
                                                            # respnse is the variable that we are getting from the apple server out in the blue using requests library using the function get.
                                                            # So whatever we are getting using requests we are making it pass through json() .

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
    print(json.dumps(response.json(), indent=2))            # dumps means dump string and .means pass threturn value of response.json(). Dots in a line means functions from right to lefts as lines from top to bottom.

# Below is our printed json txt
"""
{                                                           # Hei! this is a dictionary in python; a collection of keywords and their values
  "resultCount": 1,                                         # First key is result count which has value 1 because we instructed the url to limit to one song of the artist
  "results": [                                              # The result key has a very big value of a python list implied by square brackets. The list has only item which is again a big dictionary!
    {                                                       # So a dictionary can be inside another dictionary.
      "wrapperType": "track",
      "kind": "song",
      "artistId": 1683292330,
      "collectionId": 1683293212,
      "trackId": 1683293213,                                # itunes database specific which is an integer.
      "artistName": "Shaique",
      "collectionName": "Coriander - Single",
      "trackName": "Coriander",                             # The track name. We can make this data useful i.e, find the name or names of the songs by the artist!
      "collectionCensoredName": "Coriander - Single",
      "trackCensoredName": "Coriander",
      "artistViewUrl": "https://music.apple.com/us/artist/shaique/1683292330?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/coriander/1683293212?i=1683293213&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/coriander/1683293212?i=1683293213&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview116/v4/cb/e9/d9/cbe9d9b9-7b84-6fa7-264e-e3e96631d395/mzaf_11833184229450909782.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/67/e1/4c/67e14ca0-e7a3-2f90-1bdd-517ba8774ec6/198025128219.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/67/e1/4c/67e14ca0-e7a3-2f90-1bdd-517ba8774ec6/198025128219.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/67/e1/4c/67e14ca0-e7a3-2f90-1bdd-517ba8774ec6/198025128219.jpg/100x100bb.jpg",
      "collectionPrice": 0.99,
      "trackPrice": 0.99,
      "releaseDate": "2023-05-01T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 1,
      "trackNumber": 1,
      "trackTimeMillis": 93300,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Rock",
      "isStreamable": true
    }
  ]
}
"""
# The above json file text is designed by an enginner of itunes who decided the design of the dataset. We can manipulate after we download it of course, but that is how itunes server works

if True:
    import json
    import requests                                         # To make those http or s requests
    import sys                                              # Importing sys library to input command line arguments like spacification of the band I want to search for

    if len(sys.argv) != 2:                                  # Running some error managements, the user must input name of the file and single name of the band
        sys.exit("What's wrong with you?")                  # Let's keep things simple and exit the program(unlike break which breaks out of the loop only) prematurely in case of errors
                                                            # Now it's finally time to use the request library. The get function will simply grab and get the shits from the url which is a string, because we are grabing through txts. Let's close the url early and let's append using a catanation symbol + argv[1].
                                                            # respnse is the variable that we are getting from the apple server out in the blue using requests library using the function get.
                                                            # So whatever we are getting using requests we are making it pass through json() .

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
    
    # This time we don't print that ugly txt sorry jsojn! Let's take a variable called o!
    o = response.json()
    '''
    for object in o:
        print(object)
        print("\n")
        print("###")
    '''
    for result in o["results"]:                             # o["results"] is giving us the value of keyword "results" which is in fact a list. The list has only one object which is another dictionary.
        print(result["trackName"])                          # We are iterating through the list as it has only one element which is a dictionary so it iterates once. When it's iterating the results[which is an object by definition but the dictionary in our case] the identifier result of the for loop is the dataSET[Remember set math? exact same thing] and therefore we can print the value of the keyword "trackName" by through square brackets inside the result[is the only list object but a dictionary data set, with keywords and values, itself] variable.

# aski arts is all we had before emojis and stickers.
# We can also make libraries of our own. Up untill we have been writing all of our codes in files with .py. 
# It's better to create a package of my frequently used codes in a package rather ctrls + v ing every time.
# We can keep it local on our local machine but also we can go through steps, bundle it up and make it open source and share it to the cloud and servers so that people can download it from pypi url.


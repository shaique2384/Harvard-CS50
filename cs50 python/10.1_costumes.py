if False:
    import sys

    from PIL import Image                           #v According to the documentation of the pillow library, we can use the Image module to read and write image files in various formats like JPEG, PNG, BMP, etc. We can also use the Image module to perform various image processing tasks like resizing, cropping, rotating, etc. Let's see how we can do this.
    images = []
    for arg in sys.argv[1:]:
        images.append(Image.open(arg))              #v We can use the open() function of the image module to read an image file and create an image object. We can then use the save() function of the image object to save the image in a different format. Let's see how we can do this.
    images[0].save('animated.gif', save_all=True, append_images=images[1:], duration=500, loop=0)  #v We can use the save() function of the image object to save the image in a different format. We can also use the save_all parameter to save all the images in a list as an animated GIF. We can also use the append_images parameter to append the images in a list to the first image. We can also use the duration parameter to set the duration of each frame in milliseconds. We can also use the loop parameter to set the number of times the animation should loop. Let's see how we can do this.
    
import sys
from PIL import Image
images = []
# Here we are just appending to the empty list after opening it from cmd arv input using the open() function on every iteration of the for loop. The open() function is a function specific to the pillow library that will give us the ability to open an image from the cmd argv input and gives us more functionality to deal with it. Let's see how we can do this.
for arg in sys.argv[1:]:                                     # The sys.argv is a list in Python, which contains the command-line arguments passed to the script. With the help of the sys.argv, we can pass the image file names as command-line arguments to the script. We can use the sys.argv[1:] to get all the command-line arguments except the first one the number [0], so the slice is from 1 to whatever rather than from 0, which is the name of the script itself. Let's see how we can do this.
    image = Image.open(arg)                                  # Image is a function that is used to create an image object. So open is a function specific to this library that will give us the ability to open an image from the cmd argv input and gives us more functionality to deal with it
    images.append(image)                                     # Now on every iteration it all append into our empty list which will not stay empty anymore. Remember that the loop attractor arg will iterate over all the arguments in the command line input, so we can have as many images as we want to create an animated GIF. We can also use the append() function of the list object to append an image object to a list. Let's see how we can do this.
# now we are going to save each image from the list in the disc. We don't have to open close etc because the pillow library takes care of it by calling the function save() on the image object. We can also use the save() function of the image object to save the image in a different format. Let's see how we can do this.
# In the argument of the save() function we specify the name of the file with quotation marks as it is a string, we save_all=True to save all the images in the list as an animated GIF, we append_images=images[1] to append the images in the list to the first image, we set duration=500 to set the duration of each frame in milliseconds, and we set loop=0 to set the number of times the animation should loop forever like a circle hence zero. Let's see how we can do this.
images[0].save(
    'costumes.gif', save_all=True, append_images=[images[1]], duration=500, loop=0
)
# if we have more images we can append multiple times with another loop.
# We just scratched some surface of the world if binary file i/o

# let's work on regular expressions, we call them regex, is really just a pattern matching tool that allows us to search for specific patterns in strings. We can use the re module in Python to work with regular expressions. Let's see how we can do this.
# To match on some kind of data, often user inputs. For instances if the user types in an email address, we want to validate that they typed in an email address not something else. We can use the re module to match a pattern in a string. Let's see how we can do this.
# We will have capability to define patterns in our code to compare them with data that we receive from the user. We can use the re module to define patterns in our code and compare them with data that we receive from the user. Let's see how we can do this.
# Before using reg ex let's create a context groundwork for them, let's solve some problems using some simpler syntax, too see what kind of limitation we run up against.
# Let's terminal code 11_validate.py 

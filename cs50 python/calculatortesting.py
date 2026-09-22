# We have tested own codes, running in some samples then running it again to test it
# it is much better practice to start writting a little extra code to test our codes.
# let's remember calculater.py and pick up from where we left off
if False:
    def main():
        x=int(user_input())
        print("x squared is", square(x))
    def user_input():
        return (input("What's x? "))
    def square(n):
        return n + n                                # it means take any value n and return it n * n
    # main()

    # I haven't methodically tested it, i just ran it using the terminal
    # It's not necesssarily the cas that it can run entirely
    # We gotta think about corner cases
    # We can not try it infinite ways but the representative inputs ultimately
    # let's make sure main() is not always called

    if __name__ == "__main__":
        main()
    # I wanna make sure that when I import as a library 
    # now let'a think about using it in a library main will not be called
    # Floating point values are not possible to represent by python rather accurately
if False:
    def main():
        name = input("whats your name? ")
        hello(name)
    def hello(to="world"):                          # it's job is to print only
        print("hello,", to)

    if __name__ == "__main__":
        main()

# let's change our hello() function so that it returns an f"string
if True:
    def main():
        name = input("whats your name? ")
        print(hello(name))
    def hello(to="world"):                          # it's job is to print only
        return f"hello, {to}"
    if __name__ == "__main__":
        main()
    # This is testable because our assert funtions are good at testing arguments into functions and return values not side 

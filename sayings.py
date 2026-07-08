# main function for testing
def  main():
    hello("world")
    goodbye("world")
# greeting function
def hello(name):                                    # fstring function and def function lets us use this () as an input portal
    print(f"hello, {name}")
# Adios function
def goodbye(name):
    print(f"goodbye, {name}")
if __name__ == "__main__":
    main()
# run to see if the function is top notch ;)
# now let'a think about using it in a library
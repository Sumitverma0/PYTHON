def decorator(func):
    def wrapper():
        print("I am about to print hello")
        func()
        print("I have executed this function ")
    return wrapper


@decorator
def say_hello():
    print("Hello!")
    
say_hello()

# f= decorator(say_hello)
# f()
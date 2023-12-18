def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper

def hash(func):
    def wrapp():
        print("#"*10)
        func()
        print("#"*10)
    return wrapp
# @star
def world():
     print("world")

hash(star(world))()

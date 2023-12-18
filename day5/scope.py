# a=10 #global scope cand be accessed anywhere
# def number():
#     global a #mathi ko global variable lai function ko local variable le override garxa
#     a=11 #local scope can be accessed only within the function
#     print(a)

# number()
# print(a)


a=10
def outer():
    a=11
    def inner():
        a=12
        print("Inner sees a as a ",a)
    inner()
    print("Outer sees a as a ",a) 

print("Main sees a as a ",a)
outer()

##Assignment
##loop condition function scope list append use garera user register and login banaune ani logout pani
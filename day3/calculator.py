def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Error! Division by zero is not allowed.")
        exit()
    else:
        return a/b

while True:
    print()
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    choice=int(input("Enter your choice form 1-4 "))
    a=int(input("Enter the value of a "))
    b=int(input("Enter the value of b "))

    if choice>5:
        print("Incorrect choice")
        break
    else:
        if choice==1:
            print("The sum is ", add(a,b))
        if choice==2:
            print("The difference is ",sub(a,b))
        if choice==3:
            print("The multiplication is ", mul(a,b))
        if choice==4:
            print("The division is ", div(a,b))
        if choice==5:
            print("Bye Bye")
            exit()

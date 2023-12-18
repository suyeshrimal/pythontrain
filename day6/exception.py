def divider():
        num1=int(input("Enter first num"))
        num2=int(input("Enter second num"))
        if num1==5:
            raise Exception("Input cannot be five")
        print(num1/num2)

try: 
    divider() 
    
except ZeroDivisionError:
    print("Cannot be divided ny zero")

except Exception as e:
    print("something went wrong", e)


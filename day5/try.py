status=False

def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper


users=[ {
        'user_name':'sumpumm',
        'password':'123456'
    },{
        'user_name':'aastha',
        'password':'smp123'
    },{
        'user_name':'sadil123',
        'password':'helloWorld'
    }
]


def register():
    name=input("Enter suitable username : ")
    password=input("Enter password for your account : ")
    users.append({'user_name':name,'password':password})
    print("Congratulations! You're registered!")
    
def logIn():
    global status
    print("Welcome to login portal")
    user_name=input("Username : ")
    password=input("password : ")   
    for i in users:
        if i['user_name']==user_name and i['password']==password and status==False:
            status=True
            #print(status)
            print("You are logged in!")
            break
    if(status==False):
        print("Username or password doesn't match. Try again")
        logIn()

def logOut():
    global status
    if status==True:
        status=False
        print("You're logged out")
        print("Goodbye!")
    else:
        print("Error!! please login first")
        logIn()
@star
def main():
    print("_____MENU_____")
    print("""
    1.Login
    2.Register
    3.Logout
    4.Exit
          """)
    choice=int(input("Enter your choice : "))
    if choice==1:
        logIn()
        main()
    elif choice==2:
        register()
        main()
    elif choice==3:
        logOut()
        main()
    else:
        print("Goodbyee")
        exit()

main()
# i=0
# while i<=10:
#     print(f"{i} Hello")
#     if i==5:
#         break   
#     i+=1

# fruits=['apple','mango','orange','peach','123',1.0]
# print("apples" in fruits)
# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# numbers=list(range(1,10,2))
# print(numbers)
# for i in range(1,21):
#     if i%2==0:
#         print(i, "is even") #or print(f"{i} is even")
#     elif i%2!=0:
#         print(i,"is odd")   #or print(f"{i} is odd")

#task
#1
#12
#123 do using for and while loop both

# words="suyesh"
# for char in words:
#     print(char)

# def hello_world():
#     for i in range(4):
#         print('Hello world')

# hello_world()
# hello_world()    
# def hello(name):
#     print(f"Hello, {name}! How are you")
# hello("Ram")
# hello("Hari")    
def person(name,age,address):
    print(f"""
            Hello my name is {name}
            and my age is {age}
            and i live in {address}
            """)
person(name="Suyesh", age=12, address="lolang")
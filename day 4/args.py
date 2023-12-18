# def sum(*numbers):
#     total=0
#     for number in numbers:
#         total+=number
#     print(total)
# sum(1,2,3,4,5)        

#assignment
#create a function person which takes names of person and print the names of each individual tyo ni my name is something bhanera

def person(*names):
    for name in names:
        print(f"My name is {name}")
person("ram","hari","shyam","suyesh","chotujijash","sumpumm","hancy")  
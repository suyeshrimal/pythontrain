# def sum_by_10(a):
#     return a+10

# s=lambda a:a+10
# print(s(10))
def myfunc(n):
    return lambda x:x*n


doubler=myfunc(3)
tripler=myfunc(4)
print(doubler(10))

print(tripler(30))
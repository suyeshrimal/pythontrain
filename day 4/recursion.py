# def number(num=0):
#     print(num)
#     number(num+1)

# number()

#task
#recreate range function using recursion

def rangeeee(start,stop,step=1):
    if start >= stop:
        return []
    else:
        return [start]+rangeeee(start+step,stop,step)

print(rangeeee(1,10,2))
    


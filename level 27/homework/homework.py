#def dws(num):
#    box1 = int(str(num)[::-1])
#    return box1
#print(dws(131520))

def nums(sum):
    x1 = []
    for i in sum:
        if i % 2 == 0:
            x1.append(i)
            return x1
x2 = nums([1,2,3,4,5,6])
print(x2)
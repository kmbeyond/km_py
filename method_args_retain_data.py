
def f1(x,l):
    for i in range(x):
        l.append(i*i)
    print(l)

#f1(3, [11,44])
#f1(3, [66,77])



def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)


f(2)
f(3,[3,5,1])
f(3)

f(4,[3,5,1])



#return (x,y) if there is an intersection of same elements in same horizontal or vertical line else (999,999)

array_2d = [
    [1,0,1],
    [1,1,1],
    [0,0,1]
]
#output: (1,2)

def crossed_index(array_2d):
    print(f"--------------")
    for i in range(len(array_2d)):
        print(f"{i} -> {len(list(set(array_2d[i])))}")
        if len(list(set(array_2d[i]))) == 1:
            for j in range(len(array_2d)):
                vert_list=[array_2d[k][j] for k in range(len(array_2d[j]))]
                print(f" -> {vert_list} = {len(list(set(vert_list)))}")
                if len(list(set(vert_list))) == 1:
                    return (i,j)
    return (999,999)


#test case #1
print(crossed_index(array_2d))
#(1,2)


#test case #2
array_2d_2 = [
    [1,0,1,0],
    [0,1,1,1],
    [1,1,0,1],
    [1,1,1,1]
]
print(crossed_index(array_2d_2))
#(999,999)


#test case #3
array_2d_3 = [
    [1,1,1,0],
    [0,1,1,1],
    [1,1,0,1],
    [1,1,1,1]
]
print(crossed_index(array_2d_3))
#(3,1)


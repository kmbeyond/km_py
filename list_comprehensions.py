

#Get squares list (usual way)
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#OR
squares = list(map(lambda x: x**2, range(10)))
print(squares)


#***** list comprehensions *****

squares = [x**2 for x in range(10)]
print(squares)




A = np.array([1,2,3,4])

B = np.array([100,200,300,400])

condition = np.array([True, True,False,False])

answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
print(answer)

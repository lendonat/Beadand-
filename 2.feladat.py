import numpy as np
def alsoharomszog(matrix):
    n=0
    m=len(matrix[0])
    for i in range(0,m-2):
        if matrix[i][m-1]!=0:
            return "nem also haromszog matrix"
        for j in range(1,n):
            n+=1
            if n!=m:
                if matrix[i][j]!=0:
                    return "nem also haromszog matrix"
    return "also haromszog matrix"
x=alsoharomszog([[1,0,0,0],[1,1,0,0],[1,1,1,0],[1,1,1,1]])
print(x)




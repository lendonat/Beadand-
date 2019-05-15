def alsoharomszog(matrix):
    for i in range(0, len(matrix)): 
        for j in range(i + 1, len(matrix)): 
            if(matrix[i][j] != 0):  
                    return False
    return True            
x=alsoharomszog([[1,0,0,0],[1,1,0,0],[1,1,1,0],[1,1,1,1]]) #teszt
print(x)




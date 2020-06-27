R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the no in matrix :") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

# checking weather no is prime  
print("The prime numbers from the matrix are: ")
for i in range(R): 
    for j in range(C): 
        if( matrix[i][j] > 1):
            for num in range(2, matrix[i][j]):
                if(matrix[i][j] % num) == 0:
                    break
            else:
                print(matrix[i][j])

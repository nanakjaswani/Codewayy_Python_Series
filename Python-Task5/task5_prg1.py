# Python code to illustrate 
# working of try()  
x = int(input("Enter first no "))
y = int(input("Enter second no "))
#divide(x, y):
     
try:
    
    result = x // y
    
    print("Yeah ! Your answer is :", result)
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")

if result > 9:  
    raise Exception('your result is greater than 9')
    
        
    
    

   

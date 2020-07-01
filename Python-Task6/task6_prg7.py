marks = int(input("Enter the marks "))
try:
    marks > 90
    print("True")
except IOError:
    print("Not True")    
        
if marks < 90:  
    raise Exception('your input is less than 90')

            
        

    
       
        
           
       
              
           


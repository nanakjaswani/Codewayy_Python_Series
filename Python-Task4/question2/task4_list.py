# Python program to calculate square of a number

#input a number
def functionSquare():
    number = int(input("Enter the number "))
    squareOfNumber = number * number
    print("Square of a number is= ", squareOfNumber)

def funMax():
    
    numbers = [ 10, 20, 30, 40]
    for i in numbers:      
        num = i 
        for j in numbers:
            if num >=j:           
                result = True
            else:
                result = False
                break
        if result == True:
            maximum = num
            print("Maxium no in list is= ",maximum)
            break

def funMin():
    
    numbers = [ 10, 20, 30, 40]
    for i in numbers:      
        num = i 
        for j in numbers:
            if num <=j:           
                result = True
            else:
                result = False
                break
        if result == True:
            minimum = num
            #print("\n")
            print("minimum no of list is= ",minimum)
            break

def funSum():
    
    total = 0
    ele = 0
    list1 = [11, 5, 17, 18, 23]  
    while(ele < len(list1)): 
        total = total + list1[ele] 
        ele += 1
    print("Sum of all elements in given list: ", total)            
    


  
    

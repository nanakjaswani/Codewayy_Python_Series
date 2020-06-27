def functionSquare(number):
    #number = int(input("Enter the number to print sq "))
    squareOfNumber = number * number
    print("Square of a number is= ", squareOfNumber)
#functionSquare()


#creating a list

#inputList = []

    
#list = int(input("Enter how many no do you wnat to add in list: "))
#for num in range(list):
 #   numbers = int(input())
 #print("the list is: ",inputList)
#function to find minimum and maximum element from the list
def funMin(inputList):
    minimum = inputList[0]
    for i in inputList:
        if(minimum > i):
            minimum = i
    print("the minimum element is: ", minimum)
#funMin()

def funMax(inputList):

    maximum = inputList[0]
    for i in inputList:
        if(maximum < i):
            maximum = i
    print("the maximum element is: ", maximum)
#funMax()

#function to find sum of elements of the list
def funSum(inputList):
    total = 0
    for n in inputList:
        total = total + n
    print("sum of element is: ", total)
#funSum()

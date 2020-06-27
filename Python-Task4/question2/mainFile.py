import task4_list
import task4_string
import task4_logical

number = int(input("Enter the no to print sq "))
task4_list.functionSquare(number)


inputList = []
    
list = int(input("Enter how many no do you wnat to add in list: "))
for num in range(list):
    numbers = int(input())
    inputList.append(numbers)
print("the list is: ",inputList)

#list
task4_list.funMax(inputList)
task4_list.funMin(inputList)
task4_list.funSum(inputList)

# string
print("\n")
inputString = input("Enter the string ")  
task4_string.middleChar(inputString)
task4_string.lengthOfString(inputString)
task4_string.funVowel(inputString)

print("\n")
#logical operators
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
task4_logical.logicalAnd(x,y)
task4_logical.logicalOr(x,y)
task4_logical.logicalNot(x,y)


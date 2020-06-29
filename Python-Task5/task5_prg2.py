import math

# returning the sq root of a number
num = int(input("Enter the number to print sq.rt "))
print(math.sqrt(num))

# returning the ceil value
numCeil = float(input("Enter the  float number to return ceil and floor value "))
print ("The ceil of entered no is : ", end="") 
print (math.ceil(numCeil))

# returning the floor value
print ("The floor of entered no is : ", end="") 
print (math.floor(numCeil))

#sorting the list
print("\nsorting for list \n")
org_list = [3, 1, 4, 5, 2]
print("orignal list is ",org_list)
org_list.sort()
print("sorted list is ",org_list)
org_list.sort(reverse=True)
print("Revere of list",org_list)

#sorting the tuples
print("\nsorting for tuples \n")
org_tuple = (3, 1, 4, 5, 2)
new_tuple_list = sorted(org_tuple)
print("orignal tuple list",org_tuple)
print("sorted tuple is",new_tuple_list)
new_tuple_reverse = tuple(sorted(new_tuple_list, reverse=True))
print("Reversed tuple is ",new_tuple_reverse)

#sorting the dict
print("\nsorting for Dict \n")
di = {'name': 'Corey', 'job': 'programming','age':None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)

#sorting the set
print("\nsorting for set \n")
fruits = {'apple', 'banana', 'grapes'}
fruits_sorted = sorted(fruits)
print("sorted set is ",fruits_sorted)
fruits_sorted = sorted(fruits,reverse=True)
print("Revere of set is ",fruits_sorted)



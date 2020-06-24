#sets and its method

#creating a set
stationary = {"pen" , "paper" , "pencil" , "eraser"}
print("set of stationary",stationary)

#add
stationary.add("shopner")
print("shopner added to stationary",stationary)

#remove the specific item/element
#discard/remove both can be used to remove item
#if the item which is to be remove is not present then remove will raise an error ,discard will not.
stationary.discard("pen")  
print("pen is removed",stationary)


#check if element is present in set
print("paper" in stationary)  #in is used to check the element is present or not

#len is used to print the length of the set
print(len(stationary))

#new set
ink = {"black" , "blue" , "red"}
#union returns new set with all item from both the set
NewSet = stationary.union(ink)
print(NewSet)

#clear() is used to empty the set
stationary.clear()
print(stationary)

#del is used to delete the set completely
del stationary
print(stationary)

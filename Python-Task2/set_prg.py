#sets and its method.

#creating a set
Stationary = {"pen" , "paper" , "pencil" , "eraser", "marker"}
print("set1\n",Stationary)

#creating a new set
ink = {"black" , "blue" , "red", "marker"}
print("set2\n",ink)

#intersection
Inter=Stationary.intersection(ink)
print("Intersection of two sets",Inter) #The intersection() method returns a set that contains the similarity between two or more sets.

#difference
Diff=Stationary.difference(ink)
print("Difference between two sets",Diff) #The difference() method returns a set that contains the difference between two sets.

#update
Stationary.update(ink)
print("updated set",Stationary) #If an item is present in both sets, only one appearance of this item will be present in the updated set.

#add
Stationary.add("shopner")
print("shopner added to stationary",Stationary)

#remove the specific item/element
#discard/remove both can be used to remove item
#if the item which is to be remove is not present then remove will raise an error ,discard will not.
Stationary.discard("shopner")  
print("shopner is removed",Stationary)

#check if element is present in set
print("paper" in Stationary)  #in is used to check the element is present or not if present it will print true else false

#len is used to print the length of the set
print(len(Stationary))

#union returns new set with all item from both the set
NewSet = Stationary.union(ink)
print("New Set is=",NewSet)

#clear() is used to empty the set
Stationary.clear()
print(Stationary)

#del is used to delete the set completely
del Stationary
print(Stationary)




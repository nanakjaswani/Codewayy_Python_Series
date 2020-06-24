#Methods used with list

#Creating a list
colors = [ 'red' , 'blue' , 'green' , 'yellow']
print("Colors in Rainbow",colors)

#The append() method adds a single item to the existing list.
#The item will be added to the end of list.
colors.append('indigo')
print("color added to rainbow",colors)

#insert() is used to insert the element/item at given index
colors.insert(2,'orange')
print("List after inserting the color orange",colors)

#remove() removes a given object from the list.
colors.remove('orange')
print("List after removing the color orange",colors)

#pop() removes and returns the value of given index.
colors.pop(4)
print("\n popping color indigo",colors)

#pop() without index will remove and return last item/element of list
colors.pop()
print("popping without index",colors)

#extend() function adds the specified list element to the end of current list.
Rainbow = [ 'orange' , 'indigo' , 'violet' , 'yellow']
colors.extend(Rainbow)
print("\n After Extending-",colors)

#reverse() is used to reverse the content of list.
colors.reverse()
print("Reversed List -\n",colors)

#count() returns the count of given element in a list.
count = colors.count('red')
print("Number of counts",count) #output=1
count = colors.count('black')
print("Number of counts",count) #output=0

#copy the content of one list to another
#Here content of list colors is being copied to new list called Rainbow.
Rainbow = colors
print("\n New List Rainbow =",Rainbow)

#sort() allows use to sort the list in ascending order.
#Here the list is arranged in asc order considering the initials.
Rainbow.sort()
print("List in sorted order", Rainbow)

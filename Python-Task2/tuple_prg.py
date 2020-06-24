#Tuples
#Tuples are immutable it means they cannot be changed

#creating a Tuple
Fruits = ('apple' , 'banana' , 'grapes' , 'cherry')
print("Tuple created",Fruits)

#count is used to count the number of item in tuple
count = Fruits.count('apple')
print("Total Count =",Fruits)

#index() is used to get the index position of the given item/element
index = Fruits.index('grapes')
print("index no of given fruit is -",index)

#length() it gives the length of given element/item
length = len(Fruits)
print("length of given string",length)

#max gives the max element of tuple
max_no = max(Fruits)
print("max element of tupleis",max_no)     #op-grapes as here g is the max element 

min_no = min(Fruits)
print("min element of tuple is",Fruits)     #op-apple as here a is the min element in tuple

#del is used to delete the tuple
del Fruits #this will del the tuple Fruits

#Program without taking input from user (already defined string)
#Defining the strings
#str1 = 'Hello '
#str2 = 'World'

# + operator is use to concatenate two strings

#str3 = str1 + str2
#print(str3)

#lengthOfString = len(str3)
#print(lengthOfString)




#Input from user
print("Enter two strings")

str1 = input("Enter first string- ")
str2 = input("Enter second string- ")

#Concatination of two strings
str3 = str1 + ' ' + str2    # Here ' ' is used to give the space between str1 and str2. Note It will also count the space while couting the length.
print("Concatenated string is " , str3)  

#calculating the length of string
lengthOfString = len(str3)
print("Length of concatenated string is- " , lengthOfString)



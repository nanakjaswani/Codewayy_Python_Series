import task4_list
import task4_string
import task4_logical


choice = input ("which program do you  want to run: A) List. B)String. C) Logical. [A/B/C]? :\n ")

if choice == "A":
    task4_list.functionSquare()
    task4_list.funMax()
    task4_list.funMin()
    task4_list.funSum()
   
elif choice == "B":

    task4_string.middle_char()
    task4_string.lengthOfString()
    task4_string.funVowel()

elif choice == "B":

    task4_logical.logicalAnd()
    task4_logical.logicalOr()
    task4_logical.logicalNot()

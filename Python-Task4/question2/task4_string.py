def middleChar(inputString):
    
   # inputString = input("Enter the string to find middle char ")    
    input1 = inputString[(len(inputString)-1)//2:(len(inputString)+2)//2]
    print(input1)

  
def lengthOfString(inputString):
    #global counter        
    #str = input("Enter a string to find length: ")
    counter = 0
    for s in inputString:
        counter = counter+1
    print("Length of the input string is:\n ", counter)



def funVowel(inputString):
    
    #string = input("Enter a string to print no of vowels :")
    vowels=0
    for i in inputString:
        
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    print("Number of vowels are:\n")
    print(vowels)
    


  



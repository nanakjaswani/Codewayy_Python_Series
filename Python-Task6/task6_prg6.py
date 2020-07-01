import math
def is_abundant(n):  
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])  
    return fctr_sum > n  
a = int(input("Enter the number "));  
if is_abundant(a):  
    print("The number is Abundant .");  
else:  
    print("The number is not Abundant.")





Number = int(input("\nPlease Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print("is a Perfect Number " )
else:
    print("is not a Perfect Number" )




   
def divsum(n) :   
   sum = 0  
   i = 1  
   while i<= math.sqrt(n) :   
      if (n % i == 0) :   
     
          if (n / i == i) :   
              sum = sum + i   
          else :  
              sum = sum + i;   
              sum = sum + (n / i)   
      i = i + 1  
   return sum  
def isDef(n) :     
       
   return (divsum(n) < (2 * n))   
     
n = int(input("\nEnter the number "))  
if ( isDef(n) ):   
   print("The number is deficient .")  
else :   
   print("The number is not deficient.")  



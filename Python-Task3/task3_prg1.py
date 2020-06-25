#Function to print the personal details of student
def personalDetails():
   firstName = input("Enter your firstName ")
   lastName = input("Enter your lastName ")
   Name = firstName + ' ' + lastName
   print("Your Name is-->", Name)
   print("\n")


#Function to print the Marks of subject and total marks obtained in Examination
def totalMarksObtained():
    print("Enter 'x' for exit.");
    print("Enter marks obtained in 5 subjects: ");
    m1 = input();
    if m1 == 'x':
        exit();
    else:
        m2 = input();
        m3 = input();
        m4 = input();
        m5 = input();
        mark1 = int(m1);
        mark2 = int(m2);
        mark3 = int(m3);
        mark4 = int(m4);
        mark5 = int(m5);
    
    global sum
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    
    print("Total marks obtained ",sum)

#Function to display the Percentage obtained
def percentageObtained(sum):
    global Percentage
    Percentage=(sum/5)
    print("Your Percentage is",Percentage)

#Function to print the grade obtained as per totalMarksObtained
def gradeObtained(Percentage):
    if(Percentage>=95):
        print("You got 'A'Grade")
    elif(Percentage>=85 and Percentage<=95):
        print("You got 'B' Grade")
    elif(Percentage>=75 and Percentage<=85):
        print("You got 'C' Grade")
    elif(Percentage>=65 and Percentage<=75):
        print("You got 'D' Grade")
    else:
        print(" You Failed an Exam")
       # print(" You Failed an Exam")

#Function to call other function declared above
def allDetails():
    personalDetails()
    totalMarksObtained()
    percentageObtained(sum)
    gradeObtained(Percentage)

#call to a function
allDetails()   
        
        
    

    
        


    


   
           
    


    

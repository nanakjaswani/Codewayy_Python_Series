class Report: # class
    
    def __init__(self, firstname, lastname, college, branch, tMarks): #self- use to access the attributes and methods of the class.
        self.firstname = firstname
        self.lastname = lastname
        self.college = college
        self.branch = branch
        self.tMarks = tMarks
        

      # Function display Full name
      
    def fullName(self):
       return "{} {}".format(self.firstname,self.lastname)


     # Function to display college details
     
    def collegeDetails(self):
        return "{} {}".format(self.college,self.branch)


     # Function to display total marks
     
    def marksObtained(self):
        totalMarks = sum(self.tMarks)
        return totalMarks
        


    
    def percent(self,totalMarks):   #calc percentage
        percentage = totalMarks / len(self.tMarks)
        return percentage
        #percentage = self.percent(totalMarks)

       
       
    def Grade(self,percentage): #Grading as per marks
        if percentage >= 95:
            return("Grade : A\n")
        elif(percentage>=80 and percentage<90):
            return("Grade: B\n")
        elif(percentage>=70 and percentage<80):
            return("Grade: C\n")
        elif(percentage>=60 and percentage<70):
            return("Grade: D\n")
        else:
            return("Grade: F\n")

    print("SCORECARD OF STUDENTS\n")   

    def Info(self):
        
        print("Name of student :",self.fullName())

        print("College and Branch :",self.collegeDetails())
        
        totalMarks = self.marksObtained()
        print("Total marks out of 500 is :",totalMarks)
        
        percentage = self.percent(totalMarks)
        print("Percentage :",percentage)
        
        grade = self.Grade(percentage)
        print(grade)


# Display report:
print("\nDetails of Student-1")
student1 = Report("Ram","Sharma","YCCE","Computer Technology",[99,99,99,99,99])
student1.Info()
print("\nDetails of Student-2")
student2= Report("Sham","Sharma","Raisoni","Computer Technology",[68,65,66,69,70])
student2.Info()
        
        


    
    


    
        
    

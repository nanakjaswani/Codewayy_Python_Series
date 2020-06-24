#using strings and variables

#Introduction part
FirstName = "Nanak "
MiddleName = "Ashok "
LastName = "Jaswani "

# Marks gained in subject Maths
M1 = 70
M2 = 78
M3 = 72
M4 = 82
DMGT = 90

#college Details
ClgName = "Yeshwantrao chavan college of engineering "
ClgAdd = "hingna road Nagpur"

#concatenating the name
FullName = FirstName + MiddleName + LastName
print(FullName)

#concatenate college details
ClgDetails = ClgName + ClgAdd # '+' operator is used to concatenate
print(ClgDetails)

#printing the marks obtained in sub maths

print("Marks Obtained")
print(" Marks in mathametics1=",M1)
print(" Marks in mathametics2=",M2)
print(" Marks in mathametics=",M3)
print(" Marks in mathametics=",M4)
print("Marks obtain in Discrete maths=",DMGT)

#calculating the Total Marks
Total = M1 + M2 + M3 + M4 + DMGT
print("Overall Marks Obtained",Total) #392 Total marks obtained

#calculating the percentage 
Total_Marks = 500
Percentage = (Total / Total_Marks)* 100
print("Percentage Obtained = ",Percentage) #78.4 percentage obtained


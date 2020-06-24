#Dictionary and its method

#creation of dict
StudentDb = {'name' : 'Nanak' , 'age': 20 , 'year' : 'third' }
print("the StudentDb dictionary" , StudentDb)

#get method is used to get the value of given element
get_StudentDb =StudentDb.get("name")
print("value for name is=", get_StudentDb)

#keys is used to find the attributes used
keys=StudentDb.keys()
print("keys of StudentDb=",keys)

#length is used to find the length of dict
Length=len(StudentDb)
print("Length of studentdatabse=",Length)

#values to print the data present in student database
Data=StudentDb.values()
print("Data in studentdb=", Data)

#pop is used to remove the given element from dict
StudentDb.pop("age")
print("popping the age from student database",StudentDb)

#update is used to update the dict
StudentDb.update({"age" : "20"}) #age is added to dict
print("\nupdation of studentdb",StudentDb)


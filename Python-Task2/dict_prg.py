#Dictionary and its method

#creation of dict
studentdb = {'name' : 'Nanak' , 'age': 20 , 'year' : 'third' }
print("the studentdb dictionary" , studentdb)

#get method is used to get the value of given element
get_studentdb =studentdb.get("name")
print("value for name is=", get_studentdb)

#keys is used to find the attributes used
keys=studentdb.keys()
print("keys of studentdb=",keys)

#length is used to find the length of dict
length=len(studentdb)
print("Length of studentdatabse=",length)

#values to print the data present in student database
data=studentdb.values()
print("Data in studentdb=", data)

#pop is used to remove the given element from dict
studentdb.pop("age")
print("popping the age from student database",studentdb)

#update is used to update the dict
studentdb.update({"age" : "20"}) #age is added to dict
print("\nupdation of studentdb",studentdb)


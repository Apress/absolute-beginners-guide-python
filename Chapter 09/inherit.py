from datetime import date

class Person :

    #define initialisations
    def __init__(self, name, dob, email):
        self.name = name
        self.dob = dob
        self.email = email

    #define class methods
    def getAge(self): 
        currentDate = date.today()
        age = currentDate.year - self.dob.year
        return age


class Student(Person):
    def __init__(self, name, dob, email, course, year):
            
        #inherit the methods and properties from parent class
        super().__init__(name, dob, email)
        
        #add any new attributes for child class
        self.course = course
        self.year = year

    #add any methods for child class
    def getGradYear(self):
        return self.year + 4


class Staff(Person):
    def __init__(self, name, dob, email, salary):
            
        #inherit the methods and properties from parent class
        super().__init__(name, dob, email)        

        #add any new attributes for child class
        self.salary = salary


        

#create an object
student = Student (
         "Sophie", #name
         date(1999, 4, 2), #DOB (year, month, day)
         "Sophie@mymail.com", #email
         "Computing",
         2019
)


print("Name: ", student.name)
print("Email: ", student.email)
print("Age: ", student.getAge())
print("Course: ", student.course)
print("Graduation year: ", student.getGradYear())


#create an object
lecturer = Staff (
         "John", #name
         date(1977, 4, 2), #DOB (year, month, day)
         "John@mymail.com", #email
         44000
)

print ("\nStaff Member: ", lecturer.name)
print ("Salary: ", "£", lecturer.salary)



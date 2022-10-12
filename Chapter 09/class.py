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


#create an object
person = Person (
         "Sophie", #name
         date(1999, 4, 2), #DOB (year, month, day)
         "Sophie@mymail.com", #email
)


print(person.name)
print(person.email)
print(person.getAge())


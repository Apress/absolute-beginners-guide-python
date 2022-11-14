class Vehicle :
   def __init__(self, name, speed, mileage):
      self.name = name 
      self.speed = speed 
      self.mileage = mileage
   def getName(self):
      return self.name
   

class Taxi (Vehicle):
   def  __init__ (self, name, speed, mileage):
      super().__init__(name, speed, mileage)
      
   def getFare(self, mileage):
      self.fare = mileage * 0.20


#get data from user
rn = input("Enter route name: ")
mil = int(input("Enter Mileage: "))


#create object pass data
route = Taxi(rn, 0, mil)


#call object method to calculate fare
route.getFare(mil)


#print results

print("\n\nRoute name is %s" % (route.getName()))

print("Mileage is %d" % (route.mileage))

print("The fare is $%f" % (route.fare))




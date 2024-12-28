class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car=Car("tata","nano")
print(my_car.brand)

class ElectricCar(Car):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)#use super key to acces the upper or parent class
        self.batterytype = batterysize

my_newCar=ElectricCar("tesla","model x","20kwh")

print(my_newCar.batterytype,my_newCar.brand)#this example of inheritance here where the electric is getting the property of parent class and getting the access of model and brand name 


#lets understand polymerphism and concept of private keys and static method
class Car2():
    def __init__(self,brand,model):#init is a constructor which is symbolise that it will run first when class is called
        self.__brand = brand# this doble __ make sure this is not getting acces by the subclass or child
        self.model = model

    
    def get_brand(self):
        return self.__brand
    @staticmethod#they are called decortors in pyhon which is used to enhance the methods
    def get_car_info(car):
        return f"Brand: {car.__brand}, Model: {car.model}"
    
class ElctCar(Car2):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)
        self.batterytype = batterysize

trycar=ElctCar("mahindra","modelunk","40kwh")
#print(ElctCar.brand)# this will throw error as we have privatised the brand 
print(trycar.get_brand())#this will run and give use acces
print(Car2.get_car_info(trycar))# this is static method so we can call

#do python support multiple inheritance 
#yes python support multiple inheritance
class Car3():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
class Car4(Car3):
    def __init__(self,brand,model,name): 
        super().__init__(brand,model)
        self.name = name
class Car5(Car4):
    def __init__(self,brand,model,name,year):
        super().__init__(brand,model,name)
        self.year = year
        #lets see how it works
tester=Car5("daddy","mommy","stepson",2034)
print(tester.brand, tester.model, tester.name, tester.year) #this is how multiple inheritance


        

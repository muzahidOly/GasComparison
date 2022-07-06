
from prettytable import PrettyTable

class Car:

    def __init__(self, name, year,mpg, price):
        self.name=name
        self.year = year
        self.mpg = mpg
        self.price=price

   


    def get_price(self):
        return self.price

    def set_price(self, x):
        self.price = x


    def get_year(self):
        return self.year

    def set_year(self, x):
        self.year = x
    
    def get_mpg(self):
        return self.mpg

    def set_mpg(self, x):
        self.mpg = x

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x
    

    def toString(self):
        print("Car Name: "+self.get_name())
        print("Car Year: "+ str(self.get_year()))
        print("Car MPG: "+str(self.get_mpg()))
        print("Car Price: "+str(self.get_price()))

    
  


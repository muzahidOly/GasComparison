import CarClass

import PrintTable


def start():


    """
    name1="Camry"
    year1=2001
    mpg1=25
    price1=5000
    car1 = CarClass.Car(name1,year1,mpg1,price1)


    name2="Prius"
    year2=2013
    mpg2=40
    price2=20000
    car2 = CarClass.Car(name2,year2,mpg2,price2)

    mileDrivenPerYear=10000

    priceOfGas=6.00

    PrintTable.printTable(car1,car2,mileDrivenPerYear,priceOfGas)

    """ 

    name1=input("Enter name of Car 1: ")
    year1=int(input("Enter year of Car 1: "))
    mpg1=float(input("Enter MPG of Car 1: "))
    price1=int(input("Enter Price of Car 1: "))
    car1 = CarClass.Car(name1,year1,mpg1,price1)
    print("\n")
    name2=input("Enter name of Car 2: ")
    year2=int(input("Enter year of Car 2: "))
    mpg2=float(input("Enter MPG of Car 2: "))
    price2=int(input("Enter Price of Car 2 ($): "))
    car2 = CarClass.Car(name2,year2,mpg2,price2)
    
    print()

    mileDrivenPerYear=int(input("How many miles do you drive in a year? "))

    priceOfGas=float(input("Price of gas ($): "))
    PrintTable.printTable(car1,car2,mileDrivenPerYear,priceOfGas)
    print("\n")


   
    



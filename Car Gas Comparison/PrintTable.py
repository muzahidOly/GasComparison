#Prints care info in table

from prettytable import PrettyTable


from tabulate import tabulate

import CarClass

def printTable(c1,c2,mileDrivenPerYear,priceOfGas):

    numberOfYearUses=int(input("How many years do you plan on using it? "))

    



    myTable = PrettyTable(["Car Name", "Year", "MPG", "Price"])
    car1=c1
    car2=c2
    gallonsPerYearCostCar1=mileDrivenPerYear/car1.get_mpg()*(priceOfGas)
    gallonsPerYearCostCar2=mileDrivenPerYear/car2.get_mpg()*(priceOfGas)

    priceForYear1Car1=str(round((gallonsPerYearCostCar1*1)+car1.get_price()))
    priceForYear1Car2=str(round((gallonsPerYearCostCar2*1+car2.get_price())))
    
    priceForYearXCar1=round((gallonsPerYearCostCar1*numberOfYearUses+car1.get_price()))
    priceForYearXCar2=round((gallonsPerYearCostCar2*numberOfYearUses+car2.get_price()))

    priceForYear5Car1=str(round((gallonsPerYearCostCar1*5)+car1.get_price()))
    priceForYear5Car2=str(round((gallonsPerYearCostCar2*5)+car2.get_price()))

    priceForYear10Car1=str(round((gallonsPerYearCostCar1*10)+car1.get_price()))
    priceForYear10Car2=str(round((gallonsPerYearCostCar2*10)+car2.get_price()))

    priceForYear15Car1=str(round((gallonsPerYearCostCar1*15)+car1.get_price()))
    priceForYear15Car2=str(round((gallonsPerYearCostCar2*15)+car2.get_price()))

    priceForYear20Car1=str(round((gallonsPerYearCostCar1*20)+car1.get_price()))
    priceForYear20Car2=str(round((gallonsPerYearCostCar2*20)+car2.get_price()))

    priceForYear25Car1=str((round(gallonsPerYearCostCar1*25)+car1.get_price()))
    priceForYear25Car2=str(round((gallonsPerYearCostCar2*25)+car2.get_price()))


    
    myTable = PrettyTable(["Car Name", "Year", "MPG", "Price","Price For Year 1","Price For Year 5","Price For Year 10","Price For Year 15","Price For Year 20","Price For Year 25"])


    myTable.add_row([car1.get_name(),car1.get_year(),car1.get_mpg(),car1.get_price(),priceForYear1Car1,priceForYear5Car1,priceForYear10Car1,priceForYear15Car1,priceForYear20Car1,priceForYear25Car1])
    myTable.add_row([car2.get_name(),car2.get_year(),car2.get_mpg(),car2.get_price(),priceForYear1Car2,priceForYear5Car2,priceForYear10Car2,priceForYear15Car2,priceForYear20Car2,priceForYear25Car2])

    print(myTable)

    

    if int(priceForYearXCar1)>int(priceForYearXCar2):
        print("After "+str(numberOfYearUses)+" years, the "+car1.get_name()+" ("+str(car1.get_year())+") "+"cost more compared to the "+car2.get_name()+" ("+str(car2.get_year())+") ")
        print("Purchase the "+car2.get_name()+" ("+str(car2.get_year())+")")
    elif int(priceForYearXCar2)>int(priceForYearXCar1):
        print("After "+str(numberOfYearUses)+" years, the "+car2.get_name()+" ("+str(car2.get_year())+") "+"cost more compared to the "+car1.get_name()+" ("+str(car1.get_year())+") ")
        print("Purchase the "+car1.get_name()+" ("+str(car1.get_year())+")")



    with open((car1.get_name()+" Vs "+car2.get_name())+".txt", 'w') as f:
        f.write("Thank You for using Muzahid's Gas Compareor\n")

        f.write(tabulate(myTable))

        if int(priceForYearXCar1)>int(priceForYearXCar2):
            f.write("\nPurchase the "+car2.get_name()+" ("+str(car2.get_year())+")")
        elif int(priceForYearXCar2)>int(priceForYearXCar1):
            f.write("\nPurchase the "+car1.get_name()+" ("+str(car1.get_year())+")")




   
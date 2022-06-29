from lib2to3.pgen2 import driver
from driver import Driver

class Car:
    id = int
    licence = str
    driver = Driver("","","","")
    passenger = int

    def __init__(self, license, driver):
        self.licence = license
        self.driver = driver

    def printDataCar():
        print ("Licencia: ")
    
    def setPassenger (self, passenger):
        if passenger == 4:
            self.passenger = passenger
        else:
            print("El auto debe contener 4 pasajeros")
from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    '''def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial'''
        
    def __init__(self, license, driver):
        super().__init__(license, driver)
    
    def setPassenger(self, passenger):
        if passenger == 6:
            self.passenger = passenger
        else:
            print("UberVan debe tener 6 pasajeros")
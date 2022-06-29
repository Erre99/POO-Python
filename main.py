from uberVan import UberVan
from car import Car
from driver import Driver
from user import User

if __name__ == "__main__":
    car = Car("FTE642", Driver("Andrea Herrera", "34GDS2","eerer@gmail.com","*****"))
    print(vars(car))
    print(vars(car.driver)) #Nos muestra el contenido del objeto en formato JSON
    car.setPassenger(4)
    print(car.passenger)

    user1 = User("Ricardo Díaz", "3E4DG6", "eieiei@hotmail.com", "*****")
    print(vars(user1))

    van = UberVan("DERS33", Driver("Ricardo Perez", "43ER44", "perre@gmail.com", "peeieieie"))
    van.setPassenger(5)
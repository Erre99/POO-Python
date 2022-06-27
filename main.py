from car import Car
from account import Account

if __name__ == "__main__":
    car = Car("FTE642", Account("Andrea Herrera", "34GDS2"))
    print(vars(car))

    print(vars(car.driver)) #Nos muestra el contenido del objeto en formato JSON
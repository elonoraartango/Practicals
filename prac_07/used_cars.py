"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car
from prac_07.limo import Limo

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    my_limo = Limo(100)
    my_limo.add_fuel(20)
    my_limo.drive(115)
    #print("Fuel =", my_limo.add_fuel())
    Limo.drive(my_limo, 115)
    print("odo =".format(my_limo.drive), my_limo.odometer)

main()

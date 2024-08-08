
#Task :

# Create an abstract class Car which will have abstract methods related to a

# car functionality(start_engine,stop_engine_drive)

# Implement concrete subclasess(ElectricCar,GasolineCar)

# Use the concrete subclasess (operate_car)
from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def start_enginee(self):
        pass
    @abstractmethod
    def stop_enginee_drive(self):
        pass
class ElectricCar(Car):
    def start_enginee(self):
        print("The car started")
    def stop_enginee_drive(Car):
        print("The car is stoped")
    
class GasolineCar(Car):
    def start_enginee(self):
        print("The GasolineCar is started")
    def stop_enginee_drive(self):
        print("The GasolineCar is stoped")
    
veh=ElectricCar()
veh.start_enginee()
veh.stop_enginee_drive()
print()

oil=GasolineCar()
oil.start_enginee()
oil.stop_enginee_drive()
#Car class
class Car:
    def move (self):
        print("The car drives on the road. ")

#Boat class
class Boat:
    def move (self):
        print("The boat sails on the water. ")

#Drone class
class Drone:
    def move(self):
        print("The drone flies in the sky. ")

#We can see here that classes are independent of each other but use the same method of move...

def start_trip(vehicle):
    vehicle.move()

#This calls the move method of each class and each class has a separate output, if they all have the method 'move', then all of them are under vehicle

#creates objects
car1 = Car()
boat1 = Boat()
drone1 = Drone()

#this is what makes them move
start_trip(car1)
start_trip(boat1)
start_trip(drone1)

#southparkkenny

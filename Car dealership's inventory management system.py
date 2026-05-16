class vehicle:
    color="white"
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.seating_capacity=None
    def assign_seating_capacity(self,seating_capacity):
        self.seating_capacity=seating_capacity
    def display_properties(self):
        print("properties of the vehicle")
        print("color:",self.color)
        print("Maximum Speed:",self.max_speed)
        print("Mileage:",self.mileage)
        print("seating capacity:",self.seating_capacity)
vehicle1=vehicle(200,20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2=vehicle(180,25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()

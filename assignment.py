# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_capacity = battery_capacity

    def call(self, contact_name):
        print(f"{self.brand} {self.model} is calling {contact_name}... 📞")

    def charge(self, amount):
        self.battery_capacity += amount
        print(f"{self.brand} {self.model} charged to {self.battery_capacity}mAh 🔋")

# Derived Class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, cooling_system):
        super().__init__(brand, model, storage, battery_capacity)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with {self.cooling_system} cooling system 🎮")

# Creating objects
smartphone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 4000)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", "512GB", 6000, "advanced vapor chamber")

# Interactions
smartphone1.call("Alice")
gaming_phone.play_game("PUBG Mobile")
gaming_phone.charge(500)

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()

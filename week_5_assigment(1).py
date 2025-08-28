# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # inheritance
        self.__storage = storage         # encapsulated attribute (private)
        self.__battery = battery

    # Getter & Setter (Encapsulation)
    def get_storage(self):
        return self.__storage
    
    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print(" Storage must be positive!")

    def call(self, number):
        print(f" Calling {number} from {self.device_info()}...")

    def charge(self):
        print(f"Charging {self.device_info()}...")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S25", 256, "5000mAh")
phone2 = Smartphone("Apple", "iPhone 16", 512, "4500mAh")

# Use methods
phone1.call("0745395981")
print("Storage:", phone1.get_storage())
phone1.set_storage(512)  # update storage
print("Updated Storage:", phone1.get_storage())

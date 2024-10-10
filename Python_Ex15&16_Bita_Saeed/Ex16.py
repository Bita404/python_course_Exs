class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def turn_on(self):
        print(f"The {self.brand} {self.model} is now powered on.")

    def turn_off(self):
        print(f"The {self.brand} {self.model} is now powered off.")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")


class Laptop(Device):
    def __init__(self, brand, model, price, ram_size):
        super().__init__(brand, model, price)  
        self.ram_size = ram_size

    def open_laptop(self):
        print(f"The {self.brand} {self.model} laptop is now opened.")

    def display_info(self):
        super().display_info()
        print(f"RAM Size: {self.ram_size}GB")

class Smartphone(Device):
    def __init__(self, brand, model, price, camera_resolution):
        super().__init__(brand, model, price) 
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"The {self.brand} {self.model} has taken a photo with a {self.camera_resolution}MP camera.")

    def display_info(self):
        super().display_info()
        print(f"Camera Resolution: {self.camera_resolution}MP")

#######################################################################################

laptop1 = Laptop("Asus", "nitro5", 999.99, 16)
smartphone1 = Smartphone("Samsung", "s23 ultra", 7999999, 12)

laptop1.turn_on()          
laptop1.open_laptop()      
laptop1.display_info()     
laptop1.turn_off()         


smartphone1.turn_on()      
smartphone1.take_photo()   
smartphone1.display_info() 
smartphone1.turn_off()     

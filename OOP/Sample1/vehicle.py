# vehicle.py

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def get_brand(self):
        return self.brand
    
    def set_brand(self, brand):
        self.brand = brand
    
    def display_info(self):
        print("Brand:", self.brand)
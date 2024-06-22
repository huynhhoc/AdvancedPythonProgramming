
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand)
        self.model = model
        self.year = year
        self.color = color
    
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def display_info(self):
        super().display_info()
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)

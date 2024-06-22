# main.py

from car import Car

def main():
    # Create a Car object
    my_car = Car(brand="Toyota", model="Corolla", year=2020, color="Red")
    
    # Display initial car information
    print("Initial Car Information:")
    my_car.display_info()
    
    # Modify car properties
    my_car.set_model("Camry")
    my_car.set_year(2021)
    my_car.set_color("Blue")
    
    # Display updated car information
    print("\nUpdated Car Information:")
    my_car.display_info()

if __name__ == "__main__":
    main()

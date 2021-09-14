def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32.0)*5.0/9.0
def above_freezing(celsius):
    return celsius > 0
# dong tu 7 - 12: khong phai la main cua baking.py
if __name__ == '__main__':
    fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print ('It is above freezing.')
    else:
        print ('It is below freezing.')
else:
    print("ahihi")

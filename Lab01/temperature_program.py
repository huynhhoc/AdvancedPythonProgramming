def convert_to_celsius(fahrenheit: float) -> float:
<<<<<<< HEAD
    """Return the number of celsius degrees equivalent to fahrenheit degrees
    >>> convert_to_celsius(75)
    23.88888888888889
    """
=======
>>>>>>> 5385da7274f2db842a83d56531924c557d110361
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
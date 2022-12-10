"""
File: wind_chill_calculator.py
Author: Marcos Ismayle

Purpose: Calculate the wind chill in Fahrenheit degrees using
a temperature inputed by an user even in Fahrenheit or Celsius,
and print a list with the result for each wind speed fro 5 to 
60 miles per hour.
"""

# Function to calculate the wind chill
def compute_wind_chill(T, V):
    return (35.74 + (0.6215 * T) - 35.75 * (V ** 0.16) + ((0.4275 * T) * (V ** 0.16)))
# Function to convert celsius to Fahrenheit
def convert_temperature(celsius):
    return (celsius *(9 / 5)) + 32

again = 'Y'

while again.upper() == 'Y':
    # Declaring global variables
    T = float(input('What is the temperature? '))
    V = 0
    scale = input('Fahrenheit or Celsius (F/C)? ')
    scale = scale.upper() # Convert inputs to upper case

    # If the scale is Fahrenheit, compute the wind chill
    if scale == 'F':
        while V < 60:
            V += + 5
            wind_chill = compute_wind_chill(T, V)    
    
            print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F')
    # If the scale is Celsius, convert to Fahrenhei and then compute the wind chill
    elif scale == 'C':
        T = convert_temperature(T)
        while V < 60:
            V += + 5
            wind_chill = compute_wind_chill(T, V)    
    
            print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F')

    again = input('Calculate again? (Y/N) ')

print('Thank you, good bye!')
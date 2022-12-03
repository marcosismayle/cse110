"""
File: life-expectancy.py
Author: Marcos Ismayle

Purpose: Practice reading and using data from an external file.
"""

# 1. Download the dataset:
#   The file was saved in the same directory that the python file.

# 2. Load the dataset in your Python program:

with open('life-expectancy.csv') as expectancy_file:
    #next(expectancy_file) # skip the first line
    
    min_exp = 99999999999999999999
    max_exp = -1

# 3. Iterate through the data line by line:
    for line in expectancy_file:
        
        clean_line = line.strip() # Delete extra spaces and blank lines
# 4. Split each line into parts:        
        parts = clean_line.split(',')

        life_exp = float(parts[3]) # store Life expectancy in a variable and convert string to float

# 5. Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. (Note that at this point, you just need the value for this, not the year and the country for that value.)    
    
        min_exp = min(life_exp, min_exp) # store the minimum number
        max_exp = max(life_exp, max_exp) # store the maximun number

    print(f'\nThe overall max life expectancy is: {max_exp}')    
    print(f'The overall min life expectancy is: {min_exp}\n')

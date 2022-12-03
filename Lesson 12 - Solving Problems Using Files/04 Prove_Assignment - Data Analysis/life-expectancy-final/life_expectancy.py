"""
File: life-expectancy.py
Author: Marcos Ismayle

Purpose: Practice reading and using data from an external file.
"""

# 1. Download the dataset:
#   The file was saved in the same directory that the python file.

# 2. Load the dataset in your Python program:

with open('life-expectancy.csv') as expectancy_file:
    next(expectancy_file) # skip the first line
    
    max_exp = -1
    min_exp = 99999999999999999999
    year_interest = input('Enter the year of interest: ')
    max_entity = ''
    max_year = ''
    min_entity = ''
    min_year = ''
    max_entity_interest = ''

# 3. Iterate through the data line by line:
    for line in expectancy_file:
        
        clean_line = line.strip() # Delete extra spaces and blank lines
# 4. Split each line into parts:        
        parts = clean_line.split(',')

        entity = parts[0]
        code = parts[1]
        year = parts[2]
        life_exp = float(parts[3]) # store Life expectancy in a variable and convert string to float

# 5. Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. (Note that at this point, you just need the value for this, not the year and the country for that value.)    
    
        max_exp = max(life_exp, max_exp) # store the maximun number

        min_exp = min(life_exp, min_exp) # store the minimum number

        if max_exp == life_exp:
            max_entity = entity
            max_year = year

        elif min_exp == life_exp:
            min_entity = entity
            min_year = year

        if year == year_interest:
            print(max_exp)

"""    print(f'\nThe overall max life expectancy is: {max_exp} from {max_entity} in {max_year}')    
    print(f'The overall min life expectancy is: {min_exp} from {min_entity} in {min_year}\n')
    print(f'For the year {year_interest}:')
    #print(f'The average life expectancy across all countries was {}')
    print(f'The max life expectancy was in {max_entity_interest}')
    #print(f'The min life expectancy was in {} with {}')"""

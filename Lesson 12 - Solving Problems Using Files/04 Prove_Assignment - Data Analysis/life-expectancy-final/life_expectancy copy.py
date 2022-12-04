run_again = 'yes'

while run_again == 'yes':

    max_exp = -1
    min_exp = 99999999999999999999
    max_entity = ''
    max_year = -1
    min_entity = ''
    min_year = 4000
    max_exp_interest = -1
    min_exp_interest = 99999999999999999999999
    max_entity_interest = ''
    min_entity_interest = ''
    sum = 0
    count = 0
    average = 0    
    year_interest = int(input('\nEnter the year of interest between 1543 and 2019: '))


    with open('life-expectancy.csv') as expectancy_file:
        next(expectancy_file) # skip the first line

    # 3. Iterate through the data line by line:
        for line in expectancy_file:
            
            clean_line = line.strip() # Delete extra spaces and blank lines
    # 4. Split each line into parts:        
            parts = clean_line.split(',')

            entity = parts[0]
            code = parts[1]
            year = int(parts[2])
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
                max_exp_interest = max(life_exp, max_exp_interest)
                min_exp_interest = min(life_exp, min_exp_interest)

                if max_exp_interest == life_exp:
                    max_entity_interest = entity

                elif min_exp_interest == life_exp:
                    min_entity_interest = entity

                sum += life_exp
                count += +1
                average = sum/count
                


        print(f'\nThe overall max life expectancy is: {max_exp} from {max_entity} in {max_year}')    
        print(f'The overall min life expectancy is: {min_exp} from {min_entity} in {min_year}\n')
        print(f'For the year {year_interest}:')
        print(f'The average life expectancy across all countries was {average:.2f}')
        print(f'The max life expectancy was in {max_entity_interest} with {max_exp_interest}')
        print(f'The min life expectancy was in {min_entity_interest} with {min_exp_interest}\n')
    run_again = input('\nDo you wanna see another year? ')

print('\nGood bye!\n')
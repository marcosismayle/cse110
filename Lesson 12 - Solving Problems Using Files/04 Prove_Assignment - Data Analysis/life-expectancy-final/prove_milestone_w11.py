# W11 Prove Milestone - Write a program to help analyze a large amount of data stored in a file.

with open("life-expectancy.csv") as f:
    next(f) #skip the first line

    #set variable to find max and min life exp
    lowest = 9999999999
    lowest_country = ""
    lowest_year = 1
    highest = -1
    highest_country = ""
    highest_year = 1
    user_year = int(input("Enter the year of your interest: "))

    #iterate each line of the document
    for line in f:
        data = line.strip().split(",") #Clean and split each line into parts
        
        life_expectancy = float(data[3]) #store years of life expectancy
        country = data[0]
        year = int(data[2])

        #store the country with lowest life expectancy
        if life_expectancy < lowest:
            lowest = life_expectancy
            lowest_country = country
            lowest_year = year

        #store the country with highest life expectancy
        if life_expectancy > highest:
            highest = life_expectancy
            highest_country = country
            highest_year = year

    
print(f"\nThe overall max life expectancy is: {highest} from {highest_country} in {highest_year}")
print(f"The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}\n")
print(f"For the year {user_year}: ")


with open("life-expectancy.csv") as f:
    next(f) #skip the first line

    #set variable to find max and min life exp
    lowest = 9999999999
    lowest_country = ""
    lowest_year = 1
    highest = -1
    highest_country = ""
    highest_year = 1
    total_life_exp = 0
    average_life_exp = 0
    count = 0

    for line in f:
        data = line.strip().split(",") #Clean and split each line into parts
        
        life_expectancy = float(data[3]) #store years of life expectancy
        country = data[0]
        year = int(data[2])
        

        #store data for user selected year
        if year == user_year:
            if life_expectancy < lowest: #min life exp
                lowest = life_expectancy
                lowest_country = country
            if life_expectancy > highest: #max life exp
                highest = life_expectancy
                highest_country = country
            #average of life exp
            total_life_exp += life_expectancy
            count += +1  # count how many lines with the year choose exist ---> that is how I found the length

            average_life_exp = total_life_exp / count # average is calculated using the count variable


print(f"The average life expectancy across all countries was {average_life_exp:.2f} ")
print(f"The max life expectancy was in {highest_country} with {highest}")
print(f"The min life expectancy was in {lowest_country} with {lowest}\n")
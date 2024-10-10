# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 #variable for total month counter
total_net = 0 #variable for total net sum counter

# Add more variables to track other necessary financial data
total_change = 0 #for net change part, variable to hold value of each value in profil column
count = 0 #counter variable
previous_value = None #checks if previous row in profit column has a value or not

#Matching Month variables

#IncreaseProfits Variables
previous_valuee = None #checks if previous row in profit column has a value or not
max_difference_row = None #Variable for finding the row adjacent to the greatest increase
max_difference = 0 #To store the largest absolute difference
max_row_number = None
row_number = 0

#DecreaseProfits Variables
previous_valueee = None #checks if previous row in profit column has a value or not
max_decrease = 0 #To store the most negative difference
max_decrease_row = None #Variable for finding the row adjacent to the greatest decrease

# Open and read the csv
with open(file_to_load) as financial_data: #opens file in the file_to_load column
    reader = csv.reader(financial_data)

    # Skip the header row cause that row only has words
    #in it so don't wanna calculate anything in it
    header = next(reader)

    #Extract first row to avoid appending to net_change_list


    #Process each row of data
    for row in reader: #iterates through each row in reader variable
        #Calclates total months
        if row[0]: #grabs the data in column 0 and the amount of entries in col
            total_months += 1 #adds plus one to whatever number is total_months, which
                              #is just the amount of entries in column 0

        #Track the total
        total = row[1] #assigns tracker variable to column 1
        if total: #Ensure the value is not empty
            try:
                total_net += int(total) #adds value of each row into total_net variable over and over
            except ValueError:
                pass #Ignores values in row that can't be counted or converted to an integer

        #Track the net change
        change = row[1] #assigns tracker variable to column 1
        if change: #Ensures variable is not empty, literally if change has a value with it 
            try:
                current_value = float(change) #Converts value to to float

                if previous_value is not None: #If there's a previous value
                    delta = current_value - previous_value #change formaula
                    total_change += delta #adds value of change into total_change counter
                    count += 1 #Increment the count of changes

                previous_value = current_value #Places current value into last, then moves on to next value

            except ValueError:
                print(f"Non-numeric value found: {change}") #shows if there a non number value
                pass
            
#This caluculates the average of change between entries         
#if count > 0: # if there is a change pretty much
    #average_change = total_change / count #total sum of coulumn divided by amount of change
    #print(f"Average change: {average_change:.2f}")
#else:
    #print("No valid numeric data")
                    
        
        #Calculate the greatest increase in profits (month and amount)
        InProfits = row[1] #Collects all values in column 1
        if InProfits:
            try:
                current_valuee = int(InProfits) #converts all values of column 1 to integers

                if previous_valuee is not None: #literally if there is a value in the column 
                    difference = abs(current_valuee - previous_valuee) #gets the 

                    if difference > max_difference: #if difference is greater than 0 then that max difference is now that vlaue
                        max_difference = difference
                        max_difference_row = row
                        max_row_number = row_number
                        
                previous_valuee = current_valuee #Places current value into last, then moves on to next value
                row_number += 1

            except ValueError:
                print(f"Non-numeric value found: {InProfits}") #shows if there a non number value
                pass
            
#if max_difference_row:
    #print(f'Occurs in month: {max_difference_row[0]}') #just printing output
#else:
    #print('No valid data found')

        # Calculate the greatest decrease in losses (month and amount)
        #DeProfits = row[1]
        current_valueee = int(row[1]) #converts all values of column 1 to integers
        if previous_valueee is not None: #literally if there is a value in the column 
            decrease = current_valueee - previous_valueee

            if decrease < max_decrease: #if difference is less than 0 then that max decrease is now that vlaue 
                max_decrease = decrease
                max_decrease_row = row

                #previous_valueee = current_valueee
                #row_numberr += 1
        previous_valueee = current_valueee #Places current value into last, then moves on to next value
                    


            
#if max_decrease_row:
    #print(f"{max_decrease_row[0]} ({max_decrease})") #just printing output
#else:
    #print('No valid data foundddd')


# Calculate the average net change across the months
if count > 0:
    average_change = total_change / count #average formula: divides sum of all column by amount of rows counted in that count variable
    #print(f"Average change: {average_change:.2f}")
else:
    print("No valid numeric data")


# Generate the output summary

print("Financial Analysis \n \n"
"----------------------------\n")

print(f'Total months: {total_months}')

print(f'Total: ${total_net}')

print(f"Average Change: ${average_change:.2f}")

print(f"Greatest Increase in Profits: {max_difference_row[0]} (${max_difference})")

print(f"Greatest Decrease in Profits: {max_decrease_row[0]} (${max_decrease})")



# Print the output

# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)


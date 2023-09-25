# Import the modules
import os
import csv

# Set the path to where the csv file is located
budget_data_csv=os.path.join("Resources", "budget_data.csv")

# Set variables
total_months = 0
total_income = 0
Profloss = []
months = []
total_change_list = []

# Open as a csv file
with open(budget_data_csv) as csvfile:
    
    # Using csvreader to specify the variable and delimiter
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # Read header row first and store
    csv_header=next(csvreader)
    print(f"csv Header: {csv_header}")
    
    # Read each row of data after skipping header
    for row in csvreader:
    
        #Calculate total months
        total_months += 1
        
        #Calculate total income
        total_income += int(row[1])
        
        #Assign rows of dataset to new blank lists
        months.append(str(row[0]))
        Profloss.append(int(row[1]))

    # Caclculate change over the entire period
    for pl in range(1, len(Profloss)):
        
        # Add the changes from month to month over the period to a blank list
        total_change_list.append((int(Profloss[pl]) - int(Profloss[pl-1])))
        
        # Caculate the average of all the changes over the entire period
        total_change_average = sum(total_change_list) / len(total_change_list)
        
        # Round the average change to two decimal points
        rounded_total_average = round(total_change_average, 2)
        
        # Determine the greatest increase over the entire period
        greatest_increase = max(total_change_list)
        
        # Determine the greatest decrease over the entire period
        greatest_decrease = min(total_change_list)
        
        # Print the results to the terminal
        print("Financial Analysis")

        print("----------------------------------------")

        print(f"Total Months: {total_months}")
        print(f"Total: ${total_income}")
        print(f"Average Change:  ${rounded_total_average}")
        print(f"Greatest Increase in Profit: {months[total_change_list.index(max(total_change_list))]} (${greatest_increase})")
        print(f"Greatest Decrease in Profit: {months[total_change_list.index(min(total_change_list))]} (${greatest_decrease})")

# Set the path for where the text file will be written to
text_path =os.path.join("python-challenge", "PyBank", "Analysis", "Analysis.txt")

# Open the file path, write the analysis, and save the new text file to the path
with open(text_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_income}\n")
    txtfile.write(f"Average Change:  ${rounded_total_average}\n")
    txtfile.write(f"Greatest Increase in Profit: {months[total_change_list.index(max(total_change_list))]} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profit: {months[total_change_list.index(min(total_change_list))]} (${greatest_decrease})\n")Code will follow here

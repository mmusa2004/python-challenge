"""THIS IS MY FIRST PYTHON HOMEWORK CHALLENGE"""

#import OS and CSV libraries
import os
import csv

#create variables for calculations
month_counter = 0
sum_revenue = 0
sum_revenue_change = 0

#repeat code once for each data file
for file_count in range(1):
    file_name = "budget_data_" + str(file_count+1) + ".csv"

    #create path
    file_path = os.path.join('raw_data',file_name)

    #open file and create file handle
    with open(file_path,newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        #skip header row
        line = next(csv_reader,None)

        #grab data from first line
        line = next(csv_reader,None)
        max_month = line[0]
        min_month = line[0]
        revenue = float(line[1])
        min_revenue = revenue
        max_revenue = revenue
        previous_revenue = revenue
        month_counter = 1
        sum_revenue = float(line[1])
        sum_revenue_change = 0

        #read one line at a time
        for line in csv_reader:

            #increase counter for number of months in dataset
            month_counter = month_counter + 1

            revenue = float(line[1])

            #add to sum of revenue for data set
            sum_revenue = sum_revenue + revenue

            #find change in revenue between this month and last month
            revenue_change = revenue - previous_revenue

            #add change in revenue to net change in revenue for data set
            sum_revenue_change = sum_revenue_change + revenue_change

            #determine if change in revenue is a max or min for data set thus far
            if revenue_change > max_revenue:
                max_month = line[0]
                max_revenue = revenue_change

            if revenue_change < min_revenue:
                min_month = line[0]
                min_revenue = revenue_change

            #set previous revenue to revenue
            previous_revenue = revenue

        #finish calculations
        average_revenue = sum_revenue/month_counter
        average_revenue_change = sum_revenue_change/(month_counter-1)
        
        #print analysis to terminal
        print(f"Financial Analysis for {file_name}:")
        print("-------------------------------------------------------")
        print(f"Total Months: {month_counter}")
        print(f"Total : {sum_revenue}")
        print(f"Average Change: {average_revenue_change}"[:24])
        print(f"Greatest Increase in Profit: {max_month} {max_revenue}")
        print(f"Greatest Decrease in Profit: {min_month} {min_revenue}")
        print("")
        
        write_file = f"pybank_results_summary_{file_count}.txt"

        #open write file
        filewriter = open("Output/analysis.txt", "w")

        #print analysis to file
        filewriter.write(f"Financial Analysis for the Budget Revenue\n")
        filewriter.write("-------------------------------------------------------\n")
        filewriter.write(f"Total Months: {month_counter}\n")
        filewriter.write(f"Total : {sum_revenue}\n")
        filewriter.write(f"Average  Change: {average_revenue_change}"[:25])
        filewriter.write(f"\nGreatest Increase in Profit: {max_month} {max_revenue}\n")
        filewriter.write(f"Greatest Decrease in Profit: {min_month} {min_revenue}\n")
        filewriter.write("")

        filewriter.close()
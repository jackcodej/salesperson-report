"""Generate sales report showing total melons each salesperson sold."""

#place all code within a function named generate_sales
def generate_sales():
    #Use context manager to handle opening/closing of the .txt file
    with open('sales-report.txt') as current_file:
        #Create an empty dictionary
        employee_and_sales = {}
        #For each line in the current_file rstrip and split on '|', and add employee name as key and melon's sold as value
        for line in current_file:
            line = line.rstrip()
            entries = line.split('|')
            #If employee does not exist as a key create the entry and set value to melon_count
            if employee_and_sales.get(entries[0]) == None:
                employee_and_sales[entries[0]] = employee_and_sales.get(entries[0], int(entries[2]))
            else:
            #If employee exists in the dictionary add new value to existing value in dictionary
                employee_and_sales[entries[0]] = employee_and_sales[entries[0]] + int(entries[2])
    #for each salesperson print their name and melons sold
    for salesperson in employee_and_sales:
        print(f'{salesperson} sold {employee_and_sales[salesperson]} melons')


generate_sales()
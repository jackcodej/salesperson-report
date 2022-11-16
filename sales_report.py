"""Generate sales report showing total melons each salesperson sold."""


#Creates two empty lists (global variables) named 'salespeople' and 'melons_sold'
salespeople = []
melons_sold = []

#opening 'sales-report.txt' and setting the opened file to var f
f = open('sales-report.txt')

#for each line in the .txt file, rstrip it and split it on '|' characters
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    #set var salesperson equal to first element in the split line named entries
    salesperson = entries[0]
    #set var melons to third element and cast it as an integer
    melons = int(entries[2])

    #if the salesperson exists in the salespeople list grab the index of their location and increment the num of melons sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    #if salesperson does not exist in salespeople list, add the salesperson and melons sold to the corresponding list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#for each salesperson in salespeople print their name and melons sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
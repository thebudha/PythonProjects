import csv

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_id', 'product_id', 'price'])
    writer.writerow([1000, 0, 5])
    writer.writerow([1001, 1, 15])

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
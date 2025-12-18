import csv
total = 0
with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total += float(row[2])
print("Total Sales Amount: Rs", total)

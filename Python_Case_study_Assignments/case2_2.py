import csv
with open("attendance.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

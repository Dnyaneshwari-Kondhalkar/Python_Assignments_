import csv
count = 0
with open("attendance.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[2].lower() == "absent":
            count += 1
print("Number of employees absent:", count)

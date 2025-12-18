import csv
emp_id = input("Enter Employee ID to search: ")
found = False
with open("attendance.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[0] == emp_id:
            print("Record found:", row)
            found = True
            break
if not found:
    print("No record found for Employee ID", emp_id)

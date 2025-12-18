import csv
with open("attendance.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["EmpID", "Name", "Status"])
    n = int(input("How many employees? "))
    for i in range(n):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        status = input("Enter Status (Present/Absent): ")
        writer.writerow([emp_id, name, status])
print("attendance.csv created successfully.")

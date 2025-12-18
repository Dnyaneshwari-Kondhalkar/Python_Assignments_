import csv
with open("attendance.csv", "a", newline="") as f:
    writer = csv.writer(f)
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    status = input("Enter Status (Present/Absent): ")
    writer.writerow([emp_id, name, status])
print("Record of employee ID:", emp_id, name, status)

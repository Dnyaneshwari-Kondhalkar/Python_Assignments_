
with open("students.txt", "a") as f:
 record = input("Enter new student record (RollNo,Name,marks): ")
 f.write(record + "\t\n")

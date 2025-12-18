with open("students.txt", "w") as f:
    n = int(input("How many students? "))
    for i in range(n):
        record = input(f"Enter record {i+1} (RollNo,Name,marks): ")
        f.write(record + "\n")

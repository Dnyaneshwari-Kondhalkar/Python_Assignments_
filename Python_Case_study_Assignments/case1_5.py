name = input("Enter name to search: ")
with open("students.txt", "r") as f:
    for line in f:
        if name.lower() in line.lower():
            print("Record found:", line.strip())
            break
    else:
        print("No record found for", name)

with open("sales.txt", "a") as f:
    record = input("Enter new sales record (Date,Item,Amount): ")
    f.write(record + "\n")
print("Record appended successfully.")

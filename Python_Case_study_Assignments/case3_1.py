with open("sales.txt", "w") as f:
    n = int(input("How many sales records? "))
    for i in range(n):
        record = input(f"Enter record {i+1} (Date,Item,Amount): ")
        f.write(record + "\t\n")
print("sales.txt created successfully.")

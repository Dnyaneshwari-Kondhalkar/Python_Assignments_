import csv

with open("sales.txt", "r") as txt_file, open("sales.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Date", "Item", "Amount"])
    for line in txt_file:
        parts = [p.strip() for p in line.split(",")]
        writer.writerow(parts)
print("sales.txt converted to sales.csv successfully.")

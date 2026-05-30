import csv

employees = [["Name", "Age", "Salary"],
             ["Jack", 40, 1000],
             ["Paul", 20, 3000],
             ["Sandy",18,6000]]

file_path = "workes.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for employee in employees:
            writer.writerow(employee)
except PermissionError:
    print("Brak możliwości zapisu")
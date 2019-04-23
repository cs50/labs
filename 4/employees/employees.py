import csv

with open("employees.csv", "r") as file:
    print("Manager,LastName,FirstName")
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Manager"], row["LastName"], row["FirstName"], sep=",")

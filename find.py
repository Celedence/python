import csv

def find_user(first, last):
    with open("users.csv") as file:
        csv_reader = csv_reader(file)
        for (index, row) in enumerate(csv_reader:
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name,last_name)
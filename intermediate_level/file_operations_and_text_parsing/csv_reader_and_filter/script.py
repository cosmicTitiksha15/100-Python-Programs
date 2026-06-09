# Parse a CSV file and extract specific rows based on a criteria.

# Parsing means taking a raw chunk of data (like a string of text) and breaking it down into smaller, 
# structured pieces that a computer program can easily understand, validate, and work with.
import csv

# This function filters "engineering" employees from complete CSV file.
def filter_engineering_employees(reader):
    for row in reader:
        # row is a 'list' type.
        if row[1] == "Engineering":
            filtered_rows.append(row)
    return filtered_rows

with open("employees.csv", 'r') as infile:
    reader = csv.reader(infile)
    # reader is a _csv.reader type, not a list.
    filtered_rows = []
    filtered_rows = filter_engineering_employees(reader)
    
# writing into a new CSV file called "engineering_employees.csv" with the filtered rows.
with open("engineering_employees.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    # <class '_csv.writer'>
    writer.writerows(filtered_rows)
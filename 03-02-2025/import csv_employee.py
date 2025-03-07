import csv
import os

# Get the file path and name dynamically
file_path = input("Enter the folder path where the file should be saved (e.g., C:/Users/YourName/Documents/): ")
file_name = input("Enter the CSV file name (with .csv extension): ")

# Combine the folder path and file name to create the full path
full_path = os.path.join(file_path, file_name)

# Open file in write mode
file = open(full_path, "w", newline="")
writer = csv.writer(file)

# Writing the header
writer.writerow(["ID", "Name", "Department", "Salary"])

# Taking dynamic employee data
while True:
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    
    writer.writerow([emp_id, name, dept, salary])
    
    more = input("Add another employee? (yes/no): ").strip().lower()
    if more != 'yes':
        break

# Close the file after writing
file.close()
print(f"Data successfully written to {full_path}")

# Open file in read mode
file = open(full_path, "r")
reader = csv.reader(file)

print("\nEmployee Data from CSV File:")
for row in reader:
    print(row)

# Close the file after reading
file.close()

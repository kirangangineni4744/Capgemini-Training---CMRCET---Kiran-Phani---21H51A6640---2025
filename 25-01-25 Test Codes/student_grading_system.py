def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

name = input("Enter the student's name: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100  # Assuming each subject is out of 100
grade = calculate_grade(percentage)

print("\nStudent Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", f"{percentage:.2f}%")
print("Grade:", grade)

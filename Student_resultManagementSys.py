# Student Result Management System

students = {
    "Imran": 85,
    "Aman": 72,
    "Saurabh": 91,
    "Riya": 68,
    "Neha": 78
}

# Display all students
print("Student Results")
for name, marks in students.items():
    print(name, ":", marks)

# Calculate average marks
average = sum(students.values()) / len(students)
print("\nAverage Marks:", average)

# Find topper
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

# Display grades using list comprehension
grades = [
    f"{name} : {'A' if marks >= 90 else 'B' if marks >= 75 else 'C' if marks >= 50 else 'F'}"
    for name, marks in students.items()
]

print("\nGrades:")
for grade in grades:
    print(grade)
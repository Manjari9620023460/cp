def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


# ===== MAIN PROGRAM =====
name = "Rahul"
department = "Computer Science"
semester = "3"

marks = [85, 78, 90]   # fixed values (no input)

avg = sum(marks) / 3
grade = calculate_grade(avg)

print("\n--- Student Result ---")
print("Name       :", name)
print("Department :", department)
print("Semester   :", semester)
print("Average    :", round(avg, 2))
print("Grade      :", grade)

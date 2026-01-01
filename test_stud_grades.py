from stud_grades import calculate_grade

def test_stud_grades():
    # Test all possible grades
    assert calculate_grade(95) == "S"
    assert calculate_grade(85) == "A"
    assert calculate_grade(70) == "B"
    assert calculate_grade(55) == "C"
    assert calculate_grade(45) == "D"
    assert calculate_grade(30) == "F"

def test_average_for_hardcoded_student():
    # Hardcoded student in sgrade.py
    marks = [90, 85, 80]  # same as in your sgrade.py
    average = sum(marks) / len(marks)
    assert average == 85.0  # Confirm average is correct
    assert calculate_grade(average) == "A"  # Confirm grade is correct
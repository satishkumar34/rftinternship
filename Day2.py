def analyze_marks(marks):
    # Total students
    total_students = len(marks)

    # Average
    average = sum(marks) / total_students

    # Highest & Lowest
    highest = max(marks)
    lowest = min(marks)

    # Count above average
    above_avg_count = sum(1 for mark in marks if mark > average)

    # Grade distribution
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for mark in marks:
        if mark >= 90:
            grades["A"] += 1
        elif mark >= 75:
            grades["B"] += 1
        elif mark >= 60:
            grades["C"] += 1
        else:
            grades["F"] += 1

    # Print results
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Students Above Average:", above_avg_count)
    print("Grade Distribution:", grades)


# Example data
marks = [85, 92, 78, 60, 45, 30, 88, 76, 95]

analyze_marks(marks)

try:
    import pandas as pd
    import numpy as np
except ImportError as e:
    print(f"Error: Required modules not installed. {e}")
    print("Please install: pip install pandas numpy")
    exit()

# Create samplez dataset
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'math': [85, 92, 78, 88, 95, 72, 89, 81],
    'science': [90, 88, 82, 85, 92, 75, 91, 79],
    'english': [88, 85, 80, 90, 89, 68, 87, 84]
}

# Create DataFrame
df = pd.DataFrame(data)

print("=" * 80)
print("STUDENT PERFORMANCE DASHBOARD")
print("=" * 80)

# 1. Calculate Average Marks per Student
df['average_marks'] = df[['math', 'science', 'english']].mean(axis=1)

# 2. Add Grade Column (based on average)
def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'F'

df['grade'] = df['average_marks'].apply(assign_grade)

print("\n1. STUDENT PERFORMANCE WITH GRADES")
print("-" * 80)
print(df[['name', 'math', 'science', 'english', 'average_marks', 'grade']].to_string(index=False))

# 3. Calculate Subject-wise Average
print("\n\n2. SUBJECT-WISE AVERAGE")
print("-" * 80)
subject_avg = {
    'Math Average': df['math'].mean(),
    'Science Average': df['science'].mean(),
    'English Average': df['english'].mean()
}
for subject, avg in subject_avg.items():
    print(f"{subject}: {avg:.2f}")

# 4. Find Overall Average
overall_avg = df['average_marks'].mean()
print(f"\nOverall Class Average: {overall_avg:.2f}")

# 5. Find Topper (Highest Average Marks)
print("\n\n3. TOPPER")
print("-" * 80)
topper = df.loc[df['average_marks'].idxmax()]
print(f"Name: {topper['name']}")
print(f"Average Marks: {topper['average_marks']:.2f}")
print(f"Grade: {topper['grade']}")
print(f"Math: {topper['math']}, Science: {topper['science']}, English: {topper['english']}")

# 6. Count Students Above Average
above_avg_count = (df['average_marks'] > overall_avg).sum()
above_avg_percentage = (above_avg_count / len(df)) * 100
print(f"\n\n4. STUDENTS ABOVE AVERAGE")
print("-" * 80)
print(f"Number of students above average: {above_avg_count} ({above_avg_percentage:.1f}%)")
print("\nStudents above average:")
above_avg_students = df[df['average_marks'] > overall_avg][['name', 'average_marks', 'grade']]
print(above_avg_students.to_string(index=False))

# 7. FILTERING Examples
print("\n\n5. FILTERING EXAMPLES")
print("-" * 80)

# Filter students with grade A or above
print("\nStudents with Grade A or above:")
grade_a_students = df[df['grade'].isin(['A', 'A+'])][['name', 'average_marks', 'grade']]
print(grade_a_students.to_string(index=False))

# Filter students with math >= 85
print("\nStudents with Math >= 85:")
math_filter = df[df['math'] >= 85][['name', 'math', 'average_marks']]
print(math_filter.to_string(index=False))

# 8. Statistics and Aggregation
print("\n\n6. STATISTICS & AGGREGATION")
print("-" * 80)
print(f"Highest Average Marks: {df['average_marks'].max():.2f}")
print(f"Lowest Average Marks: {df['average_marks'].min():.2f}")
print(f"Median Average Marks: {df['average_marks'].median():.2f}")
print(f"Standard Deviation: {df['average_marks'].std():.2f}")

# Grade Distribution
print("\n\nGrade Distribution:")
grade_distribution = df['grade'].value_counts().sort_index(ascending=False)
for grade, count in grade_distribution.items():
    percentage = (count / len(df)) * 100
    print(f"Grade {grade}: {count} students ({percentage:.1f}%)")

print("\n" + "=" * 80)
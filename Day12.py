import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# BASIC DATA (Given)
# --------------------------
students = ["Amit", "Riya", "John"]
marks = [85, 92, 78]

# --------------------------
# BONUS DATA (Multiple Subjects)
# --------------------------
subjects = ["Math", "Science", "English"]

# Marks for each student in each subject
amit_marks = [85, 88, 82]
riya_marks = [92, 90, 95]
john_marks = [78, 80, 75]

# --------------------------
# SIMPLE BAR CHART
# --------------------------
plt.figure(figsize=(6, 4))
plt.bar(students, marks)

plt.title("Student Performance (Basic)")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show values on top
for i in range(len(marks)):
    plt.text(i, marks[i] + 1, str(marks[i]), ha='center')

plt.show()


# --------------------------
# GROUPED BAR CHART (BONUS)
# --------------------------

x = np.arange(len(subjects))  # label locations
width = 0.25  # width of bars

plt.figure(figsize=(8, 5))

plt.bar(x - width, amit_marks, width, label="Amit")
plt.bar(x, riya_marks, width, label="Riya")
plt.bar(x + width, john_marks, width, label="John")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Performance Comparison (Grouped Bar Chart)")

plt.xticks(x, subjects)
plt.legend()

# Add values on bars
for i in range(len(subjects)):
    plt.text(x[i] - width, amit_marks[i] + 1, str(amit_marks[i]), ha='center')
    plt.text(x[i], riya_marks[i] + 1, str(riya_marks[i]), ha='center')
    plt.text(x[i] + width, john_marks[i] + 1, str(john_marks[i]), ha='center')

plt.show()
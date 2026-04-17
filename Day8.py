# Dataset
data = [
    ("A", "IT", 50000),
    ("B", "HR", 40000),
    ("C", "IT", 60000),
    ("D", "HR", 45000)
]

from collections import defaultdict

# Grouping data
dept_salaries = defaultdict(list)
dept_employees = defaultdict(list)

for name, dept, salary in data:
    dept_salaries[dept].append(salary)
    dept_employees[dept].append((name, salary))

# 1. Average salary per department
avg_salary = {}
for dept, salaries in dept_salaries.items():
    avg_salary[dept] = sum(salaries) / len(salaries)

print("Average Salary per Department:")
for dept, avg in avg_salary.items():
    print(f"{dept}: {avg}")

# 2. Highest paid employee per department
print("\nHighest Paid Employee per Department:")
for dept, employees in dept_employees.items():
    highest = max(employees, key=lambda x: x[1])
    print(f"{dept}: {highest[0]} ({highest[1]})")

# 3. Count employees per department (Bonus)
print("\nEmployee Count per Department:")
for dept, employees in dept_employees.items():
    print(f"{dept}: {len(employees)}")

# 4. Sort departments by average salary (Bonus)
print("\nDepartments Sorted by Average Salary:")
sorted_depts = sorted(avg_salary.items(), key=lambda x: x[1], reverse=True)
for dept, avg in sorted_depts:
    print(f"{dept}: {avg}")
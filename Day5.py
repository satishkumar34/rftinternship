# ==============================
# STUDENT CSV MANAGER (MINI PROJECT)
# ==============================

def read_csv(filename):
    data_list = []
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            header = lines[0].strip().split(",")

            for line in lines[1:]:
                values = line.strip().split(",")

                record = {
                    "NAME": values[0],
                    "AGE": int(values[1]) if values[1] else None,
                    "MARKS": int(values[2]) if values[2] else None
                }

                data_list.append(record)

    except FileNotFoundError:
        print("❌ File not found!")
    
    return data_list


# ==============================
# DISPLAY DATA
# ==============================
def display_data(data):
    if not data:
        print("No data available.")
        return
    
    print("\n📋 Student Records:")
    for student in data:
        print(student)


# ==============================
# CALCULATE AVERAGE
# ==============================
def calculate_average(data):
    total = 0
    count = 0

    for student in data:
        if student["MARKS"] is not None:
            total += student["MARKS"]
            count += 1

    if count == 0:
        print("No valid marks available.")
    else:
        print(f"📊 Average Marks: {total / count:.2f}")


# ==============================
# SEARCH STUDENT
# ==============================
def search_student(data):
    name = input("Enter student name: ").upper()

    found = False
    for student in data:
        if student["NAME"].upper() == name:
            print("✅ Found:", student)
            found = True

    if not found:
        print("❌ Student not found.")


# ==============================
# MAIN MENU
# ==============================
def main():
    filename = "data.csv"
    data = read_csv(filename)

    while True:
        print("\n===== STUDENT CSV MANAGER =====")
        print("1. Display Data")
        print("2. Calculate Average Marks")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_data(data)

        elif choice == "2":
            calculate_average(data)

        elif choice == "3":
            search_student(data)

        elif choice == "4":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Try again.")


# ==============================
# RUN PROGRAM
# ==============================
if __name__ == "__main__":
    main()
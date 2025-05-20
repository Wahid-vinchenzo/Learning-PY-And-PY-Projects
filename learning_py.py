# =====================================
# ✅ Variables, Condition, Loop, Increment/Decrement
# =====================================

# 🔹 Variables & Condition
score = int(input("Enter your score (0–100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")

# 🔹 Loop Example (for loop)
marks = [30, 40, 50]
total = 0
for i in marks:
    total += i

print(f"Total = {total}")

# 🔹 Increment / Decrement
i = 5
while i >= 0:
    print(f"love you: {i}")
    i -= 1  # Python doesn't support i++ or i--

# =====================================
# ✅ List (Array)
# =====================================
fruits = ["apple", "banana", "mango"]
print("Initial list:", fruits)

fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("banana")
last = fruits.pop()
print("Popped:", last)
print("List now:", fruits)

print("First item:", fruits[0])
print("Last item:", fruits[-1])

print("Looping:")
for fruit in fruits:
    print("-", fruit)

print("Length:", len(fruits))
fruits.sort()
fruits.reverse()
fruits.append("apple")
print("Count of 'apple':", fruits.count("apple"))

# =====================================
# ✅ String
# =====================================
name = "Mamun The Coder"
print("Original:", name)
print("First letter:", name[0])
print("Slice:", name[:5])
print("Reverse:", name[::-1])
print("Length:", len(name))
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Replace:", name.replace("Coder", "Programmer"))

line = "apple,banana,mango"
print("Split:", line.split(","))
print("Join:", " & ".join(["apple", "banana", "mango"]))

for char in name:
    print("-", char)

print("Count 'a':", name.count('a'))
print("Find 'Coder':", name.find("Coder"))

age = 21
print(f"{name} is {age} years old.")

# =====================================
# ✅ Function
# =====================================
def input_marks():
    marks = []
    for subject in ["Math", "English", "Science"]:
        score = int(input(f"Enter marks for {subject}: "))
        marks.append(score)
    return marks

def calculate_total(marks):
    return sum(marks)

def calculate_average(total, count):
    return total / count

def determine_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def pass_or_fail(marks):
    for m in marks:
        if m < 33:
            return "Fail"
    return "Pass"

print("\n📘 Student Result Checker 📘")
marks = input_marks()
total = calculate_total(marks)
avg = calculate_average(total, len(marks))
grade = determine_grade(avg)
status = pass_or_fail(marks)

print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")

# =====================================
# ✅ User Input Example
# =====================================
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

name = input("Enter your name: ")
roll = input("Enter your roll number: ")
marks = list(map(int, input("Enter 5 subject marks: ").split()))

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n--- Student Report ---")
print(f"Name   : {name}")
print(f"Roll   : {roll}")
print(f"Marks  : {marks}")
print(f"Total  : {total}")
print(f"Average: {average}")
print(f"Grade  : {grade}")

# =====================================
# ✅ Dictionary
# =====================================
student = {}
student["name"] = input("Enter name: ")
student["roll"] = int(input("Enter roll: "))
student["section"] = input("Enter section: ")
student["marks"] = list(map(int, input("Enter 3 marks: ").split()))

total = sum(student["marks"])
avg = total / len(student["marks"])

if avg >= 90:
    student["grade"] = "A+"
elif avg >= 80:
    student["grade"] = "A"
elif avg >= 70:
    student["grade"] = "B"
else:
    student["grade"] = "C"

student.pop("section")

print("\n🎓 Student Info:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\n📚 All Students Record:")
students = {
    "Mamun": {"roll": 101, "marks": [90, 85, 95]},
    "Rafi": {"roll": 102, "marks": [70, 75, 80]}
}
for name, info in students.items():
    print(f"\n{name}")
    for key, val in info.items():
        print(f"{key}: {val}")

# =====================================
# ✅ File Handling & Error Handling
# =====================================
import os

def take_student_input():
    try:
        name = input("Enter student name: ")
        roll = int(input("Enter roll number: "))
        grade = input("Enter grade: ")
        return {"name": name, "roll": roll, "grade": grade}
    except ValueError:
        print("❌ Invalid input.")
        return None

def save_to_file(student, filename):
    try:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("📝 Student Records\n===================\n")
        with open(filename, "a") as f:
            for k, v in student.items():
                f.write(f"{k.capitalize()}: {v}\n")
            f.write("-------------------\n")
        print("✅ Data saved.")
    except Exception as e:
        print(f"❌ Error: {e}")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("\n📄 File Content:\n")
            print(f.read())
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

FILENAME = "student_data.txt"
while True:
    print("\n🎓 Student Data Manager")
    print("1. Add Student")
    print("2. View File")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        student = take_student_input()
        if student:
            save_to_file(student, FILENAME)
    elif choice == "2":
        read_file(FILENAME)
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice.")

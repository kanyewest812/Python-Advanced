import json

with open("C:/python/week5/students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    grades = student["grades"]
    student["average"] = round(sum(grades) / len(grades), 2)

with open("students_with_averages.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("Done! The result is in students_with_averages.json")

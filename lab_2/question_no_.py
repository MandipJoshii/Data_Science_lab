print("WELCOME TO STUDENT MARKS MANAGER \n")

students = [
    {"name":"mandip", "marks":[55, 65, 60]},
    {"name":"kritika", "marks":[45, 50, 40]},
    {"name":"dikshit", "marks":[61, 70, 65]},
    {"name":"dristi", "marks":[70, 75, 80]},
    {"name":"megha", "marks":[64, 60, 68]},
    {"name":"rushal", "marks":[89, 85, 92]},
    {"name":"yunay", "marks":[77, 72, 80]},
]

for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    student["average"] = avg
    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"
    student["grade"] = grade


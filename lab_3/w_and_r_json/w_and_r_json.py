 # 4. Writing and Reading JSON Data
# ● Stores student details (ID, name, and marks) in a JSON file
# ● Reads the JSON file and displays the student information
# ● Handles exceptions related to file access and JSON decoding

import json as js
student = [
  { "Roll_no": 101, "Name": "mandip", "Grade": "A" },
  { "Roll_no": 102, "Name": "nikhil", "Grade": "B" },
  { "Roll_no": 103, "Name": "dip", "Grade": "A" },
  { "Roll_no": 105, "Name": "yunay", "Grade": "C" },
  { "Roll_no": 106, "Name": "dikshit", "Grade": "B" },
  { "Roll_no": 107, "Name": "rushal", "Grade": "A" },
  { "Roll_no": 108, "Name": "shailendra", "Grade": "B" },
  { "Roll_no": 109, "Name": "meghana", "Grade": "C" },
  { "Roll_no": 110, "Name": "merina", "Grade": "A" }
]

try:
    with open("student_dataset.json", "w") as f:
        js.dump(student,f,indent=4)
except FileNotFoundError:   
    print("file not found") 


    
try:
    with open("student_dataset.json", "r") as f:
        data = js.load(f)
        # print(data)
        for stud in data:
            print(stud["Roll_no"], stud["Name"], stud["Grade"])
            
except FileNotFoundError:
    print("file doesnt exists")        
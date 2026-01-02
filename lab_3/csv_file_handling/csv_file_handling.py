# 3. CSV File Handling
# ● Read data from a CSV file containing student records (roll number, name, marks)
# ● Display all student records
# ● Handle file-related and data conversion errors using try-except


# with open("student_dataset.csv", "r") as f:
    #testing
    # print(f.read())

csv_content = [
    "Roll_no,Name,Grade",
    "101,mandip,A",
    "102,nikhil,B",
    "103,dip,A"
]


for text in csv_content:
        # clean_column = text.strip()
    try:
        content = text.split(",")
        # print(text)
        student_name = content[0]
        student_age = content[1]
        student_grade = content[2]
        print(f"{student_name:<15}{student_age:<15} {student_grade}") # the :<15 is used to add space :-> formatting start, < means left side dekhi space, 15 means kati white space character add agrne 
    except:
        pass    


                       




      

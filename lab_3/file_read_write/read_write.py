# 1. Basic File Read & Write
# ● Create a text file and write multiple lines into it
# ● Read the contents of the file and display them on the screen
# ● Handle the case where the file does not exist using try-except

try:
    with open("student.txt", "w") as f:
        f.write("STUDENT: MANDIP, AGE: 22, GRADE: B+\n")
        f.write("STUDENT: YUNAY, AGE: 21, GRADE: B-\n")
        f.write("STUDENT: DIP, AGE: 20, GRADE: A\n")

    with open("student.txt", "r") as f:
        print(f.read())  
except FileNotFoundError:
    print("THIS FILE DOESNT EXISTS, PLEASE CHECK YOUR PATH")          

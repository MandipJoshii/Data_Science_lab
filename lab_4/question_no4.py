# 4. Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection.
import random
student_names = ['a','b','c','d','e','f']

ran = random.sample(student_names,3)

print(ran)

"""the random.sample() helps to give a non repeting value like a or b or c ... 
cannot repeat itself more than one inside the []

like it can be in first output [a,b,d] and in second output [a,b,e]

but it doesnt give [a,b,b] or [a,c,a] etc
"""

# 1. Write a Python script that takes a list of student marks and sorts them in descending
# order (highest to lowest) using either the sorted() function or the .sort() method.


"""the key differences in sorted amd sort are:

1. sorted is a build in function where sort is a list method
2. sorted doent updates the original value  but just sort them but the sort chanegs the original value
3. sorted can be stored in a variable and returns a new sorted value but the sort can be stored 
in a new variable but will return none because we need to directly assigned original value with sort method """


marks = [10,20,30,40,50,60,70,80,90,100]

sorted_marks = sorted(marks, reverse=True)

print("sorting using sorted function:",sorted_marks)

marks.sort(reverse=True)

print("sorting using list build in function sort", marks)
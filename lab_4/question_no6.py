# 6. Given a list of student names and a list of their corresponding scores, use the zip()
# function to pair them together and then apply the reduce() function from the
# functools module to calculate the total sum of all scores.

student_name = ['a','b','c','d']
score = [10,20,30,40]

merge = list(zip(student_name,score)) #doing only zip(x,y) -> will return object at its address
#not the actual value in output

print(merge)


"""understand reduce() like this:
reduce can take multiple input and gives single output
its use in to find total of something 
like if there are value 
value = [10,20,30,40]

using zip it would be 10+20+30+40 = 100
hence output is 100 that what zip does
"""
from functools import reduce
def score_sum(result, item):
    return result + item[1]

total = reduce(score_sum,merge,0)

print(total)

"""
we can only use reduce when we call it using the module called functools
this is the syntax to use the reduce:
we need a function which takes two things inside it 
which are:
result(to store), items(to iterated the tuples)
in return we add result + item[1] 
the item one is accessing score because at index[0] there is name 
and in index[1] there is score which we need

then the reduce takes function and iterable and value to starting adding from which we have set 0
that means at first 10 will be added with 0 = 10 then 10 will be added with 20 = 30 than 30 will be 
added with 30 = 60 than 60 will be added with 40 = 100 => total
"""
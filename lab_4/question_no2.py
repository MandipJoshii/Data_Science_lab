# 2. Use a list comprehension to create a new list containing only the even numbers between
# 1 and 20, demonstrating a more concise and readable alternative to traditional loops.

even_only = [x for x in range(1,21) if x % 2 == 0]

print("even numbers only from 1 to 20:", even_only)
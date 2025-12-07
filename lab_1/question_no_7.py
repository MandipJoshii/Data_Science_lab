number = list(map(int,input("ENTER THE NUMBER: ").split()))
largest = number[0]
for num in number:
    if num > largest:
        largest = num

print(largest)    
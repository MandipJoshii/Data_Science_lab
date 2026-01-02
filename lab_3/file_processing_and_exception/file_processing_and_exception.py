# 2. File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers

with open("fruit_and_veggies.txt", "w") as f:
    f.write("1. Fruit: Tomato\n")
    f.write("PRICE = \n")
    f.write("10\n")

    f.write("2. Fruit: Mango\n")
    f.write("PRICE = \n")
    f.write("20\n")

    f.write("3. veggie: Bitter gourd\n")  
    f.write("PRICE = \n")
    f.write("30\n")

    f.write("4. Fruit: Avocado\n")    
    f.write("PRICE = \n")
    f.write("40\n")

    f.write("5. Veggie: Onion\n")
    f.write("PRICE = \n")
    f.write("50\n")


line_count = 0
sum = 0


with open("fruit_and_veggies.txt","r") as f:

    for num in f:
        try:
            n = int(num)
            sum += n
            line_count += 1
        except:
            pass   

print("Number of line in file: ",line_count)   
print("Sum: ", sum) 


average = sum/line_count

if average == 0:
    print("cannot be divisible with zero")
else:
    print("average: ", average)    

 


num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))

gcd = 1
i = 1

while i <= num1 and i <= num2:
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i += 1  

print("THE GCD OF NUM1 AND NUM2 IS:", gcd)

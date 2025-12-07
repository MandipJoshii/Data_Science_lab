num1 = input("ENTER THE FIRST NUMBER: ")
num2 = input("ENTER THE SECOND NUMBER: ")
try:
    if "." not in num1 and "." not in num2:
      var1 = int(num1)
      var2 = int(num2)

    else:
     var1= float(num1)
     var2 = float(num2)

    sum = var1 + var2
    print(f"SUM: {sum}")    
except:
  print("ITS A STRING, INPUT INTEGER OR FLOAT VALUE")    
        


temperature = float(input("ENTER YOUR TEMPERATURE: "))

print("1. FAHRENHEIT")
print("2. KELVIN")

choice = int(input("ENTER CHOICE 1 OR 2: "))

if choice == 1:
       fahrenheit = (temperature * 9/5) + 32
       print("TEMPERATURE OF FAHRENHEIT: ", fahrenheit)

elif choice == 2:
    kelvin = temperature + 273.15
    print("TEMPERATURE OF KELVIV: ", kelvin)
else:
    print("ENTER A VALID CHOICE")
#  Convert temperatures between both units seamlessly.

def cel_to_fah(temp):
    return ((temp*9/5) + 32)

def fah_to_cel(temp):
    return ((temp-32)*5/9)

while True:
    print("Celsius <--------------------------------------------------------> Fahrenheit")
    try: 
        former_unit = input("What temperature unit you want to convert from (C/F) ? : ").upper()
        magnitude = float(input("Enter the magnitude of temperature : "))
        later_unit = input("What temperature unit you want to convert to (C/F) ? : ").upper()
    
    except ValueError:
        print("Temperature must be a number.")
        continue

    if former_unit == 'C':
        if later_unit == 'C':
            converted_temp = magnitude
        elif later_unit == "F":
            converted_temp = cel_to_fah(magnitude)
        print(f"{magnitude} C = {converted_temp} {later_unit}")
    
    elif former_unit == 'F':
        if later_unit == 'F':
            converted_temp = magnitude
        elif later_unit == "C":
            converted_temp = fah_to_cel(magnitude)
        print(f"{magnitude} F = {converted_temp} {later_unit}")
    
    else:
        print("Invalid unit. You can either write C or F")
        continue

    query = input("Do you want to continue? (y/n) ").strip().lower()
    if query == 'n':
        break
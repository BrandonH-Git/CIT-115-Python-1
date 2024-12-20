# Programmer: Brandon Hodgdon
# Code: Temperature Converter
# Class : CIT-115/115L Python
# Date: Oct 14, 2024



#Input:
print("Brandon's Temperature Converter:")
fUserTemp = float(input("Enter a temperature: "))
sFahrenheitCelsius = input("Is the temp F for Fahrenheit or C for Celsius? ")

#Logic/Output:
if sFahrenheitCelsius == "F" or sFahrenheitCelsius == "f":
    if fUserTemp > 212.00:
        print(f"Temp can not be > 212")
    else:
        print(f"The Celsius equivalent is: {(5.0 / 9) * (fUserTemp - 32):.1f}")
elif sFahrenheitCelsius == "C" or sFahrenheitCelsius ==  "c":
    if fUserTemp > 100.00:
        print(f"Temp can not be > 100")
    else:
        print (f"the Fahrenheit equivalent is: {((9.0/5.0)*fUserTemp) + 32:.1f}")
else:
    print("Enter a F or C")
    raise SystemExit


# Welcome message
print("Welcome to Hunter's Temperature Converter!")
# Gets temperature
fTemperature = float(input("Enter a temperature: "))
# Asks user whether temp is F or C
sUnit = input("Is the temp F for Fahrenheit or C for Celsius? ")
# converts temperature between F and C
if sUnit == "F":
 
if fTemperature > 212:
 
print("Temp can not be > 212")
 
else:
 
fCelsius = (5.0 / 9) * (fTemperature - 32)
 
fCelsius = int(fCelsius * 10) / 10
 
print("The Celsius equivalent is: ")
 
print(fCelsius)
elif sUnit == "C":
 
if fTemperature > 100:
 
print("Temp can not be > 100")
 
else:
 
fFahrenheit = ((9.0 / 5.0) * fTemperature) + 32
 
fFahrenheit = int(fFahrenheit * 10) / 10
 
print("The Fahrenheit equivalent is: ")
 
print(fFahrenheit)
else:
 
print("You must enter a F or C")
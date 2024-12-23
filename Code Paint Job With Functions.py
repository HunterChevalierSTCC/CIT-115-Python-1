# Paint Job Estimator
# This program calculates the cost of a paint job including labor and materials
import math

def getFloatInput(strPrompt):
    while True:
        try:
            # Get input from user and convert to float
            strInput = input(strPrompt)
            fValue = float(strInput)
            # Validate that value is greater than zero
            if fValue <= 0:
                print("Error: Value must be greater than zero")
                continue
            return fValue
        except ValueError:
            print("Error: Please enter a valid number")

def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

def getLaborCost(fTotalLaborHours, fLaborChargePerHour):
    return fTotalLaborHours * fLaborChargePerHour

def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

def getSalesTax(strState):
    strState = strState.upper()
    if strState == "CT":
        return 0.06
    elif strState == "MA":
        return 0.0625
    elif strState == "ME":
        return 0.085
    elif strState == "NH":
        return 0.0
    elif strState == "RI":
        return 0.07
    elif strState == "VT":
        return 0.06
    else:
        return 0.0

def showCostEstimate(iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fTaxRate,
                     strCustomerName, strState, fSquareFeet, fPaintPrice, fFeetPerGallon,
                     fLaborHoursPerGallon, fLaborChargePerHour):
    # Calculate totals
    fSubTotal = fPaintCost + fLaborCost
    fSalesTax = round(fSubTotal * fTaxRate, 2)
    fTotalCost = round(fSubTotal + fSalesTax, 2)
   
    # Print to screen
    print("Enter wall space in square feet:", int(fSquareFeet))
    print("Enter paint price per gallon:", fPaintPrice)
    print("Enter feet per gallon:", int(fFeetPerGallon))
    print("How many labor hours per gallon:", int(fLaborHoursPerGallon))
    print("Labor charge per hour:", int(fLaborChargePerHour))
    print("State job is in:", strState)
    print("Customer Last Name:", strCustomerName)
    print("Gallons of paint:", iTotalGallons)
    print("Hours of labor: " + str(round(fLaborHours, 1)))
    print("Paint charges: $" + str(round(fPaintCost, 2)))
    print("Labor charges: $" + str(round(fLaborCost, 2)))
    print("Tax: $" + str(round(fSalesTax, 2)))
    print("Total cost: $" + str(round(fTotalCost, 2)))

def main():
    # Get input values
    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")
   
    # Get state and customer name
    strState = input("State job is in: ")
    strCustomerName = input("Customer Last Name: ")
   
    # Calculate values
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fTaxRate = getSalesTax(strState)
   
    # Show estimate
    showCostEstimate(iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fTaxRate,
                     strCustomerName, strState, fSquareFeet, fPaintPrice, fFeetPerGallon,
                     fLaborHoursPerGallon, fLaborChargePerHour)

# Start the program
main()
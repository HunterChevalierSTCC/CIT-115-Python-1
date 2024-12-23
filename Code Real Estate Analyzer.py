def getFloatInput(prompt):
    # Prompt the user for a float input and validate it
    while True:
        try:
            fValue = float(input(prompt))
            if fValue <= 0:
                print("Error: Value must be a positive number.")
                continue
            return fValue
        except ValueError:
            print("Error: Invalid numeric input.")

def getMedian(lstValues):
    # Calculate and return the median of a list of values
    lstValues.sort()
    iLength = len(lstValues)
    if iLength % 2 == 0:
        iMiddle = iLength // 2
        fMedian = (lstValues[iMiddle-1] + lstValues[iMiddle]) / 2
    else:
        iMiddle = iLength // 2
        fMedian = lstValues[iMiddle]
    return fMedian

def main():
    # Main function to collect sales data and display analytics
    lstSales = []
    
    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        lstSales.append(fSalesPrice)
        
        while True:
            sResponse = input("Enter another value Y or N: ").lower()
            if sResponse in ['y', 'n']:
                break
            print("Invalid input. Please enter Y or N.")
        
        if sResponse == 'n':
            break
    
    lstSales.sort()
    
    # Output each property with its corresponding price
    print("\nProperty List:")
    for i, fSale in enumerate(lstSales, 1):
        print(f"Property {i}: ${fSale:.2f}")
    
    # Calculate analytics
    fMinimum = min(lstSales)
    fMaximum = max(lstSales)
    fTotal = sum(lstSales)
    fAverage = fTotal / len(lstSales)
    fMedian = getMedian(lstSales)
    fCommission = fTotal * 0.03
    
    # Output formatted results
    print(f"\nMinimum: ${fMinimum:.2f}")
    print(f"Maximum: ${fMaximum:.2f}")
    print(f"Total: ${fTotal:.2f}")
    print(f"Average: ${fAverage:.2f}")
    print(f"Median: ${fMedian:.2f}")
    print(f"Commission: ${fCommission:.2f}")

# Run the main function
main()
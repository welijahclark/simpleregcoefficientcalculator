#Declared mathematics variables for calculator

def Summation(array):
    sum = 0
    for x in array:
        sum = sum + x
    return sum


def ProductSummation(barray, carray):
    sum = 0
    bArrayIndex = 0
    for y in carray:
        sum = sum + (y * barray[bArrayIndex])
        bArrayIndex += 1
    return sum


def SquareSummation(darray):
    sum = 0
    for z in darray:
        sum = sum + (z * z)
    return sum


def SummationSquare(array):
    sum = 0
    for y in array:
        sum = sum + y
    return sum * sum

#Input functions for alpha and beta regression coefficients

array_x_input = input('What are your x values? (Enter your x values, and separate them by commas.)')
array_x_input = array_x_input.split(",")
array_x = [float(entry.strip()) for entry in array_x_input]

array_y_input = input('What are your y values? (Enter your y values, and separate them by commas.)')
array_y_input = array_y_input.split(",")
array_y = [float(entry.strip()) for entry in array_y_input]

n_input = len(array_x)

#Beta and Alpha Coefficients formulas

betaco = (n_input * ProductSummation(array_x, array_y) - Summation(array_x) * Summation(array_y)) / (
            n_input * SquareSummation(array_x) - SummationSquare(array_x))
alphaco = (Summation(array_y) - betaco * (Summation(array_x))) / (n_input)

#Print the output for the variables

print('Your beta coefficient is')
print(betaco)
print('Your alpha coefficient is')
print(alphaco)

# double check arithmetic on this to see what formula this actually is...
print('Your SSE is')
print(n_input * ProductSummation(array_x, array_y) - Summation(array_x) * Summation(array_y)) / (
            n_input * SquareSummation(array_x) - SummationSquare(array_x))

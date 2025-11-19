# Problem 1

# Create lists for sales and days
Sale_list = [50, 75, 150, 125, 100]
Week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Find the maximum sale value
maxSales = max(Sale_list)

# Find the index (position) of that maximum sale
max_index = Sale_list.index(maxSales)

# Use that index to find the matching day
maxSalesDay = Week_list[max_index]

# Display results using f-strings
print(f"The Max sales is $ {maxSales}")
print(f"The Max sales day is {maxSalesDay}")

# Problem 2: Number Range

# Initialize
numbers = []

# Ask the user for the first number
value = float(input("Enter value (or 0 to end): "))

# Keep asking until the user enters 0
while value != 0:
    numbers.append(value)  # add the number to the list
    value = float(input("Enter value (or 0 to end): "))  # ask again

# Display
print(numbers)

# Initialize
max_value = numbers[0]
min_value = numbers[0]

# find max and min
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# Calculate the range
range_value = max_value - min_value

# Display the range
print(f"Range= {range_value}")

def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # This will print 0 which is expected

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}") # This will print 3.0 which is also expected

my_list = [1, 2, 'a', 4, 5] # adding a string to the list to cause error
result = calculate_average(my_list)
print(f"Average: {result}") # This will cause TypeError: unsupported operand type(s) for +: 'int' and 'str'
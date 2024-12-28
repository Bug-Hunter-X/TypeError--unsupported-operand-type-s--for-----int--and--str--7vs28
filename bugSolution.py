def calculate_average(numbers):
    if not numbers:
        return 0
    if all(isinstance(num, (int, float)) for num in numbers):
        return sum(numbers) / len(numbers)
    else:
        return "Error: List contains non-numeric values"

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 0

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 3.0

my_list = [1, 2, 'a', 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Error: List contains non-numeric values
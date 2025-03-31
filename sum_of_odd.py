def sum_of_odd_numbers(n):
    odd_sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if the number is odd
            odd_sum += i
    return odd_sum

n = int(input("Enter a number: "))  # Convert input to integer
result = sum_of_odd_numbers(n)
print(f"The sum of odd numbers from 1 to {n} is: {result}")  # Use f-string for cleaner formatting
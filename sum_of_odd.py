def sum_of_odd_numbers(n):
    sum_odd = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if the number is odd
            print(i)
            sum_odd = sum_odd + i

    return sum_odd

n = int(input("Enter a number: "))
result = sum_of_odd_numbers(n)
print(f"The sum of odd numbers from 1 to {n} is {result}")
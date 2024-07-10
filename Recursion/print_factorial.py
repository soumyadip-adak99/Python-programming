# Print factorial number using recursion


def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1

    fact_number = calculate_factorial(n - 1)
    result = n * fact_number
    return result


n = 5
result = calculate_factorial(n)
print(n, "factorial is:", result)

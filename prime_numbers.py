import time

n_of_p_numbers = int(input("Please type the number of prime numbers you want to find: "))

start_time = time.time()

number = 3 # 3 is the first number to be tested
n_of_found_p_numbers = 0
found_p_numbers = []
n_of_loops = 0

# appends the first two prime numbers to found_p_numbers
if n_of_p_numbers == 1:
    found_p_numbers.append(1)
    n_of_found_p_numbers = 1
else:
    found_p_numbers.append(1)
    found_p_numbers.append(2)
    n_of_found_p_numbers = 2

print("Loading...")

while n_of_found_p_numbers < n_of_p_numbers:

    # skips even numbers
    if number % 2 == 0:
        number += 1
        continue

    divisor = 2 # 2 is the first divisor to be tested
    number_of_divisors = 2 # all numbers have 2 divisors from the start
    number_divided_by_two = number / 2 # all numbers have no divisors greater than half of them

    while divisor < number_divided_by_two:

        n_of_loops += 1

        if number % divisor == 0:
            number_of_divisors += 1

        divisor += 1

        # breaks the loop if the number being tested has already more than two divisors
        if number_of_divisors > 2:
            number += 1
            break

    if number_of_divisors == 2:
        found_p_numbers.append(number)
        n_of_found_p_numbers += 1

    number += 1
    number_divided_by_two += 1

print(found_p_numbers)
print(str(round((time.time() - start_time), 2)) + " seconds.")
# print("Number of executed loops: " + str(n_of_loops))
# Name: Byron Ramil B. Pedrialva
# School: FEU-TECH

numbers = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39,
           71, 55, 41, 95, 70, 48, 42, 32, 13, 35]


print("List of Numbers:")
print(numbers)


average = sum(numbers) / len(numbers)
print("\nAverage:", average)


largest = max(numbers)
smallest = min(numbers)

print("\nLargest Number:", largest)
print("Smallest Number:", smallest)


sorted_numbers = sorted(numbers)

second_smallest = sorted_numbers[1]
second_largest = sorted_numbers[-2]

print("\nSecond Smallest Number:", second_smallest)
print("Second Largest Number:", second_largest)


even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print("\nNumber of Even Numbers:", even_count)


odd_count = 0

for num in numbers:
    if num % 2 != 0:
        odd_count += 1

print("Number of Odd Numbers:", odd_count)

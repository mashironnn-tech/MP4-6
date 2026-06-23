#Name: Marcus Agapay
#School: FEU-TECH
#Machine Problem - 3

numbers = [
    30, 7, 30, 2, 88, 44, 60, 40, 1, 53, 100, 72, 86,
    64, 40, 85, 3, 19, 63, 84, 17, 31, 95, 84, 99, 60,
    85, 74, 65, 38, 43, 80, 39, 70, 8, 21, 32, 68, 64,
    55, 88, 84, 49, 68, 70, 98, 21, 51, 3, 97
]

equal_values = 0
not_equal_values = 0

for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = 666
        equal_values += 1
    else:
        not_equal_values += 1

print("Name: YOURNAME")
print("School: FEU TECH")
print("Machine Problem - 3")
print(f"OUTPUT is {numbers}")
print(f"Total equal values {equal_values}")
print(f"Total not equal values {not_equal_values}")
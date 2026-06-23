#Name: YOURNAME
#School: FEU-TECH
#Machine Problem - 5.2

numbers = [18, 19, 20]

print("Name: YOURNAME")
print("School: FEU TECH")
print("Machine Problem - 2")
print(f"Original list {numbers}")

numbers[1] = 17
print(f"a {numbers}")

numbers.extend([4, 5, 6])
print(f"b {numbers}")

numbers.pop(0)
print(f"c {numbers}")

numbers.sort()
print(f"d {numbers}")

numbers = numbers * 2
print(f"e {numbers}")

numbers[3] = 25
print(f"f {numbers}")
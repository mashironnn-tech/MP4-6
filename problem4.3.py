#Name: Marcus Agapay
#School: FEU-TECH
#Machine Problem number - 3

class RomanConverter:
    def __init__(self):
        self.numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        self.mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_roman(self, num):
        if num <= 0 or num > 5000:
            return "MAX VALUE IS 5000, should only accept whole number value."
        result = ""
        for i in range(len(self.numbers)):
            while num >= self.numbers[i]:
                result += self.symbols[i]
                num -= self.numbers[i]
        return result

    def to_integer(self, s):
        s = s.upper()
        total = 0
        i = 0
        try:
            while i < len(s):
                v1 = self.mapping[s[i]]
                if i + 1 < len(s):
                    v2 = self.mapping[s[i+1]]
                    if v1 >= v2:
                        total += v1
                        i += 1
                    else:
                        total += (v2 - v1)
                        i += 2
                else:
                    total += v1
                    i += 1
            return total
        except KeyError:
            return "Invalid Roman Numeral"

def main():
    converter = RomanConverter()
    while True:
        print("\nMENU")
        print("1. convert an integer to a roman numeral")
        print("2. convert a roman numeral to an integer")
        print("3. exit")
        
        choice = input("Enter your choice:")
        
        if choice == '1':
            user_input = input("Enter Integer - ")
            if "." in user_input:
                print("MAX VALUE IS 5000, should only accept whole number value.")
                continue
            try:
                val = int(user_input)
                res = converter.to_roman(val)
                if "MAX VALUE" in str(res):
                    print(res)
                else:
                    print(f"Output in Roman numerals is: {res}")
            except ValueError:
                print("MAX VALUE IS 5000, should only accept whole number value.")
        
        elif choice == '2':
            roman_input = input("Enter roman numeral - ")
            result = converter.to_integer(roman_input)
            print(f"Output in Integer is - {result}")
            
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
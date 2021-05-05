def decimaltoBinary():
    while True:
        try:
            print("Decimal to Binary Converter")
            num = input("Enter a number: ")
            if type(num) == float:
                FloattoBinary()
            bit_num = bin(int(num)).replace("0b", "")
            print(bit_num)
            ask = input("Would you like to convert a binary number to decimal? (y/n): ")
            if ask == "y":
                BinarytoDecimal()
            elif ask == "n":
                continue
        except ValueError:
            print("Invalid Literal for Base 2 Conversion")

def BinarytoDecimal():
    print("Binary to Decimal converter")
    binary_numbers = input("Enter a binary number: ")
    decimal_number = [int(binary_number, 2) for binary_number in binary_numbers.split()]
    print(*decimal_number)

def FloattoBinary():
        num = 11203.102
    b = 2
    exp = 0
    base_b_eq = pow(b, exp)
    num_list = [f for f in str(num)]
    point = False
    int_list = []
    frac_list = []

# Eliminate the integral part
def inte_el(num_list):
    global point
    while point is not True:
        for number in num_list:
            if number != '.':
                int_list.append(int(number))
                num_list.remove(number)
            elif number == '.':
                num_list.remove('.')
                point = True
                return int_list
                break

def frac_el(num_list):
    while num_list:
        for frac in num_list:
            frac_list.append(frac)
        return frac_list
    

int_list = inte_el(num_list)
print(int_list)

frac_list = frac_el(num_list)
print(frac_list)

    

decimaltoBinary()

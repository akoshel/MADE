# input_list = ['loui IX', 'adme X', 'zili II', 'loui X']

def roman_encoder(rom_num):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4,
             'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(rom_num):
        if i + 1 < len(rom_num) and rom_num[i:i + 2] in roman:
            num += roman[rom_num[i:i + 2]]
            i += 2
        else:
            num += roman[rom_num[i]]
            i += 1
    return num


def roman_decoder(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rom_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            rom_num += syb[i]
            num -= val[i]
        i += 1
    return rom_num


input_list = []
for i in range(int(input())):
    input_list.append(input())

temp_list = []
for king in input_list:
    king_splitted = king.split(' ')
    temp_list.append([king_splitted[0], roman_encoder(king_splitted[1])])

for king in sorted(temp_list):
    print(f'{king[0]} {roman_decoder(king[1])}')

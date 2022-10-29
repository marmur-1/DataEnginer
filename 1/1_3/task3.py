# Дано целое положительное число X, необходимо вывести вариант этого числа в римской системе счисления в формате строки.

# Римские числа записываются от наибольшего числа к наименьшему слева направо.
# Однако число 4 не является “IIII”. Вместо этого число 4 записывается, как “IV”. Т.к. 1 стоит перед 5, мы вычитаем 1, делая 4. Тот же принцип применим к числу 9, которое записывается как “IX”.
# Случаи, когда используется вычитание:
# I может быть помещен перед V и X, чтобы сделать 4 и 9.
# X может быть помещен перед L и C, чтобы составить 40 и 90.
# C может быть помещен перед D и M, чтобы составить 400 и 900.

# Пример 1:
# Ввод: x = 3
# Вывод: “III”

# Пример 2:
# Ввод: x = 9
# Вывод: “IX”

# Пример 3:
# Ввод: x = 1945
# Вывод: “MCMXLV”

# Гарантируется, что введенное число X будет находиться в диапазоне от 1 до 2000




# x = 3
# x = 9
# x = 24
# x = 569
x = 1945
# x = 5945


def rm(num,one,half,full):
    sretstr = ""
    if num != 0:
        if num == 4:
            sretstr = one+half+sretstr
        elif num == 9:
            sretstr = one+full+sretstr
        elif num < 4:
            for b in range(0, num):
                sretstr = one+sretstr
        else:
            for b in range(0, num-5):
                sretstr = one+sretstr
            sretstr = half+sretstr
    return sretstr

num_str = str(x)
num_str = num_str[::-1]
num_rom_str = ""
for idi, i in enumerate(num_str):
    i = int(i)
    match idi:
        case 0:
            num_rom_str = rm(i,"I","V","X")+num_rom_str
        case 1:
            num_rom_str = rm(i,"X","L","C")+num_rom_str
        case 2:
            num_rom_str = rm(i,"C","D","M")+num_rom_str
        case 3:
            for b in range(0, i):
                num_rom_str = "M"+num_rom_str
        case _:
            print("Code not found")
num_rom_str = num_rom_str
print(num_rom_str)

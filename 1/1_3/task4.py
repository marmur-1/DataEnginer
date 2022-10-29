# Дана строка X, состоящая только из символов “{“, “}”, “[“, “]”, “(“, “)”. Программа должна вывести True, в том случае если все открытые скобки закрыты. 
# Например: “[()]{}”, все открытые скобки закрыты закрывающимися скобками, потому вывод будет True. 
# В случае же, если строка будет похожа на: “{{{}”, то вывод будет False, т.к. не все открытые скобки закрыты.

# Пример 1:
# Ввод: x = “[{}({})]”
# Вывод: True

# Пример 2:
# Ввод: x = “{]”
# Вывод: False

# Пример 3:
# Ввод: x = “{“
# Вывод: False

# Гарантируется, что введенная строка X будет содержать только скобки и не будет пустой.

x = "[{}({})]"
# x = "[{}(}{)]"
# x = "{]"
# x = "{"

def checkStaples(string):
    ch = {
        '{':'}',
        '[':']',
        '(':')'
    }
    def recurs_seach(s,index_start):
        char = s[index_start]
        length = len(s)
        if char == "{" or char == "[" or char == "(":
            for b in range(index_start+1, length):
                char_s = s[b]
                if ch[char] == char_s:
                    return b
                elif char_s == "{" or char_s == "[" or char_s == "(":
                    c = recurs_seach(s,b)
                    if c !=False:
                        b = c
                    else:
                        return False
            return False
        else:
            return False
    g = recurs_seach(string,0)
    if g !=False:
        return True
    else:
        return False

print(x)
print(checkStaples(x))

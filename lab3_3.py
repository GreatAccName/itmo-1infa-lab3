import re

def main():
    line = input()
    pattern = r'[0-9]+'
    arr = re.findall(pattern, line)

    res_line = ""
    i = 0
    while i < len(line):
        if line[i] >= "0" and line[i] <= "9":
            j = i + 1
            while j < len(line) and line[j] >= "0" and line[j] <= "9":
                j+= 1
            x = int(line[i:j])
            x = 3 * x * x + 5
            res_line += str(x)
            i = j
            continue
        else:
            res_line += line[i]
        i += 1
    print(res_line)

if __name__ == "__main__":
    main()

# Тест#1
# 21 + 22 = 42
# 1328 + 1457 = 5297
# Тест#2
# 123 4567
# 45392 62572472
# Тест#3
# 2 + 2 = 5
# 17 + 17 = 80
# Тест#4
# 2.3 + 8.7 = 0.0
# 17.32 + 197.152 = 5.5
# Тест#5
# Yes or no? True(1) or False(0)? Hmm...
# Yes or no? True(8) or False(5)? Hmm...

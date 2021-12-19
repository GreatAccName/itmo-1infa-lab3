import re

my_isu = 283566
eyes = [":", ";", "X", "8", "="]
noses = ["-", "<", "-{", "<{"];
mouths = ["(", ")", "O", "|", "\\", "/", "P"]

eye_dv = 5      # eye division remainder
nose_dv = 4     # nose division remainder
mouth_dv = 7    # mouth division remainder

def make_smile(isu_num):
    s = ""
    s += eyes[isu_num % eye_dv]
    s += noses[isu_num % nose_dv]
    s += mouths[isu_num % mouth_dv]
    return s

tests = [
":<{| ;<{\\ :-{P :<{\\",# 4
";-{P ;-{P =<( ;-{P",   # 2
"=-{| 8-( 8--{| 8-{|",  # 3
":<) :<) :<) :<)",      # 1
"\_(o_O)_/ 8o"          # 0
]

def solve():
    my_re = r'[:;X8=]{1}[-<]{1}{{0,1}[()O|\\/P]{1}'
    for i in range(len(tests)):
        print(f"Test#{i + 1}:\t" + tests[i])
        d = {}
        for j in re.findall(my_re, tests[i]):
            if (j in d):
                d[j] += 1
            else:
                d[j] = 1
        print(f"N = {len(d)}:\t", end="")
        for j in d:
            print(j, end=" ")
        print()

def main():
    print("Smile of my ISU number:")
    print(make_smile(my_isu))

    solve()

if __name__ == "__main__":
    main()

# def test():
#     # i dabble
#     my_re = r'[:;X8=]{1}[-<]{1}{{0,1}[()O|\\/P]{1}'
#     for i in range(len(tests)):
#         print(f"Test#{i + 1}:\t" + tests[i])
#         d = {}
#         for j in re.findall(my_re, tests[i]):
#             if (j in d):
#                 d[j] += 1
#             else:
#                 d[j] = 1
#         print("dict:\t", end="")
#         for j in d:
#             print(j, end=" ")
#         print()
#
#         print(len(re.findall(my_re, tests[i])), end=":\t")
#         for j in re.findall(my_re, tests[i]):
#             print(j, end=" ")
#         print()
#
#     for j in range(5):
#         for i in range(4):
#             isu_num = int(random() * 1000000)
#             print("", make_smile(isu_num), end="")
#             # s = "{0:0>6}:".format(isu_num)
#             # print(s, make_smile(isu_num))
#         print()

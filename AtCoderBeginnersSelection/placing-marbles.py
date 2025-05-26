s = input()
d = [int(d) for d in str(s)]
c = 0
for dc in d:
    if dc == 1:
        c += 1


print(c)


# ベストな方法 (ChatGPT先生)
# s = input()
# print(s.count("1"))

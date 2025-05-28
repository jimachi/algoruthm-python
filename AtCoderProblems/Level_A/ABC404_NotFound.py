s = str(input())

for i in range(ord("a"), ord("z") + 1):
    if chr(i) in s:
        continue
    else:
        print(chr(i))
        break

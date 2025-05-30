import re

s = int(input())

print(re.sub(r"[^2]", "", str(s)))

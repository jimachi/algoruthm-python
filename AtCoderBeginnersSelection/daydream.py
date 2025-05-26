s = input()

while s != "":
    if s.endswith("dreamer"):
        s = s[: -len("dreamer")]
    elif s.endswith("dream"):
        s = s[: -len("dream")]
    elif s.endswith("eraser"):
        s = s[: -len("eraser")]
    elif s.endswith("erase"):
        s = s[: -len("erase")]
    elif s != "":
        print("NO")
        exit()

print("YES")
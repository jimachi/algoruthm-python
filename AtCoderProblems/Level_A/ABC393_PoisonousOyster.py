x, y = map(str, input().split())

if x == "sick" and y == "sick":
    print(1)
elif x == "sick" and y == "fine":
    print(2)
elif x == "fine" and y == "sick":
    print(3)
else:
    print(4)

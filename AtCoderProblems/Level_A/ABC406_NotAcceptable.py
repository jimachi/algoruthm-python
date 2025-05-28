h_1, m_1, h_2, m_2 = map(int, input().split())

time_1 = h_1 * 60 + m_1
time_2 = h_2 * 60 + m_2

if time_1 >= time_2:
    print("Yes")
else:
    print("No")

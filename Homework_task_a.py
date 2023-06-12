x = [1, 3, 7, 1, 8, -4, 10, 15, -45, 9, -6]
mx = x[0]
mn = x[0]
v = []
for y in x:
    if y > mx:
        mx = y
    if y < mn:
        mn = y
    if y % 3 == 0 and y % 5 != 0:
        v.append(y)

print(mx)
print(mn)
print(v)


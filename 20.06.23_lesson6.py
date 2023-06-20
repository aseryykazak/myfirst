
# def tem(x, y, gr):
#     if gr == "F":
#         return x * 1.8 + 32
#     elif gr == "C":
#         return (y - 32)/1.8
# print(tem(5, 10, "C"))

def number(x):
    if x % 4 ==0 and x % 100!=0 or x % 400==0 or x % 400==0:
        return "YES"
    else:
        return "NO"
print(number(2023))






def tem(x, y, gr):
    if gr == "F":
        return x * 1.8 + 32
    elif gr == "C":
        return (y - 32)/1.8
print(tem(5, 10, "F"))


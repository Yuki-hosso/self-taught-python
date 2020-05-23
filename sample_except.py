def str2float(str):
    try:
        return float(str)
    except ValueError:
        print("input number")
        exit()

s = input("input string:")
print(str2float(s))

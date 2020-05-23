import random

num_list = [random.randint(0,100) for i in range(10)]
print(num_list)


while True:
    s = input("input number(0-100) or q:")
    if s == "q":
        break
    try:
        num = int(s)
        if num in num_list:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        print("数字を入力するか，qで終了します．")

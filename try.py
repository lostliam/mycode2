import os

while True:
    try:
        os.system("python3 main.py")
        break # 如果没有报错，跳出循环
    except Exception as e:
        print(e) # 如果有报错，打印错误信息，并继续循环
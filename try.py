import os

while True:
    try:
        os.system("python3 main.py")
        break # 如果没有报错，跳出循环
    except Exception as e:
        continue

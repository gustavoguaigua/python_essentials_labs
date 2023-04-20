"""
num=0
while num<=20:
    print("antes de continue")
    print(num)
    num+=2
    continue
"""

num=0
while num<=20:
    if num==10:
        num+=2
        print("llegó a 10")
        continue
    elif num==16:
        num+=2
        continue
    print(num)
    num+=2

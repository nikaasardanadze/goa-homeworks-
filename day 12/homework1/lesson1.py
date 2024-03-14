print("if you tyoe 0 you will get out of program")

while True:
    num = int(input("type a number: "))
    if num >= 1 :
        print("the number is positive")
        num = int(input("type a number: "))
    if num <= -1 :
        print("the number is negative")
        num= int(input("type a nuumber:"))
    if num == 0:
        print("the number stoles zero")
        break
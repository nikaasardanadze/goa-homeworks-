num = int(input("type a number: "))

while num % 3 == 0:
    print(num, "number is odd,  try again: ")
    num = int(input("type a number: "))
    if num % 2 == 0:
        print(num, "number is, even u got it right")
        num = int(input("type a number: "))
        break

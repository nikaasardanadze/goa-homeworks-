num = int(input("type a number thought 1 to 10 :"))

sum = ("you guessed the number right")

while num >= 0:
    print(num)
    num = int(input("type a number thought 1 to 10 :"))
    if num == 5:
        print(sum)
        break
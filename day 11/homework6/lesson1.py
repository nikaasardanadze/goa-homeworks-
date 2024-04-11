num = int(input("tell us tempeture in Celsius: "))

while num == 30:
    print("the tempeture is hot")
    num = int(input("tell us tempeture in Celsius: "))
if num <= 30:
    print("the tempeture is warm")
    num = int(input("tell us tempeture in Celsius: "))
elif num <=20:
    print("the tempeture is cold")
    num = int(input("tell us tempeture in Celsius: "))
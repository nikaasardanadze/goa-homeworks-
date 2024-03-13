num = int(input("type a number: "))

while num % 2 == 0:
    print(num, "it divides on two: ")
    num = int(input("type a number: "))

if num % 3  == 0:
    print(num, "it divides on three")
    num = int(input("type a number: "))

elif num % 2 == 0 and num % 3 == 0:
    print("it divides on two and three")
    num = int(input("type a number: "))
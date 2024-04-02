#შექმენით ლისტი სადაც ჩამოწერილიქნება თამაშის სახელები და შემდგომ თამაშებს ვანაცვლებთ სოლოლერნით , w3 , codewars - ებით და ასეშემდეგ.

list = ["fortnite", "roblox", "call of duty"]
list[0] = ("sololearn")
list[1] = ("w3")
list[2] = ("codewars")
print(list)

#შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, შემდეგ გამოიტანეთ ამ სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))
num4 = float(input("enter fourth number: "))
num5 = float(input("enter fifth number: "))
numbers = [num1, num2, num3, num4, num5]
for num in numbers:
    if num % 2 == 0:
        print(num)

#შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება). მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operation = input("Choose operation (+, -, *, /): ")


if operation in ['+', '-', '*', '/']:
    result = eval(f"{num1} {operation} {num2}")
    if operation == '/' and num2 == 0:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print("Result:", result)






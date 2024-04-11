#დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)

age = int(input("enter your age: "))
if age < 18:
    print("you are a minor")
elif age >= 18:
    print("you are an adult")
elif age <= 65:
    print("you are an adult")
else: 
    print("you are a senior citizen")
#დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის ინდექსს (BMI), მომხმარებლისგან მიღებული წონის (კილოგრამებში) და სიმაღლის (მეტრებში) გათვალისწინებით.

weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = weight_kg / (height_m ** 2)

print("Your Body Mass Index (BMI) is:", bmi)
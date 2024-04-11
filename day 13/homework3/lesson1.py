#დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)

grade = input("please enter your grade : ")

if grade == "A":
    print("Excellent")
elif grade == "B":
    print("good job") 
elif grade == "C":
    print("you passed")
elif grade == "D":
    print("you can do better")
elif grade == "F":
   print("you failed") 
else:
    print("try again")

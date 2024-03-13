score = int(input("enter your score: "))


while score >= 90 or score >= 100 :
    print(" you got an A")
    score = int(input("enter your score: "))

if score >= 80 or score >= 89:
    print(" you got a B")
    score = int(input("enter your score: "))
elif score >= 70 or score >= 79:
    print(" you got a D")
    score = int(input("enter your score: "))
else:
    print(f"{60 <=60} you got an F")
    score = int(input("enter your score: "))

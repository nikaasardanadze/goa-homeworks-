#შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს

num = int(input("choose a number between 1 and 10:"))

while num >= 0:
    print(num)
    if num == 3:
        print("the number you chose was correct")
    else:
        print("the number you chose was incorrect")
    break

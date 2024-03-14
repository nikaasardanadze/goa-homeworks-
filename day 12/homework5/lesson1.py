#მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში.

num = int(input("please enter a number from 1 to 9: "))

if num <1 or num > 9 :
    print("please enter a number from 1 to 9: ")
else:
    for i in range(1, 51):
        if i % num == 1:
            print(i)
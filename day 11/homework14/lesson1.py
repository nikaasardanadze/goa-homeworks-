name = "nika"
name1 = input("Enter Name: ")
while name1 != name:
    print("Error")
    name1=input("Enter Name: ")
    if name1 == name:
        print("You are right")

    break
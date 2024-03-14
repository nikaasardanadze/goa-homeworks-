#მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის, ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი).

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
start, end = min(num1 , num2) , max(num1,num2)
for i in range (start, end + 1 ) :
    print("the cube of", i, "is: ", i ** 3 )
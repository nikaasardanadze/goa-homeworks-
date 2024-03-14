#მომხმარებელს შეეკითხეთ სამი რიცხვი და შეამოწმეთ არიან თუ არა პითაგორას რიცხვები.

a, b, c = map(float, input("Enter three numbers separated by spaces: ").split())

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The numbers form a Pythagorean triplet.")
else:
    print("The numbers do not form a Pythagorean triplet.")

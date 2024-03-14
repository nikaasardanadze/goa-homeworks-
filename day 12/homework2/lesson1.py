#დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision".

print("1.kilometers to miles ")
print("2. miles to kilometers ")
choice = input("enter your choice(1 or 2): ")

if choice == "1" :
    km = float(input("enter kilometers:"))
    miles = km * 0.621317
    print(str(km) + "kilometers is equal to " + str(miles) + "miles")
elif choice == "2" :
    miles = float(input("enter miles: "))
    km = miles * 1.60934
    print(str(miles) + " miles is equal to " + str(km) + "kilometers")
else:
    print("wrong decision")



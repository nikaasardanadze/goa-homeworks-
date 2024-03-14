#მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა.

user_year = int(input("Enter a year: "))


if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print("Leap year!")
else:
    print("Not a leap year.")
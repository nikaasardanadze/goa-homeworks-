#დაწერეთ პროგრამა, რომელიც იღებს სთრინგს, შემდეგ მომხმარებელს ეკითხება თუ რამდენჯერ განმეორდეს და for ციკლის გამოყენებით დაბეჭდეთ ის.

input_string = input("Enter a string: ")

repeat_count = int(input("how many times do you want to repeat the string? "))
for i in range(repeat_count) :
    print(input_string)
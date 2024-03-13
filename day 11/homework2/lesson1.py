number = int(input("enter number"))
i = number
sum = 0


while i >= 0:
    print(sum)
    i = i - 1
    sum = sum + 1


for num in range(0 , number+1):
    sum = sum + num

print(sum)
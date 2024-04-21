#შექმენით ფუნქცია სახელად numbers_product. ფუნქციას გადაეცით სამი არგუმენტი - start, end, step. შემდეგ გამოიყენეთ while ციკლი (for ციკლი არ შეიძლება) და სიაში დაამატეთ რიცხვები - დაიწყეთ start-იდან, იტერაცია მოახდინეთ step-ით და ციკლი ამუშავეთ end-ამდე. განიხილეთ ეს სია და მოახდინეთ მასზე ფილტრაცია, კიდევ ახალ სიაში დაამატეთ მარტო 3-ის ჯერადი რიცხვები. საბოლოოდ დააბრუნეთ 3-ის ჯერადების სიის ყველა რიცხვის ნამრავლი - product.

def numbers_product(start, end, step):
    numbers = []
    current = start

    while current <= end:
        numbers.append(current)
        current += step
         
    multiples_of_3 = [num for num in numbers if num % 3 == 0]

    product = 1
    for num in multiples_of_3:
        product *= num
    
    print(product)
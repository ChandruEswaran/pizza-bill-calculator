def calculate_pizza_bill(size, add_pepper, extra_cheese):
    base_prices = {'s': 15, 'm': 20, 'l': 25}
    pepper_prices = {'s': 2, 'm': 3, 'l': 3}
    extra_cheese_price = 1

    bill = base_prices[size]

    if add_pepper == 'y':
        bill += pepper_prices[size]

    if extra_cheese == 'y':
        bill += extra_cheese_price

    return bill


size = input("Enter the size of the pizza (s, m, l): ").lower()
add_pepper = input("Do you want to add pepper (y/n)? ").lower()
extra_cheese = input("Do you want to add extra cheese (y/n)? ").lower()

bill = calculate_pizza_bill(size, add_pepper, extra_cheese)
print(f"The total bill is: ${bill}")
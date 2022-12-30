def find_discount(price, discount_amount):
    discount = price * (discount_amount / 100)
    return price - discount
print(find_discount(100, 20))
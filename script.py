cart_prices = [100,250,50,500,120]
total_cost = 0

for price in cart_prices:

    if price > 200:
        discounted_price = price * 0.90
        total_cost = total_cost + discounted_price
    else:
        total_cost = total_cost + price

print("The final smart cart total is: INR " + str(total_cost))


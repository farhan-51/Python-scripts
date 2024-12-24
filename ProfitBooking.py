curr_price = float(input("Enter current price of share: "))
curr_shares_count = int(input("Enter no of shares you are going to purchase: "))
target_price = float(input("Enter target price of share: "))

planned_capital = curr_price * curr_shares_count
target_capital = target_price * curr_shares_count

profit_per_share = target_price - curr_price
total_profit = profit_per_share * curr_shares_count

print('=================================================')
print(f"You are going to invest this much INR: {planned_capital}")
print(f"Profit on each share: {profit_per_share}")
print(f"Total profit: {total_profit:.2f}")
print(f"Your total capital will be: {target_capital}")

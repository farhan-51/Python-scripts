base_price = float(input("Enter base price of share: "))
initial_shares_count = int(input("Enter no of shares purchased: "))
curr_price = float(input("Enter current price of share: "))
target_shares_count = int(input("Enter no of shares you are going to purchase: "))

invested_capital = base_price * initial_shares_count

planned_capital = curr_price * target_shares_count

total_shares = initial_shares_count + target_shares_count
total_capital = invested_capital + planned_capital

new_avg_share_price = total_capital / total_shares
profit_per_share = curr_price - new_avg_share_price
total_profit = profit_per_share * total_shares

print('=================================================')
print(f"You are going to invest this much INR: {planned_capital}")
print(f"Total shares: {total_shares}")
print(f"Total capital: {total_capital:.2f}")
print(f"Average value of each share: {new_avg_share_price:.2f}")
print(f"Profit on each share: {profit_per_share}")
print(f"Total profit: {total_profit:.2f}")

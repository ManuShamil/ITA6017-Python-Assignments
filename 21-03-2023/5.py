# 5. Help the teller of Lakshmi Silks to calculate the net discount offered in Seasonal 
# Shopping for a customer based on the following criteria
# Sarees 20%
# Ethnic Wears 15%
# Gents Wears 15%
# Kids Wears 15%
# net bill amount > 6,000 Extra 5 percen


discount_map = {
    "Sarees": 0.2,
    "Ethnic Wears": 0.15,
    "Gents Wears": 0.15,
    "Kids Wears": 0.15
}

shopping_list = [
    {"item": "Sarees", "amount": 5000},
    {"item": "Sarees", "amount": 7000},
    {"item": "Ethnic Wears", "amount": 3000},
    {"item": "Gents Wears", "amount": 2000},
    {"item": "Kids Wears", "amount": 1000}
]

total_amount = 0

for x in shopping_list:

    item = x["item"]
    amount = x["amount"]
    discount = discount_map[item]

    print("{} Amount: {}, Discount: {} %".format(item, amount, discount * 100))

    total_amount += amount - (amount * discount)

if total_amount > 6000:
    total_amount -= total_amount * 0.05


print("Total amount: {}".format(total_amount))

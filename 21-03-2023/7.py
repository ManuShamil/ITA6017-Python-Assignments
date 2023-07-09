# 7. Program that accepts the On Road Price of a bike and displays the Road Tax to be 
# levied on it, based on the following guidelines
# >2,00,000 20%
# 1,00,00-1,99,000 15%
# <1,00,00 10%

amount = int(input("Enter the amount: "))
road_tax = 0
if amount > 200000:
    road_tax = amount * 0.2
elif amount >= 100000 and amount <= 199000:
    road_tax = amount * 0.15
elif amount < 100000:
    road_tax = amount * 0.1

print("Amount: {}".format(amount))
print("Road tax: {}".format(road_tax))
print("Net amount: {}".format(amount + road_tax))
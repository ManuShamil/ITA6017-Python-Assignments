# Percentage of non-defective items
# A bag contains a total of 'T' nuts and bolts. Out of which there are
# 'N' nuts. In a quality check, x% of the nuts and y% of
# bolts in the bag were found to be defective. Design
# an algorithm and write a Python code to determine the percentage of non-defective items in the bag.
# For example if T is 200, N is 150, x is 50 and y is 20 then the percentage of non-defective items in bag is 57.5.
# Round the answer to two decimal places using format function.


# Input for the Problem
# 'T' – total number of nuts and bolts in the bag
# 'N' – Number of nuts
# 'x' – Percentage of defective nuts in the bag
# 'y' – Percentage of defective bolts in the bag
# Output of the Problem
# Percentage of non-defective items in bag
# Boundary Conditions
# All inputs > 0


def calculate_percentage():
    T_nuts_and_bolts = int(input("please enter the total number of nuts and bolts in bag: "))
    N_nuts = int(input("please enter the total number of nuts in bag: "))

    # calculating total bolts in bag
    N_bolts = T_nuts_and_bolts - N_nuts

    # calculating number of defective nuts in bag
    x = int(input("please enter the defective percentage of nuts: "))
    x_defective_nuts = (x / 100) * N_nuts

    # calculating number of defective bolts in bag
    y = int(input("please enter the defective percentage of bolts: "))
    y_defective_bots = (y / 100) * N_bolts
    
    total_defective_item = x_defective_nuts + y_defective_bots
    total_non_defective = T_nuts_and_bolts - total_defective_item

    # calculating percentage of non_defective nuts and bolts
    total_non_defective_percent = (total_non_defective/ T_nuts_and_bolts) * 100

    g = float("{0:.2f}".format(total_non_defective_percent))

    print(f"percentage of non_defective item in bag is: {g} ")


if __name__ == '__main__':
    calculate_percentage()
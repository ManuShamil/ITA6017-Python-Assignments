import math


def calculate_pebble():
    m1 = int(input("Please Enter the initial level of water in the jug: "))
    m2 = int(input("Please Enter the level of water in the jug required for drinking: "))
    x = int(input("Please Enter the height which small pebble will increase: "))
    y = int(input("Please Enter the height which big pebble will increase: "))
    n = int(input("Please Enter the number of small pebbles: "))

    # raise water initially using small pebble
    initial_raise = n * x + m1

    # calculating remaining raise
    remaining_raise = m2 - initial_raise

    # calculating required number of pebble
    big_pebbles = math.ceil(remaining_raise / y)

    print("")
    print(f" The number of big pebble required is {big_pebbles} ")
    print(" ")
    print(f" Also Total Number of pebble required big pebble plus small pebble is  {big_pebbles + n} ")


if __name__ == '__main__':
    calculate_pebble()
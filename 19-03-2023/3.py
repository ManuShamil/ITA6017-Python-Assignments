# A person 'X' has a farm which is rectangular in shape. 'X' wants to plant coconut trees in the farm and he
# has heard that every tree has to be separated by 2 feet. He needs to calculate the number of plants
# to be purchased. Write a program to calculate the number of plants when provided with the length
# and breadth of the farm (in feet). The program should display the number of rows and columns along
# with the total number of plants required for the farm. For example, if the length and breadth of the
# farm is 9 feet * 4 feet then the farmer can plant trees in  positions 0, 2, 4, 6, 8 along the length
# and 0,2,4 along the breadth therefore number of trees to be purchased is 5*3 = 15.

def calculate_no_of_Plant():
    length = int(input("please enter the length of farm in feet: "))
    breadth = int(input("please enter the breadth of farm in feet: "))

    distance_between_plant = 2

    # since the distance is two it should be evenly divided by 2 using this we can calculate the no of rows and column
    plant_in_row = (length // distance_between_plant) + 1
    plant_in_col = (breadth // distance_between_plant) + 1

    # calculating total number of plant required
    total_plant = plant_in_row * plant_in_col

    print(f"Total plant in row {plant_in_row} ")
    print(f"Total plant in col {plant_in_col} ")
    print(" ")
    print(f"Total Number of plant needed: {total_plant}  ")


if __name__ == '__main__':
    calculate_no_of_Plant()








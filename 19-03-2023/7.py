# A person wants to know his Body Mass Index (BMI). He knows his weight in pounds and height in inches.
# The evaluator knows the formula for calculating BMI using the formula,
# BMI = (weight in kilograms) / (height in m * height in m)
# Help the person in finding his BMI by writing a program for him.
# (Use the conversion formulae: 1 pound =0.4536 kilograms, 1 inch = 2.54 cms)
# Input Format:
# Weight of person in pounds.
# Height of the person in inches.
# Output Format:
# BMI of the person calculated using the formula,
#  (weight in kilograms) / (height in m * height in m)


def bmi():
    weight = float(input("Please enter the weight in pounds: "))
    height_feet = float(input("Please enter the height in feet: "))
    height_inches = float(input("Please enter the remaining height in inches: "))

    # conversion of height to meters
    height_inches += height_feet * 12
    height_meters = height_inches * 0.0254

    # conversion of weight to kilograms
    weight_kg = weight * 0.4536

    # formula for calculating bmi
    bmi = weight_kg / (height_meters * height_meters)

    bmi_format = float("{0:.2f}".format(bmi))

    print(f"BMI of a person is {bmi_format}")


if __name__ == '__main__':
    bmi()

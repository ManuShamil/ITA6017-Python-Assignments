# 3. VIT follows relative grading based on the class average to grade the performance of 
# students in various examinations. Write a program that accepts the marks secured by a 
# student for a given subject along with the average marks of the respective class. Then display 
# the grade he has secured, based on the following instructions.
# a) Grading is done based on the deviation from class average. 
# b) If the deviation from class average of the student’s mark is greater than 
# or equal to 20, the student has scored S grade
# c) If the deviation from class average of the student’s mark is greater than 
# or equal to 10, the student has scored A grade
# d) If the deviation from class average of the student’s mark is within the 
# range of -5 to + 5, the student has scored B grade
# e) If the deviation from class average of the student’s mark is less than or 
# equal to 10, the student has scored C grade
# f) If the deviation from class average of the student’s mark is less than or 
# equal to 15, the student has scored D grade
# g) If the deviation from class average of the student’s mark is less than 
# 20, the student has scored F grade

if __name__ == "__main__":
    mark = int(input("Enter the mark: "))
    avg = int(input("Enter the average: "))
    deviation = mark - avg
    if deviation >= 20:
        print("S")
    elif deviation >= 10:
        print("A")
    elif deviation >= -5 and deviation <= 5:
        print("B")
    elif deviation <= 10:
        print("C")
    elif deviation <= 15:
        print("D")
    elif deviation < 20:
        print("F")
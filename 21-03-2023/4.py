# Develop a program that accepts the age and gender of the user and display whether 
# he/she is eligible for concession in this category. Also display the ticket amount 
# he/she has to pay based on the concession.
# Male Age>=60, 40% of base fare
# Female Age>=58, 50% of base fare

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")

ticket_amount = int(input("Enter your ticket amount:"))

final_amount = ticket_amount
if gender == 'M' and age >= 60 :
    final_amount = ticket_amount - (ticket_amount * 0.4)
elif gender == 'F' and age >= 58:
    final_amount = ticket_amount - (ticket_amount * 0.5)

print("Original Ticket amount: {}".format(ticket_amount))
print("After Discount: {}".format(final_amount))

# A finance consultant decides to create an application for the public who wants to decide on the
# of investment they can make. He needs an application, which when given with the initial amount,
# no of years of investment ‘n’ and the expected amount after ‘n’ years, should tell the  rate of
# based on which the customers will choose their investments. Assume that the application works with
#     only simple interest calculation. Can you code for Raman?
#     Use Rate of interest = ((expected amount-initial amount) / (initial amount * no of years))*100.

def find_interest():
    initial_amount = float(input("please enter the initial amount to be invested: "))
    no_of_year = int(input("please enter for how much year you want to invest you money: "))
    expected_amount = float(input(f"please enter the amount you are expecting after {no_of_year}: "))

    # Calculate the rate of interest
    interest_rate = ((expected_amount - initial_amount) / (initial_amount * no_of_year)) * 100

    print(f"user should invest at a interest rate of {interest_rate}")


if __name__ == '__main__':
    find_interest()

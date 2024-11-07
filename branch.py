# Name: Kaleb Lowry
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%


import datetime

########## define global variables ############
#define tax rate, service fee, and prices

import datetime

# Constants
SALES_TAX_RATE = 0.062
SERVICE_FEE_RATE = 0.10
ADULT_MEAL_PRICE = 19.95
CHILD_MEAL_PRICE = 11.95

# Global variables
num_adult_meals = 0
num_child_meals = 0
subtotal = 0
service_fee = 0
sales_tax = 0
total = 0

############ define program functions ############
def main():
    more_orders = True

    while more_orders:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more_orders = False
            print("Thank you for coming to Branch Barbeque Buffet! Enjoy your meal.")

def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("Enter the number of adult meals: "))
    num_child_meals = int(input("Enter the number of child meals: "))

def perform_calculations():
    global subtotal, service_fee, sales_tax, total
    adult_meal_cost = num_adult_meals * ADULT_MEAL_PRICE
    child_meal_cost = num_child_meals * CHILD_MEAL_PRICE
    subtotal = adult_meal_cost + child_meal_cost
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = (subtotal + service_fee) * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():
    print('------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('------------------------------')
    print("Adult meals (" + str(num_adult_meals) + " @ $" + "{:.2f}".format(ADULT_MEAL_PRICE) + ")   $ " + "{:8.2f}".format(num_adult_meals * ADULT_MEAL_PRICE))
    print("Child meals (" + str(num_child_meals) + " @ $" + "{:.2f}".format(CHILD_MEAL_PRICE) + ")   $ " + "{:8.2f}".format(num_child_meals * CHILD_MEAL_PRICE))
    print('------------------------------')
    print(f'Subtotal                  $ ' + format(subtotal, '8,.2f'))
    print(f'Service Fee (10%)         $ ' + format(service_fee,'8,.2f'))
    print(f'Sales Tax (6.2%)          $ ' + format(sales_tax,'8,.2f'))
    print('------------------------------')
    print(f'Total                     $ ' + format(total,'8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

######### call on main program to execute #########
main()

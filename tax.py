# Name: Kaleb Lowry
# Prog Purpose: This program will calculate vehicle property taxes for Charlottesville.
import datetime

def main():
    while True:
        print("\n***** PERSONAL PROPERTY TAX BILL *****")
        print("=" * 50)

        TAX_RATE = 0.044  
        RELIEF_RATE = 0.30  

        try:
            assessed_value = float(input("Enter the assessed value of the vehicle: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        eligible_for_relief = input("Is the vehicle eligible for tax relief (Y/N)? ").strip().lower()
        if eligible_for_relief not in ['y', 'n']:
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue

     
        annual_tax = assessed_value * TAX_RATE
        six_month_tax = annual_tax / 2
        relief_amount = six_month_tax * RELIEF_RATE if eligible_for_relief == 'y' else 0
        total_due = six_month_tax - relief_amount

     
        print("\n" + "=" * 50)
        print("CHARLOTTESVILLE PERSONAL PROPERTY TAX BILL")
        print(f"Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("=" * 50)
        print(f"{'Assessed Value of Vehicle:':<30} ${assessed_value:>10,.2f}")
        print(f"{'Full Annual Amount Owed:':<30} ${annual_tax:>10,.2f}")
        print(f"{'Relief Amount:':<30} ${relief_amount:>10,.2f}")
        print(f"{'Total Due:':<30} ${total_due:>10,.2f}")
        print("=" * 50)

       
        another = input("\nWould you like to calculate tax for another vehicle? (Y/N): ").strip().lower()
        if another != 'y':
            print("\nThank you for using the Charlottesville Tax Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()

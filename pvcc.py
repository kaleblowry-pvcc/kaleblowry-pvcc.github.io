# Name: Kaleb Lowry
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

########## define program functions ##########
import datetime

# Define constants for tuition & fee rates
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# Global variables for output file
outfile = 'pvccweb.html'

def main():
    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() == "N":
            more = False
            print("\n** Open this file in a browser window to see your results: " + outfile)
            close_outfile()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition and Fees </title>\n')
    f.write('<style> td{text-align: right; color: #FFD700;} th {color: #FFD700;} </style> </head>\n')
    f.write('<body style="background-color: #2E2B26; background-image: url(\'wp-pvcc.jpg\'); background-size: tile; color: #EAD2AC;">\n')
    f.write('<h1 style="text-align: center; color: #FFD700;">Piedmont Virginia Community College</h1>\n')
    f.write('<h2 style="text-align: center; color: #EAD2AC;">Tuition and Fees Report</h2>\n')

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMMUNITY COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE
    total = tuition + inst_fee + cap_fee + act_fee
    balance = total - scholarship_amt

def create_output_file():
    today = str(datetime.datetime.now())
    day_time = today[:16]

    f.write('<table border="1" style="margin: auto; font-family: Arial, sans-serif; width: 80%; text-align: left; background-color: #3B342C; border-collapse: collapse;">\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Date/Time</th><td>' + day_time + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Number of Credits</th><td>' + str(numcredits) + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Tuition</th><td>$' + format(tuition, ',.2f') + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Capital Fee</th><td>$' + format(cap_fee, ',.2f') + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Institution Fee</th><td>$' + format(inst_fee, ',.2f') + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Activity Fee</th><td>$' + format(act_fee, ',.2f') + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Total</th><td>$' + format(total, ',.2f') + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Scholarship</th><td>$' + format(scholarship_amt, ',.2f') + '</td></tr>\n')
    f.write('<tr><th colspan="2" style="padding: 10px;">Balance Owed</th><td>$' + format(balance, ',.2f') + '</td></tr>\n')
    f.write('</table><br><br>\n')

def close_outfile():
    f.write('</body></html>')
    f.close()

########## call on main program to execute##############
main()

    
    
    

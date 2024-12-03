# Name: Kaleb Lowry
# Prog Purpose: This program creates a payroll report and outputs it to a file
import datetime

############## LISTS of data ############
emp = [
    "Smith, James ",
    "Johnson, Patricia",
    "Williams, John ",
    "Brown, Michael ",
    "Jones, Elizabeth ",
    "Garcia, Brian ",
    "Miller, Deborah ",
    "Davis, Timothy ",
    "Rodriguez, Ronald",
    "Martinez, Karen ",
    "Hernandez, Lisa ",
    "Lopez, Nancy ",
    "Gonzales, Betty ",
    "Wilson, Sandra ",
    "Anderson, Margie ",
    "Thomas, Daniel ",
    "Taylor, Steven ",
    "Moore, Andrew ",
    "Jackson, Donna ",
    "Martin, Yolanda ",
    "Lee, Carolina ",
    "Perez, Kevin ",
    "Thompson, Brian ",
    "White, Deborah ",
]
job = [
    "C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
    "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",
]
hours = [
    37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
    28, 31, 37, 32, 36, 22, 28, 29, 21, 31,
]
num_emps = len(emp)

######## NEW LISTS for calculated amounts ########
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0

########### TUPLES of constants ###########
PAY_RATE = (16.50, 15.75, 15.75, 19.50)
DED_RATE = (0.12, 0.03, 0.062, 0.0145, 0.04)

########### Define program functions ###########
def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
        
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

        
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        soc_sec_amt = pay * DED_RATE[2]  
        medicare_amt = pay * DED_RATE[3]  
        ret401k_amt = pay * DED_RATE[4]  

        
        net = pay - (fed + state + soc_sec_amt + medicare_amt + ret401k_amt)

        
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(soc_sec_amt)
        medicare.append(medicare_amt)
        ret401k.append(ret401k_amt)
        net_pay.append(net)

        
        total_gross += pay
        total_net += net

def create_output_file():
    line = '-' * 100
    tab = "\t"
    
    ############## output file ###############
    out_file = "payroll.txt"
    f = open(out_file, "a")  

    f.write(line + "\n")
    f.write("\t************* FRESH FOODS MARKET *************\n")
    f.write("\t************* WEEKLY PAYROLL REPORT *************\n")
    f.write("\t" + str(datetime.datetime.now()) + "\n")
    f.write(line + "\n")
    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
    f.write(titles1 + titles2 + "\n")
    f.write(line + "\n")

   
    for i in range(num_emps):
        data = emp[i] + tab + job[i] + tab + "${:,.2f}".format(gross_pay[i]) + tab \
               + "${:,.2f}".format(fed_tax[i]) + tab + "${:,.2f}".format(state_tax[i]) + tab \
               + "${:,.2f}".format(soc_sec[i]) + tab + "${:,.2f}".format(medicare[i]) + tab \
               + "${:,.2f}".format(net_pay[i])
        f.write(data + "\n")

  
    f.write(line + "\n")
    f.write("TOTAL GROSS: ${:,.2f}\n".format(total_gross))
    f.write("TOTAL NET  : ${:,.2f}\n".format(total_net))
    f.write(line + "\n")

    f.close()
    print("Open " + out_file + " to view your report")

########## Call on main program to execute ##########
main()


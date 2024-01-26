# imported math module to carry out mathematical equation.
import math 
menu = '''
                Welcome to the Finance calculator.
                investment - To calculate the amount of interest you'll earn on your investment
                bond       - To calculate the amount you'll have to pay on a home loan
           '''
print(menu)
'''
These function named 'simple' & 'compound' will calculate the interest rates respectively with the given input where,
p is the amount deposited by the user.
r is rate of interest.  
t is the number of years.
simple interest rate equation is = p * (1 + (r * t)) 
compound rate equation is        = p * math.pow((1+r),t)
'''
def simple():
        while True:
            try:
                p = float(input("Please enter the amount of money you like to deposit"))
                r = float(input("Please enter the rate of interest (exclude % symbol)"))
                r =  r/100
                t = int(input("Please enter the years for investment "))
                sim_interest_rate = p * (1 + (r * t))
            except ValueError:
                print("You have not entered a number.")
                continue

            return print(f"You will get £{(p + sim_interest_rate):.2f} after {t} years at {r * 100}% interest rate"  )


def compound():
        while True:
            try:
                p = float(input("Please enter the amount of money you like to deposit :"))
                r = float(input("Please enter the rate of interest (exclude % symbol) :"))
                r =  r/100
                t = int(input("Please enter the years for investment :"))
                com_interest_rate = p * math.pow((1+r),t)
            except ValueError:
                print("You have not entered a number.")
                continue

            return print(f"You will get £{(p + com_interest_rate):.2f} after {t} years at {r * 100}% interest rate")
        
'''
This function named 'bond' will calculate the bond repayment amount with the given input where,
p is the present value of the house.
i is the rate of interest.  
n is the number of months planned for the repayment.
bond repayment equation rate is = (i * p) / (1- (1+ i)** (-n))
'''
def bond():
    while True:
        try:
            p = float(input("Enter the present value of your house :"))
            i = float(input("Please enter the rate of interest :"))/100
            i = i / 12
            n = int(input("Please enter the amount of months planned for repayment :"))
            bond_repay = (i * p) / (1- (1+ i)** (-n))
        except ValueError:
             print("You have not entered a number.")
             continue
        
        return print(f"You have to repay £{bond_repay:.2f} each month.")

# This function will take user inputs and check their selection and execute based on their selection.
def user_selection():
    while True:
        try: 
            selection = input('''
Enter either 'investment' or 'bond' from the menu above to proceed or type 'exit' to quit :''' ).lower()
            if  selection == "investment":
                
                while True:
                     calculation_selection = input("Please select either simple or compound interest").lower()
                    
                     if calculation_selection == "simple":
                        simple()
                        break
                     elif calculation_selection == "compound":
                        compound()
                        break
                     else:
                          print("You've entered invalid character!.Please try again.")
            elif selection == "bond":   
                bond()  
                break 
            
            elif not selection.isalpha():                   
                print("Oops!That didn't work.Please enter either 'investment' or 'bond'.")
                continue
            elif selection == "exit":
                print("Thank you for using the Finance Calculator.You have now exited the program.")
                break
            else:  
                print("Sorry You have entered invalid input.Please try again!")  
        except ValueError:
                print("You've entered invalid character.Please try again.")
        continue  
         
user_selection()  
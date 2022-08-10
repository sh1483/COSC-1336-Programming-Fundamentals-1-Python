# Steven Haynes
# Ch. 2-2 Practice Status: Complete

# A program that uses input to determine net pay, and annual pay.


# Asking user for input on income & deductions, converted to decimal format.
monthly_gross = float(input('What is your Gross Monthly Income? '))
monthly_deductions = float(input('What are your total' +
                                 ' Monthly Paycheck Deductions? '))

# Converting from Gross to Net Monthly Income.
monthly_net = (monthly_gross - monthly_deductions)

print("Your Monthly Net Income is: $", format(monthly_net, ',.2f'), sep= '')

# Determining Annual Gross Income from Monthly Gross Income.
annual_gross = (monthly_gross * 12)
print('Your Annual Gross Pay is: $', format(annual_gross, ',.2f'), sep= '')

# Determining Annual Net Pay from Monthly Net Pay.
annual_net = (monthly_net * 12)
print("Your Annual Net Pay is: $", format(annual_net, ',.2f'), sep= '')

# Definitions 
def float_input(prompt):
    return float(input(prompt))   

def print_finances(info_dict):
    for label, value in info_dict.items():
        print(f"{label}: ${value:.2f}")

def print_financial_summary(label, weekly_amount):
    print(f"{label} - Weekly: ${weekly_amount:.2f} | Monthly: ${convert_to_other(weekly_amount, 'monthly'):.2f} | Yearly: ${convert_to_other(weekly_amount, 'yearly'):.2f}")

def convert_to_weekly(amount, frequency):
    if frequency == "weekly":
        return amount
    elif frequency == "fortnightly":
        return amount / 2
    elif frequency == "monthly":
        return amount / 4.33
    elif frequency == "quarterly":
        return amount / 13
    elif frequency == "yearly":
        return amount / 52
    else:
        raise ValueError("Invalid Frequency")
    
def convert_to_other(amount, target_frequency):
    if target_frequency == "weekly":
        return amount
    elif target_frequency == "monthly":
        return amount * 4.33
    elif target_frequency == "quarterly":
        return amount * 13
    elif target_frequency == "yearly":
        return amount * 52
    else:
        raise ValueError("Invalid frequency")

# User Inputs 
print("\nEnsure all data input is after tax")  
#print("\nweekly = W, monthly = N, quarterly = Q, yearly = Y") 

payFrequency = input("What is your pay frequency? (weekly, fortnightly, monthly, yearly) ")
income = float_input("what is your income? $")
rentFrequency = input("What is your rent frequency? ")
rent = float_input("What is your rent/mortgage? $")
utilityFrequency = input("What is your electricity and/or gass and/or water Payment Frequency? (monthly, quarterly, yearly) ")
utilityElec = float_input("What is your electricity bill? $")
utilityGas = float_input("What is your gas bill? $")
utilityWater = float_input("what is your water bill? $")

bills = []
while True:
    bill_name = input("Enter bill name (or press Enter to finish): ")
    if not bill_name:
        break

    bill_frequency = input(f"How Often do you pay {bill_name}? (weekly, monthly, quarterly, yearly): ")
    bill_amount = float_input(f"How much does {bill_name} cost? $")
    bills.append({"name": bill_name, "frequency": bill_frequency, "amount": bill_amount})



#Convert frequency to weekly || monthly || yearly
#Income
weekly_income = convert_to_weekly(income, payFrequency)
monthly_income = convert_to_other(weekly_income, "monthly")
yearly_income = convert_to_other(weekly_income, "yearly")

#Rent
weekly_rent = convert_to_weekly(rent, payFrequency)
monthly_rent = convert_to_other(weekly_rent, "monthly")
yearly_rent = convert_to_other(weekly_rent, "yearly")

#Utility Gas and Elec and Water
weekly_elec = convert_to_weekly(utilityElec, utilityFrequency)
weekly_gas = convert_to_weekly(utilityGas, utilityFrequency)
weekly_water = convert_to_weekly(utilityWater, utilityFrequency)

weekly_utility = weekly_elec + weekly_gas + weekly_water

monthly_utility = convert_to_other(weekly_utility, "monthly")
yearly_utility = convert_to_other(weekly_utility, "yearly")

#Bills
weekly_bills = 0
for bill in bills:
    bill["weekly"] = convert_to_weekly(bill["amount"], bill["frequency"])
    weekly_bills += bill["weekly"]

monthly_bills = convert_to_other(weekly_bills, "monthly")
yearly_bills = convert_to_other(weekly_bills, "yearly")

#Total spend
weekly_expenses = weekly_rent + weekly_utility + weekly_bills
monthly_expenses = convert_to_other(weekly_expenses, "monthly")
yearly_expenses = convert_to_other(weekly_expenses, "yearly")

#Savings
print("Lets talk about savings. Please answer the following questions.")
leftover_wage = weekly_income - weekly_expenses
savings_percentage = float_input(f"What % of your leftover wage({leftover_wage:.2f}) would you like to save? ")

amount_to_save = leftover_wage * (savings_percentage / 100)
personal_spending = leftover_wage - amount_to_save
saving_accounts = {}
while True:
    account_name = input("enter name of savings account (eg; Emergency Fund, Vacation, House Deposit): ")
    if not account_name:
        break
    allocated_percentage = float_input(f"What % of your savings ({amount_to_save:.2f} weekly) would you like to allocate to {account_name}? ")
    allocated_amount = amount_to_save * (allocated_percentage / 100)
    saving_accounts[account_name] = allocated_amount

#Maths

financialInfo = {
    "Weekly Income": weekly_income,
    "Monthly Income": monthly_income,
    "Yearly Income": yearly_income,
     "Weekly Rent": weekly_rent, 
    "Monthly Rent": monthly_rent,
    "Yearly Rent": yearly_rent,
    "Weekly Utility": weekly_utility,
    "Monthly Utility": monthly_utility,
    "Yearly Utility": yearly_utility,
    "Weekly Bills": weekly_bills,
    "Monthly Bills": monthly_bills,
    "Yearly Bills": yearly_bills,
   
    }

financialInfo["Weekly Expenses"] = weekly_expenses
financialInfo["Monthly Expenses"] = monthly_expenses
financialInfo["Yearly Expenses"] = yearly_expenses

# Prints
print("\n=== Summary ===")
print("\n=== Financials ===")
print_financial_summary("Income", weekly_income)
print_financial_summary("Rent", weekly_rent)
print_financial_summary("Utility", weekly_utility)
print_financial_summary("Bills", weekly_bills)
print_financial_summary("Expenses", weekly_expenses)


print("\n=== Detailed Breakdown ===")
print(f"Income - Weekly: ${weekly_income:.2f} | Monthly: ${convert_to_other(weekly_income, 'monthly'):.2f} | Yearly: ${convert_to_other(weekly_income, 'yearly'):.2f}")
print(f"Electricity Bill - Weekly: ${weekly_elec:.2f} | Monthly: ${convert_to_other(weekly_elec, 'monthly'):.2f} | Yearly: ${convert_to_other(weekly_elec, 'yearly'):.2f}")
print(f"Gas Bill - Weekly: ${weekly_gas:.2f} | Monthly: ${convert_to_other(weekly_gas, 'monthly'):.2f} | Yearly: ${convert_to_other(weekly_gas, 'yearly'):.2f}")
print(f"Water Bill - Weekly: ${weekly_water:.2f} | Monthly: ${convert_to_other(weekly_water, 'monthly'):.2f} | Yearly: ${convert_to_other(weekly_water, 'yearly'):.2f}")
for bill in bills:
    print(f"{bill['name']} - Weekly: ${bill['weekly']:.2f} | Monthly: ${convert_to_other(bill['weekly'], 'monthly'):.2f} | Yearly: ${convert_to_other(bill['weekly'], 'yearly'):.2f}")
print("\n=== Savings Breakdown ===")
for account, amount in saving_accounts.items():
    print_financial_summary(account, amount)
print(f"Personal speding: ${personal_spending:.2f}")  


  


def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("input the loan amount: "))
    apr = float(input("input the amout intrest rate: "))
    years = int(input("input amount of the years: "))

    monthly_intrest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment  = principal * monthly_intrest_rate/(1 - (1 + monthly_intrest_rate) ** (-amount_of_months))

    print(" The monthly payment for this loan is:%2f " %monthly_payment)

main()
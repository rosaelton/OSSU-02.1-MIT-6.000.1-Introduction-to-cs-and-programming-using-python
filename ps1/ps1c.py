ANNUAL_SALARY = int(input("Enter the starting salary: "))

semi_annual_raise = .07
r = 0.04
portion_down_payment = .25
total_cost = 1_000_000
months = 36
down_payment = total_cost * portion_down_payment

steps = 0
min = 0
max = 10000

while True:
    current_savings = 0
    annual_salary = ANNUAL_SALARY

    portion_saved = (min + max) // 2
    portion_saved = portion_saved / 10000
    
    for month in range(36):
        if month % 6 == 0 and month > 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
        current_savings = current_savings * (1 + r/12)
        current_savings += (annual_salary/12) * portion_saved
    steps += 1

    if current_savings - down_payment > 100:
        max = int(portion_saved * 10000)
    elif current_savings - down_payment < 0 and min > max:
        print("It is not possible to pay the down payment in three years.")
        break
    elif current_savings - down_payment < 0:
        min = int(portion_saved * 10000) + 1
    else:
        print("Best savings rate:", portion_saved)
        print("Steps in bisection search", steps)
        break




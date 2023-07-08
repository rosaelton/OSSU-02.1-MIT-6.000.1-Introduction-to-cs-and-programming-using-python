#!/usr/bin/env python3

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = .25
current_savings = 0
r = 0.04

down_payment = total_cost * portion_down_payment

months = 0
while current_savings < down_payment:
    if months % 6 == 0 and months > 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
    current_savings = current_savings * (1 + r/12)
    current_savings += (annual_salary/12) * portion_saved
    months += 1

print(months)


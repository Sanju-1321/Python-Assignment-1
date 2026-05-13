annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Down payment is 25% of total cost
portion_down_payment = 0.25 * total_cost

# Initial savings
current_savings = 0

# Annual return on investment
r = 0.04

# Monthly salary
monthly_salary = annual_salary / 12

# Month counter
months = 0

# Loop until savings reach required down payment
while current_savings < portion_down_payment:

    # Monthly investment return
    current_savings += current_savings * (r / 12)

    # Monthly savings from salary
    current_savings += monthly_salary * portion_saved

    # Increase month count
    months += 1

    # Apply semi-annual raise every 6 months
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

print("Number of months:", months)

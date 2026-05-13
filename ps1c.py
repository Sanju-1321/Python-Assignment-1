annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
portion_down_payment = 0.25 * total_cost
r = 0.04
semi_annual_raise = 0.07
months = 36

def calculate_savings(salary, savings_rate):
    current_savings = 0
    monthly_salary = salary / 12

    for month in range(1, months + 1):

        current_savings += current_savings * (r / 12)
      
        current_savings += monthly_salary * savings_rate
        if month % 6 == 0:
            salary += salary * semi_annual_raise
            monthly_salary = salary / 12

    return current_savings

max_savings = calculate_savings(annual_salary, 1.0)

if max_savings < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    low = 0
    high = 10000
    epsilon = 100
    steps = 0

    while True:
        steps += 1

        mid = (low + high) // 2
        savings_rate = mid / 10000

        current_savings = calculate_savings(annual_salary, savings_rate)

        if abs(current_savings - portion_down_payment) <= epsilon:
            break

        if current_savings < portion_down_payment:
            low = mid
        else:
            high = mid

    print("Best savings rate:", round(savings_rate, 4))
    print("Steps in bisection search:", steps)

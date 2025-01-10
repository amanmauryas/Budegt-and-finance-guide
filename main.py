import matplotlib.pyplot as plt

def collect_data():
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your monthly expenses: "))
    debts = float(input("Enter your current debts (if any): "))
    savings_goal = float(input("Enter your savings goal: "))
    return income, expenses, debts, savings_goal

def analyze_data(income, expenses, debts):
    disposable_income = income - expenses
    suggested_savings = disposable_income * 0.20
    return disposable_income, suggested_savings

def provide_recommendations(disposable_income, suggested_savings, debts):
    if debts > 0:
        print(f"Your disposable income is {disposable_income:.2f}. Focus on paying debts first.")
    else:
        print(f"Your disposable income is {disposable_income:.2f}.")
        print(f"You should save at least {suggested_savings:.2f} each month to achieve your goals.")

def visualize_data(income, expenses, savings_goal):
    labels = ['Income', 'Expenses', 'Savings Goal']
    values = [income, expenses, savings_goal]
    plt.bar(labels, values, color=['blue', 'orange', 'green'])
    plt.title('Your Financial Overview')
    plt.show()

# Main Program
income, expenses, debts, savings_goal = collect_data()
disposable_income, suggested_savings = analyze_data(income, expenses, debts)
provide_recommendations(disposable_income, suggested_savings, debts)
visualize_data(income, expenses, savings_goal)

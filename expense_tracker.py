expenses = []


def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append([name, float(amount)])
    except FileNotFoundError:
        pass


def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expenses.append([name, amount])

        with open("expenses.txt", "a") as file:
            file.write(name + "," + str(amount) + "\n")

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_expenses():
    print("\n===== EXPENSES =====")

    if len(expenses) == 0:
        print("No expenses added.")
    else:
        for expense in expenses:
            print(expense[0], "₹", expense[1])


def view_total():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    print("Total Expense: ₹", total)


def search_expense():
    search = input("Enter expense name to search: ")

    found = False

    for expense in expenses:
        if expense[0].lower() == search.lower():
            print("Found:", expense[0], "₹", expense[1])
            found = True

    if found == False:
        print("Expense not found.")


def expense_summary():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    count = len(expenses)

    print("\n===== EXPENSE SUMMARY =====")
    print("Number of Expenses:", count)
    print("Total Expense: ₹", total)

    if count > 0:
        average = total / count
        print("Average Expense: ₹", round(average, 2))
    else:
        print("Average Expense: ₹0")


def main():
    load_expenses()

    while True:
        print("\n===== STUDENT EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Search Expense")
        print("5. Expense Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            expense_summary()

        elif choice == "6":
            print("Thank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
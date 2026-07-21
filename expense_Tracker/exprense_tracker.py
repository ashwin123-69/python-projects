def show_menu(expenses):
    print("1. add expense")
    print("2. view expenses")
    print("3. total spending")
    print("4. highest expense")
    print("5. delete expense")
    print("6. search expense")
    print("7. expense report")
expenses={
    "petrol":{
        "category":"travel",
        "amount":1000},
    "chicken":{
        "category":"food",
        "amount":300
    },
    'room': {'category': 'hotel',
             'amount': 3000}
}
show_menu(expenses)
def add_expense(expenses):
    expense_name=input("enter expense name: ")
    category_name=input("enter category name: ")
    amount=int(input("enter amount: "))
    expenses[expense_name]={
        "category":category_name,
        "amount":amount
    }
    print(expenses)

def view_expenses(expenses):
    print(expenses)

def total_spending(expenses):
    total=0
    for key in expenses:
        total+=expenses[key]["amount"]
    print(total)

def highest_expense(expenses):
    max_total=0
    high_expense=""
    for key in expenses:
        if expenses[key]["amount"]>max_total:
            max_total=expenses[key]["amount"]
            high_expense=key
    print(max_total)
    print(high_expense)

def delete_expenses(expenses):
    name=input("enter expense name: ")
    del expenses[name]
    print(expenses)

def search_expense(expenses):
    name=input("enter expense name: ")
    print(expenses[name])

def expense_report(expenses):
    name = input("enter expense name: ")
    category = expenses[name]["category"]
    amount = expenses[name]["amount"]
    print("expense name: ", name)
    print("category :", category)
    print("amount: ",amount)

choice=int(input("enter choice: "))
if choice==1:
   add_expense(expenses)
if choice==2:
    view_expenses(expenses)
if choice==3:
    total_spending(expenses)
if choice==4:
    highest_expense(expenses)
if choice==5:
    delete_expenses(expenses)
if choice==6:
    search_expense(expenses)
if choice==7:
    expense_report(expenses)

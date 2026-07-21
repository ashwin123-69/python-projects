habits = {
    "Workout": {
        "completed": 10
    },
    'reading': 
    {'completed': 10
    },
    "Meditation": 
    {"completed": 15
    }
    
}
def add_menu(habits):
    print("1. add habit")
    print("2. view habit")
    print("3. highest completed habit")
    print("4. total habits")
    print("5. delete habits")
    print("6. habit report")
    print("7. exit")
add_menu(habits)
def add_habit(habits):
    name=input("eneter habit name :")
    days_complete=int(input("enter completed days :"))
    habits[name]={
        "completed": days_complete
    }
    print(habits)
def view_habits(habits):
    print(habits)
def highest_completed_habit(habits):
    high_habit=0
    high_key=""
    for key in habits:
        if habits[key]["completed"]>high_habit:
            high_habit=habits[key]["completed"]
            high_key=key
    print(high_habit)
    print(high_key)
def total_habits(habits):
    print(len(habits))
def delete_habit(habits):
    name=input("enter name: ")
    del(habits[name])
    print(habits)
def habit_report(habits):
    name=input("enter name: ")
    completed_habits=habits[name]["completed"]
    print("habit name: ",name)
    print("days completed: ",completed_habits)
choice=int(input("enter choice: "))
if choice == 1:
    add_habit(habits)

if choice == 2:
    view_habits(habits)

if choice == 3:
    highest_completed_habit(habits)

if choice == 4:
    total_habits(habits)

if choice == 5:
    delete_habit(habits)

if choice == 6:
    habit_report(habits)

if choice == 7:
    print("Goodbye")

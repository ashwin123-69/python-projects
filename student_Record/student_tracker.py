gymtracker = {
    "bench press": {
        "weight": 80,
        "reps": 7
    },
    "squat": {
        "weight": 100,
        "reps": 5
    }
}
def show_menu(gymtracker):
    print("1. add exercise")
    print("2. view workouts")
    print("3. highest weight")
    print("4. total workouts")
    print("5. delete exercises")
    print("6. workout report")
    print("7. exit")
show_menu(gymtracker)
def add_workout(gymtracker):
    exercise_name=input("enter exercise name: ")
    weight=input("enter weight :")
    reps=int(input("enter reps: "))
    gymtracker[exercise_name]={
        "weight": weight,
        "reps":reps
    }
    print(gymtracker)
def view_workouts(gymtracker):
      print(gymtracker)
def highest_weight(gymtracker):
    max_weight=0
    max_key=""
    for key in gymtracker:
        if gymtracker[key]["weight"]>max_weight:
            max_weight=gymtracker[key]["weight"]
            max_key=key
    print(max_weight)
    print(max_key)
def delete_exercises(gymtracker):
    name=input("enter exercise name: ")
    del gymtracker[name]
    print(gymtracker)
def workout_report(gymtracker):
    name=input("enter name: ")
    weight=gymtracker[name]["weight"]
    reps=gymtracker[name]["reps"]
    print("exercise_name: ",name)
    print("weight: ",weight)
    print("reps: ",reps)
def total_workout(gymtracker):
    print(len(gymtracker))
choice=int(input("enter choice: "))
if choice == 1:
    add_workout(gymtracker)

if choice == 2:
    view_workouts(gymtracker)

if choice == 3:
    highest_weight(gymtracker)

if choice == 4:
    total_workout(gymtracker)

if choice == 5:
    delete_exercises(gymtracker)

if choice == 6:
    workout_report(gymtracker)

if choice == 7:
    print("Goodbye")

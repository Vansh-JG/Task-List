import check_input
import tasklist

# This is the menu function which will show the choices the user has.
def main_menu():
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Save and quit")
    user_choice = check_input.get_int_range("Enter choice: ", 1, 5)
    return user_choice

# This function is called when new task is to be added as it also needs
# due date.
def get_date():
    print("Enter due date: ")
    month = check_input.get_int_range("Enter month: ", 1, 12)
    if month < 10:
        if len(str(month)) < 2:
            month = "0" + str(month)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    if day < 10:
        if len(str(day)) < 2:
            day = "0" + str(day)
    year = check_input.get_int_range("Enter year: ", 2000, 3000)

    return f"{month}/{day}/{year}"

# This function is called when new task is to be added as it also needs
# due time.

def get_time():
    print("Enter time: ")
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    if hour < 10:
        if len(str(hour)) < 2:
            hour = "0" + str(hour)
    minute = check_input.get_int_range("Enter minute: ", 0, 59)
    if minute < 10:
        if len(str(minute)) < 2:
            minute = "0" + str(minute)

    return f"{hour}:{minute}"

# This is the main function which runs the whole code. The choices given by
# the user will define the course of the program.
def main():
    user_choice = 0

    task_list = tasklist.Tasklist()
    # Any number except 5 will run this code forward but 5 as the choice
    # will break the while loop terminating the code.
    while user_choice != 5:
        print("-Tasklist-")
        print(f"Tasks to complete: ", str(len(task_list)))
        user_choice = main_menu()
        # Shows the current task and if no tasks are there then prints
        # all tasks complete.
        if user_choice == 1:
            if len(task_list) == 0:
                print("All tasks are complete.")
            else:
                print("Current task is: ")
                print(task_list.tasklist[0])
                print()

        elif user_choice == 2:
            if len(task_list) == 0:
                print("All tasks are complete.")
            else:
                print("Tasks: ")
                for i in enumerate(task_list.tasklist):
                    print(i[-1])

                print()


        elif user_choice == 3:
            print("Marking current task as complete: ")
            print(task_list.tasklist[0])
            task_list.mark_complete()
            print("New current task is: ")
            print(task_list.tasklist[0])
            print()


        elif user_choice == 4:
            desc = input("Enter a task: ")
            date = get_date()
            time = get_time()
            task_list.add_task(desc, date, time)
            task_list.save_file()
            print()


main()






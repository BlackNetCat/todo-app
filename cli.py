#from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%d %b %a, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add {text}, show, edit {num}, complete {num}  or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row =f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            todo_to_remove = todos[number - 1]
            todos.pop(number -1)
            message = f"todo : {todo_to_remove} - was removed"
            print(message)

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not correct...")
print("Bye")



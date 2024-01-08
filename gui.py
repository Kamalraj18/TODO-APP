import functionscall
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functionscall.get_todo(), key="todos", enable_events=True, size=[65, 10])
edit = gui.Button("Edit")
complete = gui.Button("Complete")

window = gui.Window("My To Do App", layout=[[label, input_box, add_button],
                                            [list_box, edit,complete]], font=('Arial', 15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functionscall.get_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functionscall.write_file(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_list = values['todos'][0]
            new_todo = values['todo']

            todos = functionscall.get_todo()
            index = todos.index(todo_to_list)
            todos[index] = new_todo
            functionscall.write_file(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_list = values['todos'][0]
            todos = functionscall.get_todo()
            todos.remove(todo_to_list)
            functionscall.write_file(todos)
            window['todos'].update(values=todos)
        case gui.WINDOW_CLOSED:
            break
window.close()


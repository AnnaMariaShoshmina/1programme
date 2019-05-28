import tkinter
import json
from tkinter import messagebox as mb


def add():  # Добавление новой задачи
    new = {"Ask": "-", "Category": "-", "Time": "-"}

    task = taskName.get()
    cat = categoryName.get()
    time = timeName.get()

    taskName.delete(0, "end")
    categoryName.delete(0, "end")
    timeName.delete(0, "end")

    if task == "":
        mb.showerror("Error", "Your ask")
    else:
        new['Ask'] = task
        if cat != "":
            new['Category'] = cat
        if time != "":
            new['Time'] = time
        todo.append(new)
        writer('list_of_tasks.json', todo)


def end():  # Выход из менеджера задач
    window.destroy()


def writer(filename, numbers):
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)


def reader(filename):
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

def show():
    tasks = ""
    for task in todo:
        for option in task:
            tasks += option + ":" + task[option] + " "
        tasks += "\n"
    # output.config(text=tasks)
    output.config(state="normal")
    output.delete("1.0", "end")
    output.insert("end", tasks)
    output.config(state="disabled")


global todo
todo = list(reader("list_of_tasks.json"))

window = tkinter.Tk()
window.title("Answer")
window.geometry("450x150+660+440")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

name1 = tkinter.Label(frame, text="Ask:")
name1.grid(row=0, column=0)
name2 = tkinter.Label(frame, text="Category:")
name2.grid(row=1, column=0)
name3 = tkinter.Label(frame, text="Time:")
name3.grid(row=2, column=0)

taskName = tkinter.Entry(frame)
taskName.grid(row=0, column=1)
categoryName = tkinter.Entry(frame)
categoryName.grid(row=1, column=1)
timeName = tkinter.Entry(frame)
timeName.grid(row=2, column=1)

addButton = tkinter.Button(frame, text="Plus", command=add)
addButton.grid(row=3, column=1)
openTasksButton = tkinter.Button(frame, text="List of asks", command=show)
openTasksButton.grid(row=4, column=1)
exitButton = tkinter.Button(frame, text="Exit", command=end)
exitButton.grid(row=5, column=1)

# output = tkinter.Label(frame, text="", height=9, width=32, relief="groove", bg="white", wraplength=250)
output = tkinter.Text(frame, height=8, width=30, wrap="word", state="disabled")
output.grid(row=0, column=2, rowspan=6, padx=10, pady=4)

window.mainloop()

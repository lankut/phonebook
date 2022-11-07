import tkinter as tk
from classes.PhoneBook import model
from Interface import size
from classes.PhoneBook import controller

add_window: tk.Tk
change_window: tk.Tk
add_entry: [] = []
change_entry: [] = []

def createAddWindow():
    global add_window
    global add_entry

    RESIZEBLE = False

    add_window = tk.Toplevel()
    # main_window.iconphoto(False, photo)
    add_window.title('Добавить контакт')
    add_window.geometry(size.window_geometry(add_window, size.AWW, size.AWH)) # высчитывает размер текущего экрана и распологает окно справочника по центру
    add_window.resizable(RESIZEBLE, RESIZEBLE) # возможность зафиксировать окно, либо разрешить менять размер окна
    add_window.wm_attributes("-topmost", 1) # поверх остальных окон

    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_label = tk.Label(add_window, text='Имя')
    phone_label = tk.Label(add_window, text='Телефон')
    comment_label = tk.Label(add_window, text='Комментарий')
    name_label.grid(column=0, row=0, sticky='e')
    phone_label.grid(column=0, row=1, sticky='e')
    comment_label.grid(column=0, row=2, sticky='e')

    add_entry = [tk.Entry(add_window, width=30) for _ in range(3)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_window, text='Добавить', command=lambda: add_contact(add_entry))
    add_button.grid(columnspan=2, row=3)

    add_window.mainloop()

def add_contact(add_entry: list):
    global add_window

    model.my_phonebook.add(add_entry[0].get(), add_entry[1].get(), add_entry[2].get())
    controller.refresh_table()
    add_window.destroy()

def change_contact(change_entry: list, contact: list):
    global change_window

    # global add_entry
    model.my_phonebook.set(contact[0], change_entry[0].get(), change_entry[1].get(), change_entry[2].get())
    # contact = (change_entry, change_entry[0].get(), change_entry[1].get(), change_entry[2].get())
    # main_table.insert('', tk.END, values=contact)
    controller.refresh_table()
    change_window.destroy()

def createChangeWindow(contact: list):
    global change_window
    global change_entry

    RESIZEBLE = False

    change_window = tk.Toplevel()
    change_window.title('Изменить контакт')
    change_window.geometry(size.window_geometry(change_window, size.AWW, size.AWH))
    change_window.resizable(RESIZEBLE, RESIZEBLE)
    change_window.wm_attributes("-topmost", 1)

    change_window.columnconfigure(index=0, weight=50)
    change_window.columnconfigure(index=1, weight=250)

    name_label = tk.Label(change_window, text='Имя')
    phone_label = tk.Label(change_window, text='Телефон')
    comment_label = tk.Label(change_window, text='Комментарий')
    name_label.grid(column=0, row=0, sticky='e')
    phone_label.grid(column=0, row=1, sticky='e')
    comment_label.grid(column=0, row=2, sticky='e')

    change_entry = [tk.Entry(change_window, width=30) for _ in range(3)]
    for i, entry in enumerate(change_entry):
        change_entry[i].insert(0, contact[i+1])
        change_entry[i].grid(column=1, row=i)


    change_button = tk.Button(change_window, text='Изменить', command=lambda: change_contact(change_entry, contact))
    change_button.grid(columnspan=2, row=3)

    change_window.mainloop()
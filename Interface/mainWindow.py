import tkinter as tk
from tkinter import ttk
from Interface import size, topWindow
from classes.PhoneBook import controller

main_window: tk.Tk
main_label: tk.Label
add_entry: []
main_table: ttk.Treeview

def main():
    global main_window
    global main_table

    RESIZEBLE = False

    main_window = tk.Tk()
    main_window.title('Телефонный справочник')
    main_window.geometry(size.window_geometry(main_window, size.MWW, size.MWH))
    main_window.resizable(RESIZEBLE, RESIZEBLE)
    main_window.wm_attributes("-topmost", 1)

    menu_bar = tk.Menu(main_window, tearoff=0)
    main_window.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Новая книга', command=controller.new_file)
    file_menu.add_separator()
    file_menu.add_command(label='Открыть', command=controller.open_txt_file)
    file_menu.add_command(label='Сохранить как...', command=controller.save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label='Выйти', command=main_window.destroy)
    menu_bar.add_cascade(label='База данных', menu=file_menu)
    # menu_bar.add_command(label='Помощь')

    main_table = ttk.Treeview(main_window, show='headings')
    heads = ['id', 'Имя', 'Телефон', 'Комментарий']
    main_table['columns'] = heads
    for header in heads:
        main_table.heading(header, text=header, anchor='w')
    main_table.bind('<Button-3>', right_button_menu)

    main_table.pack()

    add_button = tk.Button(main_window, text='Добавить', command=open_add_window)
    add_button.pack()

    main_window.mainloop()


def open_add_window():
    topWindow.createAddWindow()

def right_button_menu(event):
    global main_window
    global main_table

    popup_menu = tk.Menu(main_window, tearoff=0)
    rowID = event.widget.identify('item', event.x, event.y)
    event.widget.focus()
    file_menu = tk.Menu(popup_menu, tearoff=0)
    file_menu.add_command(label='Изменить контакт', command=lambda : controller.change_contact(rowID))
    file_menu.add_separator()
    file_menu.add_command(label='Удалить контакт', command=lambda : controller.delete_contact(rowID))
    file_menu.post(event.x_root, event.y_root)
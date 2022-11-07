import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile
from tkinter import messagebox as mb
import model
from classes import PhoneBook
from Interface import mainWindow, topWindow


# def refresh_table():
#     mainWindow.main_table.delete(*mainWindow.main_table.get_children())
#     for row in model.my_phonebook.show_all():
#         mainWindow.main_table.insert('', 0, values=row)

def refresh_table():
    mainWindow.main_table.delete()
    # mainWindow.main_table.delete(*mainWindow.main_table.get_children())
    for row in model.my_phonebook.show_all():
        mainWindow.main_table.insert('', 0, values=row)

def change_contact(ID: int):
    contact = mainWindow.main_table.item(ID).get('values')
    topWindow.createChangeWindow(contact)

def delete_contact(ID: int):
    contact = mainWindow.main_table.item(ID).get('values')
    if mb.askyesno('Удаление', f'Вы точно хотите удалить контакт {contact[1]}?\n Все несохраненные данные будут утеряны'):
        model.my_phonebook.clear()
        refresh_table()

def new_file():
    if mb.askyesno('Создать новую книгу?', 'Вы точно хотите создать новую книгу?\nВсе несохраненные данные будут утеряны'):
        model.my_phonebook.clear()
        refresh_table()

def open_txt_file():
    types = (("all files", "*.*"),)
    full_file_name = askopenfilename(title='Открыть базу данных', filetypes=types)
    model.my_phonebook.clear()
    with open(full_file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            contact = line.replace('\n', '').replace("'", "").replace('"', '').split(', ')
            model.my_phonebook.add(contact[1], contact[2], contact[3], contact[0])
    refresh_table()


def save_as_file():
    global main_table
    types = (("Текстовый файл", "*.txt"), ("SQLite3 DB file", "*.db"), ("all files", "*.*"))
    full_file_name = asksaveasfilename(title='Сохранить как...', filetypes=types, initialfile='phonebook.txt')
    with open(full_file_name, 'w', encoding='UTF-8') as file:
        data = ''
        for contact in model.my_phonebook.show_all():
            data += str(contact)[1:-1] + '\n'
        file.write(data)
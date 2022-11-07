from classes import Contact

class PhoneBook:
    contact: list = []
    last_id: str = '0'

    def __init__(self):
        pass # это обозначает, что просто пропускаем, нет инициализации

    # def add(self, contact: classes.Contact):
    def add(self, name: str, phone: str, comment: str, id: str = None):
        if id:
            user = Contact.Contact(id, name, phone, comment)
            self.last_id = str(id)
        else:
            user = Contact.Contact(self.last_id, name, phone, comment)
            self.contact.append(user)
            self.last_id = str(int(self.last_id) + 1)

    def remove(self, id: int):
        for (index, user) in enumerate(self.contact):
            if user.id == id:
                self.contact.pop(index)

    def show(self, id: int):
        show_id = None
        for user in self.contact:
            if user.id == str(id):
                show_id = str(id)
                break
        return self.contact[id].show() if show_id else None

    def show_all(self):
        all_items = []
        for user in self.contact:
            all_items.append(user.items())
        return all_items

    def get(self, id: int) -> Contact.Contact: # в классах называются "геттер"
        get_id = None
        for (index, user) in enumerate(self.contact):
            if user.id == id:
                get_id = index
                break
        return self.contact[get_id] if get_id else None

    def set(self, id: int, name: str, phone: str, comment: str): # в классах называются "cеттер"
        for (index, user) in enumerate(self.contact):
            if int(user.id) == id:
                self.contact[index].name = name
                self.contact[index].phone = phone
                self.contact[index].comment = comment

    def search(self, find: str):
        search_list = []
        for user in self.contact:
            for attr in user.items():
                if find in str(attr):
                    search_list.append(user)
        return search_list

    def clear(self):
        self.contact.clear()
        self.last_id = '0'

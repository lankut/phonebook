class Contact:
    id: str = None
    name: str = None
    phone: str = None
    comment: str = None

    def __init__(self, id: str, name: str, phone: str, comment: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

    def items(self):
        return(self.id, self.name, self.phone, self.comment)

    def show(self):
        print (self.id, self.name, self.phone, self.comment)

    def set_name(self, name: str):
        self.name = name

stone = Contact('1', 'Stone', '8908054654', 'Work')
# lankute = Contact('2', 'Evgeni', '2333227743', 'Home', 'Fdfe', 'sfsdfsdf')
lankute = Contact('2', 'Evgeni', '2333227743', 'Home')

# print(lankute.name)
lankute.set_name('IGRUN')
# print(lankute.show())

lankute.second_phone = '297252857'

# print(lankute.second_phone)
from .man import Man
from src.const import FILE_PATH
from src.loader import phonebook


class Phone:
    def __init__(self, name: str = 'Phonebook', phones_list: list = None):
        if phones_list is None:
            self.phones_list = []
        self.name = name
        self.phones_list = phones_list


    def get_contacts(self):
        with open(FILE_PATH, 'r', encoding='utf-8') as men_data:
            for line in men_data:
                line = line.strip().split(";")
                self.phones_list.append(line)


    def add_contact(self, man: Man):
        self.phones_list.append(man)

    def remove_contact(self, man: Man):
        pass

def print_contacts(phonebook):

    result_str = f'Phonebook:\n'
    for line in phonebook.phones_list:
        result_str += f'{line[0]} {line[1]} {line[2]}: {line[3]}'
    return result_str

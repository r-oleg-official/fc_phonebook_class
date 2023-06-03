from data_worker import *
from src import data_worker


def start():

    while True:
        user_input = int(input('\n1. Вывести все контакты.'
                               '\n2. Поиск контакта ...'
                               '\n3. Добавить контакт'
                               '\n4. Изменить контакт'
                               '\n5. Удалить контакт'
                               '\n6. Сохранить в ...'
                               '\n7. Выйти'
                               '\n--> '))

        match user_input:
            case 1:
                data_worker.phonebook.print_contacts()
            case 2:
                # data_edit.search_contact()
                pass
            case 3:
                # data_edit.add_contact()
                pass
            case 4:
                pass
                # data_edit.edit_contacts()
            case 5:
                pass
                # data_edit.del_contacts()
            case 6:
                pass
            case default:
                break

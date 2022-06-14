from datetime import date
import csv

class PhoneBook:
    active_records = list()

    def __init__(self):
        self.__name = str()
        self.__birth_date = date(1999, 1, 20)
        self.__number_phone = list()
        self.__address = list()
        self.__email = list()
        self.__website = list()

    def set_data(self):
        self.__name = input("Enter name: ")
        day, month, year = input("Enter birth data (day/month/year): ").split("/")
        self.__birth_date = date(int(year), int(month), int(day))
        self.__number_phone.append(input("Enter number phone: "))
        self.__address.append(input("Enter address: "))
        self.__email.append(input("Enter email: "))
        self.__website.append(input("Enter website: "))

        record = {'name': self.__name, 'birth_date': self.__birth_date
            , 'number_phone': self.__number_phone, 'address': self.__address
            , 'email': self.__email, 'website': self.__website}

        PhoneBook.active_records.append(record)

    def __str__(self):
        value = ', '.join(self.__number_phone)
        return f'{self.__name} {self.__address} ----> {value}'


class Interface:

    def show_records(self):
        for record in PhoneBook.active_records:
            print(record)

    def add_record(self):
        record = PhoneBook()
        record.set_data()

    def add_number(self):
        temp = int()
        name = input("Enter a name: ")
        for record in PhoneBook.active_records:
            if name == record['name']:
                new_number = input("Enter number: ")
                record['number_phone'].append(new_number)
                break
            else:
                temp = -1
        if temp == -1:
            print("not found!!!")

    def add_address(self):
        temp = int()
        name = input("Enter a name: ")
        for record in PhoneBook.active_records:
            if name == record['name']:
                new_address = input("Enter address: ")
                record['address'].append(new_address)
                break
            else:
                temp = -1
        if temp == -1:
            print("not found!!!")

    def add_email(self):
        temp = int()
        name = input("Enter a name: ")
        for record in PhoneBook.active_records:
            if name == record['name']:
                new_email = input("Enter email: ")
                record['email'].append(new_email)
                break
            else:
                temp = -1
        if temp == -1:
            print("not found!!!")

    def add_website(self):
        temp = int()
        name = input("Enter a name: ")
        for record in PhoneBook.active_records:
            if name in record['name']:
                new_website = input("Enter website: ")
                record['website'].append(new_website)
                break
            else:
                temp = -1
        if temp == -1:
            print("not found!!!")

    def search_by_name(self):
        temp = -1
        key = input("Enter a name: ")
        for record in PhoneBook.active_records:
            if key in record['name']:
                print(record)
                temp = 1
                break

        if temp == -1:
            print("not found!!!")

    def search_by_website(self):
        temp = -1
        key = input("Enter website: ")
        for record in PhoneBook.active_records:
            if key in record['website']:
                print(record)
                temp = 1
                break

        if temp == -1:
            print("not found!!!")

    def search_by_address(self):
        temp = -1
        key = input("Enter address: ")
        for record in PhoneBook.active_records:
            if key in record['address']:
                print(record)
                temp = 1
                break

        if temp == -1:
            print("not found!!!")

    def search_by_email(self):
        temp = -1
        key = input("Enter email: ")
        for record in PhoneBook.active_records:
            if key in record['email']:
                print(record)
                temp = 1
                break

        if temp == -1:
            print("not found!!!")

    def delete_record(self):
        name = input("Enter a name: ")
        records = PhoneBook.active_records
        PhoneBook.active_records = list(filter(lambda record: record['name'] != name, PhoneBook.active_records))
        if records == PhoneBook.active_records:
            print("not found!!!")

    def update_menu(self):
        while True:
            choice = int(
                input("\n1-add a number\n2-add a website\n3-add a address\n4-add a email\n5-goto the menu\n\n"))
            if choice == 1:
                self.add_number()

            elif choice == 2:
                self.add_website()

            elif choice == 3:
                self.add_address()

            elif choice == 4:
                self.add_email()

            elif choice == 5:
                return 0

            else:
                print("wrong input!!!")

    def search_menu(self):
        while True:
            choice = int(
                input("\n1-search by name\n2-search by website\n3-search by address"
                      "\n4-search by email\n5-goto the menu\n\n"))

            if choice == 1:
                self.search_by_name()

            elif choice == 2:
                self.search_by_website()

            elif choice == 3:
                self.search_by_address()

            elif choice == 4:
                self.search_by_email()

            elif choice == 5:
                return 0

            else:
                print("wrong input!!!")

    def menu(self):
        self.load()
        while True:
            choice = int(input("\n1-add record\n2-delete record\n3-show records\n4-update record"
                               "\n5-search\n6-save and exit\n\n"))

            if choice == 1:
                self.add_record()

            elif choice == 2:
                self.delete_record()

            elif choice == 3:
                self.show_records()

            elif choice == 4:
                self.update_menu()

            elif choice == 5:
                self.search_menu()

            elif choice == 6:
                self.save()
                return 0
            else:
                print("wrong input")

    def save(self):
        keys = PhoneBook.active_records[0].keys()
        file = open('data.csv', 'w')
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(PhoneBook.active_records)
        file.close()

    def load(self):
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            PhoneBook.active_records = list(reader)


if __name__ == '__main__':
    inter = Interface()
    inter.menu()

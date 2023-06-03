
class Man:
    def __int__(self, first_name, middle_name, last_name, phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return f"First name: {self.first_name}; \tMiddle name: {self.middle_name}; \tLast name: {self.last_name} " \
               f"\tPhone: {self.phone}."

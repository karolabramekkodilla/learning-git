from BaseContact import BaseContact

class BusinessContact (BaseContact):
    def __init__(self,name, surname, phone_number, email, position, company_name, work_phone_number):
        super().__init__(name, surname, phone_number, email,)
        self.position = position
        self.company_name = company_name
        self.work_phone_number = work_phone_number

    def contact(self):
        print(f"Wybieram numer {self.work_phone_number} i dzwonię do \"{self.name} {self.surname}\"")
    
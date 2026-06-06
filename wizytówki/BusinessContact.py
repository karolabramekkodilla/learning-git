from BaseContact import BaseContact

class BusinessContact (BaseContact):
    def __init__(self, position, company_name, phone_number):
        super().__init__(BaseContact)
        self.position = position
        self.company_name = company_name
        self.phone_number = phone_number
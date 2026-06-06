class BaseContact():
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} - {self.email}"
    
    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do \"{self.name} {self.surname}\"")
    
    @property
    def label_length(self):
        return len(f"{self.name} {self.surname}")
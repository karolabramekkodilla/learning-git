class InfoCard():
    def __init__(self, name, surname, company_name, position, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} - {self.email}"
    
    def contact(self):
        print(f"Kontaktuje się z {self.name} {self.surname} {self.email}")
    
    @property
    def full_name_lenght(self):
        return len(f"{self.name} {self.surname}")
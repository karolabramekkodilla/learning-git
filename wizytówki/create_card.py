from faker import Faker
from BaseContact import BaseContact
from BusinessContact import BusinessContact

fake = Faker("pl_PL")

def create_fake_home_card():
    return BaseContact(
        fake.first_name(),
        fake.last_name(),
        fake.phone_number(),
        fake.email()
    )
def create_fake_buisness_card():
    return BusinessContact(
        fake.first_name(),
        fake.last_name(),
        fake.phone_number(),
        fake.email(),
        fake.job(),
        fake.company(),
        fake.phone_number()
    )
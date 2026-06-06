from faker import Faker
from BaseContact import BaseContact

fake = Faker("pl_PL")

def create_fake_card():
    return BaseContact(
        fake.first_name(),
        fake.last_name(),
        fake.email()
    )
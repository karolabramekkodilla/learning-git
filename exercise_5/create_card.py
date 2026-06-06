from faker import Faker
from InfoCard import InfoCard

fake = Faker("pl_PL")

def create_fake_card():
    return InfoCard(
        fake.first_name(),
        fake.last_name(),
        fake.company(),
        fake.job(),
        fake.email()
    )
from faker import Faker
from create_card import create_fake_home_card,create_fake_buisness_card

def create_contacts(card_type,number_of_cards):
    fake = Faker("pl_Pl")

    if card_type == "business":
        business_cards = []
        for i in range(number_of_cards):
            business_cards.append(create_fake_buisness_card())
        return business_cards
    elif card_type == "home":
        home_cards = []
        for i in range(number_of_cards):
            home_cards.append(create_fake_home_card())
        return home_cards
        
    else:
        print("Niewłaściwy card_type")
        return None
    

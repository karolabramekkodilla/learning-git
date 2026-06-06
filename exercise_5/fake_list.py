from InfoCard import InfoCard
from create_card import create_fake_card

info_card = [
    InfoCard("Nikifor","Wiśniewski","Isaly's","Management consultant","NikiforWisniewski@dayrep.com"),
    InfoCard("Brygida","Zając","Sure Save","Long haul truck driver","BrygidaZajac@armyspy.com"),
    InfoCard("Walenty","Kaczmarek","Quality Realty Service","Radar controller","WalentyKaczmarek@armyspy.com"),
    InfoCard("Stefania","Symanska","Star Merchant Services","Health education specialist","StefaniaSymanska@teleworm.us"),
    InfoCard("Gerwazy","Pawlak","Pender's Food Stores","Farmworker","GerwazyPawlak@teleworm.us"),
]

for item in info_card:
    print(item)
info_card2 = []
for i in range(5):
    info_card2.append(create_fake_card())

print()
for item in info_card2:
    print(item)

cards_sorted_by_name = sorted(info_card2, key=lambda info_card: info_card.name)
print(cards_sorted_by_name)
for i in cards_sorted_by_name:
    print(i)

cards_sorted_by_surname = sorted(info_card2, key=lambda info_card: info_card.surname)
print(cards_sorted_by_surname)
for i in cards_sorted_by_surname:
    print(i)

cards_sorted_by_email = sorted(info_card2, key=lambda info_card: info_card.email)
print(cards_sorted_by_email)
for i in cards_sorted_by_email:
    print(i)
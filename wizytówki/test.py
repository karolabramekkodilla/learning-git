from create_contacts import create_contacts
print("Kontakty do home")
contacts = create_contacts("home", 5)
for contact in contacts:
    print(contact)
    print(contact.label_length)
    contact.contact()
print("Kontakty do job")
contacts = create_contacts("business", 5)
for contact in contacts:
    print(contact)
    print(contact.label_length)
    contact.contact()
class Contact:
    def __init__(self,name,phone_number,email,address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def add_contact(self):
        self.contact_display()

    def search(self,name):
        if name == self.name:
            self.contact_display()
        else:
            print("Contact not found")

    def update(self,new_name=None,new_phone_number=None,new_email=None,new_address=None):
        if new_name:
            self.name = new_name

        if new_phone_number:
            self.phone_number = new_phone_number

        if new_email:
            self.email = new_email
        if new_address:
            self.address = new_address 
        print("Contact updated successfully")               

    def delete(self):
        self.name = None
        self.phone_number = None
        self.email = None
        self.address = None
        print("Contact deleted")

    def contact_display(self):
        if self.name is None:
            print("Contact not exist")
        print("\nCONTACT DETAILS")    
        print("contact name = ",self.name)
        print("phone number = ",self.phone_number)
        print("Email = ",self.email)
        print("Address = ",self.address)

c1 = Contact('Rajesh',9076526272,'rajesh123@gmail.com','saharanpur')
c1.contact_display()
c1.update('pradeep','Delhi')



                
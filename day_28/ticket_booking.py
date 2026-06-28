class Ticket:
    def __init__(self,ticket_id,passanger_name,source,destination,total_seats,seat_number,ticket_price):
        self.ticket_id = ticket_id
        self.passanger_name = passanger_name
        self.source = source
        self.destination = destination
        self.seat_number = seat_number
        self.ticket_price = ticket_price
        self.total_seats = total_seats
        self.is_booked = False

    def booking(self):
        if self.total_seats>0:
            self.total_seats-=1
            self.is_booked = True
            print("Seat booked")
        else:
            print("NO seat availabe")

    def cancel(self):
        if self.is_booked:
            self.total_seats+=1
            self.is_booked = False
            print("seat is cancelled !!")

    

    def book_status(self):
        if self.is_booked:
            return 'ticket booked / seat confired'
        
        return 'ticket cancelled'    

    def passanger_details(self):
        print("ticket id = ",self.ticket_id)
        print("passanger name = ",self.passanger_name)
        print("source from where to go = ",self.source)
        print("destination where to go = ",self.destination)
        print("Price of ticket = ",self.ticket_price)
        print("seat alloted = ",self.seat_number)
        print("ticket status = ",self.book_status())

t1 = Ticket(101,'shreyansh',' Greater Noida-Zero point','Gorakhpur',65,34,5000,)
t1.book_status()
print("*"*30)
t1.passanger_details()        






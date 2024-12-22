from tkinter import *
from tk_objects import DropDown, Table
import server


class BookingApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Bookings)')
        self.root.geometry('1080x720')
        
        self.title = Label(self.root, text='Bookings Table', font=('Arial', 20, 'bold', 'underline'))
        self.title.pack()
        
        self.booking_attr = ('bookingID', 'customerID', 'booking_date', 'status', 'tourID', 'staffID')
        self.booking_table = Table(self.root, self.booking_attr, server.selectTable('booking'))
        self.booking_table.frame.pack(side='top')
        self.current_booking =  len(server.selectTable('booking'))

    def run(self):
        self.root.mainloop()
        
from tkinter import *
from tk_objects import DropDown, Table
import server


class FlightApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Flights)')
        self.root.geometry('1080x720')
        
        self.flight_attr = ('flightID', 'name', 'dep_airport', 'dep_time', 'arr_airport', 'arr_time')
        self.flight_table = Table(self.root, self.flight_attr, server.selectTable('flight'))
        self.flight_table.frame.pack(side='top')
        self.current_flight=  len(server.selectTable('flight'))

    def run(self):
        self.root.mainloop()
        
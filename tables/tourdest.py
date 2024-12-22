from tkinter import *
from tk_objects import DropDown, Table
import server


class TourDestApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Tour Destinations)')
        self.root.geometry('1080x720')
        
        self.tour_dest_attr = ('tourID','destID')
        self.tour_dest_table = Table(self.root, self.tour_dest_attr, server.selectTable('tourdest'))
        self.tour_dest_table.frame.pack(side='top')
        self.current_tour_dest =  len(server.selectTable('tourdest'))

        self.tourid_label = Label(self.root, text="Tour ID")
        self.tourid_label.pack()
        self.tourid_input = Entry(self.root)
        self.tourid_input.pack()
        self.destid_label = Label(self.root, text="Dest ID")
        self.destid_label.pack()
        self.destid_input = Entry(self.root)
        self.destid_input.pack()

        self.add_btn = Button(self.root, text="Add", width=10, command=self.updateTourDest)
        self.add_btn.pack()


    def updateTourDest(self):
        tourID = self.tourid_input.get()
        destID = self.destid_input.get()
        server.addTourDest(tourID, destID)

    def refreshTable(self):
        updated_data = server.selectTable('tourdest')
        self.tour_dest_table.update_data(updated_data)  # Ensure Table has this 


    def run(self):
        self.root.mainloop()
    
    

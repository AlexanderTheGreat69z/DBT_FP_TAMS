from tkinter import *
from tk_objects import DropDown, Table
import server


class DestinationApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Destinations)')
        self.root.geometry('1080x720')
        
        self.title = Label(self.root, text='Destinations Table', font=('Arial', 20, 'bold', 'underline'))
        self.title.pack()
        
        self.dest_attr = ('destID', 'name', 'country', 'address', 'dest_desc')
        self.dest_table = Table(self.root, self.dest_attr, server.selectTable('destination'))
        self.dest_table.frame.pack(side='top')
        self.current_dest=  len(server.selectTable('destination'))


        self.destid_label = Label(self.root, text="Dest ID")
        self.destid_label.pack()
        self.destid_input = Entry(self.root)     
        self.destid_input.pack()

        self.name_label = Label(self.root, text="Name")
        self.name_label.pack()
        self.name_input = Entry(self.root)
        self.name_input.pack()

        self.country_label = Label(self.root, text="Country")
        self.country_label.pack()
        self.country_input = Entry(self.root)
        self.country_input.pack()

        self.address_label = Label(self.root, text="Address")
        self.address_label.pack()
        self.address_input = Entry(self.root)
        self.address_input.pack()

        self.desc_label = Label(self.root, text="Description")
        self.desc_label.pack()
        self.desc_input = Entry(self.root)
        self.desc_input.pack()    


        self.add_btn = Button(self.root, text="Add", width=10, command=self.updateDestination)
        self.add_btn.pack()

    def updateDestination(self):
        destID = self.destid_input.get()
        name = self.name_input.get()
        country = self.country_input.get()
        address = self.address_input.get()
        desc = self.desc_input.get()
        server.addDestination(destID, name, country, address, desc)

    def refreshTable(self):
        updated_data = server.selectTable('Destination')
        self.dest_table.update_data(updated_data)  


    def run(self):
        self.root.mainloop()
        

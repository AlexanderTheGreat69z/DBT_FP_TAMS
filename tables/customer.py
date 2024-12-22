from tkinter import *
from tk_objects import DropDown, Table
import server



class CustomerApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Customer)')
        self.root.geometry('1080x720')
        
        self.title = Label(self.root, text='Customers Table', font=('Arial', 20, 'bold', 'underline'))
        self.title.pack()
        
        self.customers_attr = ('customerID', 'fname', 'lname', 'email', 'phoneNo', 'sex', 'DOB', 'ppNo')
        self.customers_table = Table(self.root, self.customers_attr, server.selectTable('customer'))
        self.customers_table.frame.pack(side='top')
        self.current_customers =  len(server.selectTable('customer'))

    def run(self):
        self.root.mainloop()
        
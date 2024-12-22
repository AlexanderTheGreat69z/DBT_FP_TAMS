from tkinter import *
from tk_objects import DropDown, Table
import server


class StaffApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Staffs)')
        self.root.geometry('1080x720')
        
        self.title = Label(self.root, text='Staffs Table', font=('Arial', 20, 'bold', 'underline'))
        self.title.pack()
        
        self.staffs_attr = ('staffID', 'fname', 'lname', 'email', 'phoneNo', 'sex', 'salary')
        self.staffs_table = Table(self.root, self.staffs_attr, server.selectTable('staff'))
        self.staffs_table.frame.pack(side='top')
        self.current_staffs =  len(server.selectTable('staff'))
        
        self.control_panel = Frame(self.root)
        self.control_panel.rowconfigure(0, weight=3)
        
        ###########################################
        self.country_sel  = Frame(self.control_panel)
        self.options = [val[0] for val in server.selectTable('staff')]
        self.label  = Label(self.country_sel, text='Select Staff')
        self.label.pack()
        self.dd     = DropDown(self.country_sel, self.options) 
        self.dd.pack()
        
        self.salary_setting = Frame(self.control_panel)
        self.salary_button = Button(self.salary_setting, text='Update Salary', width=10, command=self.updateSalary)
        self.salary_button.grid(row=0, column=0)
        self.salary_input = Entry(self.salary_setting)
        self.salary_input.grid(row=0, column=1)
        self.salary_setting.pack()
        
        self.fire_button = Button(self.country_sel, text='Fire', width=10, command=self.fireStaff)
        self.fire_button.pack()
        self.country_sel.pack()
        ###########################################
        
        self.hire_staff_panel  = Frame(self.control_panel)
        
        self.name_label = Label(self.hire_staff_panel)
        self.name_label.grid(row=0, column=0)
        
        self.name_panel = Frame(self.hire_staff_panel)
        self.name_panel.rowconfigure(0, weight=2)
        
        self.fname_panel = Entry(self.name_panel)
        self.fname_panel.grid(row=0, column=0)
        self.lname_panel = Entry(self.name_panel)
        self.lname_panel.grid(row=0, column=1)
        
        self.name_panel.grid(row=1, column=0)
        
        self.details_panel = Frame(self.hire_staff_panel)
        self.email_panel = Entry(self.details_panel)
        self.email_panel.grid(row=0, column=0)
        self.phoneNo_panel = Entry(self.details_panel)
        self.phoneNo_panel.grid(row=0, column=1)
        self.details_panel.grid(row=2, column=0)
        
        self.hire_button = Button(self.hire_staff_panel, text='Hire', width=10, command=self.hireStaff)
        self.hire_button.grid(row=3, column=0)
        self.hire_staff_panel.pack()
        
        
        self.control_panel.pack(pady=10)
    
    def updateTable(self):
        self.staffs_table.frame.destroy()
        self.staffs_table = Table(self.root, self.staffs_attr, server.selectTable('staff'))
        self.staffs_table.frame.pack(side='top')
        self.current_staffs =  len(server.selectTable('staff'))
        
        self.options = [val[0]  for val in server.selectTable('staff')]
        self.dd.destroy()
        self.dd     = DropDown(self.country_sel, self.options) 
        self.dd.pack()
        
    def hireStaff(self):
        staffID = f'STAFF0000{self.current_staffs + 1}'
        fname, lname = self.fname_panel.get(), self.lname_panel.get()
        email, phoneNo = self.email_panel.get(), self.phoneNo_panel.get()
        server.hireStaff(staffID, fname, lname, email, phoneNo, 'M', 100000000)
        self.updateTable()
        
    
    def fireStaff(self):
        staffID = self.dd.getSelected()
        server.fireStaff(staffID)
        
    def updateSalary(self):
        staffID = self.dd.getSelected()
        salary  = self.salary_input.get()
        
        server.setStaffSalary(staffID, salary)
        self.updateTable()
    def run(self):
        self.root.mainloop()
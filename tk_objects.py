from tkinter import *

class DropDown(OptionMenu):
    def __init__ (self, root, choices:list):
        self.root = root
        self.clicked = StringVar()
        self.clicked.set(choices[0])
        super().__init__(self.root, self.clicked, *choices)
    
    def getSelected(self): return self.clicked.get()
    
    def updateChoices(self, choices:list):
        self.clicked.set(choices[0])
        super().__init__(self.root, self.clicked, *choices)
        
    def getSelected(self):
        return self.clicked.get()
    
class Table:
    def __init__(self, root, attributes:tuple, values:list=None):
        self.root = root
        self.attributes = attributes
        self.values = values
        self.combined = self.values.copy()
        self.combined.insert(0, self.attributes)
        
        self.dataframe =  {}
        self.__loadDataframe()
        
        self.frame = Frame(self.root)
        self.__loadTable()
                
    def __loadDataframe(self):
        for i in range(len(self.attributes)):
            for j in range(len(self.values)):
                self.dataframe[self.attributes[i]] = self.values[j][i]
        
    def __loadTable(self):
        for i in range(len(self.values)+1):
            row = Frame(self.frame)
            row.rowconfigure(i)
            for j in range(len(self.attributes)):
                cell = Label(
                    self.frame, 
                    text = self.combined[i][j], 
                    width = 12,
                    height = 1,
                    borderwidth=3, 
                    relief='ridge',
                    )
                cell.grid(row=i, column=j, sticky='news')
            row.grid(row=i)
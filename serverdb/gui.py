import tkinter
from tkinter import ttk

class querier(ttk.Frame):
    """The db querier gui and functions"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
   
    def init_pass(self):
        self.username = "historycard"
        

    def init_gui(self):
        """builds initial gui for db commit"""
        self.root.title('Server History Card Viewer')
        self.root.option_add('*tearOff', 'FALSE')
        
        self.root.wm_attributes('-zoomed', True)
        
        self.grid(column=0, row=0, sticky='nsew')
        
        self.menubar = tkinter.Menu(self.root)
        
        self.menu_file = tkinter.Menu(self, menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)
        self.menu_file.add_command(label='View', command=self.view
        





if __name__ == '__main__':
    root = tkinter.Tk()
    querier(root)
    root.mainloop()

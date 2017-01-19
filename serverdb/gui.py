import tkinter
from tkinter import ttk, messagebox

class querier(ttk.Frame):
    """The db querier gui and functions"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def init_pass(self):
        self.username = "historycard"
        self.password = "pstar"

    def init_gui(self):
        """builds initial gui for db commit"""
        self.root.title('Server History Card Viewer')
        self.root.option_add('*tearOff', 'FALSE')

        self.root.wm_attributes('-zoomed', True)

        self.grid(column=0, row=0, sticky='nsew')

        self.menubar = tkinter.Menu(self.root)

        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)

        self.menu_edit = tkinter.Menu(self.menubar)
        self.menu_edit.add_command(label='View', command=self.view)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

    def on_quit(self):
        temp = tkinter.messagebox.askokcancel("Server History Viewer", "Are you sure you want to quit?")
        print(temp)
        if (temp == 1):
            quit()
        else:
            pass
    def view(self):
        hfh






if __name__ == '__main__':
    root = tkinter.Tk()
    querier(root)
    root.mainloop()

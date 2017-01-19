import tkinter
from tkinter import ttk, messagebox

class Querier(ttk.Frame):
    """The db querier gui and functions"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
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

    def on_quit():
        """on quit func"""
        temp = messagebox.askokcancel("Server History Viewer", "Are you sure you want to quit?")
        print(temp)
        if (temp == 1):
            quit()
        else:
            pass
    def view(self):
        hfh

    def get_hostname():
        hostbox = tkinter.Toplevel(root)
        hostbox.title('Host Name')
        label1 = Label(hostbox, text="Enter your host name")
        label1.grid(column=1, row=0)
        entry1 = tkinter.Entry(hostbox)
        entry1.grid(column=2, row=0, columnspan=2)
        but1 = tkinter.Button(hostbox, text="OK", command=get)
        but1.grid(column=2, row=1)
        def getter():
            ip = str(entry1.get())
            return ip
        return ip




if __name__ == '__main__':
    root = tkinter.Tk()
    querier(root)
    root.mainloop()

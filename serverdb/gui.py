import tkinter, logging
from tkinter import ttk, messagebox, showerror

def excepts_handle(arg):
    """show's fatal box and quits"""
    tkmessagebox.showerror("Fatal", "%s" % arg)
    quit()

def new():
    sdf

def on_quit():
    """on quit func"""
    temp = messagebox.askokcancel("Server History Viewer", "Are you sure you want to quit?")
    print(temp)
    if (temp == 1):
        quit()
    else:
        pass
def view():
    """dialog box for lookup"""
    def gets():
        """retrieves data"""
        logging.debug('getting vars')
        cn_get = str(entry1.get()).lower()
        pn_get = str(entry2.get()).lower()
        sn_get = str(entry3.get()).lower()
        logging.debug('closing window')
        viewvar.destroy()
        logging.debug('returning data to parent window')
        return (cn_get, pn_get, sn_get)
    logging.debug('building window')
    viewvar = tkinter.Toplevel(root)
    viewvar.title('Machine lookup')
    label1 = tkinter.Label(viewvar, text="Company Name  ")
    label1.grid(column=0, row=0, sticky='wns')
    label2 = tkinter.Label(viewvar, text="Plant Name    ")
    label2.grid(column=0, row=1, sticky='wns')
    label3 = tkinter.Label(viewvar, text="Serial Number ")
    label3.grid(column=0, row=2, sticky='wns')
    entry1 = tkinter.Entry(viewvar)
    entry1.grid(column=1, row=0, columnspan=3, sticky='ns')
    entry2 = tkinter.Entry(viewvar)
    entry2.grid(column=1, row=1, columnspan=3, sticky='ns')
    entry3 = tkinter.Entry(viewvar)
    entry3.grid(column=1, row=2, columnspan=3, sticky='ns')
    but1 = tkinter.Button(viewvar, text="OK", command=gets)
    but1.grid(column=2, row=3, sticky='ens')
    for child in viewvar.winfo_children():
        child.grid_configure(padx=5, pady=5)
    logging.debug('returning data to main')
    return gets

def get_hostname():
    """dialog box for hostname"""
    try:
        def gets():
            """retrieves data"""
            logging.debug('getting ip entry')
            ip_get = str(entry1.get()).lower()
            logging.debug('closing window')
            hostbox.destroy()
            logging.debug('returning data to parent window')
            return ip_get
        logging.debug('building window')
        hostbox = tkinter.Toplevel(root)
        hostbox.title('Host Name')
        label1 = Label(hostbox, text="Enter your host name")
        label1.grid(column=0, row=0)
        entry1 = tkinter.Entry(hostbox)
        entry1.grid(column=1, row=0, columnspan=2)
        but1 = tkinter.Button(hostbox, text="OK", command=gets)
        but1.grid(column=2, row=1, sticky='w')
        for child in hostbox.winfo_children():
            child.grid_configure(padx=5, pady=5)
        logging.debug('returning data to main')
        return gets
    except * as excepts:
        logging.fatal('Something went wrong with the hostname dialog %s') % (excepts)
        excepts_handle(excepts)

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
        self.menu_file.add_command(label='New', command=new)
        self.menu_file.add_command(label='View', command=view)
        self.menu_file.add_command(label='Exit', command=on_quit)
        

        self.menu_edit = tkinter.Menu(self.menubar)
        self.menu_edit.add_command(label='Reset', command=resetvars)
        

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

    
        




if __name__ == '__main__':
    root = tkinter.Tk()
    Querier(root)
    root.mainloop()

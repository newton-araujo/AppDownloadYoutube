import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class App:
    def __init__(self,root):
        self.root = root
        self.root.title("DOWNLOAD YOUTUBE")
        self.root.geometry("700x600")
        
        #Config grid
        #column
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
        self.root.columnconfigure(2,weight=1)
        #Row
        self.root.rowconfigure(0,weight=1)
        self.root.rowconfigure(1,weight=1)
        self.root.rowconfigure(2,weight=1)
        self.root.rowconfigure(3,weight=1)
        self.root.rowconfigure(4,weight=1)
        
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20,pady=20)
        
        #Title page
        self.lb_title = ttk.Label(self.frame,text="DOWNLOAD YOUTUBE", font=("MS Serif",20))
        self.lb_title.grid(column=1,row=1,padx=10,pady=50)
        
        #Open file
        self.lb_file = ttk.Label(self.frame, text="File", font=("MS Serif",16))
        self.lb_file.grid(column=0, row=2,padx=10,pady=10)
        self.entre_file = ttk.Entry(self.frame,width=60)
        self.entre_file.grid(column=1,row=2,padx=10,pady=10)
        self.btn_file = ttk.Button(self.frame, text="Open File",padding=5)
        self.btn_file.grid(column=2,row=2)
        
        
        

if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = App(root)
    root.mainloop()
#from tkinter.ttk import Notebook,Style


class project_Menu:

    def __init__(self,master = None,notebook = None):
        self.root = master
        self.note = notebook

    def draw(self):
        from tkinter import Canvas,Button,Label
        from PIL import ImageTk,Image
        w,h = self.root.winfo_screenwidth(),self.root.winfo_screenheight()
#        if w == 1536 and h == 864:
#            self.op_menu = "source\\land15.jpg"
#        elif w == 1366 and h == 768:
#            self.op_menu = "source\\land13.jpg"
#        elif w>1920 and h>1080:
#            self.op_menu = "source\\land19.jpg"
#        else:
#            self.op_menu = "source\\land13.jpg"
        self.op_menu = "source\\land19.jpg"
        self.can = Canvas(self.note,border=0,highlightthickness=0)#,width=1000,height=1000)
        self.can.pack(fill="both",expand=1)

        self.x = ImageTk.PhotoImage(Image.open(self.op_menu).resize((w,h)))
        self.can.create_image(0,0,anchor="nw",image=self.x)
        self.label = Label(self.can,text="Welcome!",bg="#333",fg="white",font=(None,32))
        self.label.pack(fill="x")

        #ex = Button(can,width=0,text='EXIT',bg="#333",font="None ",command=root.destroy)
        #ex.place(x=root.winfo_screenwidth()-ex.winfo_reqwidth(),y=0)#.pack(anchor=NE)


        # ______________________ BASIC ____________________________
        # canvas at-->> can, Tk() at -->> root
        self.xby4 = round(self.root.winfo_reqwidth()//0.8)#260
        self.yby4 = round(self.root.winfo_reqheight()//1.7)#120

        self.bil = ImageTk.PhotoImage(Image.open("source\\BillingRect.png").resize((self.xby4,self.yby4)))
        self.cus = ImageTk.PhotoImage(Image.open("source\\CustomerRect.png").resize((self.xby4,self.yby4)))
        self.emp = ImageTk.PhotoImage(Image.open("source\\EmpRect.png").resize((self.xby4,self.yby4)))
        self.sto = ImageTk.PhotoImage(Image.open("source\\StocksRect.png").resize((self.xby4,self.yby4)))
        self.log = ImageTk.PhotoImage(Image.open("source\\LogoutRect.png").resize((self.xby4,self.yby4)))
        self.qui = ImageTk.PhotoImage(Image.open("source\\QuitRect.png").resize((self.xby4,self.yby4)))
#        self.men = ImageTk.PhotoImage(Image.open("source\\MenuRect.png").resize((self.xby4,self.yby4)))

        #fr = LabelFrame(can,border=0,highlightthickness=0,bg="orange",padx=20,pady=20)
        #fr.pack(expand=1)
        #re = 1E gr = 3D bl = 7E

        self.customer = Button(self.can,image=self.cus,border=0,highlightthickness=0,relief="flat")
        self.customer.place(relx=0.25,rely=0.25)

        self.bill = Button(self.can,image=self.bil ,border=0,highlightthickness=0,relief="flat")
        self.bill.place(relx=0.55,rely=0.25)

        self.employee = Button(self.can,image=self.emp ,border=0,highlightthickness=0,relief="flat")
        self.employee.place(relx=0.25,rely=0.45)

        self.logout = Button(self.can,image=self.log ,border=0,highlightthickness=0,relief="flat")
        self.logout.place(relx=0.25,rely=0.65)

        self.stock = Button(self.can,image=self.sto ,border=0,highlightthickness=0,relief="flat")
        self.stock.place(relx=0.55,rely=0.45)

        self.quit = Button(self.can,image=self.qui ,border=0,highlightthickness=0,relief="flat",
		command=self.root.destroy)
        self.quit.place(relx=0.55,rely=0.65)

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    root.attributes("-fullscreen",True)
    a = project_Menu(master=root)
    a.draw()
    root.mainloop()

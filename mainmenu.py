class project_Menu:

    def __init__(self,master =None,notebook =None):
        self.root = master
        self.note = notebook

    def draw(self):
        from tkinter import Canvas,Button
        from PIL import ImageTk,Image

        w,h = self.root.winfo_screenwidth(),self.root.winfo_screenheight()

        op_menu = "source\\back.png"
        self.can = Canvas(self.note,border=0,highlightthickness=0)
        self.can.pack(fill="both",expand=1)

        self.x = ImageTk.PhotoImage(Image.open(op_menu).resize((w,h)))
        self.can.create_image(0,0,anchor="nw",image=self.x)
        
        siz_210 = round(w//6.504)
        self.cust_img = ImageTk.PhotoImage(Image.open("Buttons\cust420x210.png").resize((siz_210,siz_210)))
        
        self.emp_img = ImageTk.PhotoImage(Image.open("Buttons\emp210x210.png").resize((siz_210,round(h//3.764))))
        
        self.bill_img = ImageTk.PhotoImage(Image.open("Buttons/bill420x210.png").resize((round(w//3.176),siz_210)))
        
        self.log_img = ImageTk.PhotoImage(Image.open("Buttons\log210x210.png").resize((round(w//6.383),round(h//3.764))))
        
        self.stock_img = ImageTk.PhotoImage(Image.open("Buttons\stock210x420.png").resize((siz_210,round(h//1.828))))
        
        self.quit_img = ImageTk.PhotoImage(Image.open("Buttons\quit420x210.png").resize((round(w//3.176),siz_210)))
        

        self.butt_cust = Button(self.can,border=0,highlightthickness=0, image = self.cust_img)
        self.butt_cust.place(relx=0.49 , rely= 0.078)
        
        self.butt_emp = Button(self.can,border=0,highlightthickness=0, image = self.emp_img)
        
        self.butt_bill = Button(self.can,border=0,highlightthickness=0, image = self.bill_img)
        
        self.butt_log = Button(self.can,border=0,highlightthickness=0, image = self.log_img)
        
        self.butt_stock = Button(self.can,border=0,highlightthickness=0, image = self.stock_img)
        
        self.butt_quit = Button(self.can,border=0,highlightthickness=0, image = self.quit_img,command=self.root.destroy)        


        self.butt_bill.place(relx=0.647,rely=0.078)
        self.butt_emp.place(relx=0.49,rely=0.36)
        self.butt_log.place(relx=0.647,rely=0.36)
        self.butt_stock.place(relx=0.808,rely=0.36)
        self.butt_quit.place(relx=0.49,rely=0.632)


if __name__ =="__main__":
  from tkinter import Tk
  root = Tk()
  root.attributes("-fullscreen",True)
  a = project_Menu(root,root)
  a.draw()
  root.mainloop()

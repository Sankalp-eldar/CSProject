from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.attributes("-fullscreen", True)

# butt_holder = LabelFrame(root, borderwidth = 0, highlightthickness = 0)


background_img = ImageTk.PhotoImage(Image.open("back.png"))
background_canv = Canvas(root, width = 1366, height = 768)

background_canv.create_image(0, 0, anchor = NW, image = background_img)
background_canv.pack()




# button images
cust_img = ImageTk.PhotoImage(Image.open("Buttons\cust420x210.png"))
emp_img = ImageTk.PhotoImage(Image.open("Buttons\emp210x210.png"))
bill_img = ImageTk.PhotoImage(Image.open("Buttons/bill420x210.png"))
stock_img = ImageTk.PhotoImage(Image.open("Buttons\stock210x420.png"))
quit_img = ImageTk.PhotoImage(Image.open("Buttons\quit420x210.png"))
log_img = ImageTk.PhotoImage(Image.open("Buttons\log210x210.png"))

butt_bill = Button(background_canv, image = bill_img, highlight = None, relief = FLAT, height = 204, width = 424)
butt_cust = Button(background_canv, image = cust_img, highlight = None, relief = FLAT, height = 204, width = 204, highlightthickness = 0)
butt_log = Button(background_canv, image = log_img, highlight = None, relief = FLAT, height = 204, width = 208, highlightthickness = 0)
butt_emp = Button(background_canv, image = emp_img, highlight = None, relief = FLAT, height = 204, width = 204, highlightthickness = 0)
butt_quit = Button(background_canv, image = quit_img, highlight = None, relief = FLAT, height = 204, width = 424, command = root.destroy, highlightthickness = 0)
butt_stock = Button(background_canv, image = stock_img, highlight = None, relief = FLAT, width = 204, height = 419, highlightthickness = 0)


# butt_cust.grid(column = 0,row = 0, padx = 1, pady = 1)
# butt_bill.grid(column = 1,row = 0, columnspan = 2 , padx = 1, pady = 1)
# butt_emp.grid(column = 0, row = 1, pady = 1)
# butt_log.grid(column = 1,row = 1, padx = 1, pady = 1)
# butt_stock.grid(column = 2, row  = 1, rowspan = 2, padx = 1, pady = 1)
# butt_quit.grid(column = 0,row = 2, columnspan = 2, padx = 1, pady = 1)

# butt_holder.place(x = 650, y = 60)
# background_label.place(x=0, y=0)
# butt_holder.lift()
butt_cust.place(x = 670, y = 60)
butt_bill.place(x = 885, y = 60)
butt_emp.place(x = 670 , y = 275)
butt_log.place(x = 885, y = 275)
butt_stock.place(x =1105 , y = 275)
butt_quit.place(x = 670, y = 490)



butt_bill.focus_set()



root.mainloop()

# Hare Krishna
from tkinter import *
import tkinter.messagebox
import random

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1400x700+70+50')
        self.root.maxsize(width=1350, height=685)
        self.root.minsize(width=1350, height=685)
        self.root.title('Biling Software')

        # ================== Variables ===================

        self.cus_name = StringVar()
        self.cus_phone = StringVar()
        self.cus_bill_no = StringVar()

        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()

        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()

        self.mango = IntVar()
        self.nimka = IntVar()
        self.soda = IntVar()
        self.biscuit = IntVar()
        self.lassi = IntVar()

        self.total_cosmetics = IntVar()
        self.total_grocery = IntVar()
        self.total_other = IntVar()
        self.cos_tax = IntVar()
        self.gro_tax = IntVar()
        self.other_tax = IntVar()

        # ============================

        bg_color = '#074463'
        fg_color = 'white'
        lbl_color = 'white'

        # ================= Title of App ==================
        title = Label(self.root, text='Billing Software', bd=12, relief=GROOVE, fg=fg_color, bg=bg_color, font=('times new roman', 30, 'bold'), pady=3).pack(fill=X)

        # ================= Customer Frame =================
        f1 = LabelFrame(text='Customer Details', font=('times new roman', 12, 'bold'), fg='gold', bg=bg_color, relief=GROOVE, bd=10)
        f1.place(x=0, y=71, relwidth=1)
        
        # Customer Name
        cname_lbl = Label(f1, text='Customer Name', bg=bg_color, fg=fg_color, font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(f1, bd=8, relief=GROOVE, textvariable = self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # Customer Phone
        cphone_lbl = Label(f1, text='Phone No. ', bg=bg_color, fg=fg_color, font=('times new roman', 15, 'bold')).grid(row=0, column=2, padx=20)
        cphone_en = Entry(f1, bd=8, relief=GROOVE, textvariable=self.cus_phone)
        cphone_en.grid(row=0, column=3, ipadx=30, ipady=4, pady=5)

        # Customer Bill No
        cbill_lbl = Label(f1, text='Bill No.', bg=bg_color, fg=fg_color, font=('times new roman', 15, 'bold'))
        cbill_lbl.grid(row=0, column=4, padx= 20)
        cbill_en = Entry(f1, bd=8, relief=GROOVE, textvariable=self.cus_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # Bill Search Button
        bill_btn = Button(f1, text='Enter', bd=7, relief=GROOVE, font=('times new roman', 12, 'bold'), bg=bg_color, fg=fg_color)
        bill_btn.grid(row=0, column=6, ipadx=19, padx=60, ipady=5, pady=5)

        # ================== Cosmetics Frame =======================

        f2 = LabelFrame(self.root, text='Cosmetics', bd=10, relief=GROOVE, bg=bg_color, fg='gold', font=('times new roman', 13, 'bold'))
        f2.place(x=0, y=165, width=350, height=380)

        # frame content

        bath_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Bath Soap (Rs.15)')
        bath_lbl.grid(row=0, column=0, padx=3, pady=20, sticky=W)
        bath_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.bath_soap)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # face cream

        face_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Face Cream (Rs.30)')
        face_lbl.grid(row=1, column=0, padx=3, pady=20)
        face_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.face_cream)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # face wash

        wash_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Face Wash (Rs.25)')
        wash_lbl.grid(row=2, column=0, padx=3, pady=20)
        wash_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.face_wash)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # Hair Spray

        hair_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Hair Spray (Rs.35)')
        hair_lbl.grid(row=3, column=0, padx=3, pady=20)
        hair_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.hair_spray)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # Body Lotion

        lotion_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Body Lotion (Rs.50)')
        lotion_lbl.grid(row=4, column=0, padx=3, pady=20)
        lotion_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.body_lotion)
        lotion_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ============================ Grocery Content ============================

        f2 = LabelFrame(self.root, text='Grocery',bd=10, relief=GROOVE, bg=bg_color, fg='gold', font=('times new roman', 13, 'bold'))
        f2.place(x=350, y=165, width=350, height=380)

        # Frame Content

        rice_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Rice (Rs.60/kg)')
        rice_lbl.grid(row=0, column=0, padx=3, pady=20)
        rice_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

        oil_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Food Oil (Rs.70/lit)')
        oil_lbl.grid(row=1, column=0, padx=3, pady=20)
        oil_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.oil)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        daal_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Daal (Rs.85/kg)')
        daal_lbl.grid(row=2, column=0, padx=3, pady=20)
        daal_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.daal)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        wheat_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Wheat (Rs.45/kg)')
        wheat_lbl.grid(row=3, column=0, padx=3, pady=20)
        wheat_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        sugar_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Sugar (Rs.30/kg)')
        sugar_lbl.grid(row=4, column=0, padx=3, pady=20)
        sugar_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.sugar)
        sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ============================ Others ============================

        f2 = LabelFrame(self.root, text='Others',bd=10, relief=GROOVE, bg=bg_color, fg='gold', font=('times new roman', 13, 'bold'))
        f2.place(x=700, y=165, width=350, height=380)

        # Frame Content

        mango_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Mango Juice(Rs.30)')
        mango_lbl.grid(row=0, column=0, padx=3, pady=20)
        mango_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.mango)
        mango_en.grid(row=0, column=1, ipady=5, ipadx=5)

        soda_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Soda(Rs.20)')
        soda_lbl.grid(row=1, column=0, padx=3, pady=20)
        soda_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.soda)
        soda_en.grid(row=1, column=1, ipady=5, ipadx=5)

        nimka_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Nimka(Rs.25)')
        nimka_lbl.grid(row=2, column=0, padx=3, pady=20)
        nimka_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.nimka)
        nimka_en.grid(row=2, column=1, ipady=5, ipadx=5)

        biscuit_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Biscuit(Rs.10)')
        biscuit_lbl.grid(row=3, column=0, padx=3, pady=20)
        biscuit_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.biscuit)
        biscuit_en.grid(row=3, column=1, ipady=5, ipadx=5)

        lassi_lbl = Label(f2, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Lassi(Rs.15)')
        lassi_lbl.grid(row=4, column=0, padx=3, pady=20)
        lassi_en = Entry(f2, bd=8, relief=GROOVE, textvariable=self.lassi)
        lassi_en.grid(row=4, column=1, ipady=5, ipadx=5)

        #===================Bill Aera================#
        f3 = Label(self.root,bd = 10,relief = GROOVE)
        f3.place(x = 1050,y = 165,width = 310,height = 380)
        #===========
        bill_title = Label(f3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)
        

        # Scroll Bars
        scroll_y = Scrollbar(f3, orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.txt = Text(f3, yscrollcommand=scroll_y.set)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        #===========Buttons Frame=============#
        f4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        f4.place(x = 0,y = 540,relwidth = 1,height = 145)

        # Total Cosmetics
        cosm_lbl = Label(f4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(f4,bd = 8,relief = GROOVE,textvariable = self.total_cosmetics)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5, pady=1)

        # Total Grocery
        gro_label = Label(f4, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Total Grocery', justify=LEFT)
        gro_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        gro_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5, pady=1)

        # Total other
        other_label = Label(f4, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Other Total')
        other_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        other_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_other)
        other_en.grid(row=2, column=1, ipady=2, ipadx=5, pady=1)

        # Cosmetic Tax
        cos_tax_label = Label(f4, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Cosmetics Tax')
        cos_tax_label.grid(row=0, column=2, padx=30, pady=0)
        cos_tax_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.cos_tax)
        cos_tax_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # Grocery tac
        gro_tax_label = Label(f4, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Grocery Tax')
        gro_tax_label.grid(row=1, column=2, padx=30, pady=5)
        gro_tax_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.gro_tax)
        gro_tax_en.grid(row=1, column=3, ipady=2, ipadx=5)

        # Tax Other
        other_tax_label = Label(f4, font=('times new roman', 15, 'bold'), fg=lbl_color, bg=bg_color, text='Other Tax')
        other_tax_label.grid(row=2, column=2, padx=10, pady=5)
        other_tax_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.other_tax)
        other_tax_en.grid(row=2, column=3, ipady=2, ipadx=5)

        # Buttons

        # total button
        total_btn = Button(f4, text='Total', bg=bg_color, fg=fg_color, font=('lucida', 12, 'bold'), bd=7, relief=GROOVE, command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=20)

        # generate bill button
        genbill_btn = Button(f4, text='Generate Bill', bg=bg_color, fg=fg_color, font=('licida', 12, 'bold'), bd=7, relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20, padx=20)

        # clear button
        clear_btn = Button(f4, text='Clear', bg=bg_color, fg=fg_color, font=('lucida', 12, 'bold'), bd=7, relief=GROOVE, command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

        # exit button
        exit_btn = Button(f4, text='Exit', bg=bg_color, fg=fg_color, font=('lucida', 12, 'bold'), bd=7, relief=GROOVE, command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)

    # Function to get total 
    def total(self):
        # pass
        # Total Cosmetics
        self.total_cosmetics_prices = (
            (self.bath_soap.get()*15)+
            (self.face_cream.get()*30)+
            (self.face_wash.get()*25)+
            (self.hair_spray.get()*35)+
            (self.body_lotion.get()*50)
        )

        self.total_cosmetics.set('Rs. '+ str(self.total_cosmetics_prices))
        self.cos_tax.set('Rs. '+ str(round(self.total_cosmetics_prices*0.05)))
        # 5% tax on cosmetics

        # Total Grocery Prices
        self.total_grocery_prices = (
            (self.rice.get()*60) +
            (self.oil.get()*75) +
            (self.daal.get()*85)+
            (self.wheat.get()*45)+
            (self.sugar.get()*30) 
        )

        self.total_grocery.set('Rs. '+str(self.total_grocery_prices))
        self.gro_tax.set('Rs. '+str(round(self.total_grocery_prices*0.05)))

        # total other
        self.total_other_prices = (
            (self.mango.get()*30)+
            (self.soda.get()*20)+
            (self.nimka.get()*25)+
            (self.biscuit.get()*10)+
            (self.lassi.get()*15)
        )

        self.total_other.set('Rs. '+str(self.total_other_prices))
        self.other_tax.set('Rs '+str(round(self.total_other_prices*0.05)))

    # Function for Text Area
    def welcome_text(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, '      Welcome to Sangamesh Shop \n')
        self.txt.insert(END, f'\n Bill no. :      {str(self.cus_bill_no.get())}')
        self.txt.insert(END, f'\n Customer Name : {str(self.cus_name.get())}')
        self.txt.insert(END, f'\n Phone No. :     {str(self.cus_phone.get())}')
        self.txt.insert(END, '\n================================')
        self.txt.insert(END, '\nProduct       Qty      Price')
        self.txt.insert(END, '\n================================')

    def bill_area(self):
        # pass
        self.welcome_text()

        if self.bath_soap.get() != 0:
            self.txt.insert(END, f'\nBath Soap      {self.bath_soap.get()}        {self.bath_soap.get()*15}')
        if self.face_cream.get() != 0:
            self.txt.insert(END, f'\nFace Cream     {self.face_cream.get()}        {self.face_cream.get()*30}')
        if self.face_wash.get() != 0:
            self.txt.insert(END, f'\nFace Wash      {self.face_wash.get()}        {self.face_wash.get()*25}')
        if self.hair_spray.get() != 0:
            self.txt.insert(END, f'\nHair Spray     {self.hair_spray.get()}        {self.hair_spray.get()*35}')
        if self.body_lotion.get() != 0:
            self.txt.insert(END, f'\nBody Lotion    {self.body_lotion.get()}        {self.body_lotion.get()*50}')
        if self.rice.get() != 0:
            self.txt.insert(END, f'\nRice           {self.rice.get()}        {self.rice.get()*60}')
        if self.oil.get() != 0:
            self.txt.insert(END, f'\nOil            {self.oil.get()}        {self.oil.get()*70}')
        if self.daal.get() != 0:
            self.txt.insert(END, f'\nDaal           {self.daal.get()}        {self.daal.get()*85}')
        if self.wheat.get() != 0:
            self.txt.insert(END, f'\nWheat          {self.wheat.get()}        {self.wheat.get()*45}')
        if self.sugar.get() != 0:
            self.txt.insert(END, f'\nSugar          {self.sugar.get()}        {self.sugar.get()*30}')
        if self.mango.get() != 0:
            self.txt.insert(END, f'\nMango Juice    {self.mango.get()}        {self.mango.get()*30}')
        if self.soda.get() != 0:
            self.txt.insert(END, f'\nSoda           {self.soda.get()}        {self.soda.get()*20}')
        if self.nimka.get() != 0:
            self.txt.insert(END, f'\nNimka          {self.nimka.get()}        {self.nimka.get()*25}')
        if self.biscuit.get() != 0:
            self.txt.insert(END, f'\nBiscuit        {self.biscuit.get()}        {self.biscuit.get()*10}')
        if self.lassi.get() != 0:
            self.txt.insert(END, f'\nLassi          {self.lassi.get()}        {self.lassi.get()*15}' )
        self.txt.insert(END, '\n================================')
        self.txt.insert(END, f'\n               Total : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices*0.05 + self.total_other_prices*0.05}')

    def clear(self):
        # pass
        self.txt.delete('1.0', END)
        self.cus_name.set('')
        self.cus_phone.set('')
        self.cus_bill_no.set('')

        self.bath_soap.set(0)
        self.face_cream.set(0)   
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.body_lotion.set(0)

        self.rice.set(0)
        self.oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)

        self.mango.set(0)
        self.nimka.set(0)
        self.soda.set(0)
        self.biscuit.set(0)
        self.lassi.set(0)

        self.total_cosmetics.set(0)
        self.total_grocery.set(0)
        self.total_other.set(0)
        self.cos_tax.set(0)
        self.gro_tax.set(0)
        self.other_tax.set(0)


    def exit(self):
        # pass
        self.exit = tkinter.messagebox.askyesno('Exit', 'Confirm if you want to exit')
        if self.exit > 0:
            self.root.destroy()

root = Tk()
object = Bill_App(root)
root.mainloop()

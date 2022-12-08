from tkinter import *


class ATMPutOnMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.my_amount = IntVar()
        self.money = StringVar()
        self.active_bool = True
        self.status = ""

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=0)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).grid(columnspan=4, row=1)

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=2)

        master.put_details = PhotoImage(file='../images/ATM/PutWithdraw/atm_amount_put.png')
        Label(self, bg="#f7f0c6", width=960, image=master.put_details).grid(columnspan=4, row=3)

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=4)

        master.amount_50 = PhotoImage(file='../images/ATM/PutWithdraw/atm_500.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.amount_50,
               width=170, height=50, command=lambda: self.put_amount(50)) \
            .grid(column=1, row=5, pady=(0, 5))

        master.amount_100 = PhotoImage(file='../images/ATM/PutWithdraw/atm_100.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.amount_100,
               width=170, height=50, command=lambda: self.put_amount(100)) \
            .grid(column=1, row=6, pady=(0, 5))

        master.amount_200 = PhotoImage(file='../images/ATM/PutWithdraw/atm_200.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.amount_200,
               width=170, height=50, command=lambda: self.put_amount(200)) \
            .grid(column=1, row=7, pady=(0, 5))

        master.amount_500 = PhotoImage(file='../images/ATM/PutWithdraw/atm_500.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.amount_500,
               width=170, height=50, command=lambda: self.put_amount(500)) \
            .grid(column=2, row=5, pady=(0, 5))

        master.amount_1000 = PhotoImage(file='../images/ATM/PutWithdraw/atm_1000.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.amount_1000,
               width=170, height=50, command=lambda: self.put_amount(1000)) \
            .grid(column=2, row=6, pady=(0, 5))

        master.amount_5000 = PhotoImage(file='../images/ATM/PutWithdraw/atm_5000.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.amount_5000,
               width=170, height=50, command=lambda: self.put_amount(5000)) \
            .grid(column=2, row=7, pady=(0, 5))

        master.my_amount = PhotoImage(file='../images/ATM/PutWithdraw/atm_my_amount.png')
        master.amount_check_btn = Checkbutton(self, text="", background='#f7f0c6', variable=self.my_amount,
                                              onvalue=1, offvalue=0, image=master.my_amount, command=self.my_upd)
        master.amount_check_btn.grid(column=1, row=8, pady=(0, 5))

        self.amount_entry = Entry(self, font=("orbitron", 14), textvariable=self.money, state="disabled")
        self.amount_entry.config(fg='black')
        self.amount_entry.grid(column=2, row=8, pady=(0, 15))

        master.put_btn = PhotoImage(file='../images/ATM/PutWithdraw/atm_put_on_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.put_btn,
               width=170, height=50, command=lambda: self.check_amount()).grid(column=2, row=9)

        Label(self, bg="#f7f0c6", height=6).grid(columnspan=4, row=10)
        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.status)
        self.check_data.grid(columnspan=4, row=11)

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).grid(columnspan=4, row=12)

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).grid(columnspan=4, row=13)

    def my_upd(self):
        if self.active_bool:
            self.amount_entry.config(state="normal")
            self.active_bool = False
        elif not self.active_bool:
            self.amount_entry.config(state="disabled")
            self.active_bool = True

    def put_amount(self, value):
        self.status = PhotoImage(file='../images/ATM/PutWithdraw/atm_success_put.png')
        self.check_data.config(image=self.status)
        self.money.set("")
        print(value)

    def check_amount(self):
        if self.money.get().isdigit():
            self.put_amount(int(self.money.get()))
        else:
            self.status = PhotoImage(file='../images/ATM/PutWithdraw/atm_error.png')
            self.check_data.config(image=self.status)

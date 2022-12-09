from tkinter import *


class ATMDepositMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.balance = 5890
        self.get = StringVar()
        self.put = StringVar()

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=0)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).grid(columnspan=4, row=1)

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=2)

        master.depo_info = PhotoImage(file='../images/ATM/DepositMenu/dep_page.png')
        Label(self, bg="#f7f0c6", width=960, image=master.depo_info).grid(columnspan=4, row=3, pady=(0, 10))

        master.depo_bal = PhotoImage(file='../images/ATM/DepositMenu/dep_balance.png')
        Label(self, bg="#f7f0c6", image=master.depo_bal).grid(column=1, row=4, pady=(0, 10))

        self.depo_amount = Label(self, bg="#f7f0c6", font=("orbitron", 12, 'bold'), text=str(self.balance))
        self.depo_amount.grid(column=2, row=4, pady=(0, 10))

        master.depo_get_img = PhotoImage(file='../images/ATM/DepositMenu/dep_get.png')
        Label(self, bg="#f7f0c6", image=master.depo_get_img).grid(column=1, row=5, pady=(0, 5))

        self.get_entry = Entry(self, font=("orbitron", 14), textvariable=self.get)
        self.get_entry.config(fg='black')
        self.get_entry.grid(column=1, row=6, pady=(0, 15))

        master.get_btn = PhotoImage(file='../images/ATM/DepositMenu/dep_get_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.get_btn,
               width=170, height=50, command=lambda: self.get_on()).grid(column=2,
                                                                         row=6, pady=(0, 5))

        master.depo_put_img = PhotoImage(file='../images/ATM/DepositMenu/dep_put.png')
        Label(self, bg="#f7f0c6", image=master.depo_put_img).grid(column=1, row=7, pady=(0, 5))

        self.put_entry = Entry(self, font=("orbitron", 14), textvariable=self.put)
        self.put_entry.config(fg='black')
        self.put_entry.grid(column=1, row=8, pady=(0, 15))

        master.put_btn = PhotoImage(file='../images/ATM/DepositMenu/dep_put_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.put_btn,
               width=170, height=50, command=lambda: self.put_on()).grid(column=2,
                                                                         row=8, pady=(0, 10))

        self.stat_depo = ""
        self.check_depo = Label(self, bg="#f7f0c6", image=self.stat_depo)
        self.check_depo.grid(columnspan=4, row=9, pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).grid(columnspan=4, row=10)

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).grid(columnspan=4, row=11)

    def put_on(self):
        if self.put.get().isdigit():
            self.stat_depo = PhotoImage(file='../images/ATM/DepositMenu/dep_putted.png')
            self.check_depo.config(image=self.stat_depo)
            self.balance += int(self.put.get())
            self.depo_amount.config(text=str(self.balance))
        elif not self.put.get().isdigit():
            self.stat_depo = PhotoImage(file='../images/ATM/DepositMenu/dep_error.png')
            self.check_depo.config(image=self.stat_depo)
        else:
            self.stat_depo = PhotoImage(file='../images/ATM/DepositMenu/dep_error.png')
            self.check_depo.config(image=self.stat_depo)
        self.put.set("")

    def get_on(self):
        if not self.get.get().isdigit():
            self.stat_depo = PhotoImage(file='../images/ATM/DepositMenu/dep_error.png')
            self.check_depo.config(image=self.stat_depo)
        elif self.get.get().isdigit():
            if int(self.get.get()) > int(self.balance):
                self.stat_depo = PhotoImage(file='../images/ATM/DepositMenu/dep_error.png')
                self.check_depo.config(image=self.stat_depo)
            else:
                self.stat_depo = PhotoImage(file='../images/ATM/DepositMenu/dep_returned.png')
                self.check_depo.config(image=self.stat_depo)
                self.balance -= int(self.get.get())
                self.depo_amount.config(text=str(self.balance))
        self.get.set("")

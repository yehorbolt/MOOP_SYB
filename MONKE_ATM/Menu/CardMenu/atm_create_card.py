from tkinter import *
from ConnectToDB import ConnectToDb as con
from Account.Account import *
from User.User import User
from Card.Card import *
from Card.Credit import Credit
from Card.Checking import Checking
from Card.Savings import Savings

class ATMCreateCard(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        self.incorrect_image = ""

        self.pin = StringVar()

        self.card_type = StringVar()
        self.card_type.set("credit")

        master.credit_card = PhotoImage(file='../images/ATM/RegMenu/reg_credit.png')
        master.checking_card = PhotoImage(file='../images/ATM/RegMenu/reg_checking.png')
        master.saving_card = PhotoImage(file='../images/ATM/RegMenu/reg_saving.png')
        r_1 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.card_type,
                          value="credit", image=master.credit_card)
        r_2 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.card_type,
                          value="checking", image=master.checking_card)
        r_3 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.card_type,
                          value="savings", image=master.saving_card)

        r_1.pack()
        r_2.pack()
        r_3.pack(pady=(0, 10))

        master.pin_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_pin.png')
        Label(self, text="", bg='#f7f0c6', image=master.pin_reg).pack()

        conf_pin_entry = Entry(self, font=("arial", 12), textvariable=self.pin)
        conf_pin_entry.config(fg='black', show='●')
        conf_pin_entry.pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_image)

        self.check_data.pack(pady=(2, 2))

        master.conf_btn = PhotoImage(file='../images/ATM/create_card_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.conf_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=lambda: master.quit_app()).pack(pady=(0, 5))

    def check(self):
        sel_type = self.card_type.get()
        pin_code = self.pin.get()

        check_type = True
        for i in range(len(self.master.card_list)):
            if self.master.card_list[i].type == sel_type:
                check_type = False

        if (len(pin_code) != 4) or (not self.pin.get().isdigit):
            self.incorrect_image = PhotoImage(file='../images/ATM/CardPin/atm_invalid_pass.png')
            self.check_data.config(image=self.incorrect_image)
        else:
            if check_type:
                if sel_type == "credit":
                    Credit(int(pin_code), "credit", self.master.account_data.id, False)
                elif sel_type == "savings":
                    Savings(int(pin_code), "savings", self.master.account_data.id, False)
                elif sel_type == "checking":
                    Checking(int(pin_code), "checking", self.master.account_data.id, False)
                self.master.card_list = con.restoreCards(self.master.account_data.id)
                self.incorrect_image = PhotoImage(file='../images/ATM/CreateCard/create_card_success.png')
                self.check_data.config(image=self.incorrect_image)
                self.pin.set("")
            else:
                self.incorrect_image = PhotoImage(file='../images/ATM/bad_type.png')
                self.check_data.config(image=self.incorrect_image)

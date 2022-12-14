from tkinter import *
from ConnectToDB import ConnectToDb as con
from Account.Account import *
from User.User import User
from Card.Card import *
from Card.Credit import Credit
from Card.Checking import Checking
from Card.Savings import Savings


class ATMDeleteAccount(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        self.incorrect_dt = ""
        self.password = StringVar()

        master.del_acc = PhotoImage(file='../images/ATM/DeleteAccount/del_acc_1.png')
        Label(self, text="", bg='#f7f0c6', image=master.del_acc).pack()

        master.pass_del_acc = PhotoImage(file='../images/ATM/ChangePass/ch_enter_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.pass_del_acc).pack()

        password_entry_del_acc = Entry(self, font=("arial", 12), textvariable=self.password)
        password_entry_del_acc.config(fg='black', show='●')
        password_entry_del_acc.pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_dt)
        self.check_data.pack(pady=(10, 10))

        master.delete_btn = PhotoImage(file='../images/ATM/delete.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.delete_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def check(self):
        if self.password.get() != self.master.user_data.password:
            self.incorrect_dt = PhotoImage(file='../images/ATM/DeleteAccount/incorrect_pass.png')
            self.check_data.config(image=self.incorrect_dt)
        else:
            self.incorrect_dt = PhotoImage(file='../images/ATM/DeleteAccount/delete_acc.png')
            self.check_data.config(image=self.incorrect_dt)
            # account deleting

            # card delete
            for i in range(len(self.master.card_list)):
                    self.master.card_list[i].deleteCard()

            # account delete
            self.master.account_data.deleteAccount()

            # user delete
            self.master.user_data.deleteUser()

            self.master.switch_frame("ATMLoginPage")

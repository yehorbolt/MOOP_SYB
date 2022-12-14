from tkinter import *
from ConnectToDB import ConnectToDb as con
from Account.Account import *
from User.User import User
from Card.Card import *
from Card.Credit import Credit
from Card.Checking import Checking
from Card.Savings import Savings

class ATMCardListPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.select_card = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 15))

        master.select_card_btn = PhotoImage(file='../images/ATM/CardList/cl_select.png')

        for i in range(0, len(self.master.card_list)):
            Label(self, bg="#f7f0c6", width=170, text="Number: " + str(self.master.card_list[i].number),
                  font=('orbitron', 14, 'bold')).pack()
            Label(self, bg="#f7f0c6", width=170, text="Type: " + str(self.master.card_list[i].type),
                  font=('orbitron', 14, 'bold')).pack()
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT,
                   image=master.select_card_btn, width=130, height=40,
                   command=lambda a=i: self.function(a)).pack(pady=(0, 15))

        master.new_card_btn = PhotoImage(file='../images/ATM/create_card_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.new_card_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCreateCard")).pack(pady=(15, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=lambda: master.quit_app()).pack(pady=(0, 5))

    def function(self, val):
        # self.master.card_list[val].id, self.master.card_list[val].number,
        # self.master.card_list[val].password, self.master.card_list[val].type,
        # self.master.card_list[val].balance, self.master.card_list[val].valid,
        # self.master.card_list[val].limit, self.master.card_list[val].leftToPay,
        # self.master.card_list[val].account_id
        if self.master.card_list[val].type == "checking":
            self.master.selected_card = Checking(self.master.card_list[val].password, "checking",
                                                 self.master.card_list[val].account_id, True)
        elif self.master.card_list[val].type == "credit":
            self.master.selected_card = Credit(self.master.card_list[val].password, "credit",
                                               self.master.card_list[val].account_id, True)
        else:
            self.master.selected_card = Savings(self.master.card_list[val].password, "savings",
                                                self.master.card_list[val].account_id, True)
        print(self.master.selected_card)
        self.master.switch_frame("ATMCardPin")

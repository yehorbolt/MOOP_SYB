from tkinter import *


class StartPage(Frame):

    # Create main menu screen
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.user_id = 0
        self.master.user_data = ""
        self.master.account_data = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        master.login_btn = PhotoImage(file='../images/ATM/login_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.login_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMLoginPage")).pack(pady=(0, 5))

        master.reg_btn = PhotoImage(file='../images/ATM/RegMenu/reg_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.reg_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMRegistrationPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=lambda: master.quit_app()).pack(pady=(0, 5))

        Label(self, text="", bg='#f7f0c6', height=13).pack()

        master.who_is_it_this_is_monke = PhotoImage(file='../images/ATM/by_monkeys.png')
        Label(self, text="", bg='#f7f0c6', image=master.who_is_it_this_is_monke).pack(pady=(48, 0))

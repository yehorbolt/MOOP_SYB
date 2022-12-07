from tkinter import *


class ATMLoginPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.password = StringVar()
        self.login = StringVar()

        self.incorrect_dt = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(10, 0))

        # add donkey logo
        master.logo = PhotoImage(file='../images/ATM/donkey_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack(pady=10)

        master.login_sign = PhotoImage(file='../images/ATM/login_sign_in.png')
        Label(self, text="", bg='#f7f0c6', image=master.login_sign).pack()

        master.login_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_login.png')
        Label(self, text="", bg='#f7f0c6', image=master.login_reg).pack()

        login_entry = Entry(self, font=("arial", 12), textvariable=self.login)
        login_entry.config(fg='black')
        login_entry.pack(pady=(0, 10))

        master.pass_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.pass_reg).pack()

        password_entry = Entry(self, font=("arial", 12), textvariable=self.password)
        password_entry.config(fg='black', show='*')
        password_entry.pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_dt)
        self.check_data.pack(pady=(2, 2))

        master.enter_btn = PhotoImage(file='../images/ATM/enter_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.enter_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("StartPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def check(self):
        if len(self.login.get()) < 3:
            self.incorrect_dt = PhotoImage(file='../images/ATM/Login/login_incorrect.png')
            self.check_data.config(image=self.incorrect_dt)
        else:
            self.check_data.config(image="")
            self.master.switch_frame("ATMMainMenuPage")

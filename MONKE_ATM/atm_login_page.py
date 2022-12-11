from tkinter import *
from ConnectToDB import ConnectToDb as con
from Account.Account import *
from User.User import User


class ATMLoginPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.user_id = 0
        self.master.user_data = ""
        self.master.account_data = ""

        self.password = StringVar()
        self.login = StringVar()

        self.incorrect_dt = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

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
        u = str(self.login.get())
        p = str(self.password.get())
        check_lp = False
        try:
            if not User.checkLogin(self, u):
                u_id = User.findUserId(self, u)
                self.master.user_id = u_id
                data = con.restoreUser(u)
                self.master.user_data = User(data[0], data[1], data[2], data[3])
                if self.master.user_data.password == p:
                    self.incorrect_dt = ""
                    self.check_data.config(image=self.incorrect_dt)
                    check_lp = True
                else:
                    raise Exception
            else:
                raise Exception
        except Exception as e:
            print(e)
            self.incorrect_dt = PhotoImage(file='../images/ATM/Login/login_incorrect.png')
            self.check_data.config(image=self.incorrect_dt)
            check_lp = False

        if check_lp:
            self.master.account_data = con.restoreAccount(self.master.user_id)
            print(self.master.user_data)
            print(self.master.account_data)
            print(self.master.user_id)
            self.master.switch_frame("ATMMainMenuPage")

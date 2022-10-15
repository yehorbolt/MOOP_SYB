from tkinter import *


class ATMLoginPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        password = StringVar()
        login = StringVar()

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack()

        # add donkey logo
        master.logo = PhotoImage(file='../images/ATM/donkey_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack(pady=10)

        master.login_sign = PhotoImage(file='../images/ATM/login_sign_in.png')
        Label(self, text="", bg='#f7f0c6', image=master.login_sign).pack()

        master.login_reg = PhotoImage(file='../images/ATM/reg_enter_login.png')
        Label(self, text="", bg='#f7f0c6', image=master.login_reg).pack()

        login_entry = Entry(self, font=("arial", 10), textvariable=login)
        login_entry.config(fg='black')
        login_entry.pack()

        master.pass_reg = PhotoImage(file='../images/ATM/reg_enter_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.pass_reg).pack()

        password_entry = Entry(self, font=("arial", 10), textvariable=password)
        password_entry.config(fg='black', show='●')
        password_entry.pack()

        Label(self, text="", bg='#f7f0c6').pack(pady=5)

        master.enter_btn = PhotoImage(file='../images/ATM/enter_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.enter_btn,
               width=170, height=50, command=lambda: master.switch_frame("StartPage")).pack(pady=5)

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("StartPage")).pack(pady=5)

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=5)

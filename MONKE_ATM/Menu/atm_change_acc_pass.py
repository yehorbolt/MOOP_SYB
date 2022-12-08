from tkinter import *


class ATMChangePassword(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(10, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        self.incorrect_dt = ""
        self.new_password = StringVar()
        self.conf_password = StringVar()

        master.pass_reg = PhotoImage(file='../images/ATM/ChangePass/ch_enter_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.pass_reg).pack()

        password_entry = Entry(self, font=("arial", 12), textvariable=self.new_password)
        password_entry.config(fg='black', show='●')
        password_entry.pack(pady=(0, 10))

        master.conf_reg = PhotoImage(file='../images/ATM/ChangePass/ch_confirm_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.conf_reg).pack()

        conf_password_entry = Entry(self, font=("arial", 12), textvariable=self.conf_password)
        conf_password_entry.config(fg='black', show='●')
        conf_password_entry.pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_dt)
        self.check_data.pack(pady=(10, 10))

        master.conf_btn = PhotoImage(file='../images/ATM/ChangePass/ch_change.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.conf_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def check(self):
        if len(self.new_password.get()) < 8:
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_invalid_pass.png')
            self.check_data.config(image=self.incorrect_dt)
        elif self.new_password.get() != self.conf_password.get():
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_invalid_pass.png')
            self.check_data.config(image=self.incorrect_dt)
        else:
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_success.png')
            self.check_data.config(image=self.incorrect_dt)
            self.new_password.set("")
            self.conf_password.set("")

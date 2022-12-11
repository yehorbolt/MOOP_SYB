from tkinter import *


class ATMRegistrationPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.name = StringVar()
        self.surname = StringVar()
        self.login = StringVar()
        self.password = StringVar()
        self.conf_password = StringVar()

        self.card_type = StringVar()
        self.card_type.set("Credit")
        self.pin = StringVar()
        self.status = StringVar()
        self.status.set("workless")

        self.incorrect_dt = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        master.name_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_name.png')
        Label(self, text="", bg='#f7f0c6', image=master.name_reg).pack()

        name_entry = Entry(self, font=("arial", 12), textvariable=self.name)
        name_entry.config(fg='black')
        name_entry.pack(pady=(0, 5))

        master.surname_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_surname.png')
        Label(self, text="", bg='#f7f0c6', image=master.surname_reg).pack()

        surname_entry = Entry(self, font=("arial", 12), textvariable=self.surname)
        surname_entry.config(fg='black')
        surname_entry.pack(pady=(0, 7))

        master.login_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_login.png')
        Label(self, text="", bg='#f7f0c6', image=master.login_reg).pack()

        login_entry = Entry(self, font=("arial", 12), textvariable=self.login)
        login_entry.config(fg='black')
        login_entry.pack(pady=(0, 7))

        master.pass_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.pass_reg).pack()

        password_entry = Entry(self, font=("arial", 12), textvariable=self.password)
        password_entry.config(fg='black', show='●')
        password_entry.pack(pady=(0, 7))

        master.conf_reg = PhotoImage(file='../images/ATM/RegMenu/reg_confirm_pass.png')
        Label(self, text="", bg='#f7f0c6', image=master.conf_reg).pack()

        conf_password_entry = Entry(self, font=("arial", 12), textvariable=self.conf_password)
        conf_password_entry.config(fg='black', show='●')
        conf_password_entry.pack(pady=(0, 10))

        master.choose_card = PhotoImage(file='../images/ATM/RegMenu/reg_card_type.png')
        Label(self, text="", bg='#f7f0c6', image=master.choose_card).pack()

        master.credit_card = PhotoImage(file='../images/ATM/RegMenu/reg_credit.png')
        master.checking_card = PhotoImage(file='../images/ATM/RegMenu/reg_checking.png')
        master.saving_card = PhotoImage(file='../images/ATM/RegMenu/reg_saving.png')
        r_1 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.card_type,
                          value="Credit", image=master.credit_card)
        r_2 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.card_type,
                          value="Checking", image=master.checking_card)
        r_3 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.card_type,
                          value="Saving", image=master.saving_card)

        r_1.pack()
        r_2.pack()
        r_3.pack(pady=(0, 10))

        master.pin_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_pin.png')
        Label(self, text="", bg='#f7f0c6', image=master.pin_reg).pack()

        conf_pin_entry = Entry(self, font=("arial", 12), textvariable=self.pin)
        conf_pin_entry.config(fg='black', show='●')
        conf_pin_entry.pack(pady=(0, 10))

        master.choose_status = PhotoImage(file='../images/ATM/RegMenu/reg_stat.png')
        Label(self, text="", bg='#f7f0c6', image=master.choose_status).pack()

        master.stat_has = PhotoImage(file='../images/ATM/RegMenu/reg_has_job.png')
        master.stat_not = PhotoImage(file='../images/ATM/RegMenu/reg_workless.png')
        s_1 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.status,
                          value="working", image=master.stat_has)
        s_2 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.status,
                          value="workless", image=master.stat_not)

        s_1.pack()
        s_2.pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_dt)
        self.check_data.pack(pady=(2, 2))

        master.reg_btn = PhotoImage(file='../images/ATM/RegMenu/reg_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.reg_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("StartPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def check(self):
        print(self.card_type.get())
        if len(self.login.get()) < 3:
            self.incorrect_dt = PhotoImage(file='../images/ATM/RegMenu/reg_incorrect.png')
            self.check_data.config(image=self.incorrect_dt)
        elif len(self.pin.get()) != 4 or (not self.pin.get().isdigit()):
            self.incorrect_dt = PhotoImage(file='../images/ATM/RegMenu/reg_incorrect.png')
            self.check_data.config(image=self.incorrect_dt)
        elif len(self.password.get()) < 8:
            self.incorrect_dt = PhotoImage(file='../images/ATM/RegMenu/reg_incorrect_pass.png')
            self.check_data.config(image=self.incorrect_dt)
        elif self.password.get() != self.conf_password.get():
            self.incorrect_dt = PhotoImage(file='../images/ATM/RegMenu/reg_incorrect_conf.png')
            self.check_data.config(image=self.incorrect_dt)
        else:
            self.incorrect_dt = PhotoImage(file='../images/ATM/RegMenu/reg_success.png')
            self.check_data.config(image=self.incorrect_dt)

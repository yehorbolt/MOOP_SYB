from tkinter import *
from User.User import User
from ConnectToDB import ConnectToDb as con


class ATMChangePin(Frame):

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
        self.new_pin = StringVar()
        self.conf_pin = StringVar()

        master.pin_reg = PhotoImage(file='../images/ATM/ChangePass/ch_enter_pin.png')
        Label(self, text="", bg='#f7f0c6', image=master.pin_reg).pack()

        Entry(self, font=("orbitron", 14), textvariable=self.new_pin, width=4,fg='black', show='●').pack(pady=(0, 10))

        master.conf_reg = PhotoImage(file='../images/ATM/ChangePass/ch_confirm_pin.png')
        Label(self, text="", bg='#f7f0c6', image=master.conf_reg).pack()

        Entry(self, font=("orbitron", 14), textvariable=self.conf_pin, width=4, fg='black', show='●').pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_dt)
        self.check_data.pack(pady=(10, 10))

        master.conf_btn = PhotoImage(file='../images/ATM/ChangePass/ch_change.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.conf_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=lambda: master.quit_app()).pack(pady=(0, 5))

    def check(self):
        if len(self.new_pin.get()) != 4 or (not self.new_pin.get().isdigit()):
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_pin_error.png')
            self.check_data.config(image=self.incorrect_dt)
        elif self.new_pin.get() != self.conf_pin.get():
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_pin_error.png')
            self.check_data.config(image=self.incorrect_dt)
        elif self.new_pin.get() == self.master.selected_card.password:
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_pin_success.png')
            self.new_pin.set("")
            self.conf_pin.set("")
        else:
            self.incorrect_dt = PhotoImage(file='../images/ATM/ChangePass/ch_pin_success.png')
            self.check_data.config(image=self.incorrect_dt)
            self.master.selected_card.changePassword(int(self.new_pin.get()))
            self.master.card_list = con.restoreCards(self.master.account_data.id)
            self.new_pin.set("")
            self.conf_pin.set("")

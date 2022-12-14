from tkinter import *


class ATMCreditMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        self.new_credit = StringVar()

        # my credit info left

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        master.credit_info = PhotoImage(file='../images/ATM/Credit/credit_info.png')
        Label(self, bg="#f7f0c6", width=960, image=master.credit_info).pack(pady=(20, 10))

        master.credit_enter_img = PhotoImage(file='../images/ATM/Credit/cr_enter_new.png')
        Label(self, bg="#f7f0c6", width=960, image=master.credit_enter_img).pack(pady=(10, 0))

        self.credit_entry = Entry(self, font=("orbitron", 14), textvariable=self.new_credit)
        self.credit_entry.config(fg='black')
        self.credit_entry.pack(pady=(10, 0))

        self.stat = ""
        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.stat)
        self.check_data.pack(pady=(15, 15))

        master.change_credit_btn = PhotoImage(file='../images/ATM/Credit/cr_apply_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.change_credit_btn,
               width=170, height=50, command=lambda: self.get_credit()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def get_credit(self):
        if not self.new_credit.get().isdigit():
            self.stat = PhotoImage(file='../images/ATM/Credit/cr_error.png')
            self.check_data.configure(image=self.stat)
        else:
            self.stat = PhotoImage(file='../images/ATM/Credit/cr_approved.png')
            self.check_data.configure(image=self.stat)
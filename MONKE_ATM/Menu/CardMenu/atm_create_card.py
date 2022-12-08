from tkinter import *


class ATMCreateCard(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(10, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        self.incorrect_image = ""
        self.pin = StringVar()

        master.pin_reg = PhotoImage(file='../images/ATM/RegMenu/reg_enter_pin.png')
        Label(self, text="", bg='#f7f0c6', image=master.pin_reg).pack()

        conf_pin_entry = Entry(self, font=("arial", 12), textvariable=self.pin)
        conf_pin_entry.config(fg='black', show='●')
        conf_pin_entry.pack(pady=(0, 10))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.incorrect_image)

        self.check_data.pack(pady=(2, 2))

        master.conf_btn = PhotoImage(file='../images/ATM/create_card_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.conf_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def check(self):
        pin_code = self.pin.get()
        if len(pin_code) != 4:
            self.incorrect_image = PhotoImage(file='../images/ATM/CardPin/atm_invalid_pass.png')
            self.check_data.config(image=self.incorrect_image)
        else:
            self.incorrect_image = PhotoImage(file='../images/ATM/CreateCard/create_card_success.png')
            self.check_data.config(image=self.incorrect_image)
            self.pin.set("")

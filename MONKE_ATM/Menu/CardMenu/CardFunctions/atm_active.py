from tkinter import *


class ATMActiveMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.activated = BooleanVar()
        self.activated.set(self.master.selected_card.valid)

        self.status = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        master.active_card = PhotoImage(file='../images/ATM/ActiveMenu/active_act.png')
        master.deactive_card = PhotoImage(file='../images/ATM/ActiveMenu/active_deact.png')
        r_1 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.activated,
                          value=True, image=master.active_card)
        r_2 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.activated,
                          value=False, image=master.deactive_card)

        r_1.pack()
        r_2.pack(pady=(0, 15))

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.status)
        self.check_data.pack(pady=(2, 2))

        master.change_btn = PhotoImage(file='../images/ATM/ActiveMenu/active_change.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.change_btn,
               width=170, height=50, command=lambda: self.check()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=lambda: master.quit_app()).pack(pady=(0, 5))

    def check(self):
        if self.activated.get():
            self.status = PhotoImage(file='../images/ATM/ActiveMenu/active_activated.png')
            self.check_data.config(image=self.status)
        elif not self.activated.get():
            self.status = PhotoImage(file='../images/ATM/ActiveMenu/active_deactivated.png')
            self.check_data.config(image=self.status)

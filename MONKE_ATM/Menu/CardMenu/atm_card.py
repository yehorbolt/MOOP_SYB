from tkinter import *


class ATMCardPage(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)

        self.card_type = self.master.select_card[2]
        print(self.card_type)
        Label(self, bg="#f7f0c6").grid(columnspan=4, row=0)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).grid(columnspan=4, row=1)

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.grid(columnspan=4, row=2)

        Label(self, bg='#f7f0c6', font=('orbitron', 12, 'bold'), text="Number: " + self.master.select_card[1])\
            .place(x=15, y=60)
        Label(self, bg='#f7f0c6', font=('orbitron', 12, 'bold'), text="Type: " + self.master.select_card[2])\
            .place(x=15, y=90)
        Label(self, bg='#f7f0c6', font=('orbitron', 12, 'bold'), text="Active: " + str(self.master.select_card[3]))\
            .place(x=15, y=120)

        if self.card_type == "Checking":
            master.cp_put = PhotoImage(file='../images/ATM/CardMenu/cm_put_on.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_put,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=3, pady=(0, 5))

            master.cp_withdraw = PhotoImage(file='../images/ATM/CardMenu/cm_withdraw.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_withdraw,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=4, pady=(0, 5))

            master.cp_transfer = PhotoImage(file='../images/ATM/CardMenu/cm_transfer.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_transfer,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=5, pady=(0, 5))

            master.cp_daemon = PhotoImage(file='../images/ATM/CardMenu/cm_daemon.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_daemon,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=6, pady=(0, 5))

        elif self.card_type == "Savings":
            master.cp_put = PhotoImage(file='../images/ATM/CardMenu/cm_put_on.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_put,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=3, pady=(0, 5))

            master.cp_withdraw = PhotoImage(file='../images/ATM/CardMenu/cm_withdraw.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_withdraw,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=4, pady=(0, 5))

            master.cp_transfer = PhotoImage(file='../images/ATM/CardMenu/cm_transfer.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_transfer,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=5, pady=(0, 5))

            master.cp_daemon = PhotoImage(file='../images/ATM/CardMenu/cm_daemon.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_daemon,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=6, pady=(0, 5))

            master.cp_deposit = PhotoImage(file='../images/ATM/CardMenu/cm_deposit.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_deposit,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=7, pady=(0, 5))

        else:
            master.cp_put = PhotoImage(file='../images/ATM/CardMenu/cm_put_on.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_put,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=3, pady=(0, 5))

            master.cp_transfer = PhotoImage(file='../images/ATM/CardMenu/cm_transfer.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_transfer,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=4, pady=(0, 5))

            master.cp_credit = PhotoImage(file='../images/ATM/CardMenu/cm_credit.png')
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_credit,
                   width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
                .grid(column=1, row=5, pady=(0, 5))

        master.cp_active = PhotoImage(file='../images/ATM/CardMenu/cm_active.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_active,
               width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
            .grid(column=2, row=3, pady=(0, 5))

        master.cp_delete = PhotoImage(file='../images/ATM/CardMenu/cm_delete.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_delete,
               width=170, height=50, command=lambda: master.switch_frame("StartPage")) \
            .grid(column=2, row=4, pady=(0, 5))

        master.cp_menu = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_menu,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage"))\
            .grid(column=2, row=5, pady=(0, 5))

        master.cp_exit = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.cp_exit,
               width=170, height=50, command=lambda: quit())\
            .grid(column=2, row=6, pady=(0, 5))

from tkinter import *


class ATMMainMenuPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(10, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        self.name = "Brittanie"

        self.master.welcome_name = Label(self, bg='#f7f0c6', font=('orbitron', 12, 'bold'), text="Welcome " + self.name)
        self.master.welcome_name.place(x=15, y=50)

        master.card_menu = PhotoImage(file='../images/ATM/menu_cards_menu.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.card_menu,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardListPage")).pack(pady=(0, 5))

        master.change_pass = PhotoImage(file='../images/ATM/menu_change_pass.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.change_pass,
               width=170, height=50, command=lambda: master.switch_frame("ATMChangePassword")).pack(pady=(0, 5))

        master.delete_user = PhotoImage(file='../images/ATM/menu_delete_acc.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.delete_user,
               width=170, height=50, command=lambda: master.switch_frame("ATMDeleteAccount")).pack(pady=(0, 5))

        master.tick_tack_toe = PhotoImage(file='../images/ATM/atm_tic_tac_toe.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.tick_tack_toe,
               width=170, height=50, command=lambda: master.switch_frame("ATMTicTacToePage")).pack(pady=(0, 5))

        master.log_out_btn = PhotoImage(file='../images/ATM/menu_log_out.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.log_out_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMLoginPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

from tkinter import *


class ATMCardListPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(10, 15))

        master.select_card_btn = PhotoImage(file='../images/ATM/CardList/cl_select.png')

        for i in range(0, len(self.master.pseudo_card_list)):
            Label(self, bg="#f7f0c6", width=170, text="Number: " + str(self.master.pseudo_card_list[i][1]),
                  font=('orbitron', 14, 'bold')).pack()
            Label(self, bg="#f7f0c6", width=170, text="Type: " + str(self.master.pseudo_card_list[i][2]),
                  font=('orbitron', 14, 'bold')).pack()
            Label(self, bg="#f7f0c6", width=170, text="Activated: " + str(self.master.pseudo_card_list[i][3]),
                  font=('orbitron', 14, 'bold')).pack()
            Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT,
                   image=master.select_card_btn, width=130, height=40,
                   command=lambda a=i: self.function(self.master.pseudo_card_list[a])).pack(pady=(0, 15))

        master.new_card_btn = PhotoImage(file='../images/ATM/create_card_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.new_card_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCreateCard")).pack(pady=(15, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def function(self, card):
        self.master.select_card = card
        print(self.master.select_card)
        self.master.switch_frame("ATMCardPin")

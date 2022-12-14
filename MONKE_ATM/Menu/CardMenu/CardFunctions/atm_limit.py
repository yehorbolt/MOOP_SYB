from tkinter import *


class ATMLimitMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        self.new_lim = StringVar()

        Label(self, bg='#f7f0c6', font=('orbitron', 12, 'bold'),
              text="Number: " + str(self.master.selected_card.number)) \
            .place(x=15, y=60)

        self.lim_bal = Label(self, bg='#f7f0c6', font=('orbitron', 12, 'bold'),
                             text="Limit: " + str(format(float(self.master.selected_card.limit), '.2f')))
        self.lim_bal.place(x=15, y=90)

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        master.lim_info = PhotoImage(file='../images/ATM/Limit/lim_info.png')
        Label(self, bg="#f7f0c6", width=960, image=master.lim_info).pack(pady=(20, 10))

        master.lim_enter_img = PhotoImage(file='../images/ATM/Limit/enter_new_lim.png')
        Label(self, bg="#f7f0c6", width=960, image=master.lim_enter_img).pack(pady=(10, 0))

        self.lim_entry = Entry(self, font=("orbitron", 14), textvariable=self.new_lim)
        self.lim_entry.config(fg='black')
        self.lim_entry.pack(pady=(10, 0))

        self.stat = ""
        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.stat)
        self.check_data.pack(pady=(15, 15))

        master.change_lim_btn = PhotoImage(file='../images/ATM/ActiveMenu/active_change.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.change_lim_btn,
               width=170, height=50, command=lambda: self.upd_limit()).pack(pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).pack(pady=(0, 5))

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def change_lim(self, value):
        if value <= 0:
            self.stat = PhotoImage(file='../images/ATM/Limit/lim_error.png')
            self.check_data.configure(image=self.stat)
        else:
            self.stat = PhotoImage(file='../images/ATM/Limit/lim_upd.png')
            self.check_data.configure(image=self.stat)
            self.master.selected_card.changeLimit(float(self.new_lim.get()))
            print(self.master.selected_card)
            self.master.switch_frame("ATMLimitMenu")

    def upd_limit(self):
        try:
            float(self.new_lim.get())
            self.change_lim(float(self.new_lim.get()))
        except Exception as e:
            print(e)
            self.stat = PhotoImage(file='../images/ATM/Limit/lim_error.png')
            self.check_data.configure(image=self.stat)


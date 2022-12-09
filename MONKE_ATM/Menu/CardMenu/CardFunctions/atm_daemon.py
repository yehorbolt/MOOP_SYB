from tkinter import *


class ATMDaemonMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.dae_netflix = IntVar()
        self.dae_ps = IntVar()
        self.dae_spotify = IntVar()

        self.status = ""

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        # add banana logo
        master.logo = PhotoImage(file='../images/ATM/mp_logo.png')
        panel = Label(self, image=master.logo, bg='#f7f0c6')
        panel.pack()

        master.subs = PhotoImage(file='../images/ATM/DaemonMenu/dae_subscriptions.png')
        Label(self, image=master.subs, bg='#f7f0c6').pack(pady=(5, 10))

        master.netflix = PhotoImage(file='../images/ATM/DaemonMenu/dae_netflix.png')
        Checkbutton(self, text="", background='#f7f0c6', variable=self.dae_netflix, onvalue=1, offvalue=0,
                    image=master.netflix).pack(pady=(0, 5))

        master.ps = PhotoImage(file='../images/ATM/DaemonMenu/dae_ps.png')
        Checkbutton(self, text="", background='#f7f0c6', variable=self.dae_ps, onvalue=1, offvalue=0,
                    image=master.ps).pack(pady=(0, 5))

        master.spotify = PhotoImage(file='../images/ATM/DaemonMenu/dae_spotify.png')
        Checkbutton(self, text="", background='#f7f0c6', variable=self.dae_spotify, onvalue=1, offvalue=0,
                    image=master.spotify).pack(pady=(0, 10))

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
               width=170, height=50, command=quit).pack(pady=(0, 5))

    def check(self):
        self.status = PhotoImage(file='../images/ATM/DaemonMenu/dae_changed.png')
        self.check_data.config(image=self.status)
        print(self.dae_netflix.get())
        print(self.dae_ps.get())
        print(self.dae_spotify.get())

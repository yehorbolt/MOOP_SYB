from tkinter import *


class ATMTransferMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).pack(pady=(20, 0))

        Label(self, bg="#bed2dd", text="TransferMenu").pack(pady=(10, 0))

        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).pack(pady=(0, 5))

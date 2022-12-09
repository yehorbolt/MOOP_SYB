from tkinter import *
import datetime

class ATMTransferMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.my_card = self.master.select_card[1]
        self.print = BooleanVar()
        self.print.set(False)

        self.card_num = StringVar()
        self.card_num.set("")

        self.amount_num = StringVar()
        self.amount_num.set("")

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=0)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).grid(columnspan=4, row=1)

        Label(self, bg="#f7f0c6").grid(columnspan=4, row=2)

        master.transfer_info = PhotoImage(file='../images/ATM/Transfer/tr_menu.png')
        Label(self, bg="#f7f0c6", width=960, image=master.transfer_info).grid(columnspan=4, row=3, pady=(0, 10))

        master.enter_num = PhotoImage(file='../images/ATM/Transfer/enter_num.png')
        Label(self, bg="#f7f0c6", image=master.enter_num).grid(column=1, row=4, pady=(0, 5))

        self.num_entry = Entry(self, font=("orbitron", 14), textvariable=self.card_num)
        self.num_entry.config(fg='black')
        self.num_entry.grid(column=1, row=5, pady=(0, 15))

        master.enter_amount = PhotoImage(file='../images/ATM/Transfer/enter_amount.png')
        Label(self, bg="#f7f0c6", image=master.enter_amount).grid(column=1, row=6, pady=(0, 5))

        self.amount_entry = Entry(self, font=("orbitron", 14), textvariable=self.amount_num)
        self.amount_entry.config(fg='black')
        self.amount_entry.grid(column=1, row=7, pady=(0, 15))

        master.want_print = PhotoImage(file='../images/ATM/Transfer/want_to_print.png')
        Label(self, bg="#f7f0c6", image=master.want_print).grid(column=1, row=8, pady=(0, 5))

        master.yes = PhotoImage(file='../images/ATM/Transfer/print_receipt.png')
        master.no = PhotoImage(file='../images/ATM/Transfer/not_print_receipt.png')
        r_1 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.print,
                          value=True, image=master.yes)
        r_2 = Radiobutton(self, text='', bg='#f7f0c6', variable=self.print,
                          value=False, image=master.no)

        r_1.grid(column=1, row=9, pady=(0, 5))
        r_2.grid(column=1, row=10, pady=(0, 5))

        master.transfer_btn = PhotoImage(file='../images/ATM/Transfer/tr_transfer.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.transfer_btn,
               width=170, height=50, command=lambda: self.transfer()).grid(column=1, row=11, pady=(0, 15))

        self.stat_transfer = ""
        self.check_transfer = Label(self, bg="#f7f0c6", image=self.stat_transfer)
        self.check_transfer.grid(columnspan=4, row=12, pady=(0, 5))

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMCardPage")).grid(columnspan=4, row=13)

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).grid(columnspan=4, row=14, pady=(0, 20))

        self.receipt_entry = Text(self, font=("orbitron", 12), width=19, height=3)
        self.receipt_entry.config(fg='black', bg="light yellow", state=DISABLED)
        self.receipt_entry.grid(row=5, column=2, rowspan=4, sticky=E + W + S + N)

    def transfer(self):
        if (not self.card_num.get().isdigit()) or (len(self.card_num.get()) != 16):
            self.stat_transfer = PhotoImage(file='../images/ATM/Transfer/tr_error.png')
            self.check_transfer.config(image=self.stat_transfer)
        elif not self.amount_num.get().isdigit():
            self.stat_transfer = PhotoImage(file='../images/ATM/Transfer/tr_error.png')
            self.check_transfer.config(image=self.stat_transfer)
        else:
            if self.print.get():
                self.receipt_entry.config(state=NORMAL)
                self.receipt_entry.delete("1.0", "end")
                now = datetime.datetime.now()
                self.receipt_entry.insert(END, "-------------MonkePaY TAX SYSTEM-------------\n")
                self.receipt_entry.insert(END, "| Transferred from: " + str(self.my_card)+"\n")
                self.receipt_entry.insert(END, "| Transferred to:   " + str(self.card_num.get())+"\n")
                self.receipt_entry.insert(END, "| In quantity:      " + str(self.amount_num.get())+"\n")
                self.receipt_entry.insert(END, "| Current balance:  " + str(1000)+"\n")
                self.receipt_entry.insert(END, "--------------------------------------------------------------\n")
                self.receipt_entry.insert(END, "| Printed at:       " + str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
                self.receipt_entry.insert(END, "--------------------------------------------------------------\n")
                self.receipt_entry.config(state=DISABLED)
                self.stat_transfer = PhotoImage(file='../images/ATM/Transfer/transferred.png')
                self.check_transfer.config(image=self.stat_transfer)
            else:
                self.receipt_entry.config(state=NORMAL)
                self.receipt_entry.delete("1.0", "end")
                self.receipt_entry.config(state=DISABLED)
                self.stat_transfer = PhotoImage(file='../images/ATM/Transfer/transferred.png')
                self.check_transfer.config(image=self.stat_transfer)

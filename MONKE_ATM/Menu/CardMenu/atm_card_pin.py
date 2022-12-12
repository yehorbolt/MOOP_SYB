from tkinter import *


class ATMCardPin(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.pin = StringVar()
        self.incorrect_image = ""

        Label(self, bg="#f7f0c6").grid(columnspan=9, row=0)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).grid(columnspan=9, row=1)

        Label(self, text="", bg='#f7f0c6').grid(column=0, row=2)

        # pin input btn
        pin_entry = Entry(self, font=("orbitron", 14), textvariable=self.pin, width=4, state="readonly")
        pin_entry.config(fg='black', show='●')
        pin_entry.grid(column=4, row=3, pady=(0, 15))

        Label(self, text="", bg='#f7f0c6', width=40).grid(column=0, row=5)
        Label(self, text="", bg='#f7f0c6', width=40).grid(column=8, row=5)

        master.btn1_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_1.png')
        self.btn1 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn1_pin, width=90, height=90,
                           command=lambda: self.add(1))
        self.btn1.grid(column=3, row=5)

        master.btn2_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_2.png')
        self.btn2 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn2_pin, width=90, height=90,
                           command=lambda: self.add(2))
        self.btn2.grid(column=4, row=5)

        master.btn3_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_3.png')
        self.btn3 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn3_pin, width=90, height=90,
                           command=lambda: self.add(3))
        self.btn3.grid(column=5, row=5)

        master.btn4_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_4.png')
        self.btn4 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn4_pin, width=90, height=90,
                           command=lambda: self.add(4))
        self.btn4.grid(column=3, row=6)

        master.btn5_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_5.png')
        self.btn5 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn5_pin, width=90, height=90,
                           command=lambda: self.add(5))
        self.btn5.grid(column=4, row=6)

        master.btn6_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_6.png')
        self.btn6 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn6_pin, width=90, height=90,
                           command=lambda: self.add(6))
        self.btn6.grid(column=5, row=6)

        master.btn7_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_7.png')
        self.btn7 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn7_pin, width=90, height=90,
                           command=lambda: self.add(7))
        self.btn7.grid(column=3, row=7)

        master.btn8_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_8.png')
        self.btn8 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn8_pin, width=90, height=90,
                           command=lambda: self.add(8))
        self.btn8.grid(column=4, row=7)

        master.btn9_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_9.png')
        self.btn9 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn9_pin, width=90, height=90,
                           command=lambda: self.add(9))
        self.btn9.grid(column=5, row=7)

        master.btn_min_pin = PhotoImage(file='../images/ATM/CardPin/atm_back_one.png')
        self.btn_min_pin = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                                  image=master.btn_min_pin, width=90, height=90,
                                  command=lambda: self.min())
        self.btn_min_pin.grid(column=3, row=8)

        master.btn0_pin = PhotoImage(file='../images/ATM/CardPin/atm_pin_0.png')
        self.btn0 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn0_pin, width=90, height=90,
                           command=lambda: self.add(0))
        self.btn0.grid(column=4, row=8)

        Label(self, text="", bg='#f7f0c6').grid(columnspan=9, row=9)

        self.incorrect_pin = Label(self, text="", bg='#f7f0c6', image=self.incorrect_image)
        self.incorrect_pin.grid(columnspan=9, row=9)

        Label(self, text="", bg='#f7f0c6').grid(columnspan=9, row=10)

        master.enter_btn = PhotoImage(file='../images/ATM/enter_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.enter_btn,
               width=170, height=50, command=lambda: self.check()).grid(columnspan=9, row=11)

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).grid(columnspan=9, row=12)

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).grid(columnspan=9, row=13)

    def check(self):
        print(self.master.selected_card)
        pin_code = self.pin.get()
        if len(pin_code) != 4:
            self.incorrect_image = PhotoImage(file='../images/ATM/CardPin/atm_invalid_pass.png')
            self.incorrect_pin.config(image=self.incorrect_image)
        else:
            if self.master.selected_card.password == int(pin_code):
                self.incorrect_pin.config(image="")
                self.master.switch_frame("ATMCardPage")
            else:
                self.incorrect_image = PhotoImage(file='../images/ATM/CardPin/atm_invalid_pass.png')
                self.incorrect_pin.config(image=self.incorrect_image)


    def add(self, value):
        self.pin.set(self.pin.get() + str(value))

    def min(self):
        if len(self.pin.get()) != 0:
            self.pin.set(self.pin.get()[0:-1])

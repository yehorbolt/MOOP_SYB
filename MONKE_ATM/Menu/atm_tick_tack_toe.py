from tkinter import *
from User.User import User
from ConnectToDB import ConnectToDb as con


class TicTacToe(Frame):
    is_won = True
    value = []

    def __init__(self, master):

        Frame.__init__(self, master)
        self.empty_box = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.ttt_x = PhotoImage(file='../images/ATM/TicTacToe/ttt_x.png')
        self.ttt_o = PhotoImage(file='../images/ATM/TicTacToe/ttt_o.png')
        self.turn = 'X'
        self.winOrLose = ""

        Label(self, bg="#f7f0c6").grid(columnspan=9, row=0)

        # add MonkePay on the head
        master.mp_name = PhotoImage(file='../images/ATM/mp_name.png')
        Label(self, bg="#bed2dd", width=960, image=master.mp_name).grid(columnspan=9, row=1)

        Label(self, text="", bg='#f7f0c6').grid(column=0, row=2)

        master.ttt_info = PhotoImage(file='../images/ATM/TicTacToe/ttt_info.png')
        Label(self, text="", bg='#f7f0c6', image=master.ttt_info).grid(columnspan=9, row=3)

        Label(self, text="", bg='#f7f0c6', width=40).grid(column=0, row=4)
        Label(self, text="", bg='#f7f0c6', width=40).grid(column=8, row=4)

        master.btn1_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn1 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn1_i, width=120, height=120, command=lambda: self.onclick(1))
        self.btn1.grid(column=3, row=4)

        master.btn2_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn2 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn2_i, width=120, height=120, command=lambda: self.onclick(2))
        self.btn2.grid(column=4, row=4)

        master.btn3_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn3 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn3_i, width=120, height=120, command=lambda: self.onclick(3))
        self.btn3.grid(column=5, row=4)

        master.btn4_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn4 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn4_i, width=120, height=120, command=lambda: self.onclick(4))
        self.btn4.grid(column=3, row=5)

        master.btn5_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn5 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn5_i, width=120, height=120, command=lambda: self.onclick(5))
        self.btn5.grid(column=4, row=5)

        master.btn6_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn6 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn6_i, width=120, height=120, command=lambda: self.onclick(6))
        self.btn6.grid(column=5, row=5)

        master.btn7_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn7 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn7_i, width=120, height=120, command=lambda: self.onclick(7))
        self.btn7.grid(column=3, row=6)

        master.btn8_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn8 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn8_i, width=120, height=120, command=lambda: self.onclick(8))
        self.btn8.grid(column=4, row=6)

        master.btn9_i = PhotoImage(file='../images/ATM/TicTacToe/ttt_empty.png')
        self.btn9 = Button(self, bg='#f7f0c6', activebackground='#f7f0c6', text='', relief=FLAT,
                           image=master.btn9_i, width=120, height=120, command=lambda: self.onclick(9))
        self.btn9.grid(column=5, row=6)

        Label(self, text="", bg='#f7f0c6').grid(columnspan=9, row=7)

        self.check_data = Label(self, text="", bg='#f7f0c6', image=self.winOrLose)
        self.check_data.grid(columnspan=9, row=8)

        Label(self, text="", bg='#f7f0c6').grid(columnspan=9, row=9)

        master.menu_btn = PhotoImage(file='../images/ATM/menu_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.menu_btn,
               width=170, height=50, command=lambda: master.switch_frame("ATMMainMenuPage")).grid(columnspan=9, row=10)

        master.exit_btn = PhotoImage(file='../images/ATM/exit_btn.png')
        Button(self, bg='#f7f0c6', activebackground='#f7f0c6', relief=FLAT, image=master.exit_btn,
               width=170, height=50, command=quit).grid(columnspan=9, row=11)

    def win(self):
        self.master.user_data.money += 100
        self.master.user_data.updateMoney()
        data = con.restoreUser(self.master.user_data.login)
        self.master.user_data = User(data[0], data[1], data[2], data[3])
        print(self.master.user_data)

    def erase_after(self):
        self.btn1['text'] = ''
        self.btn1.config(image=self.empty_box)
        self.btn2['text'] = ''
        self.btn2.config(image=self.empty_box)
        self.btn3['text'] = ''
        self.btn3.config(image=self.empty_box)
        self.btn4['text'] = ''
        self.btn4.config(image=self.empty_box)
        self.btn5['text'] = ''
        self.btn5.config(image=self.empty_box)
        self.btn6['text'] = ''
        self.btn6.config(image=self.empty_box)
        self.btn7['text'] = ''
        self.btn7.config(image=self.empty_box)
        self.btn8['text'] = ''
        self.btn8.config(image=self.empty_box)
        self.btn9['text'] = ''
        self.btn9.config(image=self.empty_box)

    def onclick(self, args):
        if args == 1:
            if self.btn1['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn1['text'] = self.turn
                self.btn1.config(image=self.ttt_x)
        if args == 2:
            if self.btn2['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn2['text'] = self.turn
                self.btn2.config(image=self.ttt_x)
        if args == 3:
            if self.btn3['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn3['text'] = self.turn
                self.btn3.config(image=self.ttt_x)
        if args == 4:
            if self.btn4['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn4['text'] = self.turn
                self.btn4.config(image=self.ttt_x)
        if args == 5:
            if self.btn5['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn5['text'] = self.turn
                self.btn5.config(image=self.ttt_x)
        if args == 6:
            if self.btn6['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn6['text'] = self.turn
                self.btn6.config(image=self.ttt_x)
        if args == 7:
            if self.btn7['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn7['text'] = self.turn
                self.btn7.config(image=self.ttt_x)
        if args == 8:
            if self.btn8['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn8['text'] = self.turn
                self.btn8.config(image=self.ttt_x)
        if args == 9:
            if self.btn9['text'] == '':
                self.winOrLose = ""
                self.check_data.configure(image=self.winOrLose)
                self.btn9['text'] = self.turn
                self.btn9.config(image=self.ttt_x)
        self.value = [self.btn1['text'], self.btn2['text'], self.btn3['text'],
                      self.btn4['text'], self.btn5['text'], self.btn6['text'],
                      self.btn7['text'], self.btn8['text'], self.btn9['text']]
        self.computer(self.value)
        self.winner_checker()
        self.tie_checker(self.value)

    def winner_checker(self):
        check1 = self.btn1['text'] == self.btn2['text'] == self.btn3['text'] != ''
        check2 = self.btn4['text'] == self.btn5['text'] == self.btn6['text'] != ''
        check3 = self.btn7['text'] == self.btn8['text'] == self.btn9['text'] != ''

        check4 = self.btn1['text'] == self.btn4['text'] == self.btn7['text'] != ''
        check5 = self.btn2['text'] == self.btn5['text'] == self.btn8['text'] != ''
        check6 = self.btn3['text'] == self.btn6['text'] == self.btn9['text'] != ''

        check7 = self.btn1['text'] == self.btn5['text'] == self.btn9['text'] != ''
        check8 = self.btn3['text'] == self.btn5['text'] == self.btn7['text'] != ''

        def add_points():
            if check1:
                if 'O' in [self.btn1['text'], self.btn2['text'], self.btn3['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check2:
                if 'O' in [self.btn4['text'], self.btn5['text'], self.btn6['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check3:
                if 'O' in [self.btn7['text'], self.btn8['text'], self.btn9['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check4:
                if 'O' in [self.btn1['text'], self.btn4['text'], self.btn7['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check5:
                if 'O' in [self.btn2['text'], self.btn5['text'], self.btn8['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check6:
                if 'O' in [self.btn3['text'], self.btn6['text'], self.btn9['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check7:
                if 'O' in [self.btn1['text'], self.btn5['text'], self.btn9['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()
            elif check8:
                if 'O' in [self.btn3['text'], self.btn5['text'], self.btn7['text']]:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_lose.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                else:
                    self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_won.png')
                    self.check_data.configure(image=self.winOrLose)
                    self.erase_after()
                    self.win()

        if self.is_won:
            if check1:
                add_points()
            elif check2:
                add_points()
            elif check3:
                add_points()
            elif check4:
                add_points()
            elif check5:
                add_points()
            elif check6:
                add_points()
            elif check7:
                add_points()
            elif check8:
                add_points()

    def tie_checker(self, check):
        if self.is_won:
            if ('X' in check) and ('O' in check) and ('' not in check):
                self.winOrLose = PhotoImage(file='../images/ATM/TicTacToe/ttt_tie.png')
                self.check_data.configure(image=self.winOrLose)
                self.erase_after()

    def computer(self, value):
        comp_turn = 'O'

        if (value[0] == value[1] != '') and value[2] == '':
            self.btn3['text'] = comp_turn
            self.btn3.config(image=self.ttt_o)
        elif (value[1] == value[2] != '') and value[0] == '':
            self.btn1['text'] = comp_turn
            self.btn1.config(image=self.ttt_o)
        elif (value[0] == value[2] != '') and value[1] == '':
            self.btn2['text'] = comp_turn
            self.btn2.config(image=self.ttt_o)
        elif (value[3] == value[4] != '') and value[5] == '':
            self.btn6['text'] = comp_turn
            self.btn6.config(image=self.ttt_o)
        elif (value[4] == value[5] != '') and value[3] == '':
            self.btn4['text'] = comp_turn
            self.btn4.config(image=self.ttt_o)
        elif (value[3] == value[5] != '') and value[4] == '':
            self.btn5['text'] = comp_turn
            self.btn5.config(image=self.ttt_o)
        elif (value[5] == value[7] != '') and value[8] == '':
            self.btn9['text'] = comp_turn
            self.btn9.config(image=self.ttt_o)
        elif (value[7] == value[8] != '') and value[6] == '':
            self.btn7['text'] = comp_turn
            self.btn7.config(image=self.ttt_o)
        elif (value[5] == value[8] != '') and value[7] == '':
            self.btn8['text'] = comp_turn
            self.btn8.config(image=self.ttt_o)
        elif (value[0] == value[3] != '') and value[6] == '':
            self.btn7['text'] = comp_turn
            self.btn7.config(image=self.ttt_o)
        elif (value[3] == value[6] != '') and value[0] == '':
            self.btn1['text'] = comp_turn
            self.btn1.config(image=self.ttt_o)
        elif (value[0] == value[6] != '') and value[3] == '':
            self.btn4['text'] = comp_turn
            self.btn4.config(image=self.ttt_o)
        elif (value[1] == value[4] != '') and value[7] == '':
            self.btn8['text'] = comp_turn
            self.btn8.config(image=self.ttt_o)
        elif (value[4] == value[7] != '') and value[1] == '':
            self.btn2['text'] = comp_turn
            self.btn2.config(image=self.ttt_o)
        elif (value[1] == value[7] != '') and value[4] == '':
            self.btn5['text'] = comp_turn
            self.btn5.config(image=self.ttt_o)
        elif (value[2] == value[5] != '') and value[8] == '':
            self.btn9['text'] = comp_turn
            self.btn9.config(image=self.ttt_o)
        elif (value[5] == value[8] != '') and value[2] == '':
            self.btn3['text'] = comp_turn
            self.btn3.config(image=self.ttt_o)
        elif (value[2] == value[8] != '') and value[5] == '':
            self.btn6['text'] = comp_turn
            self.btn6.config(image=self.ttt_o)
        elif (value[0] == value[4] != '') and value[8] == '':
            self.btn9['text'] = comp_turn
            self.btn9.config(image=self.ttt_o)
        elif (value[4] == value[8] != '') and value[0] == '':
            self.btn1['text'] = comp_turn
            self.btn1.config(image=self.ttt_o)
        elif (value[0] == value[8] != '') and value[4] == '':
            self.btn5['text'] = comp_turn
            self.btn5.config(image=self.ttt_o)
        elif (value[2] == value[4] != '') and value[6] == '':
            self.btn7['text'] = comp_turn
            self.btn7.config(image=self.ttt_o)
        elif (value[4] == value[6] != '') and value[2] == '':
            self.btn3['text'] = comp_turn
            self.btn3.config(image=self.ttt_o)
        elif (value[2] == value[6] != '') and value[4] == '':
            self.btn5['text'] = comp_turn
            self.btn5.config(image=self.ttt_o)
        else:
            for i in range(len(value)):
                if value[i] == '':
                    if i == 0:
                        self.btn1['text'] = comp_turn
                        self.btn1.config(image=self.ttt_o)
                        break
                    if i == 1:
                        self.btn2['text'] = comp_turn
                        self.btn2.config(image=self.ttt_o)
                        break
                    if i == 2:
                        self.btn3['text'] = comp_turn
                        self.btn3.config(image=self.ttt_o)
                        break
                    if i == 3:
                        self.btn4['text'] = comp_turn
                        self.btn4.config(image=self.ttt_o)
                        break
                    if i == 4:
                        self.btn5['text'] = comp_turn
                        self.btn5.config(image=self.ttt_o)
                        break
                    if i == 5:
                        self.btn6['text'] = comp_turn
                        self.btn6.config(image=self.ttt_o)
                        break
                    if i == 6:
                        self.btn7['text'] = comp_turn
                        self.btn7.config(image=self.ttt_o)
                        break
                    if i == 7:
                        self.btn8['text'] = comp_turn
                        self.btn8.config(image=self.ttt_o)
                        break
                    if i == 8:
                        self.btn9['text'] = comp_turn
                        self.btn9.config(image=self.ttt_o)
                        break
        self.value = [self.btn1['text'], self.btn2['text'], self.btn3['text'],
                      self.btn4['text'], self.btn5['text'], self.btn6['text'],
                      self.btn7['text'], self.btn8['text'], self.btn9['text']]
        self.winner_checker()
        self.tie_checker(self.value)

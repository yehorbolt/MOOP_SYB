from tkinter import *
import time

from Menu.atm_tick_tack_toe import TicTacToe
from atm_main_menu_page import ATMMainMenuPage
from atm_start_page import StartPage
from atm_login_page import ATMLoginPage
from atm_registration_page import ATMRegistrationPage
from Menu.CardMenu.atm_card import ATMCardPage
from Menu.CardMenu.atm_card_pin import ATMCardPin
from Menu.atm_card_list import ATMCardListPage
from Menu.atm_change_acc_pass import ATMChangePassword
from Menu.CardMenu.atm_create_card import ATMCreateCard
from Menu.atm_delete_acc import ATMDeleteAccount
from Menu.CardMenu.CardFunctions.atm_delete_card import ATMDeleteCard
from Menu.CardMenu.CardFunctions.atm_active import ATMActiveMenu
from Menu.CardMenu.CardFunctions.atm_credit import ATMCreditMenu
from Menu.CardMenu.CardFunctions.atm_daemon import ATMDaemonMenu
from Menu.CardMenu.CardFunctions.atm_deposit import ATMDepositMenu
from Menu.CardMenu.CardFunctions.atm_put_on import ATMPutOnMenu
from Menu.CardMenu.CardFunctions.atm_transfer import ATMTransferMenu
from Menu.CardMenu.CardFunctions.atm_withdraw import ATMWithdrawMenu
from Menu.CardMenu.CardFunctions.atm_limit import ATMLimitMenu

pages = {
    "StartPage": StartPage,
    "ATMLoginPage": ATMLoginPage,
    "ATMRegistrationPage": ATMRegistrationPage,
    "ATMMainMenuPage": ATMMainMenuPage,
    "ATMTicTacToePage": TicTacToe,
    "ATMCardPage": ATMCardPage,
    "ATMCardPin": ATMCardPin,
    "ATMCardListPage": ATMCardListPage,
    "ATMChangePassword": ATMChangePassword,
    "ATMCreateCard": ATMCreateCard,
    "ATMDeleteAccount": ATMDeleteAccount,
    "ATMDeleteCard": ATMDeleteCard,
    "ATMActiveMenu": ATMActiveMenu,
    "ATMCreditMenu": ATMCreditMenu,
    "ATMDaemonMenu": ATMDaemonMenu,
    "ATMDepositMenu": ATMDepositMenu,
    "ATMPutOnMenu": ATMPutOnMenu,
    "ATMTransferMenu": ATMTransferMenu,
    "ATMWithdrawMenu": ATMWithdrawMenu,
    "ATMLimitMenu": ATMLimitMenu
}


class SampleApp(Tk):

    amount = 0

    def __init__(self):
        Tk.__init__(self)
        self.time_label = None
        self.resizable(False, False)
        self.geometry("960x740")
        self.center()
        self.title("MonkePay")
        self.iconphoto(False, PhotoImage(file='../images/ATM/mp_logo.png'))
        self.configure(bg='#f7f0c6')
        self._frame = None
        self.user_data = ""
        self.account_data = ""
        self.user_id = 0
        self.amount = 1000
        self.pseudo_card_list = [[1, "4149898947631523", "Credit", True], [2, "5789478963214586", "Savings", False],
                                 [3, "4789458963548749", "Checking", False]]
        self.selected_card = {}
        self.switch_frame("StartPage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.configure(bg='#f7f0c6')
        self.time_label = Label(bg='#f7f0c6', font=('orbitron', 12, 'bold'))
        self.time_label.place(x=860, y=700)
        self.tick()
        self._frame.pack()

    def tick(self):
        current_time = time.strftime('%I:%M %p')
        self.time_label.config(text=current_time)
        self.time_label.after(200, self.tick)

    def center(self):
        """
        centers a tkinter window
        :param self: the main window or Toplevel window to center
        """
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

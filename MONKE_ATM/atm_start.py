from tkinter import *

from atm_start_page import StartPage
from atm_login_page import ATMLoginPage
from atm_registration_page import ATMRegistrationPage

pages = {
    "StartPage": StartPage,
    "ATMLoginPage": ATMLoginPage,
    "ATMRegistrationPage": ATMRegistrationPage
}


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.resizable(False, False)
        self.geometry("960x740")
        self.center()
        self.title("MonkePay")
        self.iconphoto(False, PhotoImage(file='../images/ATM/mp_logo.png'))
        self.configure(bg='#f7f0c6')
        self._frame = None
        self.switch_frame("StartPage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.configure(bg='#f7f0c6')
        self._frame.pack()

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


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

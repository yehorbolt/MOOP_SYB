# import User... (return needed data)
import random
import datetime
import os


class ATM:

    # update depo and daemon
    def update(self):
        randon_num = random.randint(1, 5)
        if randon_num == 2:
            for n in range(len(self.card_list)):
                if self.card_list[n][2]:
                    if self.card_list[n][1]:
                        if int(self.card_list[n][4]) > 0:
                            self.card_list[n][4] *= 1.04
                            self.card_list[n][5] = 10000
                    else:
                        if int(self.card_list[n][4]) > 0:
                            self.card_list[n][4] *= 1.04
                            self.card_list[n][5] = 1000
                    if int(self.card_list[n][3]) > int(self.card_list[n][6]):
                        self.card_list[n][3] -= self.card_list[n][6]
        print("\nA new day has come, the deposit has been updated and money for subscriptions has been withdrawn")

    # add User information like User
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.list = dict_users
        self.users_list = cards_list
        self.amount = 10000
        user_cards = []
        for v in range(len(dict_users)):
            if dict_users[v]["user"][0] == login:
                for y in range(len(dict_users[v]["cards"])):
                    user_cards.append(dict_users[v]["cards"][y])
        self.card_list = user_cards
        # cards from db and ...
        # self.cards_list = cards

    # Main Menu
    def menu(self):
        print("\n---------------------------MonkePal---------------------------")
        print("Welcome to ATM user " + self.login)
        print("\nMain menu:")
        # there we can deposit/transfer and all we can do with our card
        print("1. Check my e-pocket")
        # change pass
        print("2. Change account password")
        print("an. Log out")
        print("--------------------------------------------------------------\n")

        choose_menu = input("Enter a number: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choose_menu == "1":
            atm.e_pocket()
        elif choose_menu == "2":
            atm.change_pass()
        else:
            print("Log out..")
            return True

    # Menu E-Pocket
    def e_pocket(self):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("** Balance on hand: " + str(self.amount))
        print("E-Pocket")
        print("\nYou need to choose one of these cards or one of functions")
        print("Your cards:")
        i = 1
        num_array = []
        for n in range(len(self.card_list)):
            print(str(i) + ". " + str(self.card_list[n][0]) + " status: "
                  + ("Gold" if self.card_list[n][1] else "Primary"))
            num_array.append(str(i))
            i += 1
        print(str(i) + ". Add new card")
        print("an. Exit")
        atm.update()
        print("\nChoose your action action:")
        choose_card = input("Enter a number: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choose_card in num_array:
            atm.card_menu(int(choose_card) - 1)
        elif choose_card == str(i):
            atm.add_card()
        else:
            atm.menu()

    # E-Pocket Card menu
    def card_menu(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("Card menu")
        print("\nCard number: " + str(self.card_list[card_num][0]))
        print("Card balance: " + str(self.card_list[card_num][3]))
        print("Card status: " + ("Gold" if self.card_list[card_num][1] else "Primary"))
        print("Card active status: " + ("Activated" if self.card_list[card_num][2] else "Deactivated"))
        print("Daemon: " + str(self.card_list[card_num][6]))
        print("\nCard Menu ")
        print("1. Put on card")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Deposit")
        print("5. Daemon")
        print("6. Activate/Deactivate")
        print("an. Exit")
        choose_card_menu = input("\nEnter your number: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choose_card_menu == "1":
            atm.put_on_card(card_num)
        elif choose_card_menu == "2":
            atm.withdraw(card_num)
        elif choose_card_menu == "3":
            atm.transfer(card_num)
        elif choose_card_menu == "4":
            atm.deposit(card_num)
        elif choose_card_menu == "5":
            atm.daemon(card_num)
        elif choose_card_menu == "6":
            atm.card_status(card_num)
        else:
            print("Exit")
        atm.e_pocket()

    # 1
    def put_on_card(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("** Balance on hand: " + str(self.amount))
        print("Put money on card")

        if self.card_list[card_num][2]:
            print("\n How much do you want to put:")
            print("1. 100")
            print("2. 500")
            print("3. My amount")
            print("an. Exit")
            choose_amount = input("\nEnter a number: ")
            if choose_amount == "1":
                if self.amount < 100:
                    print("You don`t have enough money on hand")
                else:
                    self.amount -= 100
                    self.card_list[card_num][3] += 100
                    print("Successfully")
            elif choose_amount == "2":
                if self.amount < 500:
                    print("You don`t have enough money on hand")
                else:
                    self.amount -= 500
                    self.card_list[card_num][3] += 500
                    print("Successfully")
            elif choose_amount == "3":
                how_amount = input("How much do you want to pay: ")
                if self.amount < int(how_amount):
                    print("You don`t have enough money on hand")
                else:
                    self.amount -= int(how_amount)
                    self.card_list[card_num][3] += int(how_amount)
                    print("Successfully")
            else:
                print("Exit")
        else:
            print("Your card is inactive")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.update()
        atm.card_menu(card_num)

    # 2
    def withdraw(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("Your daily high for withdraw: " + str(self.card_list[card_num][5]))
        if self.card_list[card_num][2]:
            print("Withdraw")
            print("Your card balance: " + str(self.card_list[card_num][3]))
            print("\n How much do you want to withdraw:")
            print("1. 100")
            print("2. 500")
            print("3. My amount")
            print("an. Exit")
            choose_amount = input("\nEnter a number: ")
            if choose_amount == "1":
                if 100 > int(self.card_list[card_num][5]):
                    print("You cant withdraw, sorry")
                else:
                    if int(self.card_list[card_num][3]) < 100:
                        print("You don`t have enough money on card")
                    else:
                        self.card_list[card_num][3] -= 100
                        self.amount += 100
                        self.card_list[card_num][5] -= 100
                        print("Successfully")
            elif choose_amount == "2":
                if 500 > int(self.card_list[card_num][5]):
                    print("You cant withdraw, sorry")
                else:
                    if int(self.card_list[card_num][3]) < 500:
                        print("You don`t have enough money on card")
                    else:
                        self.card_list[card_num][3] -= 500
                        self.amount += 100
                        self.card_list[card_num][5] -= 500
                        print("Successfully")
            elif choose_amount == "3":
                how_amount = input("How much do you want to withdraw: ")
                if int(how_amount) > int(self.card_list[card_num][5]):
                    print("You cant withdraw, sorry")
                else:
                    if int(self.card_list[card_num][3]) < int(how_amount):
                        print("You don`t have enough money on card")
                    else:
                        self.card_list[card_num][3] -= int(how_amount)
                        self.amount += int(how_amount)
                        print("Successfully")
            else:
                print("Exit")
        else:
            print("Your card is inactive")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.update()
        atm.card_menu(card_num)

    # 3
    def transfer(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        if self.card_list[card_num][2]:
            print("Transfer (using user card list**)")
            print("Your card balance: " + str(self.card_list[card_num][3]))

            tr_card_num = input("\nEnter card number to what you want to transfer (1 if want to exit): ")
            check_num = False
            for n in range(len(self.users_list)):
                if str(self.users_list[n][0]) == str(tr_card_num):
                    check_num = True
            if check_num:
                amount = input("How much you want to transfer: ")
                if int(amount) > int(self.card_list[card_num][3]):
                    print("You do not have enough of money on card")
                else:
                    a = 0
                    for n in range(len(self.users_list)):
                        if str(self.users_list[n][0]) == str(tr_card_num):
                            a = n
                    self.users_list[card_num][3] -= int(amount)
                    self.users_list[a][3] += int(amount)
                    now = datetime.datetime.now()
                    print("Transfer was completed, do you wan to print a tax?")
                    print("1. Yes")
                    print("2. No")
                    want_to_print = input("Enter your number: ")
                    if want_to_print == "1":
                        print("--------------------MonkePal TAX SYSTEM------------------")
                        print("| Transferred from: " + str(self.card_list[card_num][0]))
                        print("| Transferred to:   " + str(self.users_list[a][0]))
                        print("| Current balance on card: " + str(self.users_list[card_num][3]))
                        print("| Printed at: " + str(now))
                        print("---------------------------------------------------------")
                    else:
                        print("Tax is not printed")
            elif tr_card_num == "1":
                print("Exit..")
            else:
                print("This card does not exist")
        else:
            print("Your card is inactive")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.update()
        atm.card_menu(card_num)

    # 4
    def deposit(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        if self.card_list[card_num][2]:
            print("Deposit page")
            print("\nYour deposit balance " + str(self.card_list[card_num][4]))
            print("Your card balance " + str(self.card_list[card_num][3]))
            print("Menu")
            print("1. Withdraw deposit")
            print("2. Put on Deposit")
            print("an. Exit")
            choose_dep = input("\nEnter a number: ")
            if choose_dep == "1":
                how_dep = input("How much do you want to withdraw: ")
                if int(how_dep) > int(self.card_list[card_num][4]):
                    print("Hmm, you do not have that amount of money on deposit")
                else:
                    self.card_list[card_num][4] -= int(how_dep)
                    self.card_list[card_num][3] += int(how_dep)
                    print("Withdraw successfully")
            if choose_dep == "2":
                how_dep = input("How much do you put in deposit: ")
                if int(how_dep) > int(self.card_list[card_num][3]):
                    print("Hmm, you do not have that amount of money on card balance")
                else:
                    self.card_list[card_num][3] -= int(how_dep)
                    self.card_list[card_num][4] += int(how_dep)
                    print("Put successfully")
            else:
                print("Exit")
        else:
            print("Your card is inactive")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.update()
        atm.card_menu(card_num)

    # 5
    def daemon(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        if self.card_list[card_num][2]:
            print("Daemon")
            print("\n Your daemons: ")
            print("By card status: " + ("Gold = 20" if self.card_list[card_num][1] else "Primary = 0"))
            print("By subscription on Spotify: " + ("Premium = 5" if self.card_list[card_num][7] else "Free = 0"))
            print("By subscription on Netflix: " + ("Premium = 10" if self.card_list[card_num][8] else "Tor*ent = 0"))
            print("\n Daemon menu: ")
            print("1. Deactivate Spotify" if self.card_list[card_num][7] else "2. Activate Spotify")
            print("2. Deactivate Netflix" if self.card_list[card_num][8] else "2. Activate Netflix")
            print("an. Exit")
            choose_daemon = input("\n Enter number: ")
            if choose_daemon == "1":
                if self.card_list[card_num][7]:
                    print("Deactivate subscription on Spotify")
                    self.card_list[card_num][6] -= 5
                    self.card_list[card_num][7] = False
                else:
                    print("Subscription on Spotify activated")
                    self.card_list[card_num][6] += 5
                    self.card_list[card_num][7] = True
                print("Successfully")
            if choose_daemon == "2":
                if self.card_list[card_num][8]:
                    print("Deactivate subscription on Netflix")
                    self.card_list[card_num][6] -= 10
                    self.card_list[card_num][8] = False
                else:
                    print("Subscription on Netflix activated")
                    self.card_list[card_num][6] += 10
                    self.card_list[card_num][8] = True
                print("Updated successfully")
            else:
                print("Exit")
        else:
            print("Your card is inactive")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.update()
        atm.card_menu(card_num)

    # 6
    def card_status(self, card_num):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("Card status")
        print("\nYour status is: " + ("Activated" if self.card_list[card_num][2] else "Deactivated"))
        print("Do you want to " + ("deactivate" if self.card_list[card_num][2] else "activate") + " your card?")

        print("1. Yes")
        print("2. No")
        print("an. Exit (like No :) )")

        status_card = input("Enter a number: ")
        if status_card == "1":
            if self.card_list[card_num][2]:
                self.card_list[card_num][2] = False
            else:
                self.card_list[card_num][2] = True
            print("Updated successfully")
        elif status_card == "2":
            atm.card_menu(card_num)
        else:
            atm.card_menu(card_num)
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.update()
        atm.card_menu(card_num)

    # E-pocket Add card
    def add_card(self):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("Adding new card")
        print("\nDo you want add new card? ")
        print("1. Yes")
        print("2. No")
        print("an. Exit (like No :) )")

        choose_card = input("Enter a number: ")
        if choose_card == "1":
            print("Choose your type of card:")
            print("1. Gold (20 hryvnias per ATM day)")
            print("2. Primary (free)")
            card_type = input("\nEnter a number: ")
            if card_type == "1":
                have_one = False
                card_num = 0
                while not have_one:
                    card_num = random.randint(4000000000000000, 5000000000000000)
                    have_one = True
                    for n in range(len(self.card_list)):
                        if str(self.card_list[n][0]) == str(card_num):
                            have_one = False
                self.card_list.append([card_num, True, True, 0, 0, 10000, 20, False, False])
            elif card_type == "2":
                have_one_1 = False
                card_num = 0
                while not have_one_1:
                    card_num = random.randint(4000000000000000, 5000000000000000)
                    have_one_1 = True
                    for n in range(len(self.card_list)):
                        if str(self.card_list[n][0]) == str(card_num):
                            have_one_1 = False
                self.card_list.append([card_num, False, True, 0, 0, 1000, 0, False, False])
            else:
                atm.add_card()
            print("Created successfully")
        elif choose_card == "2":
            print("Exit")
        else:
            print("Exit")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.e_pocket()

    # Menu Change password
    def change_pass(self):
        print("\n-----------------------MonkePal--------------------------")
        print("User " + self.login)
        print("Change account password")
        print("\nDo you want to change your password? ")
        print("1. Yes")
        print("2. No")
        choose_pass = input("\nEnter a number: ")
        if choose_pass == "1":
            print("Your password need to be more than 8 symbols length")
            new_pass = input("Enter new password: ")
            while len(new_pass) < 8:
                print("\nYour password length is no more than 8 symbols")
                new_pass = input("Enter new password: ")
            # there we check password and update on db if true
            print("\n Your password was changed")
            self.password = new_pass
            for r in range(len(self.list)):
                if self.list[r]["user"][0] == self.login:
                    self.list[r]["user"][1] = self.password
        elif choose_pass == "2":
            print("Return to menu")
        else:
            print("Return to menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        atm.menu()


# login, password
# num, status (gold primary...), activated/inactivate, balance,
# dep. balance, withdraw by day, daemon (Card type, Spotify, Netflix)
dict_users = [
    {"user": ["login", "password"], "cards": [["4149499378941895", False, True, 900, 250, 1000, 5, True, False],
                                              ["4487489778941895", True, True, 850, 0, 10000, 30, False, True],
                                              ["4148789658751925", False, True, 0, 0, 1000, 0, False, False]]},
    {"user": ["login1", "password1"], "cards": [["4586499378941895", False, True, 900, 250, 1000, 0, False, False]]}
]

cards_list = []
for b in range(len(dict_users)):
    for t in range(len(dict_users[b]["cards"])):
        cards_list.append(dict_users[b]["cards"][t])

while True:

    print("-------------------------------------------------------------")
    print("--------------------Welcome to the MonkePal------------------")
    print("------------------------Sign in/Sign up----------------------")
    print("-------------------------------------------------------------")
    print("Enter a number: ")
    print("1. Sign in")
    print("2. I don`t have an account")
    print("an. Exit")
    print("-------------------------------------------------------------\n")
    choose = input("Choose your action: ")

    if choose == "1":
        print("\n-----------------------MonkePal--------------------------")
        print("Sign in")
        accName = input("\nInput your login: ")
        accPass = input("Input your password: ")
        # check entered login and pass

        # check data
        lg = False
        for p in range(len(dict_users)):
            if dict_users[p]["user"][0] == accName:
                if dict_users[p]["user"][1] == accPass:
                    lg = True

        if lg:
            os.system('cls' if os.name == 'nt' else 'clear')
            atm = ATM(accName, accPass)
            atm.menu()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wrong login/password")
    elif choose == "2":
        print("-----------------------MonkePal--------------------------")
        print("\nSign up")
        accName = input("Input your login: ")
        accPass = "0"
        lg = True

        for p in range(len(dict_users)):
            if dict_users[p]["user"][0] == accName:
                lg = False
        if len(accName) < 3:
            lg = False

        if not lg:
            print("That login was created/Length less than 3")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            while True:
                print("Password must be 8 symbols or more")
                accPass = input("Input your password: ")
                if len(accPass) >= 8:
                    break
            # create user wit rn card
            c_num = random.randint(4000000000000000, 9000000000000000)
            cards_list.append([str(c_num), False, True, 0, 0, 0, 0, False, False])
            dict_users.append({"user": [accName, accPass],
                               "cards": [[str(c_num), False, True, 0, 0, 0, 0, False, False]]})
        print(dict_users)
        print(cards_list)
        # there we add all information we need to input for creating an account
    else:
        break

print("-------------------------------------------------------------\n")
print("System closed. Thank You")

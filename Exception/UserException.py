# this class is responsible for exceptions that my occur while working w/ the User class

class UserException(Exception):
    message = "";

    def PassException(self, User, password):
        if len(password) < 8:
            message = "You've entered password with length less than 8!\n" \
                      "Enter a new one with length 8 or more"
            print(message)
        if User.password == input:
            message = "You've entered the same password!\n" \
                      "Enter a new one"
            print(message)

#    def LoginException(self, User, login):

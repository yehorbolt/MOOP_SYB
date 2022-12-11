# MOOP_SYB
MonkeFlip! 
This project is a final task for a discipline called "OOP Methods". 
It is a console program that represents the interaction between user and atm.
Its' usage can be widened, because there are lot of other abilities except for working with ATM as a User.

## Technologies used:
1. Python
2. MySQL
3. Git

## Used Python libraries and modules:
1. mysql
2. mysql-connector
3. tkinter

## Entities:
1. User
2. Account
3. Card
4. Transaction
5. ATM
6. Bank

## Database realtions:
1. 1 User     has 1   Account
2. 1 Account  has N   Cards
3. 1 Card     has N   Transactions
4. 1 ATM      has N   Transactios
5. 1 Bank     has N   ATMs
6. 1 Bank     has N   Accounts

All the classes are the representations of objects in database and in real life.
## So, how the program works?
A user creates his account when registrating. After that he creates cards in the bank and puts some money on it. 
That's all! After card creation he can use them according to the bank policy (it's lower in the README).

## User has various things to do:
1. Withdraw money.
2. Put money on the card.
3. Make transaction.
4. Create a new card.
5. Delete card.
6. Delete account (deletes user itself).

## There are 3 different types of cards:
1. Savings (user is paid for his money on this card, user interest - 8%)
2. Credit (user can only take credit money and all the money he will transfer or put on this card will go to pay for the credit, bank interest - 10%)
3. Checking (user can sue this card for different transactions and payments)
User can withdraw money from: savings and checking cards.
User can put on all cards his money.
User can make a transfer only from: credit and checking cards.
If user has a job, he can take credit that is equal or more than 1/4 of all money he has on the cards.
if user is workless, he can take creit that is equal or more than 1/2 of all money he has on the cards.
user can have only one credit!

## How to install a project?
In your IDE, clone the project and use the command:
pip install -r requirements.txt
And you can start the project!

## That's all!
Clone the project & enjoy it!

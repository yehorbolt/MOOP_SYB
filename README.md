# MOOP_SYB
MonkeFlip! 
This project is a final task for a discipline called "OOP Methods". 
It is a small game that represents the interaction between user and atm. 

Technologies used:
1. Python
2. MySQL
3. Git

Entities:
1. User
2. Account
3. Card
4. Transaction
5. ATM
6. Bank

Database realtions:
1. 1 User has 1 Account
2. 1 Account has N Cards
3. 1 Card has N Transactions
4. 1 ATM has N Transactios
5. 1 Bank has N ATMs

All the classes are the representations of objects in database and in real life.
So, how the program works?
A user creates his account when registrating -> created new user and his account in database
Then user chooses a card he wants to have -> card is added to database

And then user has various things to do:
1. Withdraw money.
2. Put money on the card.
3. Make transaction.
4. Create a new card.
5. Delete card.
6. Delete account (deletes user itself).

There are 3 different types of cards:
1. Savings ()
2. Credit ()
3. Checking ()

This is an account management simulator program.
It uses Python and MySQL.

The program allows the user to:
- set up an account(If first time user)
- log in (if you have an account)
- Deposit money
- Withdraw money
- Update password
- View account details

NB!! YOU NEED TO ENTER YOUR DATABASE DATAILS FOR THE PROGRAM TO WORK
In line 7, enter your database hostname inside the empty single quotes ''.
In line 8, enter your database username inside the empty single quotes ''.
In line 9, enter your database password inside the empty single quotes ''.
In line 10, enter the database you will be using inside the empty single quotes ''.

When you set up an account, a table is created in your mysql database and your details are saved in the table.
When you log in, the program fetches your details from mysql and checks if the details you provided match the datails on your database,
if the datails match, you will be granted access to your account. 
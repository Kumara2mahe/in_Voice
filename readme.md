###
# in Voice

A simple inVoice application build in Python by Tkinter. It is mainly built for generating inVoices from the user entered data by converting it to '.docx' file format for making it a human readable information. It also has a basic login system where user can create their own accounts to work separate on their own invoice data .

<br>

## Description


- This application has a login system where user can create their own account to work with their own set of inVoices. Each user data is separate from each other and they never interact in any case. After user logged in they can work with four Interfaces, which helps user to create their own inVoice according to the data they provide.

- As said before there are four Interfaces to generate a complete InVoice, the interfaces are named as Clients, Stocks, InVoices and Settings.

- Clients, Stocks and InVoices Interface are there to do all the CRUD operations. That means each interface supports all the Database operations of Create, Read (View), Update, and also user can Delete the data they stored.

- First one is the Client Interface, which is for working with the users client data, which means they can add, update and delete the data about a client. That client data stored is later used to create InVoice for specific clients.

- Second one is the Stocks Interface, which is for working with the users particular stocks(products) they used to create inVoices and it also has the all the CRUD operations.

- InVoices Panel is where the users can built their inVoice from the data provided by the client, stocks panels. In this panel all data are used to create a InVoice and it not only creates the inVoice in '.docx'  file it also updates the products stored in the Stocks panel.

- The '.docx' file is created by the Python-docx module and there are other modules are used for styling and modifiying data, to get the full list of modules used see the [requirements.txt](https://github.com/Kumara2mahe/in_Voice/blob/main/requirements.txt)

<br>

## Features

<br>

> ### Authentication Panels

- Authentication Panels include the signIn and signUp panel, where not only the account creation and account authentication logic. Like while creating a new account it setsup the application with some predefined data like the due dates and currency exchange values, symbols and their Codes which are used in the application in all the Interfaces while working with prices.

- Also the default values used for currency exchange rate and tax calculation is settingup by the predefined data while creating a new account. 

<br>

> ### Auto-Update Currency Exchange Rate


- While a user logging in to the application with their credentials, the predefined data of currency exchange rate it updated by parsing the json data from the website and updates in to the apps local database when the user is connected to the internet.

- If there is no internet the data from the user's database is quered and updated as currency exchange rates for that session.


<br>

> ### Settings Panel

-   Settings panel is an optional feature for this application but it is used to modify or update the default values of Currency code, due date and tax (%) value.

- These default values play a major part while doing all the CRUD operations of all the other three panels. Like the defaults set here are the defaults for displaying the product prices in all the panel if not changed.

- There is also one extra privelage in the Settings panel is to change old password to a new one if when needed.

<br>

> ### InVoices Panel

- In the InVoices panel there is a option for updating the today's date displayed by the user desired date.

- There is also a currency value picker option to change the currency format of the current inVoice from default to their desired from the options.

- And the changing of currency code updates all the fields with price data at the same time.

- There is also a Customer message box to write short message on the inVoice created for every customer. And the Customer message box is occupied according to the client selection box, this message is by default set while creating and updating the client data and it can be modified like the currency rate for the current inVoice.

<br>

## License
[MIT](https://choosealicense.com/licenses/mit/)
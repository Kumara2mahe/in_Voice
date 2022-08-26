###
# in Voice

A simple inVoice application build in Python by Tkinter. It is mainly built for generating inVoices from the user entered data by converting it to '.txt' file format for making it a human readable information. It also has a basic login system where user can create their own accounts to work separate on their own invoice data .

<br>

## Description


- This application has a login system where user can create their own account to work with their own set of inVoices. Each user data is separate from each other and they never interact in any case. After user logged in they can work with four Interfaces, which helps user to create their own inVoice according to the data they provide.

- As said before there are four Interfaces to generate a complete InVoice, the interfaces are named as Clients, Stocks, InVoices and Settings.

- Clients, Stocks and InVoices Interface are there to do all the CRUD operations. That means each interface supports all the Database operations of Create, Read (View), Update, and also user can Delete the data they stored.

- First one is the Client Interface, which is for working with the users client data, which means they can add, update and delete the data about a client. That client data stored is later used to create InVoice for specific clients.

- Second one is the Stocks Interface, which is for working with the users particular stocks(products) they used to create inVoices and it also has the all the CRUD operations.

- InVoices Panel is where the users can built their inVoice from the data provided by the client, stocks panels. In this panel all data are used to create a InVoice and it not only creates the inVoice in '.txt'  file it also updates the products stored in the Stocks panel.

<br>

## License
[MIT](https://choosealicense.com/licenses/mit/)
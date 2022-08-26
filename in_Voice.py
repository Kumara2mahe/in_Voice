# ---- in Voice ---- a invoice application designed and created by Kumara

# Importing tkinter and tkinter.ttk modules
from tkinter import *
from tkinter.ttk import *

# assigning tkinter a name for special purposes
import tkinter as tk

# Importing the messagebox, dialog box , colorchooser and scrolledtext
from tkinter import messagebox, filedialog, scrolledtext

# Importing from pillow module
from PIL import ImageTk, Image, ImageChops, ImageDraw

# importing textwrap for wrapping the some text
import textwrap

# importing datetime modules for getting the datetime
from datetime import date, timedelta

# importing tkcalendar modules for showing calendars
from tkcalendar import Calendar
# importing babel.numbers module to make the calendar working after converting this app into .exe file
from babel.numbers import *

# importing the autocomplete entry
from ttkwidgets.autocomplete import AutocompleteEntry

# importing random and string for generating numbers and string in random order
import random
import string

# importing sqlite3 for create and work with databases
import sqlite3


root = Tk()
# Giving Title to the root window
root.title("in Voice")

# To remove the toolbar of the root window
root.overrideredirect(True)

# Setting the window width, height and position on the user screen
window_width = 400
window_height = 260

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("%dx%d+%d+%d" % (window_width,
              window_height, x_cordinate, y_cordinate))


# Setting the icon
# Assigning the image as an object of PhotoImage class.
p1 = PhotoImage(file="Images/logo.png")
# Setting icon to the window using iconphoto() method
root.iconphoto(False, p1)

# Assigning the initial values to the timer text
txt1 = "Starting in "
txt2 = 5
txt3 = " s"
dots = "..."

# Assign the images used in this project and this should be predefined
# Opening, resize and Setting image as variable for --- icon ---
icon = Image.open(
    "Images/logo.png").convert("RGBA")
icon = icon.resize((33, 30), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)

# Opening, resize and Setting image as variable for  --- maxi-icon ---
icon1 = Image.open(
    "Images/logo.png").convert("RGBA")
icon1 = icon1.resize((40, 40), Image.ANTIALIAS)
icon1 = ImageTk.PhotoImage(icon1)

# Opening, resize and Setting image as variable for  --- SignIn-icon ---
icon2 = Image.open(
    "Images/logo_C.png").convert("RGBA")
icon2 = icon2.resize((150, 150), Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(icon2)

# Opening, resize and Setting image as variable for  --- Generate Key-icon ---
icon3 = Image.open(
    "Images/key.png").convert("RGBA")
icon3 = icon3.resize((40, 40), Image.ANTIALIAS)
icon3 = ImageTk.PhotoImage(icon3)

# Opening, resize and Setting image as variable for  --- ShowPassword-icon ---
icon4 = Image.open(
    "Images/show.png").convert("RGBA")
icon4 = icon4.resize((30, 30), Image.ANTIALIAS)
icon4 = ImageTk.PhotoImage(icon4)

# Opening, resize and Setting image variable for ---  dashboard icon  ---
icon5 = Image.open(
    "Images/dashboard.png").convert("RGBA")
icon5 = icon5.resize((30, 30), Image.ANTIALIAS)
icon5 = ImageTk.PhotoImage(icon5)

# Opening, resize and Setting image variable for ---  invoice icon  ---
icon6 = Image.open(
    "Images/invoice.png").convert("RGBA")
icon6 = icon6.resize((30, 30), Image.ANTIALIAS)
icon6 = ImageTk.PhotoImage(icon6)

# Opening, resize and Setting image variable for ---  clients icon  ---
icon7 = Image.open(
    "Images/clients.png").convert("RGBA")
icon7 = icon7.resize((40, 40), Image.ANTIALIAS)
icon7 = ImageTk.PhotoImage(icon7)

# Opening, resize and Setting image variable for ---  stocks icon  ---
icon8 = Image.open(
    "Images/stocks.png").convert("RGBA")
icon8 = icon8.resize((30, 30), Image.ANTIALIAS)
icon8 = ImageTk.PhotoImage(icon8)

# Opening, resize and Setting image variable for ---  settings icon  ---
icon9 = Image.open(
    "Images/settings.png").convert("RGBA")
icon9 = icon9.resize((35, 35), Image.ANTIALIAS)
icon9 = ImageTk.PhotoImage(icon9)

# Opening, resize and Setting image variable for ---  sidepanel icon  ---
icon10 = Image.open(
    "Images/fold.png").convert("RGBA")
icon10 = icon10.resize((30, 30), Image.ANTIALIAS)
icon10 = ImageTk.PhotoImage(icon10)

# Opening, resize and Setting image variable for ---  menu icon  ---
icon11 = Image.open(
    "Images/menu.png").convert("RGBA")
icon11 = icon11.resize((40, 40), Image.ANTIALIAS)
icon11 = ImageTk.PhotoImage(icon11)

# Opening, resize and Setting image variable for ---  control icon  ---
icon12 = Image.open(
    "Images/control.png").convert("RGBA")
icon12 = icon12.resize((65, 65), Image.ANTIALIAS)
icon12 = ImageTk.PhotoImage(icon12)

# Opening, resize and Setting image variable for ---  edit icon  ---
icon13 = Image.open(
    "Images/edit.png").convert("RGBA")
icon13 = icon13.resize((40, 40), Image.ANTIALIAS)
icon13 = ImageTk.PhotoImage(icon13)

# Opening, resize and Setting image variable for ---  trash icon  ---
icon14 = Image.open(
    "Images/trash.png").convert("RGBA")
icon14 = icon14.resize((40, 40), Image.ANTIALIAS)
icon14 = ImageTk.PhotoImage(icon14)

# Opening, resize and Setting image variable for ---  calendar icon  ---
icon15 = Image.open(
    "Images/calendar.png").convert("RGBA")
icon15 = icon15.resize((35, 35), Image.ANTIALIAS)
icon15 = ImageTk.PhotoImage(icon15)

# Opening, resize and Setting image variable for ---  profile photo ---
img1 = Image.open(
    "Images/profile.png")
img1 = img1.resize((150, 150), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

img12 = Image.open(
    "Images/profile.png")
img12 = img12.resize((45, 45), Image.ANTIALIAS)
img12 = ImageTk.PhotoImage(img12)

# Assign variable for creating a database in this location
inVoiceDB = ""

# Setting the initial timer value for generate-KEY option
timing = 31

# Assign a variable for naming profile picture
n = 0

# # Assign a variable for creating invoice number
in_number = 0

# Assigning a variable for item_number and for row
item_number = 0

# Setting dummy value for amounts
initial_amount = "%.2f" % 0

# Creating a list for adding the product details table values
productDetail = []

# Creating global variable for converting different country currencies
currency = 1

# Assign value for calculating which entry widget has focus
QuantityEntryFocus = ""
RateEntryFocus = ""


def main():  # function which creates the default template for other functions and widgets

    def settingsTab():  # function for creating settings tab

        # assign a global value for inserting it into another function
        global value
        value = 5

        # this calls the function for workspace layout
        workSpace()

    def stocksTab():  # function for creating stocks tab

        # assign a global value for inserting it into another function
        global value
        value = 4

        # this calls the function for workspace layout
        workSpace()

    def clientsTab():  # function for creating clients tab

        # assign a global value for inserting it into another function
        global value
        value = 3

        # this calls the function for workspace layout
        workSpace()

    def invoicesTab():  # function for creating invoices tab

        # assign a global value for inserting it into another function
        global value
        value = 2

        # this calls the function for workspace layout
        workSpace()

    def workSpace():  # function for creating the working space

        def dashboardTab():  # function for returning back to the dashboard

            # this gets back to the dashboard
            root.after(300, lambda: left_panel.destroy())
            root.after(220, lambda: right_panel.destroy())

        def invoices_btn():  # function for creating the invoices panel

            def limitingOption():  # function for making the full screen non-shrinkable

                def limitingOption5():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with settings button
                        settingsTab()
                        dashboardTab()
                        # Changing the close button function
                        close_button.configure(
                            command=lambda: root.destroy())

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption4():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with stocks button
                        stocksTab()
                        dashboardTab()
                        # Changing the close button function
                        close_button.configure(
                            command=lambda: root.destroy())

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption3():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function for clients panel and closes the add client panel
                        clientsTab()
                        dashboardTab()
                        # Changing the close button function
                        close_button.configure(
                            command=lambda: root.destroy())

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption2():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function to invoice panel
                        invoicesTab()
                        dashboardTab()
                        # Changing the close button function
                        close_button.configure(
                            command=lambda: root.destroy())

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption1():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with dashboard button
                        # Changing the close button function
                        close_button.configure(
                            command=lambda: root.destroy())
                        dashboardTab()

                # changing the function of all option buttons
                option1.configure(command=lambda: limitingOption1())
                option2.configure(style="Options.TLabel",
                                  state=NORMAL, command=lambda: limitingOption2())
                option3.configure(command=lambda: limitingOption3())
                option4.configure(command=lambda: limitingOption4())
                option5.configure(command=lambda: limitingOption5())
                root.after(200, lambda: leftTop_panel_bgImg.unbind(
                    "<Button-1>", unbindExpand))

            def newInvoice():  # function for creating a new invoice template

                def triggeringSavedInvoice():  # function for saving the invoice in txt file

                    # Creating new database for the new user
                    user_inV = sqlite3.connect(
                        str(inVoiceDB)+"in_voice.db")

                    # Creating a cursor
                    co = user_inV.cursor()

                    # Creating a new frame on the rightBottom panel
                    rightBottom2_panel = Frame(right_panel, height=int(screen_height/1.04),
                                               width=int(screen_width-(screen_width/15.1)))
                    rightBottom2_panel.place(relx=1, rely=1, anchor=SE)

                    # Creating a labels for background color of frame
                    rightBottom2_panel_label0 = Label(
                        rightBottom2_panel, background="#B3C6E7", width=int(screen_width/4.6))
                    rightBottom2_panel_label0.place(relx=0.5, rely=0.5, height=int(
                        screen_height/1), anchor=CENTER)

                    # Background and Foreground color for label and the buttons in the leftBottom panel
                    rightBottom2_label1_bG = "#F0EFF4"
                    rightBottom2_label1_fG = "#401414"
                    # Creating a labels for background color
                    rightBottom_panel_label_01 = Label(
                        rightBottom2_panel, background=rightBottom2_label1_bG, width=int(screen_width/6.75))
                    rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                        screen_height/1.1), anchor=CENTER)

                    rightBottom2_panel_fG = "#3C2212"

                    invoicePreview = scrolledtext.ScrolledText(rightBottom2_panel, font=("Dodge", 12, "bold"), foreground=rightBottom2_label1_fG, height=int(
                        screen_height/1.04), width=int(screen_width-(screen_width/15.1)), wrap=WORD)
                    invoicePreview.place(relx=0.5, rely=0.5, anchor=CENTER)

                    # Creating a new frame on the rightBottom panel
                    rightBottom2_panel = Frame(right_panel, height=int(screen_height/1.04),
                                               width=int(screen_width-(screen_width/15.1)))
                    rightBottom2_panel.place(relx=1, rely=1, anchor=SE)

                    # Creating a labels for background color of frame
                    rightBottom2_panel_label0 = Label(
                        rightBottom2_panel, background="#B3C6E7", width=int(screen_width/4.6))
                    rightBottom2_panel_label0.place(relx=0.5, rely=0.5, height=int(
                        screen_height/1), anchor=CENTER)

                    # Background and Foreground color for label and the buttons in the leftBottom panel
                    rightBottom2_label1_bG = "#F0EFF4"
                    rightBottom2_label1_fG = "#401414"
                    # Creating a labels for background color
                    rightBottom_panel_label_01 = Label(
                        rightBottom2_panel, background=rightBottom2_label1_bG, width=int(screen_width/6.75))
                    rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                        screen_height/1.1), anchor=CENTER)

                    # Creating new database for the new user
                    user_inV = sqlite3.connect(
                        str(inVoiceDB)+"in_voice.db")

                    # Creating a cursor
                    co = user_inV.cursor()

                    # query the database
                    co.execute("SELECT *, oid FROM clientDetails WHERE clientName = " +
                               "'" + clientSelect_box.get() + "'")
                    clients = co.fetchall()
                    # print(clients)

                    client_name = ""
                    for client in clients:
                        client_name += str(client[0])

                    client_address1 = ""
                    for client in clients:
                        client_address1 += str(client[3])

                    client_address2 = ""
                    for client in clients:
                        client_address2 += str(client[4])

                    client_address3 = ""
                    for client in clients:
                        client_address3 += str(client[5])

                    rightBottom2_panel_fG = "#3C2212"

                    invoicePreview = scrolledtext.ScrolledText(rightBottom2_panel, font=(
                        "Dodge", 15, "bold"), foreground=rightBottom2_panel_fG, background=rightBottom2_label1_bG, borderwidth=0, width=int(screen_width/13), height=int(screen_height/28), wrap=WORD)
                    invoicePreview.place(relx=0.5, rely=0.5, anchor=CENTER)

                    invoicePreview.delete(1.0, END)
                    invoicePreview.delete(1.0, END)
                    invoicePreview.insert(
                        END, "\n================================================================================================\n")
                    invoicePreview.insert(
                        END, "\n\n\t\t\t\t\t\t\t\t\t\t  [ Invoice No:  "+str(invoiceEntry_Var.get())+" ]")
                    invoicePreview.insert(
                        END, "\n\tClient Details:\n\t\t\t\t\t\t\t\t\t\t   ")
                    invoicePreview.insert(
                        END, "\n\t\t"+str(client_name)+"\r\n\n\t\t"+str(client_address1))
                    invoicePreview.insert(
                        END, "\n\n\t\t"+str(client_address2)+"\r\t\t\t\t\t\t\t\tDated on:  "+str(formatedDate))
                    invoicePreview.insert(
                        END, "\n\n\t\t\t\t\t\t\t\t\t\t\n")
                    invoicePreview.insert(
                        END, "\n================================================================================================\n")
                    invoicePreview.insert(
                        END, "\r\n\tDue Date:  "+str(duedate)+"\t\t\t\t\t\t\t\tBalance Due:  "+str(balanceAmount))
                    invoicePreview.insert(
                        END, "\r\n")
                    invoicePreview.insert(
                        END, "\r\n_________________________________________________________________________________________________________\r\n")
                    invoicePreview.insert(
                        END, "\r\n   #\t\tItem Description\t\t\t\t\t\tRate\t\tQuantity\t\tAmount\r\n")
                    invoicePreview.insert(
                        END, "\r\n_________________________________________________________________________________________________________\r\n")

                    # query the database
                    co.execute("SELECT *, oid FROM itemsPurchased WHERE invoiceNumber = " +
                               "'" + invoiceEntry_Var.get() + "'")
                    items = co.fetchall()

                    for item in items:

                        invoicePreview.insert(
                            END, "\r\n   "+str(item[5])+"\t"+str(item[1])+"\t\t\t\t\t\t\t"+str(item[2])+"\t\t"+str(item[3])+"\t\t"+str(item[4])+"\r\n\n")

                    invoicePreview.insert(
                        END, "\r\n_________________________________________________________________________________________________________\r\n")
                    invoicePreview.insert(
                        END, "\r\n\n\t\t\t\t\t\t\t\t\tSub Total:\t\t"+str(subtotal)+"\r\n")
                    invoicePreview.insert(
                        END, "\r\n\n\t\t\t\t\t\t\t\t\tTax:\t\t"+str(("%.2f" % taxEntryValue))+"\r\n")
                    invoicePreview.insert(
                        END, "\r\n\n\t\t\t\t\t\t\t\t\tTotal:\t\t"+str(totalAmountCalculated)+"\r\n")

                    file = open(str(invoiceEntry_Var.get())+".txt", "w")
                    file.write(invoicePreview.get(1.0, END))
                    file.close()

                    # this calls the function for invoices panel and closes the add invoice panel
                    invoicesTab()
                    dashboardTab()

                    # changing the function of all option buttons back to the previous one
                    option1.configure(
                        command=lambda: dashboardTab())
                    option2.configure(
                        command=lambda: [invoicesTab(), dashboardTab()])
                    option3.configure(
                        command=lambda: [clientsTab(), dashboardTab()])
                    option4.configure(
                        command=lambda: [stocksTab(), dashboardTab()])
                    option5.configure(
                        command=lambda: [settingsTab(), dashboardTab()])

                def saveInvoice():  # function which saves the invoice as word document

                    # Checking for any empty fields
                    if clientSelect_box.get() == "":
                        messagebox.showerror(
                            "Required", "Select a Client to proceed")

                    else:

                        # Creating new database for the new user
                        user_inV = sqlite3.connect(
                            str(inVoiceDB)+"in_voice.db")

                        # Creating a cursor
                        co = user_inV.cursor()

                        # inserting the updated data into table
                        co.execute("SELECT *, oid FROM itemsPicked")
                        products = co.fetchall()
                        # print(products)

                        for productDetail in products:
                            if item_number == productDetail[8]:
                                if item_entry.get() == "" or quantity_entry.get() == "" or rate_entry.get() == "" or amount_entry.get() == "":
                                    messagebox.showerror(
                                        "Empty", "Required field is Empty")

                                else:
                                    messagebox.askyesno(
                                        "Save Invoice", "Before pressing 'yes', make sure the data are correct")

                                    if "yes":

                                        # creating table for the items purchased
                                        co.execute("""CREATE TABLE IF NOT EXISTS itemsPurchased (
                                                        invoiceNumber TEXT,
                                                        itemDescription TEXT,
                                                        itemQuantity INTEGER,
                                                        itemRate REAL,
                                                        itemAmount REAL              
                                                        )""")

                                        # creating table for the invoice details
                                        co.execute("""CREATE TABLE IF NOT EXISTS invoiceDetails (
                                                        invoiceNumber TEXT,
                                                        clientDetails TEXT,
                                                        datePurchased DATE,
                                                        dueDate DATE,
                                                        currency TEXT,
                                                        customerMessage TEXT,
                                                        taxInPercentage INTEGER,
                                                        subTotal REAL,
                                                        calculatedTAX REAL,
                                                        totalAmount REAL,
                                                        balanceAmount REAL           
                                                        )""")

                                        # for productDetail in products:
                                        if productDetail[0] == "":
                                            print("Description Zero: ",
                                                  productDetail[0])
                                        else:

                                            if productDetail[1] == "" or (productDetail[1])*1 == 0:
                                                print("Quantity Zero: ",
                                                      productDetail[0], productDetail[1])

                                            else:
                                                if productDetail[2] == "" or (productDetail[2])*1 == 0:

                                                    print("Rate Zero: ",
                                                          productDetail[0], productDetail[1], productDetail[2])

                                                else:
                                                    global balanceAmount
                                                    if dueSelect_box.get() == "Nil":
                                                        balanceAmount = totalAmountCalculated
                                                    elif not dueSelect_box.get() == "Nil":
                                                        balanceAmount = float(
                                                            totalAmountCalculated)-float(paidAmount_entry.get())

                                                    for productDetail in products:
                                                        co.execute("INSERT INTO itemsPurchased VALUES (:invoiceNumber, :itemDescription, :itemQuantity, :itemRate, :itemAmount)",
                                                                   {
                                                                       "invoiceNumber": invoiceEntry_Var.get(),
                                                                       "itemDescription": productDetail[0],
                                                                       "itemQuantity": productDetail[1],
                                                                       "itemRate": productDetail[2],
                                                                       "itemAmount": productDetail[3],
                                                                   })

                                                    co.execute("INSERT INTO invoiceDetails VALUES (:invoiceNumber, :clientDetails, :datePurchased, :dueDate, :currency, :customerMessage, :taxInPercentage, :subTotal, :calculatedTAX, :totalAmount, :balanceAmount)",
                                                               {
                                                                   "invoiceNumber": invoiceEntry_Var.get(),
                                                                   "clientDetails": clientSelect_box.get(),
                                                                   "datePurchased": formatedDate,
                                                                   "dueDate": duedate,
                                                                   "currency": currencySelect_box.get(),
                                                                   "customerMessage": customernoteEntry.get("1.0", 'end-1c'),
                                                                   "taxInPercentage": taxEntry_box_Var.get(),
                                                                   "subTotal": subtotal,
                                                                   "calculatedTAX": ("%.2f" % taxEntryValue),
                                                                   "totalAmount": totalAmountCalculated,
                                                                   "balanceAmount": balanceAmount
                                                               })

                                                    co.execute(
                                                        "DROP TABLE IF EXISTS itemsPicked")

                                                    # this saves the invoice in text file and calls the function for showing the saved invoice
                                                    triggeringSavedInvoice()

                                                    # Changing the close button function
                                                    close_button.configure(
                                                        command=lambda: root.destroy())
                                    else:
                                        co.execute(
                                            "DROP TABLE IF EXISTS itemsPicked")

                        # commit changes
                        user_inV.commit()

                        # close connection
                        user_inV.close()

                def closeInvoiceApp():  # function for ask save or not the invoice before closing the window
                    close_buttonValue = messagebox.askyesnocancel(
                        "Save & Close", "Do you want to save the invoice?")

                    if close_buttonValue == True:

                        # Checking for any empty fields
                        if clientSelect_box.get() == "":
                            messagebox.showerror(
                                "Required", "Select a Client to proceed")

                        else:

                            # Creating new database for the new user
                            user_inV = sqlite3.connect(
                                str(inVoiceDB)+"in_voice.db")

                            # Creating a cursor
                            co = user_inV.cursor()

                            # inserting the updated data into table
                            co.execute("SELECT *, oid FROM itemsPicked")
                            products = co.fetchall()
                            # print(products)

                            for productDetail in products:
                                if item_number == productDetail[8]:
                                    if item_entry.get() == "" or quantity_entry.get() == "" or rate_entry.get() == "" or amount_entry.get() == "":
                                        messagebox.showerror(
                                            "Empty", "Required field is Empty")

                                    else:
                                        messagebox.askyesno(
                                            "Save Invoice", "Before pressing 'yes', make sure the data are correct")

                                        if "yes":

                                            # creating table for the items purchased
                                            co.execute("""CREATE TABLE IF NOT EXISTS itemsPurchased (
                                                            invoiceNumber TEXT,
                                                            itemDescription TEXT,
                                                            itemQuantity INTEGER,
                                                            itemRate REAL,
                                                            itemAmount REAL              
                                                            )""")

                                            # Creating a table invoiceDetails
                                            co.execute("""CREATE TABLE IF NOT EXISTS invoiceDetails (
                                                            invoiceNumber TEXT,
                                                            clientDetails TEXT,
                                                            datePurchased DATE,
                                                            dueDate DATE,
                                                            currency TEXT,
                                                            customerMessage TEXT,
                                                            taxInPercentage INTEGER,
                                                            subTotal REAL,
                                                            calculatedTAX REAL,
                                                            totalAmount REAL,
                                                            balanceAmount REAL           
                                                            )""")

                                            # for productDetail in products:
                                            if productDetail[0] == "":
                                                print("Description Zero: ",
                                                      productDetail[0])
                                            else:

                                                if productDetail[1] == "" or (productDetail[1])*1 == 0:
                                                    print("Quantity Zero: ",
                                                          productDetail[0], productDetail[1])

                                                else:
                                                    if productDetail[2] == "" or (productDetail[2])*1 == 0:

                                                        print("Rate Zero: ",
                                                              productDetail[0], productDetail[1], productDetail[2])

                                                    else:

                                                        if dueSelect_box.get() == "Nil":
                                                            balanceAmount = totalAmountCalculated
                                                        elif not dueSelect_box.get() == "Nil":
                                                            balanceAmount = float(
                                                                totalAmountCalculated)-float(paidAmount_entry.get())

                                                        for productDetail in products:
                                                            co.execute("INSERT INTO itemsPurchased VALUES (:invoiceNumber, :itemDescription, :itemQuantity, :itemRate, :itemAmount)",
                                                                       {
                                                                           "invoiceNumber": invoiceEntry_Var.get(),
                                                                           "itemDescription": productDetail[0],
                                                                           "itemQuantity": productDetail[1],
                                                                           "itemRate": productDetail[2],
                                                                           "itemAmount": productDetail[3],
                                                                       })

                                                        co.execute("INSERT INTO invoiceDetails VALUES (:invoiceNumber, :clientDetails, :datePurchased, :dueDate, :currency, :customerMessage, :taxInPercentage, :subTotal, :calculatedTAX, :totalAmount, :balanceAmount)",
                                                                   {
                                                                       "invoiceNumber": invoiceEntry_Var.get(),
                                                                       "clientDetails": clientSelect_box.get(),
                                                                       "datePurchased": formatedDate,
                                                                       "dueDate": duedate,
                                                                       "currency": currencySelect_box.get(),
                                                                       "customerMessage": customernoteEntry.get("1.0", 'end-1c'),
                                                                       "taxInPercentage": taxEntry_box_Var.get(),
                                                                       "subTotal": subtotal,
                                                                       "calculatedTAX": ("%.2f" % taxEntryValue),
                                                                       "totalAmount": totalAmountCalculated,
                                                                       "balanceAmount": balanceAmount
                                                                   })

                                                        co.execute(
                                                            "DROP TABLE IF EXISTS itemsPicked")
                                        else:
                                            co.execute(
                                                "DROP TABLE IF EXISTS itemsPicked")

                            # commit changes
                            user_inV.commit()

                            # close connection
                            user_inV.close()

                        # closing the app
                        root.after(100, lambda: root.destroy())

                    elif close_buttonValue == False:
                        # closing the app
                        root.destroy()

                # function for calculating the custom tax and also checks input is a whole number
                def check_taxEntry(var, index, mode):

                    # neglecting the empty value
                    if taxEntry_box_Var.get() == "":
                        return
                    else:
                        try:  # if value is integer
                            int(taxEntry_box_Var.get())

                            global subtotal
                            subtotal = 0
                            for productamount in productDetail:
                                subtotal = int(subtotal) + \
                                    int(float(productamount.get()))

                            # calculating the tax from user entry
                            global taxEntryValue
                            taxEntryValue = int(subtotal) * \
                                ((int(taxEntry_box_Var.get())/100))
                            taxEntry.configure(text="%.2f" % taxEntryValue)

                            global totalAmountCalculated
                            totalAmountCalculated = "%.2f" % int(
                                subtotal + taxEntryValue)
                            totalEntry.configure(text=totalAmountCalculated)

                            # limiting tax value
                            if len(taxEntry_box_Var.get()) > 2:
                                messagebox.showerror(
                                    "EntryError", "Exceeded tax percentage")
                                taxEntry_box_Var.set(0)

                        except ValueError:  # if value is other than integers
                            taxEntry_box_Var.set(0)

                # function for deleting the value in taxEntry_box
                def deleteTaxEntry(event):

                    # deleting the value
                    taxEntry_box.delete(0, END)
                    taxEntry_box.unbind("<Button-1>", taxEntry_box0)

                # function for deleting the text in customer note
                def deleteCustomerNote(event):

                    # deleting the pre-occupied message
                    customernoteEntry.delete(1.0, END)
                    customernoteEntry.unbind("<Button-1>", customernoteEntry0)

                # function which scrolls the fields according to the mouse wheel over product details table
                def scroll_tableFields(event):

                    # moving canvas to the exact value mouse wheel rotates
                    invoiceTable_fields_canvas.yview_scroll(
                        int(-1*(event.delta/120)), "units")

                def addRow():  # function which add new entry rows

                    # function for adding the each item total as a subtotal
                    def update_amountEntry():

                        # neglecting the empty value
                        if amount_entry_Var.get() == "":
                            return
                        else:

                            try:  # if value is float or integer
                                float(amount_entry_Var.get())

                                global subtotal
                                subtotal = 0
                                for productamount in productDetail:
                                    subtotal = int(subtotal) + \
                                        int(float(productamount.get()))
                                # print(productDetail)
                                # print("%.2f" % subtotal)

                                # Changing the subtotal, tax and  total
                                subtotalEntry.configure(
                                    text="%.2f" % subtotal)

                                global taxEntryValue
                                taxEntryValue = int(subtotal) * \
                                    ((int(taxEntry_box_Var.get())/100))
                                taxEntry.configure(text="%.2f" % taxEntryValue)

                                global totalAmountCalculated
                                totalAmountCalculated = "%.2f" % int(
                                    subtotal + taxEntryValue)
                                totalEntry.configure(
                                    text=totalAmountCalculated)

                            # if value is other than floats or integer
                            except ValueError:
                                amount_entry_Var.set("%.2f" % 0)

                    # function for checking the value of rate is float or not
                    def update_rateEntry(var, index, mode):

                        # neglecting the empty value
                        if rate_entry_Var.get() == "":
                            return
                        else:
                            try:  # if value is float or integer
                                float(rate_entry_Var.get())

                                global item_amount
                                item_amount = (float(
                                    quantity_entry_Var.get())) * (float(rate_entry_Var.get()))

                                # Changing the amount with the calculated value
                                amount_entry_Var.set("%.2f" % item_amount)

                                # Creating new database for the new user
                                user_inV = sqlite3.connect(
                                    str(inVoiceDB)+"in_voice.db")

                                # Creating a cursor
                                co = user_inV.cursor()

                                # inserting the updated data into table
                                co.execute("UPDATE itemsPicked SET itemRate = :itemRate, itemamount = :itemamount WHERE rateEntry_ID = :rateEntry_ID",
                                           {
                                               "itemRate": rate_entry_Var.get(),
                                               "itemamount": amount_entry_Var.get(),

                                               "rateEntry_ID": RateEntryFocus
                                           })

                                # commit changes
                                user_inV.commit()

                                # close connection
                                user_inV.close()

                                # calling the function to calculate total amount
                                update_amountEntry()

                            # if value is other than floats or integer
                            except (ValueError, TclError, FloatingPointError):
                                rate_entry_Var.set("%.2f" % 0.00)

                    # function for checking the value of quantity is integer or not
                    def check_quantityEntry(var, index, mode):

                        # this shows error when item description is empty
                        if item_entry_Var.get() == "":

                            quantity_entry_Var.set("")

                        else:
                            # neglecting the empty value
                            if quantity_entry_Var.get() == "":
                                return
                            else:
                                try:  # if value is integer
                                    int(quantity_entry_Var.get())

                                    global item_amount
                                    item_amount = "%.2f" % ((float(
                                        quantity_entry_Var.get())) * (float(rate_entry_Var.get())))

                                    # Changing the amount with the calculated value
                                    amount_entry_Var.set(item_amount)

                                    # Creating new database for the new user
                                    user_inV = sqlite3.connect(
                                        str(inVoiceDB)+"in_voice.db")

                                    # Creating a cursor
                                    co = user_inV.cursor()

                                    # inserting the updated data into table
                                    co.execute("UPDATE itemsPicked SET itemquantity = :itemquantity, itemamount = :itemamount WHERE quantityEntry_ID = :quantityEntry_ID",
                                               {
                                                   "itemquantity": quantity_entry_Var.get(),
                                                   "itemamount": amount_entry_Var.get(),

                                                   "quantityEntry_ID": QuantityEntryFocus
                                               })

                                    # commit changes
                                    user_inV.commit()

                                    # close connection
                                    user_inV.close()

                                    # calling the function to calculate total amount
                                    update_amountEntry()

                                except ValueError:  # if value is other than integers
                                    quantity_entry_Var.set(0)

                    # function for getting and setting the rate for the item entered
                    def update_itemEntry(var, index, mode):

                        # function for deleting the value in quantity_entry
                        def delete_entry(event):

                            quantity_entry.delete(0, END)
                            quantity_entry.unbind(
                                "<Double-1>", quantity_entry0)

                        # print(quantity_entry.get())
                        # quantity_entry_Var.set("")

                        # Creating new database for the new user
                        user_inV = sqlite3.connect(
                            str(inVoiceDB)+"in_voice.db")

                        # Creating a cursor
                        co = user_inV.cursor()

                        # query the database
                        co.execute("SELECT * FROM productDetails WHERE productName = " +
                                   "'" + item_entry_Var.get() + "'")
                        items = co.fetchall()
                        # print(items)
                        # itemName = [r for r, in items]
                        # print(itemName)

                        # Getting the product name according to the input
                        productName = ""
                        for item in items:
                            productName += str(item[0])

                        productQuantity = ""
                        for item in items:
                            productQuantity += str(item[2])

                        # Getting the product rate if user input matches the product name in database
                        if item_entry_Var.get() == productName:

                            productPrice = ""
                            for item in items:
                                productPrice += str(item[4])

                                # Setting the product rate for the product selected
                                try:
                                    rate_entry_Var.set("%.2f" %
                                                       float(float(productPrice)/float(currency)))

                                except ValueError:
                                    item_entry_Var.set("")

                                # Updating fields to the itemsPicked table
                                co.execute("UPDATE itemsPicked SET itemDescription = :itemDescription, itemRate = :itemRate WHERE itemEntry_ID = :itemEntry_ID",
                                           {
                                               "itemDescription": item_entry_Var.get(),
                                               "itemRate": rate_entry_Var.get(),

                                               "itemEntry_ID": ItemEntryFocus
                                           })

                        else:
                            rate_entry_Var.set("%.2f" % 0)

                        # Updating fields to the itemsPicked table
                        co.execute("UPDATE itemsPicked SET itemDescription = :itemDescription WHERE itemEntry_ID = :itemEntry_ID",
                                   {
                                       "itemDescription": item_entry_Var.get(),

                                       "itemEntry_ID": ItemEntryFocus
                                   })

                        # commit changes
                        user_inV.commit()

                        # close connection
                        user_inV.close()

                        # this triggers the function to clear quantity_entry
                        quantity_entry0 = quantity_entry.bind(
                            "<Double-1>", delete_entry)

                    # function for getting the current RateEntry widget value
                    def gettingRateEntry_focus(event):

                        # Setting that value as string to a global variable
                        global RateEntryFocus
                        RateEntryFocus = str(event.widget)

                    # function for getting the current quantityEntry widget value
                    def gettingQuantityEntry_focus(event):

                        # Setting that value as string to a global variable
                        global QuantityEntryFocus
                        QuantityEntryFocus = str(event.widget)

                    # function for getting the current itemEntry widget value
                    def gettingItemEntry_focus(event):

                        # Setting that value as string to a global variable
                        global ItemEntryFocus
                        ItemEntryFocus = str(event.widget)

                    # function for enable the invoice entry by entered_amountEntry() function
                    def leaved_amountEntry(event):

                        # making it editable
                        amount_entry.configure(state=NORMAL)

                    # function for disabling the invoice entry by the mouse hover over amount_entry
                    def entered_amountEntry(event):

                        # making it non-editable
                        # Styling updateDate button
                        amount_entry_style = Style()
                        amount_entry_style.theme_use("default")
                        # mouse hover style for updateDate button
                        amount_entry_style.map("AmountEntry.TEntry", foreground=[(
                            "active", "disabled", "black")], fieldbackground=[("active", "disabled", "white")])
                        amount_entry.configure(
                            style="AmountEntry.TEntry", state=DISABLED)

                    # Creating the individual fields for product details table row
                    global item_number
                    item_number += 1

                    # ---------------------
                    #      Item Number
                    # ---------------------

                    number_entry = Label(invoiceTable_fields_frame,
                                         text=item_number, background=field_bgColor, font=("Dodge", 14, "bold"), anchor=CENTER)
                    number_entry.grid(row=item_number, column=0,
                                      padx=(40, 0), pady=(20, 6))

                    # Database for table in stocks
                    # Creating new database for the new user
                    user_inV = sqlite3.connect(
                        str(inVoiceDB)+"in_voice.db")

                    # Creating a cursor
                    co = user_inV.cursor()

                    # Creating a table productDetails
                    co.execute("""CREATE TABLE IF NOT EXISTS productDetails (
                                    productName TEXT,
                                    productMRP REAL,
                                    quantity INTEGER,
                                    purchaseRate REAL,
                                    salesRate REAL,
                                    reOrderQuantity INTEGER
                                    )""")

                    # query the database
                    co.execute("SELECT productName FROM productDetails")
                    items = co.fetchall()
                    description = [r for r, in items]
                    # print(description)

                    # ---------------------
                    #   Item Description
                    # ---------------------

                    item_entry_Var = StringVar()
                    global item_entry
                    # Creating a entry for product description
                    item_entry = AutocompleteEntry(invoiceTable_fields_frame, textvariable=item_entry_Var, width=int(
                        screen_width/45), font=("Dodge", 12, "bold"), completevalues=description)
                    item_entry.grid(row=item_number, column=1, ipady=6,
                                    padx=(50, 0), pady=(20, 6))

                    # this triggers the function add the product value related to the name
                    item_entry_Var.trace_add("write", update_itemEntry)

                    # commit changes
                    user_inV.commit()

                    # close connection
                    user_inV.close()

                    # ---------------------
                    #       Quantity
                    # ---------------------

                    quantity_entry_Var = StringVar()
                    quantity_entry_Var.set(0)

                    global quantity_entry
                    # Creating a entry for product quantity
                    quantity_entry = tk.Entry(invoiceTable_fields_frame,
                                              font=("Dodge", 14, "bold"), textvariable=quantity_entry_Var, width=int(screen_width/180), justify=RIGHT)
                    quantity_entry.grid(row=item_number, column=2, ipady=6,
                                        padx=(250, 0), pady=(20, 6))

                    # this triggers the function to check the input is a integer
                    quantity_entry_Var.trace_add("write", check_quantityEntry)

                    # ---------------------
                    #         Rate
                    # ---------------------

                    rate_entry_Var = StringVar()
                    rate_entry_Var.set("%.2f" % 0)

                    global rate_entry
                    # Creating a entry for product rate
                    rate_entry = tk.Entry(invoiceTable_fields_frame,
                                          font=("Dodge", 14, "bold"), textvariable=rate_entry_Var, width=int(screen_width/150), justify=RIGHT)
                    rate_entry.grid(row=item_number, column=3, ipady=6,
                                    padx=(70, 0), pady=(20, 6))

                    # this triggers the function for calculating the amount
                    rate_entry_Var.trace_add("write", update_rateEntry)

                    # ---------------------
                    #       amount
                    # ---------------------
                    # global productDetail

                    amount_entry_Var = StringVar()
                    amount_entry_Var.set("%.2f" % 0)

                    global amount_entry
                    # Creating a entry for product amount
                    amount_entry = Entry(invoiceTable_fields_frame,
                                         font=("Dodge", 14, "bold"), textvariable=amount_entry_Var, width=int(screen_width/120), cursor="arrow", justify=RIGHT)
                    amount_entry.grid(row=item_number, column=4, ipady=6,
                                      padx=(60, 0), pady=(20, 6))

                    productDetail.append(amount_entry)

                    # this calls the function assigned with the mouse hover over amount entry
                    amount_entry.bind("<Enter>", entered_amountEntry)
                    amount_entry.bind("<Leave>", leaved_amountEntry)

                    # this calls the function to scroll the canvas widget
                    number_entry.bind("<MouseWheel>", scroll_tableFields)
                    item_entry.bind("<MouseWheel>", scroll_tableFields)
                    quantity_entry.bind("<MouseWheel>", scroll_tableFields)
                    rate_entry.bind("<MouseWheel>", scroll_tableFields)
                    amount_entry.bind("<MouseWheel>", scroll_tableFields)

                    # Creating new database for the new user
                    user_inV = sqlite3.connect(
                        str(inVoiceDB)+"in_voice.db")

                    # Creating a cursor
                    co = user_inV.cursor()

                    # Creating a table itemsPicked
                    co.execute("""CREATE TABLE IF NOT EXISTS itemsPicked (
                            itemDescription TEXT,
                            itemQuantity INTEGER,
                            itemRate REAL,
                            itemAmount REAL,
                            itemEntry_ID TEXT,
                            quantityEntry_ID TEXT,
                            rateEntry_ID TEXT,
                            amountEntry_ID TEXT
                            )""")

                    # Inserting new fields to the itemsPicked table
                    co.execute("INSERT INTO itemsPicked VALUES (:itemDescription, :itemquantity, :itemrate, :itemamount, :itemEntry_ID, :quantityEntry_ID, :rateEntry_ID, :amountEntry_ID)",
                               {
                                   "itemDescription": item_entry.get(),
                                   "itemquantity": quantity_entry.get(),
                                   "itemrate": rate_entry.get(),
                                   "itemamount": amount_entry.get(),
                                   "itemEntry_ID": str(item_entry),
                                   "quantityEntry_ID": str(quantity_entry),
                                   "rateEntry_ID": str(rate_entry),
                                   "amountEntry_ID": str(amount_entry)
                               })
                    # commit changes
                    user_inV.commit()

                    # close connection
                    user_inV.close()

                    # this calls the function assigned with the mouse left click over particular widgets
                    item_entry.bind("<Button-1>", gettingItemEntry_focus)
                    quantity_entry.bind(
                        "<Button-1>", gettingQuantityEntry_focus)
                    rate_entry.bind("<Button-1>", gettingRateEntry_focus)

                # function for setting the whole canvas wigdet scrollable
                def onFrameConfigure(invoiceTable_fields_canvas):

                    # Setting the scrollable area of canvas to all
                    invoiceTable_fields_canvas.configure(
                        scrollregion=invoiceTable_fields_canvas.bbox("all"))

                # function for calculating the due date according to the billing date
                def dueValue(event):

                    def checkPaidAmount(var, index, mode):

                        # neglecting the empty value
                        if paidAmount_entry_var.get() == "":
                            return
                        else:
                            try:  # if value is float or integer
                                float(paidAmount_entry_var.get())

                            # if value is other than floats or integer
                            except (ValueError, TclError, FloatingPointError):
                                paidAmount_entry_var.set("%.2f" % 0.00)

                    global duedate

                    if dueSelect_box.get() == " Nil":

                        duedate = "Nil"

                    if dueSelect_box.get() == " 7 days":

                        duedate = str(todayDate + timedelta(days=7))

                    if dueSelect_box.get() == " 14 days":

                        duedate = str(todayDate + timedelta(days=14))

                    if dueSelect_box.get() == " 28 days":

                        duedate = str(todayDate + timedelta(days=28))

                    if dueSelect_box.get() == " 84 days":

                        duedate = str(todayDate + timedelta(days=84))

                    if not dueSelect_box.get() == " Nil":

                        # label for paid amount entry
                        paidAmountEntry_label = Label(rightBottom1_panel, text="Amount Paid", font=(
                            "Dodge", 14, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                        paidAmountEntry_label.place(
                            relx=0.6, rely=0.1, anchor=CENTER)

                        # Entry for paid amount
                        global paidAmount_entry
                        paidAmount_entry_var = StringVar()
                        paidAmount_entry = Entry(rightBottom1_panel, textvariable=paidAmount_entry_var,
                                                 font=("Dodge", 13, "bold"), width=int(screen_width/70), justify=CENTER)
                        paidAmount_entry.place(
                            relx=0.6, rely=0.15, height=int(screen_height/23), anchor=CENTER)

                        # this function checks the input is a valid number or not
                        paidAmount_entry_var.trace_add(
                            "write", checkPaidAmount)

                def calendarShow():  # function for displaying a calendar

                    def updateDate():  # function for update today's date with preferred date

                        # Changing dateEntry label with user modified date
                        global formatedDate
                        formatedDate = (calendar_label.get_date()) + " "
                        dateEntry.configure(text=formatedDate)

                        # deleting calendar and set button
                        updateDate_btn.destroy()
                        calendar_label.destroy()

                        # enabling the disabled function
                        calendar_Btn.configure(state=NORMAL)

                    # this prevents the function to be called twice by disabling the button
                    calendar_Btn.configure(state=DISABLED)

                    # Creating a calendar and displaying it on the screen
                    calendar_label = Calendar(
                        rightBottom1_panel, date_pattern="y-mm-dd", selectmode="day", year=todayDate.year, month=todayDate.month, day=todayDate.day)
                    calendar_label.place(relx=0.66, rely=0.39, anchor=CENTER)

                    # Adding a button to update the date entry
                    # Styling updateDate button
                    updateDate_btn_style = Style()
                    updateDate_btn_style.theme_use("default")
                    updateDate_btn_style.configure("UpdateButton.TButton", font=("Dodge", 12, "bold"),
                                                   foreground=rightBottom1_label1_fG, borderwidth=0, width=6, focuscolor="none", relief=FLAT, highlightthickness=0)
                    # mouse hover style for updateDate button
                    updateDate_btn_style.map("UpdateButton.TButton", foreground=[(
                        "active", "!disabled", "#011932")], background=[("active", "#B9B5B0")])

                    updateDate_btn = Button(
                        rightBottom1_panel, text="Set", style="UpdateButton.TButton", command=lambda: updateDate())
                    updateDate_btn.place(relx=0.73, rely=0.53, anchor=CENTER)

                # function for changing the currency symbol and value related to currencySelect combobox values
                def currencyValue(event):

                    # Creating new database for the new user
                    user_inV = sqlite3.connect(
                        str(inVoiceDB)+"in_voice.db")

                    # Creating a cursor
                    co = user_inV.cursor()

                    # query the database
                    co.execute(
                        "SELECT *, oid FROM updateCurrency WHERE currrency = " + "'" + str(currencySelect_box.get()) + "'")
                    currencys = co.fetchall()

                    global currency
                    currency = ""
                    for currency_value in currencys:
                        currency += str(currency_value[1])

                    # Getting the currencySelect combobox values
                    if currencySelect_box.get() == " USD $":  # United States Dollar

                        currency_symbolLabel.configure(text="$")
                        invoiceTable_heading4_sym.configure(text="$")
                        invoiceTable_heading5_sym.configure(text="$")

                    if currencySelect_box.get() == " EUR €":  # Euro

                        currency_symbolLabel.configure(text="€")
                        invoiceTable_heading4_sym.configure(text="€")
                        invoiceTable_heading5_sym.configure(text="€")

                    if currencySelect_box.get() == " INR ₹":

                        currency_symbolLabel.configure(text="₹")
                        invoiceTable_heading4_sym.configure(text="₹")
                        invoiceTable_heading5_sym.configure(text="₹")

                    if currencySelect_box.get() == " JPY ¥":  # Japanese Yen

                        currency_symbolLabel.configure(text="¥")
                        invoiceTable_heading4_sym.configure(text="¥")
                        invoiceTable_heading5_sym.configure(text="¥")

                    if currencySelect_box.get() == " GBP £":  # British Pound

                        currency_symbolLabel.configure(text="£")
                        invoiceTable_heading4_sym.configure(text="£")
                        invoiceTable_heading5_sym.configure(text="£")

                    if currencySelect_box.get() == " CHF":  # Swiss Franc

                        currency_symbolLabel.configure(text="  CHF")
                        invoiceTable_heading4_sym.configure(text="  CHF")
                        invoiceTable_heading5_sym.configure(text="  CHF")

                    if currencySelect_box.get() == " CAD $":  # Canadian Dollar

                        currency_symbolLabel.configure(text="$")
                        invoiceTable_heading4_sym.configure(text="$")
                        invoiceTable_heading5_sym.configure(text="$")

                    if currencySelect_box.get() == " AUD $":  # Australian Dollar

                        currency_symbolLabel.configure(text="$")
                        invoiceTable_heading4_sym.configure(text="$")
                        invoiceTable_heading5_sym.configure(text="$")

                    if currencySelect_box.get() == " NZD $":  # New Zealand Dollar

                        currency_symbolLabel.configure(text="$")
                        invoiceTable_heading4_sym.configure(text="$")
                        invoiceTable_heading5_sym.configure(text="$")

                    if currencySelect_box.get() == " ZAR R":  # South African Rand

                        currency_symbolLabel.configure(text="R")
                        invoiceTable_heading4_sym.configure(text="R")
                        invoiceTable_heading5_sym.configure(text="R")

                # function for enable the invoice entry by entered_invoiceNumber() function
                def leaved_invoiceNumber(event):

                    # making it editable
                    invoiceEntry.configure(state=NORMAL)

                # function for disabling the invoice entry by the mouse hover over invoiceEntry
                def entered_invoiceNumber(event):

                    # making it non-editable
                    invoiceEntry.configure(state=DISABLED)

                # this function makes the panel non-shrikable
                limitingOption()

                # Changing the close button function
                close_button.configure(command=lambda: closeInvoiceApp())

                # Creating a new frame on the rightBottom panel
                rightBottom1_panel = Frame(right_panel, height=int(screen_height/1.044),
                                           width=int(screen_width-(screen_width/15.1)))
                rightBottom1_panel.place(relx=1, rely=1, anchor=SE)

                # Creating a labels for background color of frame
                rightBottom1_panel_label0 = Label(
                    rightBottom1_panel, background="#B3C6E7", width=int(screen_width/4.6))
                rightBottom1_panel_label0.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1), anchor=CENTER)

                # Background and Foreground color for label and the buttons in the leftBottom panel
                rightBottom1_label1_bG = "#F0EFF4"
                rightBottom1_label1_fG = "#401414"
                # Creating a labels for background color
                rightBottom_panel_label_01 = Label(
                    rightBottom1_panel, background=rightBottom1_label1_bG, width=int(screen_width/6.75))
                rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1.1), anchor=CENTER)

                # Creating labels of invoice create panel
                # Client entry label
                clientSelect_box_label = Label(
                    rightBottom1_panel, text="Client", font=("Dodge", 14), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                clientSelect_box_label.place(
                    relx=0.13, rely=0.1, anchor=CENTER)

                # Invoice entry label
                invoiceEntry_label = Label(
                    rightBottom1_panel, text="Invoice No.", font=("Dodge", 14), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                invoiceEntry_label.place(relx=0.83, rely=0.1, anchor=CENTER)

                # Currency entry label
                currencySelect_box_label = Label(
                    rightBottom1_panel, text="Currency", font=("Dodge", 14), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                currencySelect_box_label.place(
                    relx=0.14, rely=0.25, anchor=CENTER)

                # date entry label
                dateEntry_label = Label(
                    rightBottom1_panel, text="Date", font=("Dodge", 14), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                dateEntry_label.place(relx=0.47, rely=0.25, anchor=CENTER)

                # due entry label
                dueSelect_box_label = Label(
                    rightBottom1_panel, text="Due", font=("Dodge", 14), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                dueSelect_box_label.place(relx=0.82, rely=0.25, anchor=CENTER)

                # sub Total label
                subtotalEntry_label = Label(
                    rightBottom1_panel, text="Subtotal", font=("Dodge", 12), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                subtotalEntry_label.place(relx=0.71, rely=0.76, anchor=CENTER)

                # tax label
                taxEntry_label = Label(
                    rightBottom1_panel, text="Tax (%)", font=("Dodge", 11), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                taxEntry_label.place(relx=0.7, rely=0.81, anchor=CENTER)

                # Getting the previous invoice number
                # Creating new database for the new user
                user_inV = sqlite3.connect(
                    str(inVoiceDB)+"in_voice.db")

                # Creating a cursor
                co = user_inV.cursor()

                # Creating a table clientDetails if not exists
                co.execute("""CREATE TABLE IF NOT EXISTS clientDetails (
                                clientName TEXT,
                                emailId TEXT,
                                contactNumber Integer,
                                addressLine1 TEXT,
                                addressLine2 TEXT,
                                addressLine3 TEXT,
                                cityName TEXT,
                                pinCode TEXT,
                                customerNote TEXT
                                )""")

                # query the database
                co.execute(
                    "SELECT *, oid FROM clientDetails")
                clients = co.fetchall()

                # Making a tuple from database
                clientName_s = []
                for client in clients:
                    clientName_s.append(client[0])
                # print(clientName_s)

                # Creating entries of invoice create panel
                # Styling the Combobox invoice create panel
                invoiceCreate_btn_style = Style(rightBottom1_panel)
                invoiceCreate_btn_style.theme_use("default")
                invoiceCreate_btn_style.configure(
                    "InvoiceSelect.TCombobox")
                # Changing the mapping style of Combobox invoice create panel
                invoiceCreate_btn_style.map("InvoiceSelect.TCombobox", fieldbackground=[("readonly", "!focus", "white"), ("readonly", "focus", "white")],
                                            selectbackground=[("readonly", "!focus", "none"), ("readonly", "focus", "none")], selectforeground=[("readonly", "focus", "#0A0908"), ("readonly", "!focus", rightBottom1_label1_fG)])

                # Client select
                clientSelect_box = Combobox(rightBottom1_panel, font=("Dodge", 10, "bold"), style="InvoiceSelect.TCombobox",
                                            width=int(screen_width/25), state="readonly")
                clientSelect_box.place(
                    relx=0.09, rely=0.15, height=int(screen_height/25), anchor=W)

                # assigning values to dropdown box
                clientSelect_box["values"] = clientName_s

                # Invoice entry
                invoiceEntry_Var = StringVar()
                invoiceEntry = tk.Entry(rightBottom1_panel, textvariable=invoiceEntry_Var,
                                        font=("Dodge", 13, "bold"), width=int(screen_width/80), borderwidth=2, cursor="arrow", relief=GROOVE, justify=RIGHT)
                invoiceEntry.place(relx=0.85, rely=0.15, height=int(
                    screen_height/25), anchor=CENTER)

                # Creating a table invoiceDetails
                co.execute("""CREATE TABLE IF NOT EXISTS invoiceDetails (
                                invoiceNumber TEXT,
                                clientDetails TEXT,
                                datePurchased DATE,
                                dueDate DATE,
                                currency TEXT,
                                customerMessage TEXT,
                                taxInPercentage INTEGER,
                                subTotal REAL,
                                calculatedTAX REAL,
                                totalAmount REAL,
                                balanceAmount REAL              
                                )""")

                # query the database
                co.execute(
                    "SELECT *, oid FROM invoiceDetails ORDER BY invoiceNumber")

                invoices = co.fetchall()

                global in_number
                for invoice in invoices:
                    in_number = invoice[11]

                # Adding the next invoice number
                in_number += 1

                if len(str(in_number)) < 2:
                    invoiceEntry_Var.set("inV#00" + str(in_number))

                elif len(str(in_number)) < 3:
                    invoiceEntry_Var.set("inV#0" + str(in_number))

                else:
                    invoiceEntry_Var.set("inV#" + str(in_number))

                # commit changes
                user_inV.commit()

                # close connection
                user_inV.close()

                # this calls the function assigned with the mouse hover over invoice entry
                invoiceEntry.bind("<Enter>", entered_invoiceNumber)
                invoiceEntry.bind("<Leave>", leaved_invoiceNumber)

                # Currency select
                currencySelect_box = Combobox(rightBottom1_panel, font=("Dodge", 10, "bold"), style="InvoiceSelect.TCombobox",
                                              width=int(screen_width/40), state="readonly")

                currencySelect_box.place(relx=0.09, rely=0.3,
                                         height=int(screen_height/30), anchor=W)

                # assigning values to dropdown box
                currencySelect_box["values"] = (" USD $",
                                                " EUR €",
                                                " INR ₹",
                                                " JPY ¥",
                                                " GBP £",
                                                " CHF",
                                                " CAD $",
                                                " AUD $",
                                                " NZD $",
                                                " ZAR R")
                currencySelect_box.current(2)
                # # Assigning a function with currency select
                currencySelect_box.bind("<<ComboboxSelected>>", currencyValue)

                # CurrentDate entry
                # setting current date as today
                todayDate = date.today()
                formatedDate = str(todayDate)+" "
                dateEntry = Label(rightBottom1_panel, text=formatedDate,
                                  font=("Dodge", 12, "bold"), width=int(screen_width/80), background="white", borderwidth=1, relief=SUNKEN, anchor=E)
                dateEntry.place(relx=0.5, rely=0.3, height=int(
                    screen_height/25), anchor=CENTER)

                # Adding the calendar in button
                # Styling calendar button
                calendar_Btn_style = Style()
                calendar_Btn_style.theme_use("default")
                calendar_Btn_style.configure("Calendar.TButton", font=("Playball", 16, "italic"), background=rightBottom1_label1_bG,
                                             foreground=rightBottom1_label1_fG, borderwidth=0, width=6, focuscolor="none", relief=FLAT, highlightthickness=0)
                # mouse hover style for calendar button
                calendar_Btn_style.map("Calendar.TButton", foreground=[(
                    "active", "!disabled", "#F0EFF4")], background=[("active", "#B9B5B0")])
                calendar_Btn = Button(rightBottom1_panel,
                                      image=icon15, style="Calendar.TButton", command=lambda: calendarShow())
                calendar_Btn.place(relx=0.59, rely=0.3, anchor=CENTER)

                # Due Date select
                global dueSelect_box
                dueSelect_box = Combobox(rightBottom1_panel, font=("Dodge", 10, "bold"), style="InvoiceSelect.TCombobox",
                                         width=int(screen_width/80), state="readonly")
                dueSelect_box.place(relx=0.8, rely=0.3,
                                    height=int(screen_height/30), anchor=W)

                # assigning values to dropdown box
                dueSelect_box["values"] = (" Nil",
                                           " 7 days",
                                           " 14 days",
                                           " 28 days",
                                           " 84 days")
                dueSelect_box.current(0)

                # Calculating due date according to the initial value
                if dueSelect_box.get() == " Nil":

                    duedate = "Nil"
                # Assign a function with due select
                dueSelect_box.bind("<<ComboboxSelected>>", dueValue)

                # Creating a table for product details
                # Creating a frame for the product details table header
                invoiceTable_header0 = Frame(rightBottom1_panel, height=int(screen_height/10),
                                             width=int(screen_width-(screen_width/5.5)))
                invoiceTable_header0.place(relx=0.5, rely=0.45, anchor=CENTER)

                # Setting background color for product details table header
                invoiceTable_header0_bgColor = Label(
                    invoiceTable_header0, background=header_bgColor)
                invoiceTable_header0_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/10),
                                                   width=int(screen_width-(screen_width/5.5)), anchor=CENTER)

                # Creating headings for the product details table header
                invoiceTable_heading1 = Label(
                    invoiceTable_header0, text="#", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading1.place(relx=0.04, rely=0.3, anchor=N)
                invoiceTable_heading2 = Label(
                    invoiceTable_header0, text="Description", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading2.place(relx=0.2, rely=0.3, anchor=N)
                invoiceTable_heading3 = Label(
                    invoiceTable_header0, text="Qty", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading3.place(relx=0.6, rely=0.3, anchor=N)
                invoiceTable_heading4 = Label(
                    invoiceTable_header0, text="Rate", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading4.place(relx=0.74, rely=0.3, anchor=N)
                invoiceTable_heading4_sym = Label(
                    invoiceTable_header0, text="₹", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading4_sym.place(relx=0.77, rely=0.3, anchor=N)
                invoiceTable_heading5 = Label(
                    invoiceTable_header0, text="Amount", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading5.place(relx=0.9, rely=0.3, anchor=N)
                invoiceTable_heading5_sym = Label(
                    invoiceTable_header0, text="₹", font=("Dodge", 14, "bold"), background=header_bgColor, anchor=CENTER)
                invoiceTable_heading5_sym.place(relx=0.95, rely=0.3, anchor=N)

                # Creating a frame for adding the entry for product details table
                invoiceTable_fields = Frame(rightBottom1_panel, height=int(screen_height/7),
                                            width=int(screen_width-(screen_width/5.5)))
                invoiceTable_fields.place(relx=0.5, rely=0.6, anchor=CENTER)

                # Setting background color for product details table
                invoiceTable_field_bgColor = Label(
                    invoiceTable_fields, background="#C2C5AA")
                invoiceTable_field_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/7),
                                                 width=int(screen_width-(screen_width/5.5)), anchor=CENTER)

                # Background color for product details table fields
                field_bgColor = "#C2C5AA"
                # Creating a canvas widget for making a scrollable table
                invoiceTable_fields_canvas = Canvas(invoiceTable_fields, background=field_bgColor, height=int(screen_height/7),
                                                    width=int(screen_width-(screen_width/5.5)), borderwidth=0,
                                                    highlightthickness=0)
                invoiceTable_fields_canvas.pack(
                    side=LEFT, fill=BOTH, expand=True)

                # Creating a frame to place the entry field
                invoiceTable_fields_frame = Frame(
                    invoiceTable_fields_canvas, width=int(screen_width-(screen_width/5.5)))

                # Setting background color for product details table
                invoiceTable_field_bgColor = Label(
                    invoiceTable_fields_frame, background=field_bgColor)
                invoiceTable_field_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height*5),
                                                 width=int(screen_width-(screen_width/5.5)), anchor=CENTER)

                # Creating scrollbar to scroll the fields table
                invoiceTable_scrollbar = Scrollbar(invoiceTable_fields, orient="vertical",
                                                   command=invoiceTable_fields_canvas.yview)
                invoiceTable_fields_canvas.configure(
                    yscrollcommand=invoiceTable_scrollbar.set)

                # Placing the created frame on the canvas
                invoiceTable_fields_canvas.create_window(
                    (4, 4), window=invoiceTable_fields_frame, anchor=S)

                invoiceTable_fields_frame.bind("<Configure>", lambda event,
                                               invoiceTable_fields_canvas=invoiceTable_fields_canvas: onFrameConfigure(invoiceTable_fields_canvas))

                # this calls the function to scroll the canvas widget
                invoiceTable_fields_canvas.bind(
                    "<MouseWheel>", scroll_tableFields)
                invoiceTable_field_bgColor.bind(
                    "<MouseWheel>", scroll_tableFields)

                # Creating a button to add new row
                # Styling the addRow Button
                addRow_btn_style = Style(rightBottom1_panel)
                addRow_btn_style.theme_use("default")
                addRow_btn_style.configure(
                    "AddRow_Button.TButton", font=("Dodge", 10, "bold", "italic"), foreground="#B3C6E7", background="#073B4C", borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of minimize button
                addRow_btn_style.map("AddRow_Button.TButton", font=[("active", "!disabled", ("Dodge", 11, "bold"))], foreground=[("active", "!disabled", "#01102E")],
                                     background=[("active", "#656D4A")])

                addRow_btn = Button(rightBottom1_panel,
                                    text="Add row", style="AddRow_Button.TButton", command=lambda: addRow())
                addRow_btn.place(relx=0.1, rely=0.7, anchor=CENTER)

                # Adding a message box for typing customer note
                customernoteEntry = scrolledtext.ScrolledText(
                    rightBottom1_panel, font=("Dodge", 12, "italic"), width=int(screen_width/35), height=int(screen_height/120), wrap=WORD)
                customernoteEntry.place(relx=0.1, rely=0.92, anchor=SW)

                customernoteEntry.insert(INSERT, "Your message here !")

                # this triggers the function for deleting the values in textbox
                customernoteEntry0 = customernoteEntry.bind(
                    "<Button-1>", deleteCustomerNote)

                # Showing sub total value
                subtotalEntry = Label(
                    rightBottom1_panel, text=initial_amount, font=("Dodge", 12), background=rightBottom1_label1_bG, foreground="black")
                subtotalEntry.place(relx=0.85, rely=0.76, anchor=CENTER)

                # entry for adding tax percentage
                taxEntry_box_Var = StringVar()
                taxEntry_box_Var.set(3)

                taxEntry_box = tk.Entry(rightBottom1_panel, textvariable=taxEntry_box_Var,
                                        font=("Dodge", 12, "bold"), width=int(screen_width/280), borderwidth=2, justify=RIGHT)
                taxEntry_box.place(relx=0.74, rely=0.81, height=int(
                    screen_height/25), anchor=CENTER)

                # this triggers the function to check the input is a integer
                taxEntry_box_Var.trace_add("write", check_taxEntry)

                # this triggers the function for deleting the values in textbox
                taxEntry_box0 = taxEntry_box.bind("<Button-1>", deleteTaxEntry)

                # Showing tax for the sub total value
                taxEntry = Label(
                    rightBottom1_panel, text=initial_amount, font=("Dodge", 12), background=rightBottom1_label1_bG, foreground="black")
                taxEntry.place(relx=0.85, rely=0.81, anchor=CENTER)

                # Creating a box for total amount
                totalAmount_bg = "#401414"
                totalAmount = tk.Frame(rightBottom1_panel, height=int(screen_height/15),
                                       width=int(screen_width-(screen_width/1.3)), highlightbackground=totalAmount_bg, highlightthickness=2)
                totalAmount.place(relx=0.78, rely=0.89, anchor=CENTER)

                # Showing total value including tax
                # Styling total
                totalEntry_style = Style(rightBottom1_panel)
                totalEntry_style.theme_use("default")
                totalEntry_style.configure(
                    "totalEntry.TLabel", font=("Dodge", 8, "bold"), background=rightBottom1_label1_bG, foreground="black", anchor=CENTER)

                totalEntry = Label(
                    rightBottom1_panel, text=initial_amount, font=("Dodge", 15, "bold"), style="totalEntry.TLabel")
                totalEntry.place(relx=0.872, rely=0.89, anchor=E)

                # Adding a label for currency symbol
                currency_symbolLabel = Label(
                    rightBottom1_panel, text="₹", font=("Dodge", 16, "bold"), background=rightBottom1_label1_bG, foreground="#401414")
                currency_symbolLabel.place(relx=0.93, rely=0.89, anchor=E)

                # Adding a total label
                totalEntry_label = Label(
                    totalAmount, text="Total", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background=totalAmount_bg, anchor=CENTER)
                totalEntry_label.place(relx=0, rely=0.5, height=int(
                    screen_height/15), width=int(screen_width-(screen_width/1.08)), anchor=W)

                # Creating a saveInvoice button
                # Styling the saveInvoice Button
                saveInvoice_btn_style = Style(rightBottom1_panel)
                saveInvoice_btn_style.theme_use("default")
                saveInvoice_btn_style.configure(
                    "SaveInvoice_Button.TButton", font=("Dodge", 15, "bold"), foreground="#B3C6E7", background="#2D361C", borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of minimize button
                saveInvoice_btn_style.map("SaveInvoice_Button.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))], foreground=[("active", "!disabled", "#01102E")],
                                          background=[("active", "#656D4A")])

                saveInvoice_btn = Button(
                    rightBottom1_panel, text="Save", image=icon6, compound=LEFT, style="SaveInvoice_Button.TButton", command=lambda: saveInvoice())
                saveInvoice_btn.place(relx=0.5, rely=0.92, anchor=CENTER)

                # adding a row to the product details table
                root.after(100, lambda: addRow())

            def triggering_newInvoice():  # function for deleting the invoice widgets and triggers the function for new invoice template

                # this prevents the function to be called twice by disabling the button
                invoiceCreate_btn.configure(state=DISABLED)

                # Calling shrink_leftPanel() to shrink the left panel and also expand the right panel
                root.after(100, lambda: shrink_invoicesLeftPanel())

                # this triggers the function for invoice templete
                root.after(200, lambda: newInvoice())

            # function which wraps the text inside table fields
            def wrapLength(string, length=45):

                # this returns the textwrapped in it's field
                return "\n".join(textwrap.wrap(string, length))

            # function for destroying the label widget created by entered_fields() function
            def leaved_fields(event):

                # deleting the label
                fields_info.destroy()

            # function for creating and showing a label with some text when called by the mouse hover over table fields
            def entered_fields_B(event):

                # assigning the label as global variable
                global fields_info

                # creating and positioning the label
                fields_info = Label(rightBottom_panel, text="# Double click on the invoice to delete", font=("Dodge", 14, "bold"),
                                    background=rightBottom_label1_bG, foreground="#401414")
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            # function for creating and showing a label with some text when called by the mouse hover over table fields
            def entered_fields(event):

                # assigning the label as global variable
                global fields_info

                # creating and positioning the label
                fields_info = Label(rightBottom_panel, text="# Double click on the invoice to delete", font=("Dodge", 12, "bold"),
                                    background=rightBottom_label1_bG, foreground="#401414")
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            def shrink_invoicesLeftPanel():

                def expand_invoicesLeftPanel(event):

                    # Enable the disabled button
                    rightTop_panel_wrapBtn.configure(state=NORMAL)

                    # shrinking the widgets of right panel
                    right_panel.configure(height=int(screen_height/1.035),
                                          width=int(screen_width-(screen_width/4.6)))

                    # shrinking the widgets of rightTop panel
                    rightTop_panel.configure(height=int(screen_height/10),
                                             width=int(screen_width-(screen_width/4.6)))

                    rightTop_panel_label0.configure(
                        width=int(screen_width/7.55))

                    # deleting the profile picture on rightTop panel
                    rightTop_panel_profile.destroy()

                    # shrinking the widgets of rightBottom panel
                    rightBottom_panel.configure(
                        width=int(screen_width-(screen_width/4.6)))

                    rightBottom_panel_label_01.configure(
                        width=int(screen_width/8.3))

                    # expanding the widgets of left panel
                    left_panel.configure(height=int(
                        screen_height/1.035), width=int(screen_width/4.55))

                    # expanding the widgets of leftTop panel
                    leftTop_panel.configure(height=int(screen_height/3.05),
                                            width=int(screen_width/4.55))
                    # showing the wrap button
                    rightTop_panel_wrapBtn.lift(rightTop_panel_label0)

                    # Showing the profile picture again
                    leftTop_panel_bgImg.configure(image=img1)
                    # this changes the function assigned with the profile picture by mouse left-click
                    root.after(100, lambda: leftTop_panel_bgImg.bind(
                        "<Button-1>", change_profile))

                    # expanding the widgets of leftBottom panel
                    leftBottom_panel.configure(height=int(
                        screen_height/1.55), width=int(screen_width/4.55))

                    # Changing the button size and position to normal
                    option1.configure(text="    Dashboard")
                    option1.place(relx=0.5, rely=0.1, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option2.configure(text="    Invoices   ")
                    option2.place(relx=0.5, rely=0.24, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option3.configure(text="   Clients       ")
                    option3.place(relx=0.5, rely=0.38, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option4.configure(text="    Stocks      ")
                    option4.place(relx=0.5, rely=0.52, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option5.configure(text="   Settings    ")
                    option5.place(relx=0.5, rely=0.66, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)

                    # shrinking the invoices table
                    invoicesTable_header.configure(
                        width=int(screen_width-(screen_width/3)))
                    invoicesTable_header_bgColor.place(
                        width=int(screen_width-(screen_width/3)))

                    # table rows
                    fields.place(width=int(screen_width/1.5))

                    # Changing back to the initial function assigned with the hover on table
                    root.after(100, lambda: fields.bind(
                        "<Enter>", entered_fields))

                # Calling the function to shrink left panel
                shrink_leftPanel()
                # this changes the function assigned with the profile picture by mouse left-click
                global unbindExpand
                unbindExpand = leftTop_panel_bgImg.bind(
                    "<Button-1>", expand_invoicesLeftPanel)

                # expanding the invoices table
                invoicesTable_header.configure(
                    width=int(screen_width-(screen_width/5.5)))
                invoicesTable_header_bgColor.place(
                    width=int(screen_width-(screen_width/5.5)))

                # table rows
                fields.place(width=int(screen_width/1.222))

                # Changing the function assigned with the hover on table
                root.after(100, lambda: fields.bind(
                    "<Enter>", entered_fields_B))

            # Changing the wrap button function
            rightTop_panel_wrapBtn.configure(
                command=lambda: shrink_invoicesLeftPanel())

            # Creating a label showing the icon and text
            rightBottom_panel_label1 = Label(
                rightBottom_panel, image=icon6, text="   Invoices", font=("Dodge", 16, "bold"), background=rightBottom_label1_bG, compound=LEFT)
            rightBottom_panel_label1.place(relx=0.12, rely=0.12, anchor=CENTER)

            # Creating a button to call new invoice template
            invoiceCreate_btn_style = Style(rightBottom_panel)
            invoiceCreate_btn_style.theme_use("default")
            invoiceCreate_btn_style.configure(
                "CreateInvoice.TButton", font=("Dodge", 10, "bold"), background="#0CB0A9", borderwidth=3, focuscolor="none", anchor=CENTER)

            # Changing the mapping style of background color button
            invoiceCreate_btn_style.map("CreateInvoice.TButton", foreground=[("active", "!disabled", "black")],
                                        background=[("active", "#61818D")])
            invoiceCreate_btn = Button(
                rightBottom_panel, text="New invoice", style="CreateInvoice.TButton", command=lambda: triggering_newInvoice())
            invoiceCreate_btn.place(relx=0.15, rely=0.2, anchor=CENTER)

            # Creating a table showing the previously created invoices
            # Creating a frame for the invoices table header
            invoicesTable_header = Frame(rightBottom_panel, height=int(screen_height/10),
                                         width=int(screen_width-(screen_width/3)))
            invoicesTable_header.place(relx=0.5, rely=0.33, anchor=CENTER)

            # Background color for label invoices table header
            header_bgColor = "#9BA984"

            invoicesTable_header_bgColor = Label(
                invoicesTable_header, background=header_bgColor)
            invoicesTable_header_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/10),
                                               width=int(screen_width-(screen_width/3)), anchor=CENTER)

            # Creating headings for the invoices table header
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="No.", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            invoicesTable_heading1.place(relx=0.05, rely=0.3, anchor=N)
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="Clients", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=W)
            invoicesTable_heading1.place(relx=0.2, rely=0.3, anchor=N)
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="Date", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            invoicesTable_heading1.place(relx=0.43, rely=0.3, anchor=N)
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="Due date", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            invoicesTable_heading1.place(relx=0.565, rely=0.3, anchor=N)
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="Amount", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            invoicesTable_heading1.place(relx=0.69, rely=0.3, anchor=N)
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="Balance", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            invoicesTable_heading1.place(relx=0.825, rely=0.3, anchor=N)
            invoicesTable_heading1 = Label(
                invoicesTable_header, text="Status", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            invoicesTable_heading1.place(relx=0.945, rely=0.3, anchor=N)

            # Styling the invoices table fields
            fields_style = Style(rightBottom_panel)
            fields_style.theme_use("default")
            fields_style.configure(
                "Fields.Treeview", font=("Dodge", 12), borderwidth=0, highlightthickness=0, rowheight=120, anchor=CENTER)

            # Creating the invoices table columns and rows
            fields = Treeview(rightBottom_panel, selectmode=NONE,
                              style="Fields.Treeview")
            fields.place(relx=0.5, rely=0.35, width=int(
                screen_width/1.5), height=int(screen_height/2.8), anchor=N)

            fields["columns"] = ["1", "2", "3", "4", "5", "6", "7"]
            fields.column("1", width=int(screen_width/2000), anchor=CENTER)
            fields.column("2", width=int(screen_width/10), anchor=CENTER)
            fields.column("3", width=int(screen_width/60), anchor=CENTER)
            fields.column("4", width=int(screen_width/60), anchor=CENTER)
            fields.column("5", width=int(screen_width/60), anchor=CENTER)
            fields.column("6", width=int(screen_width/60), anchor=CENTER)
            fields.column("7", width=int(screen_width/2000), anchor=CENTER)

            fields["show"] = ["headings"]

            # Creating new database for the new user
            user_inV = sqlite3.connect(
                str(inVoiceDB)+"in_voice.db")

            # Creating a cursor
            co = user_inV.cursor()

            # Creating a table invoiceDetails if not exists
            co.execute("""CREATE TABLE IF NOT EXISTS invoiceDetails (
                            invoiceNumber TEXT,
                            clientDetails TEXT,
                            datePurchased DATE,
                            dueDate DATE,
                            currency TEXT,
                            customerMessage TEXT,
                            taxInPercentage INTEGER,
                            subTotal REAL,
                            calculatedTAX REAL,
                            totalAmount REAL,
                            balanceAmount REAL
                            )""")

            # query the database
            co.execute(
                "SELECT *, oid FROM invoiceDetails")
            invoices = co.fetchall()
            # print(len(invoices))

            if not len(invoices) == 0:
                for invoice in invoices:

                    if int(invoice[11]) % 2 == 0:

                        if not str(invoice[10]) == 0:

                            fields.insert("", "end",
                                          values=(str(invoice[0]), wrapLength(str(invoice[1])), str(invoice[2]), str(invoice[3]), str(invoice[9]), str(invoice[10]), "Pending"), tag="even")
                        elif str(invoice[10]) == 0:

                            fields.insert("", "end",
                                          values=(str(invoice[0]), wrapLength(str(invoice[1])), str(invoice[2]), str(invoice[3]), str(invoice[9]), str(invoice[10]), "Paid"), tag="even")

                    else:

                        if not str(invoice[10]) == 0:

                            fields.insert("", "end",
                                          values=(str(invoice[0]), wrapLength(str(invoice[1])), str(invoice[2]), str(invoice[3]), str(invoice[9]), str(invoice[10]), "Pending"), tag="odd")
                        elif str(invoice[10]) == 0:

                            fields.insert("", "end",
                                          values=(str(invoice[0]), wrapLength(str(invoice[1])), str(invoice[2]), str(invoice[3]), str(invoice[9]), str(invoice[10]), "Paid"), tag="odd")

                # Changing intermediate background
                fields.tag_configure("even", background="#E8E8E4")

                # commit changes
                user_inV.commit()

                # close connection
                user_inV.close()

            elif len(invoices) == 0:
                # Creating a label to occupy the empty fields
                field_label1 = Label(fields, text="SORRY!", font=(
                    "Dodge", 17, "bold"), background="white", foreground="#401414", justify=CENTER)
                field_label1.place(relx=0.5, rely=0.4, anchor=CENTER)
                field_label2 = Label(fields, text="no invoice details to show", font=(
                    "Dodge", 14, "bold"), background="white", foreground="#401414", justify=CENTER)
                field_label2.place(relx=0.5, rely=0.6, anchor=CENTER)

            # To lift the frame over invoices table header
            invoicesTable_header.lift(fields)

        def clients_btn():  # function for creating the clients panel

            def limitingOption():  # function for making the full screen non-shrinkable

                def limitingOption5():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with settings button
                        settingsTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption4():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with stocks button
                        stocksTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption3():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function for clients panel and closes the add client panel
                        clientsTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption2():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function to invoice panel
                        invoicesTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption1():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with dashboard button
                        dashboardTab()

                # changing the function of all option buttons
                option1.configure(command=lambda: limitingOption1())
                option2.configure(command=lambda: limitingOption2())
                option3.configure(style="Options.TLabel",
                                  state=NORMAL, command=lambda: limitingOption3())
                option4.configure(command=lambda: limitingOption4())
                option5.configure(command=lambda: limitingOption5())
                root.after(200, lambda: leftTop_panel_bgImg.unbind(
                    "<Button-1>", unbindExpand))

            def clientShow(event):  # function which shows the selected client

                def clientDelete():  # function for deleting the selected client

                    deletingClient = messagebox.askyesno(
                        "Delete Client", "Are you sure you want to delete client details?")

                    if deletingClient == True:

                        # Creating new database for the new user
                        user_inV = sqlite3.connect(
                            str(inVoiceDB)+"in_voice.db")

                        # Creating a cursor
                        co = user_inV.cursor()

                        # Deleting client from clientDetails table
                        co.execute(
                            "DELETE from clientDetails WHERE oid = " + str(clientNumber))

                        # commit changes
                        user_inV.commit()

                        # close connection
                        user_inV.close()

                        # this calls the function for clients panel and closes the add client panel
                        clientsTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                    elif deletingClient == False:
                        return

                def clientEdit():  # function for editing the selected client

                    def updateClientDetails():  # function for saving the new changes to database

                        # Checking the entries are not empty
                        if nameEntry_Var.get() == "" or addressEntry1_Var.get() == "" or cityEntry_Var.get() == "" or pincodeEntry_Var.get() == "" or contactEntry_Var.get() == "" or emailEntry_Var.get() == "":

                            messagebox.showerror(
                                "Empty field", "Make sure the field with asterisk are field")

                        elif len(nameEntry_Var.get()) < 3 or len(addressEntry2_Var.get()) < 3 or len(cityEntry_Var.get()) < 3:

                            messagebox.showerror(
                                "Required", "ClientName, Address Line1, City should have minimum 3 characters")

                        elif len(addressEntry1_Var.get()) < 5:

                            messagebox.showerror(
                                "Required", "Address Line1 should have minimum 5 characters")

                        elif not cityEntry_Var.get().isalpha():

                            messagebox.showerror(
                                "Required", "City name must be alphabets")

                        elif not pincodeEntry_Var.get().isdigit() or not contactEntry_Var.get().isdigit():

                            messagebox.showerror(
                                "Required", "Pincode and Contact must contain numbers only")
                            pincodeEntry_Var.set("")
                            contactEntry_Var.set("")

                        elif len(pincodeEntry_Var.get()) > 6 or len(pincodeEntry_Var.get()) < 6:

                            messagebox.showerror(
                                "Required", "Pin code must be 6 digits")

                        elif emailEntry_Var.get().isdigit() or emailEntry_Var.get().isalpha():

                            messagebox.showerror(
                                "Required", "Enter a valid emailId")
                            emailEntry_Var.set("")

                        elif not len(emailEntry_Var.get()) > 14 or len(emailEntry_Var.get()) > 35:

                            messagebox.showerror(
                                "Required", "email may have 15-40 characters")

                        elif len(contactEntry_Var.get()) > 10 or len(contactEntry_Var.get()) < 10:

                            messagebox.showerror(
                                "Required", "Contact must be 10 digits")
                            contactEntry_Var.set("")

                        else:

                            updatingtoClients = messagebox.askyesno(
                                "Save Client", "Are you sure you want to save changes?")

                            if updatingtoClients == True:

                                # Creating new database for the new user
                                user_inV = sqlite3.connect(
                                    str(inVoiceDB)+"in_voice.db")

                                # Creating a cursor
                                co = user_inV.cursor()

                                # insert into table
                                co.execute("UPDATE clientDetails SET  clientName = :clientName, emailId = :emailId, contactNumber = :contactNumber, addressLine1 = :addressLine1, addressLine2 = :addressLine2, addressLine3 = :addressLine3, cityName = :cityName, pinCode = :pinCode, customerNote = :customerNote WHERE oid = :clientNumber",
                                           {
                                               "clientName": nameEntry_Var.get(),
                                               "emailId": emailEntry_Var.get(),
                                               "contactNumber": contactEntry_Var.get(),
                                               "addressLine1": addressEntry1_Var.get(),
                                               "addressLine2": addressEntry2_Var.get(),
                                               "addressLine3": addressEntry3_Var.get(),
                                               "cityName": cityEntry_Var.get(),
                                               "pinCode": pincodeEntry_Var.get(),
                                               "customerNote": customernoteEntry.get("1.0", 'end-1c'),

                                               "clientNumber": clientNumber
                                           })

                                # commit changes
                                user_inV.commit()

                                # close connection
                                user_inV.close()

                                # this calls the function for clients panel and closes the add client panel
                                clientsTab()
                                dashboardTab()

                                # changing the function of all option buttons back to the previous one
                                option1.configure(
                                    command=lambda: dashboardTab())
                                option2.configure(
                                    command=lambda: [invoicesTab(), dashboardTab()])
                                option3.configure(
                                    command=lambda: [clientsTab(), dashboardTab()])
                                option4.configure(
                                    command=lambda: [stocksTab(), dashboardTab()])
                                option5.configure(
                                    command=lambda: [settingsTab(), dashboardTab()])

                            elif updatingtoClients == False:
                                return

                    # Creating entries of client create panel
                    # Name entry
                    nameEntry_Var = StringVar()
                    nameEntry_Var.set(show_clientName)
                    nameEntry = tk.Entry(rightBottom2_panel, textvariable=nameEntry_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                    nameEntry.place(relx=0.35, rely=0.17, height=int(
                        screen_height/20), anchor=CENTER)

                    # Email entry
                    emailEntry_Var = StringVar()
                    emailEntry_Var.set(show_emailId)
                    emailEntry = tk.Entry(rightBottom2_panel, textvariable=emailEntry_Var,
                                          font=("Dodge", 15, "bold"), width=int(screen_width/50), justify=RIGHT)
                    emailEntry.place(relx=0.8, rely=0.17, height=int(
                        screen_height/20), anchor=CENTER)

                    # Contact entry
                    contactEntry_Var = StringVar()
                    contactEntry_Var.set(show_contactNumber)
                    contactEntry = tk.Entry(rightBottom2_panel, textvariable=contactEntry_Var,
                                            font=("Dodge", 15, "bold"), width=int(screen_width/70), justify=RIGHT)
                    contactEntry.place(relx=0.765, rely=0.29, height=int(
                        screen_height/20), anchor=CENTER)

                    # Address entry1
                    addressEntry1_Var = StringVar()
                    addressEntry1_Var.set(show_AddressLine1)
                    addressEntry1 = tk.Entry(rightBottom2_panel, textvariable=addressEntry1_Var,
                                             font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                    addressEntry1.place(relx=0.35, rely=0.32, height=int(
                        screen_height/20), anchor=CENTER)

                    # Address entry2
                    addressEntry2_Var = StringVar()
                    addressEntry2_Var.set(show_AddressLine2)
                    addressEntry2 = tk.Entry(rightBottom2_panel, textvariable=addressEntry2_Var,
                                             font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                    addressEntry2.place(relx=0.35, rely=0.42, height=int(
                        screen_height/20), anchor=CENTER)

                    # Address entry3
                    addressEntry3_Var = StringVar()
                    addressEntry3_Var.set(show_AddressLine3)
                    addressEntry3 = tk.Entry(rightBottom2_panel, textvariable=addressEntry3_Var,
                                             font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                    addressEntry3.place(relx=0.35, rely=0.5, height=int(
                        screen_height/20), anchor=CENTER)

                    # City entry
                    cityEntry_Var = StringVar()
                    cityEntry_Var.set(show_cityName)
                    cityEntry = tk.Entry(rightBottom2_panel, textvariable=cityEntry_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/50), justify=RIGHT)
                    cityEntry.place(relx=0.3, rely=0.64, height=int(
                        screen_height/20), anchor=CENTER)

                    # Pincode entry
                    pincodeEntry_Var = StringVar()
                    pincodeEntry_Var.set(show_pinCode)
                    pincodeEntry = tk.Entry(rightBottom2_panel, textvariable=pincodeEntry_Var,
                                            font=("Dodge", 15, "bold"), width=int(screen_width/90), justify=RIGHT)
                    pincodeEntry.place(relx=0.25, rely=0.74, height=int(
                        screen_height/20), anchor=CENTER)

                    # Adding a message box for typing customer note
                    customernoteEntry = scrolledtext.ScrolledText(
                        rightBottom2_panel, font=("Dodge", 12, "italic", "bold"), width=int(screen_width/35), height=int(screen_height/100), wrap=WORD)
                    customernoteEntry.place(relx=0.65, rely=0.69, anchor=SW)
                    customernoteEntry.insert(INSERT, show_customerNote)

                    # Setting asterisk to the important field
                    nameAsterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    nameAsterisk.place(relx=0.15, rely=0.15)

                    emailAsterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    emailAsterisk.place(relx=0.63, rely=0.15)

                    contactAsterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    contactAsterisk.place(relx=0.64, rely=0.27)

                    address1Asterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    address1Asterisk.place(relx=0.12, rely=0.3)

                    address2Asterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    address2Asterisk.place(relx=0.12, rely=0.39)

                    address3Optional = Label(
                        rightBottom2_panel, text="(optional)", background=rightBottom2_label1_bG, foreground="#0A014F")
                    address3Optional.place(relx=0.13, rely=0.52)

                    cityAsterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    cityAsterisk.place(relx=0.12, rely=0.62)

                    pincodeAsterisk = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    pincodeAsterisk.place(relx=0.14, rely=0.72)

                    customernoteOptional = Label(
                        rightBottom2_panel, text="(optional)", background=rightBottom2_label1_bG, foreground="#0A014F")
                    customernoteOptional.place(relx=0.7, rely=0.43)

                    asteriskNote = Label(rightBottom2_panel, text="Note: field with asterisk            must be filled", font=("Dodge", 12, "bold"),
                                         background=rightBottom2_label1_bG, foreground="#0A014F")
                    asteriskNote.place(relx=0.18, rely=0.9)

                    asteriskNoteA = Label(rightBottom2_panel, text="*", font=(
                        "Dodge", 20, "bold"), background=rightBottom2_label1_bG, foreground="#EF233C")
                    asteriskNoteA.place(relx=0.335, rely=0.9)

                    # destroying all values
                    nameLabel.destroy()
                    emailLabel.destroy()
                    contactLabel.destroy()
                    address1Label.destroy()
                    address2Label.destroy()
                    address3Label.destroy()
                    cityLabel.destroy()
                    pincodeLabel.destroy()
                    customerNoteLabel.destroy()

                    # Changing the edit button to save button
                    editClient_btn.configure(
                        text="save", image=icon7, compound=LEFT, command=lambda: updateClientDetails())

                # Getting the client details according to the field selection
                clientNumber = fields.item(fields.focus())['values'][0]
                # print(clientNumber)

                # Unbinding the click function on clients table
                fields.unbind("<Double-1>", unBindclients)

                # Creating new database for the new user
                user_inV = sqlite3.connect(
                    str(inVoiceDB)+"in_voice.db")

                # Creating a cursor
                co = user_inV.cursor()

                # query the database
                co.execute("SELECT * FROM clientDetails WHERE oid = " +
                           "'" + str(clientNumber) + "'")
                clients = co.fetchall()
                # print(clients)

                # converting tuples into separate strings
                show_clientName = ""
                for client in clients:
                    show_clientName += str(client[0])

                show_AddressLine1 = ""
                for client in clients:
                    show_AddressLine1 += str(client[3])

                show_AddressLine2 = ""
                for client in clients:
                    show_AddressLine2 += str(client[4])

                show_AddressLine3 = ""
                for client in clients:
                    show_AddressLine3 += str(client[5])

                show_cityName = ""
                for client in clients:
                    show_cityName += str(client[6])

                show_pinCode = ""
                for client in clients:
                    show_pinCode += str(client[7])

                show_emailId = ""
                for client in clients:
                    show_emailId += str(client[1])

                show_contactNumber = ""
                for client in clients:
                    show_contactNumber += str(client[2])

                show_customerNote = ""
                for client in clients:
                    show_customerNote += str(client[8])

                # commit changes
                user_inV.commit()

                # close connection
                user_inV.close()

                # Calling shrink_leftPanel() to shrink the left panel and also expand the right panel
                shrink_clientsLeftPanel()
                # this function makes the panel non-shrikable
                limitingOption()

                # Creating a new frame on the rightBottom panel
                rightBottom2_panel = Frame(right_panel, height=int(screen_height/1.04),
                                           width=int(screen_width-(screen_width/15.1)))
                rightBottom2_panel.place(relx=1, rely=1, anchor=SE)

                # Creating a labels for background color of frame
                rightBottom2_panel_label0 = Label(
                    rightBottom2_panel, background="#B3C6E7", width=int(screen_width/4.6))
                rightBottom2_panel_label0.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1), anchor=CENTER)

                # Background and Foreground color for label and the buttons in the leftBottom panel
                rightBottom2_label1_bG = "#F0EFF4"
                rightBottom2_label1_fG = "#401414"
                # Creating a labels for background color
                rightBottom_panel_label_01 = Label(
                    rightBottom2_panel, background=rightBottom2_label1_bG, width=int(screen_width/6.75))
                rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1.1), anchor=CENTER)

                rightBottom2_panel_fG = "#3C2212"

                # Creating labels of client create panel
                # Name entry label
                nameEntry_label = Label(
                    rightBottom2_panel, text="Client Name  :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG, justify=RIGHT)
                nameEntry_label.place(
                    relx=0.1, rely=0.17, anchor=CENTER)

                # Name label value
                nameLabel = Label(rightBottom2_panel, text=show_clientName, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                nameLabel.place(relx=0.22, rely=0.17, anchor=W)

                # Email entry label
                emailEntry_label = Label(
                    rightBottom2_panel, text="Email  :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                emailEntry_label.place(
                    relx=0.6, rely=0.17, anchor=CENTER)

                # Email label value
                emailLabel = Label(rightBottom2_panel, text=show_emailId, font=(
                    "Dodge", 15, "bold"), wraplength=300, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                emailLabel.place(relx=0.7, rely=0.17, anchor=W)

                # Contact entry label
                contactEntry_label = Label(
                    rightBottom2_panel, text="Contact  :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG, justify=RIGHT)
                contactEntry_label.place(
                    relx=0.6, rely=0.29, anchor=CENTER)

                # Contact label value
                contactLabel = Label(rightBottom2_panel, text=show_contactNumber, font=(
                    "Dodge", 15, "bold"), wraplength=300, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                contactLabel.place(relx=0.7, rely=0.29, anchor=W)

                # Address entry label
                addressEntry_label = Label(
                    rightBottom2_panel, text="Address", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG, justify=RIGHT)
                addressEntry_label.place(
                    relx=0.1, rely=0.27, anchor=CENTER)

                # Address entry1 label
                addressEntry1_label = Label(
                    rightBottom2_panel, text="line 1  :", font=("Dodge", 13), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                addressEntry1_label.place(
                    relx=0.12, rely=0.32, anchor=CENTER)

                # Address1 label value
                address1Label = Label(rightBottom2_panel, text=show_AddressLine1, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                address1Label.place(relx=0.22, rely=0.32, anchor=W)

                # Address entry2 label
                addressEntry2_label = Label(
                    rightBottom2_panel, text="line 2  :", font=("Dodge", 13), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                addressEntry2_label.place(
                    relx=0.12, rely=0.41, anchor=CENTER)

                # Address2 label value
                address2Label = Label(rightBottom2_panel, text=show_AddressLine2, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                address2Label.place(relx=0.22, rely=0.41, anchor=W)

                # Address entry3 label
                addressEntry3_label = Label(
                    rightBottom2_panel, text="line 3  :", font=("Dodge", 13), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                addressEntry3_label.place(
                    relx=0.12, rely=0.5, anchor=CENTER)

                # Address3 label value
                address3Label = Label(rightBottom2_panel, text=show_AddressLine3, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                address3Label.place(relx=0.22, rely=0.5, anchor=W)

                # City entry label
                cityEntry_label = Label(
                    rightBottom2_panel, text="City  :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                cityEntry_label.place(
                    relx=0.1, rely=0.64, anchor=CENTER)

                # City label value
                cityLabel = Label(rightBottom2_panel, text=show_cityName, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                cityLabel.place(relx=0.22, rely=0.64, anchor=W)

                # Pincode entry label
                pincodeEntry_label = Label(
                    rightBottom2_panel, text="Pin Code  :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                pincodeEntry_label.place(
                    relx=0.1, rely=0.74, anchor=CENTER)

                # PinCode label value
                pincodeLabel = Label(rightBottom2_panel, text=show_pinCode, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                pincodeLabel.place(relx=0.22, rely=0.74, anchor=W)

                # Customernote Entry Label
                customernoteEntry_label = Label(rightBottom2_panel, text="Customer Note  :-", font=(
                    "Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                customernoteEntry_label.place(
                    relx=0.63, rely=0.44, anchor=CENTER)

                # CustomerNote label value
                customerNoteLabel = Label(rightBottom2_panel, text=show_customerNote, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                customerNoteLabel.place(relx=0.7, rely=0.57, anchor=W)

                # Creating a editClient button
                # Styling the editClient Button
                editClient_btn_style = Style(rightBottom2_panel)
                editClient_btn_style.theme_use("default")
                editClient_btn_style.configure(
                    "EditClientButton.TButton", font=("Dodge", 16, "bold"), foreground="#B3C6E7", background="#656D4A", borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of minimize button
                editClient_btn_style.map("EditClientButton.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))], foreground=[("active", "!disabled", "#B3C6E7")],
                                         background=[("active", "#2D361C")])

                editClient_btn = Button(
                    rightBottom2_panel, text="edit", image=icon13, compound=LEFT, style="EditClientButton.TButton", command=lambda: clientEdit())
                editClient_btn.place(relx=0.83, rely=0.88, width=int(
                    screen_width/11), anchor=CENTER)

                # Styling delete client button
                deleteClient_style = Style()
                deleteClient_style.theme_use("default")
                deleteClient_style.configure("DeleteClientButton.TButton", background=rightBottom2_label1_bG,
                                             foreground=rightBottom2_label1_fG, borderwidth=0, focuscolor="none", relief=FLAT, highlightthickness=0)
                # mouse hover style for delete client button
                deleteClient_style.map("DeleteClientButton.TButton", foreground=[(
                    "active", "!disabled", "#F0EFF4")], background=[("active", rightBottom2_label1_bG)])

                # Adding a delete button for deleting the client details
                deleteClient_btn = Button(
                    rightBottom2_panel, image=icon14, style="DeleteClientButton.TButton", command=lambda: clientDelete())
                deleteClient_btn.place(relx=0.94, rely=0.08, anchor=CENTER)

            def newClient():  # function for creating a new client template

                def addClient():  # function for adding client to the database

                    # Checking the entries are not empty
                    if nameEntry_Var.get() == "" or addressEntry1_Var.get() == "" or cityEntry_Var.get() == "" or pincodeEntry_Var.get() == "" or contactEntry_Var.get() == "" or emailEntry_Var.get() == "":

                        messagebox.showerror(
                            "Empty field", "Make sure the field with asterisk are field")

                    elif len(nameEntry_Var.get()) < 3 or len(addressEntry2_Var.get()) < 3 or len(cityEntry_Var.get()) < 3:

                        messagebox.showerror(
                            "Required", "ClientName, Address Line1, City should have minimum 3 characters")

                    elif len(addressEntry1_Var.get()) < 5:

                        messagebox.showerror(
                            "Required", "Address Line1 should have minimum 5 characters")

                    elif not cityEntry_Var.get().isalpha():

                        messagebox.showerror(
                            "Required", "City name must be alphabets")

                    elif not pincodeEntry_Var.get().isdigit() or not contactEntry_Var.get().isdigit():

                        messagebox.showerror(
                            "Required", "Pincode and Contact must contain numbers only")
                        pincodeEntry_Var.set("")
                        contactEntry_Var.set("")

                    elif len(pincodeEntry_Var.get()) > 6 or len(pincodeEntry_Var.get()) < 6:

                        messagebox.showerror(
                            "Required", "Pin code must be 6 digits")

                    elif emailEntry_Var.get().isdigit() or emailEntry_Var.get().isalpha():

                        messagebox.showerror(
                            "Required", "Enter a valid emailId")
                        emailEntry_Var.set("")

                    elif not len(emailEntry_Var.get()) > 14 or len(emailEntry_Var.get()) > 35:

                        messagebox.showerror(
                            "Required", "email may have 15-40 characters")

                    elif len(contactEntry_Var.get()) > 10 or len(contactEntry_Var.get()) < 10:

                        messagebox.showerror(
                            "Required", "Contact must be 10 digits")
                        contactEntry_Var.set("")

                    else:

                        savingtoClients = messagebox.askyesno(
                            "Save Client", "Are you sure you want to save changes?")

                        if savingtoClients == True:

                            # Creating new database for the new user
                            user_inV = sqlite3.connect(
                                str(inVoiceDB)+"in_voice.db")

                            # Creating a cursor
                            co = user_inV.cursor()

                            # insert into table
                            co.execute("INSERT INTO clientDetails VALUES (:clientName, :emailId, :contactNumber, :addressLine1, :addressLine2, :addressLine3, :cityName, :pinCode, :customerNote)",
                                       {
                                           "clientName": nameEntry_Var.get(),
                                           "emailId": emailEntry_Var.get(),
                                           "contactNumber": contactEntry_Var.get(),
                                           "addressLine1": addressEntry1_Var.get(),
                                           "addressLine2": addressEntry2_Var.get(),
                                           "addressLine3": addressEntry3_Var.get(),
                                           "cityName": cityEntry_Var.get(),
                                           "pinCode": pincodeEntry_Var.get(),
                                           "customerNote": customernoteEntry.get("1.0", 'end-1c')
                                       })

                            # commit changes
                            user_inV.commit()

                            # close connection
                            user_inV.close()

                            # this calls the function for clients panel and closes the add client panel
                            clientsTab()
                            dashboardTab()

                            # changing the function of all option buttons back to the previous one
                            option1.configure(command=lambda: dashboardTab())
                            option2.configure(
                                command=lambda: [invoicesTab(), dashboardTab()])
                            option3.configure(
                                command=lambda: [clientsTab(), dashboardTab()])
                            option4.configure(
                                command=lambda: [stocksTab(), dashboardTab()])
                            option5.configure(
                                command=lambda: [settingsTab(), dashboardTab()])

                        elif savingtoClients == False:
                            return

                # this function makes the panel non-shrikable
                limitingOption()

                # Creating a new frame on the rightBottom panel
                rightBottom1_panel = Frame(right_panel, height=int(screen_height/1.04),
                                           width=int(screen_width-(screen_width/15.1)))
                rightBottom1_panel.place(relx=1, rely=1, anchor=SE)

                # Creating a labels for background color of frame
                rightBottom1_panel_label0 = Label(
                    rightBottom1_panel, background="#B3C6E7", width=int(screen_width/4.6))
                rightBottom1_panel_label0.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1), anchor=CENTER)

                # Background and Foreground color for label and the buttons in the leftBottom panel
                rightBottom1_label1_bG = "#F0EFF4"
                rightBottom1_label1_fG = "#401414"
                # Creating a labels for background color
                rightBottom_panel_label_01 = Label(
                    rightBottom1_panel, background=rightBottom1_label1_bG, width=int(screen_width/6.75))
                rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1.1), anchor=CENTER)

                # Creating labels of client create panel
                # Name entry label
                nameEntry_label = Label(
                    rightBottom1_panel, text="Client Name", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                nameEntry_label.place(
                    relx=0.1, rely=0.15, anchor=CENTER)

                nameAsterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                nameAsterisk.place(relx=0.15, rely=0.13)

                # Email entry label
                emailEntry_label = Label(
                    rightBottom1_panel, text="Email", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                emailEntry_label.place(
                    relx=0.6, rely=0.15, anchor=CENTER)

                emailAsterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                emailAsterisk.place(relx=0.63, rely=0.13)

                # Contact entry label
                contactEntry_label = Label(
                    rightBottom1_panel, text="Contact", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                contactEntry_label.place(
                    relx=0.6, rely=0.27, anchor=CENTER)

                contactAsterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                contactAsterisk.place(relx=0.64, rely=0.25)

                # Address entry label
                addressEntry_label = Label(
                    rightBottom1_panel, text="Address", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                addressEntry_label.place(
                    relx=0.1, rely=0.25, anchor=CENTER)

                # Address entry1 label
                addressEntry1_label = Label(
                    rightBottom1_panel, text="line 1", font=("Dodge", 13, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                addressEntry1_label.place(
                    relx=0.15, rely=0.3, anchor=CENTER)

                address1Asterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                address1Asterisk.place(relx=0.12, rely=0.28)

                # Address entry2 label
                addressEntry2_label = Label(
                    rightBottom1_panel, text="line 2", font=("Dodge", 13, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                addressEntry2_label.place(
                    relx=0.15, rely=0.39, anchor=CENTER)

                address2Asterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                address2Asterisk.place(relx=0.12, rely=0.37)

                # Address entry3 label
                addressEntry3_label = Label(
                    rightBottom1_panel, text="line 3", font=("Dodge", 13, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                addressEntry3_label.place(
                    relx=0.15, rely=0.48, anchor=CENTER)

                address3Optional = Label(
                    rightBottom1_panel, text="(optional)", background=rightBottom1_label1_bG, foreground="#0A014F")
                address3Optional.place(relx=0.13, rely=0.5)

                # City entry label
                cityEntry_label = Label(
                    rightBottom1_panel, text="City", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                cityEntry_label.place(
                    relx=0.1, rely=0.62, anchor=CENTER)

                cityAsterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                cityAsterisk.place(relx=0.12, rely=0.6)

                # Pincode entry label
                pincodeEntry_label = Label(
                    rightBottom1_panel, text="Pin Code", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                pincodeEntry_label.place(
                    relx=0.1, rely=0.72, anchor=CENTER)

                pincodeAsterisk = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                pincodeAsterisk.place(relx=0.14, rely=0.7)

                # Customernote Entry Label
                customernoteEntry_label = Label(rightBottom1_panel, text="Customer Note", font=(
                    "Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                customernoteEntry_label.place(
                    relx=0.63, rely=0.42, anchor=CENTER)

                customernoteOptional = Label(
                    rightBottom1_panel, text="(optional)", background=rightBottom1_label1_bG, foreground="#0A014F")
                customernoteOptional.place(relx=0.7, rely=0.41)

                asteriskNote = Label(rightBottom1_panel, text="Note: field with asterisk            must be filled", font=("Dodge", 12, "bold"),
                                     background=rightBottom1_label1_bG, foreground="#0A014F")
                asteriskNote.place(relx=0.18, rely=0.88)

                asteriskNoteA = Label(rightBottom1_panel, text="*", font=(
                    "Dodge", 20, "bold"), background=rightBottom1_label1_bG, foreground="#EF233C")
                asteriskNoteA.place(relx=0.335, rely=0.88)

                # Creating entries of client create panel
                # Name entry
                nameEntry_Var = StringVar()
                nameEntry = tk.Entry(rightBottom1_panel, textvariable=nameEntry_Var,
                                     font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                nameEntry.place(relx=0.35, rely=0.15, height=int(
                    screen_height/20), anchor=CENTER)

                # Email entry
                emailEntry_Var = StringVar()
                emailEntry = tk.Entry(rightBottom1_panel, textvariable=emailEntry_Var,
                                      font=("Dodge", 15, "bold"), width=int(screen_width/50), justify=RIGHT)
                emailEntry.place(relx=0.8, rely=0.15, height=int(
                    screen_height/20), anchor=CENTER)

                # Contact entry
                contactEntry_Var = StringVar()
                contactEntry = tk.Entry(rightBottom1_panel, textvariable=contactEntry_Var,
                                        font=("Dodge", 15, "bold"), width=int(screen_width/70), justify=RIGHT)
                contactEntry.place(relx=0.765, rely=0.27, height=int(
                    screen_height/20), anchor=CENTER)

                # Address entry1
                addressEntry1_Var = StringVar()
                addressEntry1 = tk.Entry(rightBottom1_panel, textvariable=addressEntry1_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                addressEntry1.place(relx=0.35, rely=0.3, height=int(
                    screen_height/20), anchor=CENTER)

                # Address entry2
                addressEntry2_Var = StringVar()
                addressEntry2 = tk.Entry(rightBottom1_panel, textvariable=addressEntry2_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                addressEntry2.place(relx=0.35, rely=0.39, height=int(
                    screen_height/20), anchor=CENTER)

                # Address entry3
                addressEntry3_Var = StringVar()
                addressEntry3 = tk.Entry(rightBottom1_panel, textvariable=addressEntry3_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/35), justify=RIGHT)
                addressEntry3.place(relx=0.35, rely=0.48, height=int(
                    screen_height/20), anchor=CENTER)

                # City entry
                cityEntry_Var = StringVar()
                cityEntry = tk.Entry(rightBottom1_panel, textvariable=cityEntry_Var,
                                     font=("Dodge", 15, "bold"), width=int(screen_width/50), justify=RIGHT)
                cityEntry.place(relx=0.3, rely=0.62, height=int(
                    screen_height/20), anchor=CENTER)

                # Pincode entry
                pincodeEntry_Var = StringVar()
                pincodeEntry = tk.Entry(rightBottom1_panel, textvariable=pincodeEntry_Var,
                                        font=("Dodge", 15, "bold"), width=int(screen_width/90), justify=RIGHT)
                pincodeEntry.place(relx=0.25, rely=0.72, height=int(
                    screen_height/20), anchor=CENTER)

                # Adding a message box for typing customer note
                customernoteEntry = scrolledtext.ScrolledText(
                    rightBottom1_panel, font=("Dodge", 12, "italic", "bold"), width=int(screen_width/35), height=int(screen_height/100), wrap=WORD)
                customernoteEntry.place(relx=0.65, rely=0.67, anchor=SW)

                customernoteEntry.insert(INSERT, "Thank you for purchasing :)")

                # Creating a AddClient button
                # Styling the AddClient Button
                addClient_btn_style = Style(rightBottom1_panel)
                addClient_btn_style.theme_use("default")
                addClient_btn_style.configure(
                    "AddClientButton.TButton", font=("Dodge", 16, "bold"), foreground="#B3C6E7", background="#2D361C", borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of minimize button
                addClient_btn_style.map("AddClientButton.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))], foreground=[("active", "!disabled", "#01102E")],
                                        background=[("active", "#656D4A")])

                addClient_btn = Button(
                    rightBottom1_panel, text="Add Client", image=icon7, compound=LEFT, style="AddClientButton.TButton", command=lambda: addClient())
                addClient_btn.place(relx=0.83, rely=0.88, anchor=CENTER)

            def triggering_newClient():  # function for deleting the client widgets and triggers the function for adding new client template

                # this prevents the function to be called twice by disabling the button
                clientsCreate_btn.configure(state=DISABLED)

                # Calling shrink_leftPanel() to shrink the left panel and also expand the right panel
                shrink_clientsLeftPanel()

                # this triggers the function for adding client templete
                root.after(200, lambda: newClient())

            # function for destroying the label widget created by entered_fields() function
            def leaved_fields(event):

                # deleting the label
                fields_info.destroy()

            # function for creating and showing a label with some text when called by the mouse hover over table fields
            def entered_fields_B(event):

                # assigning the label as global variable
                global fields_info

                # creating and positioning the label
                fields_info = Label(rightBottom_panel, text="# Double click on the client name to view", font=("Dodge", 14, "bold"),
                                    background=rightBottom_label1_bG, foreground="#401414")
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            # function for creating and showing a label with some text when called by the mouse hover over table fields
            def entered_fields(event):

                # assigning the label as global variable
                global fields_info

                # creating and positioning the label
                fields_info = Label(rightBottom_panel, text="# Double click on the client name to view", font=("Dodge", 12, "bold"),
                                    background=rightBottom_label1_bG, foreground="#401414")
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            # function which wraps the text inside table fields
            def wrapLength(string, length=45):

                # this returns the textwrapped in it's field
                return "\n".join(textwrap.wrap(string, length))

            # function which wraps the text inside table fields
            def wrapLengthE(string, length=25):

                # this returns the textwrapped in it's field
                return "\n".join(textwrap.wrap(string, length))

            def shrink_clientsLeftPanel():

                def expand_clientsLeftPanel(event):

                    # Enable the disabled button
                    rightTop_panel_wrapBtn.configure(state=NORMAL)

                    # shrinking the widgets of right panel
                    right_panel.configure(height=int(screen_height/1.035),
                                          width=int(screen_width-(screen_width/4.6)))

                    # shrinking the widgets of rightTop panel
                    rightTop_panel.configure(height=int(screen_height/10),
                                             width=int(screen_width-(screen_width/4.6)))

                    rightTop_panel_label0.configure(
                        width=int(screen_width/7.55))

                    # deleting the profile picture on rightTop panel
                    rightTop_panel_profile.destroy()

                    # shrinking the widgets of rightBottom panel
                    rightBottom_panel.configure(
                        width=int(screen_width-(screen_width/4.6)))

                    rightBottom_panel_label_01.configure(
                        width=int(screen_width/8.3))

                    # expanding the widgets of left panel
                    left_panel.configure(height=int(
                        screen_height/1.035), width=int(screen_width/4.55))

                    # expanding the widgets of leftTop panel
                    leftTop_panel.configure(height=int(screen_height/3.05),
                                            width=int(screen_width/4.55))
                    # showing the wrap button
                    rightTop_panel_wrapBtn.lift(rightTop_panel_label0)

                    # Showing the profile picture again
                    leftTop_panel_bgImg.configure(image=img1)
                    # this changes the function assigned with the profile picture by mouse left-click
                    root.after(100, lambda: leftTop_panel_bgImg.bind(
                        "<Button-1>", change_profile))

                    # expanding the widgets of leftBottom panel
                    leftBottom_panel.configure(height=int(
                        screen_height/1.55), width=int(screen_width/4.55))

                    # Changing the button size and position to normal
                    option1.configure(text="    Dashboard")
                    option1.place(relx=0.5, rely=0.1, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option2.configure(text="    Invoices   ")
                    option2.place(relx=0.5, rely=0.24, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option3.configure(text="   Clients       ")
                    option3.place(relx=0.5, rely=0.38, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option4.configure(text="    Stocks      ")
                    option4.place(relx=0.5, rely=0.52, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option5.configure(text="   Settings    ")
                    option5.place(relx=0.5, rely=0.66, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)

                    # shrinking the clients table
                    clientsTable_header.configure(
                        width=int(screen_width-(screen_width/3)))
                    clientsTable_header_bgColor.place(
                        width=int(screen_width-(screen_width/3)))

                    # table rows
                    fields.place(width=int(screen_width/1.5))

                    # Changing back to the initial function assigned with the hover on table
                    root.after(100, lambda: fields.bind(
                        "<Enter>", entered_fields))

                # Calling the function to shrink left panel
                shrink_leftPanel()
                # this changes the function assigned with the profile picture by mouse left-click
                global unbindExpand
                unbindExpand = leftTop_panel_bgImg.bind(
                    "<Button-1>", expand_clientsLeftPanel)

                # expanding the clients table
                clientsTable_header.configure(
                    width=int(screen_width-(screen_width/5.5)))
                clientsTable_header_bgColor.place(
                    width=int(screen_width-(screen_width/5.5)))

                # table rows
                fields.place(width=int(screen_width/1.222))

                # Changing the function assigned with the hover on table
                root.after(100, lambda: fields.bind(
                    "<Enter>", entered_fields_B))

            # Changing the wrap button function
            rightTop_panel_wrapBtn.configure(
                command=lambda: shrink_clientsLeftPanel())

            # Creating a label showing the icon and text
            rightBottom_panel_label1 = Label(
                rightBottom_panel, image=icon7, text="   Clients", font=("Dodge", 16, "bold"), background=rightBottom_label1_bG, compound=LEFT)
            rightBottom_panel_label1.place(relx=0.12, rely=0.12, anchor=CENTER)

            # Creating a button to call new clients template
            clientsCreate_btn_style = Style(rightBottom_panel)
            clientsCreate_btn_style.theme_use("default")
            clientsCreate_btn_style.configure(
                "CreateClients.TButton", font=("Dodge", 10, "bold"), background="#0CB0A9", borderwidth=3, focuscolor="none", anchor=CENTER)

            # Changing the mapping style of background color button
            clientsCreate_btn_style.map("CreateClients.TButton", foreground=[("active", "!disabled", "black")],
                                        background=[("active", "#61818D")])
            clientsCreate_btn = Button(
                rightBottom_panel, text="Add client", style="CreateClients.TButton", command=lambda: triggering_newClient())
            clientsCreate_btn.place(relx=0.15, rely=0.2, anchor=CENTER)

            # Creating a table showing the previously created clients
            # Creating a frame for the clients table header
            clientsTable_header = Frame(rightBottom_panel, height=int(screen_height/10),
                                        width=int(screen_width-(screen_width/3)))
            clientsTable_header.place(relx=0.5, rely=0.33, anchor=CENTER)

            # Background color for label clients table header
            header_bgColor = "#9BA984"

            clientsTable_header_bgColor = Label(
                clientsTable_header, background=header_bgColor)
            clientsTable_header_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/10),
                                              width=int(screen_width-(screen_width/3)), anchor=CENTER)

            # Creating headings for the clients table header
            clientsTable_heading1 = Label(
                clientsTable_header, text="No.", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            clientsTable_heading1.place(relx=0.08, rely=0.3, anchor=N)
            clientsTable_heading2 = Label(
                clientsTable_header, text="Client Name", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=W)
            clientsTable_heading2.place(relx=0.32, rely=0.3, anchor=N)
            clientsTable_heading3 = Label(
                clientsTable_header, text="Email", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            clientsTable_heading3.place(relx=0.69, rely=0.3, anchor=N)
            clientsTable_heading4 = Label(
                clientsTable_header, text="Contact", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            clientsTable_heading4.place(relx=0.9, rely=0.3, anchor=N)

            # Styling the clients table fields
            fields_style = Style(rightBottom_panel)
            fields_style.theme_use("default")
            fields_style.configure(
                "Fields.Treeview", font=("Dodge", 12), borderwidth=0, highlightthickness=0, rowheight=120, anchor=CENTER)

            # Creating the clients table columns and rows
            fields = Treeview(rightBottom_panel, selectmode=NONE,
                              style="Fields.Treeview")
            fields.place(relx=0.5, rely=0.35, width=int(
                screen_width/1.5), height=int(screen_height/2.8), anchor=N)

            fields["columns"] = ["1", "2", "3", "4"]
            fields.column("1", width=int(screen_width/1000), anchor=CENTER)
            fields.column("2", width=int(screen_width/6), anchor=CENTER)
            fields.column("3", width=int(screen_width/15), anchor=CENTER)
            fields.column("4", width=int(screen_width/60), anchor=CENTER)

            fields["show"] = ["headings"]

            # Creating new database for the new user
            user_inV = sqlite3.connect(
                str(inVoiceDB)+"in_voice.db")

            # Creating a cursor
            co = user_inV.cursor()

            # Creating a table clientDetails if not exists
            co.execute("""CREATE TABLE IF NOT EXISTS clientDetails (
                            clientName TEXT,
                            emailId TEXT,
                            contactNumber Integer,
                            addressLine1 TEXT,
                            addressLine2 TEXT,
                            addressLine3 TEXT,
                            cityName TEXT,
                            pinCode TEXT,
                            customerNote TEXT
                            )""")

            # query the database
            co.execute(
                "SELECT *, oid FROM clientDetails")
            clients = co.fetchall()
            # print(len(clients))

            if not len(clients) == 0:

                for client in clients:

                    if int(client[9]) % 2 == 0:

                        fields.insert("", "end",
                                      values=(str(client[9]), wrapLength(str(client[0])), wrapLengthE(str(client[1])), str(client[2])), tag="even")

                    else:

                        fields.insert("", "end",
                                      values=(str(client[9]), wrapLength(str(client[0])), wrapLengthE(str(client[1])), str(client[2])), tag="odd")

                # Changing intermediate background
                fields.tag_configure("even", background="#E8E8E4")

                # # this calls the function assigned with double-click mouse left button
                unBindclients = fields.bind("<Double-1>", clientShow)

                # this calls the function assigned with the cursor entry and leaving over clients table
                fields.bind("<Enter>", entered_fields)
                fields.bind("<Leave>", leaved_fields)

                # commit changes
                user_inV.commit()

                # close connection
                user_inV.close()

            elif len(clients) == 0:
                # Creating a label to occupy the empty fields
                field_label1 = Label(fields, text="SORRY!", font=(
                    "Dodge", 17, "bold"), background="white", foreground="#401414", justify=CENTER)
                field_label1.place(relx=0.5, rely=0.4, anchor=CENTER)
                field_label2 = Label(fields, text="no client details to show", font=(
                    "Dodge", 14, "bold"), background="white", foreground="#401414", justify=CENTER)
                field_label2.place(relx=0.5, rely=0.6, anchor=CENTER)

            # To lift the frame over clients table header
            clientsTable_header.lift(fields)

        def stocks_btn():  # function for creating the stocks panel

            def limitingOption():  # function for making the full screen non-shrinkable

                def limitingOption5():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with settings button
                        settingsTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption4():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with stocks button
                        stocksTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption3():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function for clients panel and closes the add client panel
                        clientsTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption2():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function to invoice panel
                        invoicesTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                def limitingOption1():  # function for asking a question

                    # Creating a askquestion message box
                    limitingOptions_value = messagebox.askquestion(
                        "Warning !", "Discard Changes?")

                    # Setting a condition
                    if limitingOptions_value == "yes":

                        # this calls the function assigned with dashboard button
                        dashboardTab()

                # changing the function of all option buttons
                option1.configure(command=lambda: limitingOption1())
                option2.configure(command=lambda: limitingOption2())
                option3.configure(command=lambda: limitingOption3())
                option4.configure(style="Options.TLabel",
                                  state=NORMAL, command=lambda: limitingOption4())
                option5.configure(command=lambda: limitingOption5())
                root.after(200, lambda: leftTop_panel_bgImg.unbind(
                    "<Button-1>", unbindExpand))

            def stockShow(event):  # function which shows the selected stock

                def stockDelete():  # function for deleting the selected stock

                    deletingStock = messagebox.askyesno(
                        "Delete Stock", "Are you sure you want to delete product details?")

                    if deletingStock == True:

                        # Creating new database for the new user
                        user_inV = sqlite3.connect(
                            str(inVoiceDB)+"in_voice.db")

                        # Creating a cursor
                        co = user_inV.cursor()

                        # Deleting stock from productDetails table
                        co.execute(
                            "DELETE from productDetails WHERE oid = " + str(stockNumber))

                        # commit changes
                        user_inV.commit()

                        # close connection
                        user_inV.close()

                        # this calls the function for stocks panel and closes the add stock panel
                        stocksTab()
                        dashboardTab()

                        # changing the function of all option buttons back to the previous one
                        option1.configure(command=lambda: dashboardTab())
                        option2.configure(
                            command=lambda: [invoicesTab(), dashboardTab()])
                        option3.configure(
                            command=lambda: [clientsTab(), dashboardTab()])
                        option4.configure(
                            command=lambda: [stocksTab(), dashboardTab()])
                        option5.configure(
                            command=lambda: [settingsTab(), dashboardTab()])

                    elif deletingStock == False:
                        return

                def stockEdit():  # function for editing the selected stock

                    def updateStockDetails():  # function for saving the new changes to database

                        # Checking the entries are not empty
                        if nameEntry_Var.get() == "" or MRPEntry_Var.get() == "" or quantityEntry_Var.get() == "" or purchaseRateEntry_Var.get() == "" or salesRateEntry_Var.get() == "" or reOrderEntry_Var.get() == "":

                            messagebox.showerror(
                                "Empty field", "Make sure all fields are filled")

                        elif len(nameEntry_Var.get()) < 3:

                            messagebox.showerror(
                                "Required", "Product Name should have minimum 3 characters")

                        elif not quantityEntry_Var.get().isdigit() or not reOrderEntry_Var.get().isdigit():

                            messagebox.showerror(
                                "Required", "Quantities must contain numbers only")
                            quantityEntry_Var.set("0")
                            reOrderEntry_Var.set("0")

                        else:

                            updatingtoStocks = messagebox.askyesno(
                                "Save Product", "Are you sure you want to save changes?")

                            if updatingtoStocks == True:

                                # Creating new database for the new user
                                user_inV = sqlite3.connect(
                                    str(inVoiceDB)+"in_voice.db")

                                # Creating a cursor
                                co = user_inV.cursor()

                                # insert into table
                                co.execute("UPDATE productDetails SET  productName = :productName, productMRP = :productMRP, quantity = :quantity, purchaseRate = :purchaseRate, salesRate = :salesRate, reOrderQuantity = :reOrderQuantity WHERE oid = :stockNumber",
                                           {
                                               "productName": nameEntry_Var.get(),
                                               "productMRP": MRPEntry_Var.get(),
                                               "quantity": quantityEntry_Var.get(),
                                               "purchaseRate": purchaseRateEntry_Var.get(),
                                               "salesRate": salesRateEntry_Var.get(),
                                               "reOrderQuantity": reOrderEntry_Var.get(),

                                               "stockNumber": stockNumber
                                           })

                                # commit changes
                                user_inV.commit()

                                # close connection
                                user_inV.close()

                                # this calls the function for stocks panel and closes the add client panel
                                stocksTab()
                                dashboardTab()

                                # changing the function of all option buttons back to the previous one
                                option1.configure(
                                    command=lambda: dashboardTab())
                                option2.configure(
                                    command=lambda: [invoicesTab(), dashboardTab()])
                                option3.configure(
                                    command=lambda: [clientsTab(), dashboardTab()])
                                option4.configure(
                                    command=lambda: [stocksTab(), dashboardTab()])
                                option5.configure(
                                    command=lambda: [settingsTab(), dashboardTab()])

                            elif updatingtoStocks == False:
                                return

                    # Creating entries of client create panel
                    # Name entry
                    nameEntry_Var = StringVar()
                    nameEntry_Var.set(show_productName)
                    nameEntry = tk.Entry(rightBottom2_panel, textvariable=nameEntry_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/35))
                    nameEntry.place(relx=0.58, rely=0.17, height=int(
                        screen_height/20), anchor=CENTER)

                    # MRP entry
                    MRPEntry_Var = StringVar()
                    MRPEntry_Var.set(show_MRP)
                    MRPEntry = tk.Entry(rightBottom2_panel, textvariable=MRPEntry_Var,
                                        font=("Dodge", 15, "bold"), width=int(screen_width/70))
                    MRPEntry.place(relx=0.5, rely=0.3, height=int(
                        screen_height/20), anchor=CENTER)

                    # Quantity entry
                    quantityEntry_Var = StringVar()
                    quantityEntry_Var.set(show_quantity)
                    quantityEntry = tk.Entry(rightBottom2_panel, textvariable=quantityEntry_Var,
                                             font=("Dodge", 15, "bold"), width=int(screen_width/70))
                    quantityEntry.place(relx=0.5, rely=0.43, height=int(
                        screen_height/20), anchor=CENTER)

                    # PurchaseRate entry
                    purchaseRateEntry_Var = StringVar()
                    purchaseRateEntry_Var.set(show_purchaseRate)
                    purchaseRateEntry = tk.Entry(rightBottom2_panel, textvariable=purchaseRateEntry_Var,
                                                 font=("Dodge", 15, "bold"), width=int(screen_width/70))
                    purchaseRateEntry.place(relx=0.5, rely=0.56, height=int(
                        screen_height/20), anchor=CENTER)

                    # SalesRate entry
                    salesRateEntry_Var = StringVar()
                    salesRateEntry_Var.set(show_salesRate)
                    salesRateEntry = tk.Entry(rightBottom2_panel, textvariable=salesRateEntry_Var,
                                              font=("Dodge", 15, "bold"), width=int(screen_width/70))
                    salesRateEntry.place(relx=0.5, rely=0.69, height=int(
                        screen_height/20), anchor=CENTER)

                    # Re-Order entry
                    reOrderEntry_Var = StringVar()
                    reOrderEntry_Var.set(show_reOrderQuantity)
                    reOrderEntry = tk.Entry(rightBottom2_panel, textvariable=reOrderEntry_Var,
                                            font=("Dodge", 15, "bold"), width=int(screen_width/70))
                    reOrderEntry.place(relx=0.5, rely=0.82, height=int(
                        screen_height/20), anchor=CENTER)

                    # destroying all values
                    nameLabel.destroy()
                    MRPLabel.destroy()
                    quantityLabel.destroy()
                    purchaseRateLabel.destroy()
                    salesRateLabel.destroy()
                    reOrderQuantityLabel.destroy()

                    # Changing the edit button to save button
                    editStock_btn.configure(
                        text="save", image=icon7, compound=LEFT, command=lambda: updateStockDetails())

                # Getting the stock details according to the field selection
                stockNumber = fields.item(fields.focus())['values'][0]
                # print(stockNumber)

                # Unbinding the click function on stocks table
                fields.unbind("<Double-1>", unBindStocks)

                # Creating new database for the new user
                user_inV = sqlite3.connect(
                    str(inVoiceDB)+"in_voice.db")

                # Creating a cursor
                co = user_inV.cursor()

                # query the database
                co.execute("SELECT * FROM productDetails WHERE oid = " +
                           "'" + str(stockNumber) + "'")
                stocks = co.fetchall()
                # print(stocks)

                # converting tuples into separate strings
                show_productName = ""
                for stock in stocks:
                    show_productName += str(stock[0])

                show_MRP = ""
                for stock in stocks:
                    show_MRP += str(stock[1])

                show_quantity = ""
                for stock in stocks:
                    show_quantity += str(stock[2])

                show_purchaseRate = ""
                for stock in stocks:
                    show_purchaseRate += str(stock[3])

                show_salesRate = ""
                for stock in stocks:
                    show_salesRate += str(stock[4])

                show_reOrderQuantity = ""
                for stock in stocks:
                    show_reOrderQuantity += str(stock[5])

                # commit changes
                user_inV.commit()

                # close connection
                user_inV.close()

                # Calling shrink_leftPanel() to shrink the left panel and also expand the right panel
                shrink_stocksLeftPanel()
                # this function makes the panel non-shrikable
                limitingOption()

                # Creating a new frame on the rightBottom panel
                rightBottom2_panel = Frame(right_panel, height=int(screen_height/1.04),
                                           width=int(screen_width-(screen_width/15.1)))
                rightBottom2_panel.place(relx=1, rely=1, anchor=SE)

                # Creating a labels for background color of frame
                rightBottom2_panel_label0 = Label(
                    rightBottom2_panel, background="#B3C6E7", width=int(screen_width/4.6))
                rightBottom2_panel_label0.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1), anchor=CENTER)

                # Background and Foreground color for label and the buttons in the leftBottom panel
                rightBottom2_label1_bG = "#F0EFF4"
                rightBottom2_label1_fG = "#401414"
                # Creating a labels for background color
                rightBottom_panel_label_01 = Label(
                    rightBottom2_panel, background=rightBottom2_label1_bG, width=int(screen_width/6.75))
                rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1.1), anchor=CENTER)

                rightBottom2_panel_fG = "#3C2212"

                # Creating labels of stocks create panel
                # Name entry label
                nameEntry_label = Label(
                    rightBottom2_panel, text="Product Name  :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG, justify=RIGHT)
                nameEntry_label.place(
                    relx=0.29, rely=0.17, anchor=CENTER)

                # Name label value
                nameLabel = Label(rightBottom2_panel, text=show_productName, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                nameLabel.place(relx=0.39, rely=0.17, anchor=W)

                # MRP entry label
                MRPEntry_label = Label(
                    rightBottom2_panel, text="M.R.P         :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                MRPEntry_label.place(
                    relx=0.3, rely=0.3, anchor=CENTER)

                # MRP label value
                MRPLabel = Label(rightBottom2_panel, text=show_MRP, font=(
                    "Dodge", 15, "bold"), wraplength=300, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                MRPLabel.place(relx=0.39, rely=0.3, anchor=W)

                # Quantity entry label
                quantityEntry_label = Label(
                    rightBottom2_panel, text="Quantity      :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                quantityEntry_label.place(
                    relx=0.3, rely=0.43, anchor=CENTER)

                # Quantity  label value
                quantityLabel = Label(rightBottom2_panel, text=show_quantity, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                quantityLabel.place(relx=0.4, rely=0.43, anchor=W)

                # Purchase Rate entry label
                purchaseRateEntry_label = Label(
                    rightBottom2_panel, text="Purchase Rate   :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                purchaseRateEntry_label.place(
                    relx=0.285, rely=0.56, anchor=CENTER)

                # Purchase Rate label value
                purchaseRateLabel = Label(rightBottom2_panel, text=show_purchaseRate, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                purchaseRateLabel.place(relx=0.39, rely=0.56, anchor=W)

                # Sales Rate entry label
                salesRateEntry_label = Label(
                    rightBottom2_panel, text="Sales Rate       :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                salesRateEntry_label.place(
                    relx=0.285, rely=0.69, anchor=CENTER)

                # Sales Rate label value
                salesRateLabel = Label(rightBottom2_panel, text=show_salesRate, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                salesRateLabel.place(relx=0.39, rely=0.69, anchor=W)

                # Re-Order Quantity entry label
                reOrderQuantityEntry_label = Label(
                    rightBottom2_panel, text="Re-Order Quantity   :", font=("Dodge", 15), background=rightBottom2_label1_bG, foreground=rightBottom2_panel_fG)
                reOrderQuantityEntry_label.place(
                    relx=0.27, rely=0.82, anchor=CENTER)

                # Re-Order Quantity label value
                reOrderQuantityLabel = Label(rightBottom2_panel, text=show_reOrderQuantity, font=(
                    "Dodge", 15, "bold"), wraplength=350, background=rightBottom2_label1_bG, foreground=rightBottom2_label1_fG, justify=LEFT)
                reOrderQuantityLabel.place(relx=0.4, rely=0.82, anchor=W)

                # Creating a EditStock button
                # Styling the EditStock Button
                editStock_btn_style = Style(rightBottom2_panel)
                editStock_btn_style.theme_use("default")
                editStock_btn_style.configure(
                    "EditStockButton.TButton", font=("Dodge", 16, "bold"), foreground="#B3C6E7", background="#656D4A", borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of EditStock button
                editStock_btn_style.map("EditStockButton.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))], foreground=[("active", "!disabled", "#B3C6E7")],
                                        background=[("active", "#2D361C")])

                editStock_btn = Button(
                    rightBottom2_panel, text="edit", image=icon13, compound=LEFT, style="EditStockButton.TButton", command=lambda: stockEdit())
                editStock_btn.place(relx=0.83, rely=0.88, width=int(
                    screen_width/12), anchor=CENTER)

                # Styling delete stock button
                deletestock_style = Style()
                deletestock_style.theme_use("default")
                deletestock_style.configure("DeleteStockButton.TButton", background=rightBottom2_label1_bG,
                                            foreground=rightBottom2_label1_fG, borderwidth=0, focuscolor="none", relief=FLAT, highlightthickness=0)
                # mouse hover style for delete stock button
                deletestock_style.map("DeleteStockButton.TButton", foreground=[(
                    "active", "!disabled", "#F0EFF4")], background=[("active", rightBottom2_label1_bG)])

                # Adding a delete button for deleting the stock details
                deletestock_btn = Button(
                    rightBottom2_panel, image=icon14, style="DeleteStockButton.TButton", command=lambda: stockDelete())
                deletestock_btn.place(relx=0.94, rely=0.08, anchor=CENTER)

            def newStock():  # function for creating a new product template

                def addStock():  # function for adding product to the database

                    # Checking the entries are not empty
                    if nameEntry_Var.get() == "" or MRPEntry_Var.get() == "" or quantityEntry_Var.get() == "" or purchaseRateEntry_Var.get() == "" or salesRateEntry_Var.get() == "" or reOrderEntry_Var.get() == "":

                        messagebox.showerror(
                            "Empty field", "Make sure all fields are filled")

                    elif len(nameEntry_Var.get()) < 3:

                        messagebox.showerror(
                            "Required", "Product Name should have minimum 3 characters")

                    elif not quantityEntry_Var.get().isdigit() or not reOrderEntry_Var.get().isdigit():

                        messagebox.showerror(
                            "Required", "Quantities must contain numbers only")
                        quantityEntry_Var.set("0")
                        reOrderEntry_Var.set("0")

                    else:

                        savingtoStocks = messagebox.askyesno(
                            "Save Product", "Are you sure you want to save changes?")

                        if savingtoStocks == True:

                            # Creating new database for the new user
                            user_inV = sqlite3.connect(
                                str(inVoiceDB)+"in_voice.db")

                            # Creating a cursor
                            co = user_inV.cursor()

                            # insert into table
                            co.execute("INSERT INTO productDetails VALUES (:productName, :productMRP, :quantity, :purchaseRate, :salesRate, :reOrderQuantity)",
                                       {
                                           "productName": nameEntry_Var.get(),
                                           "productMRP": MRPEntry_Var.get(),
                                           "quantity": quantityEntry_Var.get(),
                                           "purchaseRate": purchaseRateEntry_Var.get(),
                                           "salesRate": salesRateEntry_Var.get(),
                                           "reOrderQuantity": reOrderEntry_Var.get()
                                       })

                            # commit changes
                            user_inV.commit()

                            # close connection
                            user_inV.close()

                            # this calls the function for stocks panel and closes the add stock panel
                            stocksTab()
                            dashboardTab()

                            # changing the function of all option buttons back to the previous one
                            option1.configure(command=lambda: dashboardTab())
                            option2.configure(
                                command=lambda: [invoicesTab(), dashboardTab()])
                            option3.configure(
                                command=lambda: [clientsTab(), dashboardTab()])
                            option4.configure(
                                command=lambda: [stocksTab(), dashboardTab()])
                            option5.configure(
                                command=lambda: [settingsTab(), dashboardTab()])

                        elif savingtoStocks == False:
                            return

                # this function makes the panel non-shrikable
                limitingOption()

                # Creating a new frame on the rightBottom1 panel
                rightBottom1_panel = Frame(right_panel, height=int(screen_height/1.04),
                                           width=int(screen_width-(screen_width/15.1)))
                rightBottom1_panel.place(relx=1, rely=1, anchor=SE)

                # Creating a labels for background color of frame
                rightBottom1_panel_label0 = Label(
                    rightBottom1_panel, background="#B3C6E7", width=int(screen_width/4.6))
                rightBottom1_panel_label0.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1), anchor=CENTER)

                # Background and Foreground color for label and the buttons in the leftBottom panel
                rightBottom1_label1_bG = "#F0EFF4"
                rightBottom1_label1_fG = "#401414"
                # Creating a labels for background color
                rightBottom_panel_label_01 = Label(
                    rightBottom1_panel, background=rightBottom1_label1_bG, width=int(screen_width/6.75))
                rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
                    screen_height/1.1), anchor=CENTER)

                # Creating labels of stock create panel
                # Name entry label
                nameEntry_label = Label(
                    rightBottom1_panel, text="Product Name", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                nameEntry_label.place(
                    relx=0.2, rely=0.15, anchor=CENTER)

                # MRP entry1 label
                MRPEntry_label = Label(
                    rightBottom1_panel, text="M.R.P", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                MRPEntry_label.place(
                    relx=0.2, rely=0.3, anchor=CENTER)

                # Quantity entry label
                quantityEntry_label = Label(
                    rightBottom1_panel, text="Quantity", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                quantityEntry_label.place(
                    relx=0.55, rely=0.3, anchor=CENTER)

                # PurchaseRate entry1 label
                purchaseRateEntry1_label = Label(
                    rightBottom1_panel, text="Purchase Rate", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG)
                purchaseRateEntry1_label.place(
                    relx=0.18, rely=0.48, anchor=CENTER)

                # SalesRate entry label
                salesRateEntry_label = Label(
                    rightBottom1_panel, text="Sales Rate", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                salesRateEntry_label.place(
                    relx=0.55, rely=0.48, anchor=CENTER)

                # Re-Order entry label
                reOrderEntry_label = Label(
                    rightBottom1_panel, text="Re-Order Quantity", font=("Dodge", 15, "bold"), background=rightBottom1_label1_bG, foreground=rightBottom1_label1_fG, justify=RIGHT)
                reOrderEntry_label.place(
                    relx=0.3, rely=0.7, anchor=CENTER)

                # Creating entries of stock create panel
                # Name entry
                nameEntry_Var = StringVar()
                nameEntry = tk.Entry(rightBottom1_panel, textvariable=nameEntry_Var,
                                     font=("Dodge", 15, "bold"), width=int(screen_width/30), justify=RIGHT)
                nameEntry.place(relx=0.5, rely=0.15, height=int(
                    screen_height/20), anchor=CENTER)

                # MRP entry
                MRPEntry_Var = StringVar()
                MRPEntry = tk.Entry(rightBottom1_panel, textvariable=MRPEntry_Var,
                                    font=("Dodge", 15, "bold"), width=int(screen_width/70), justify=RIGHT)
                MRPEntry.place(relx=0.35, rely=0.3, height=int(
                    screen_height/20), anchor=CENTER)

                # Quantity entry
                quantityEntry_Var = StringVar()
                quantityEntry = tk.Entry(rightBottom1_panel, textvariable=quantityEntry_Var,
                                         font=("Dodge", 15, "bold"), width=int(screen_width/90), justify=RIGHT)
                quantityEntry.place(relx=0.7, rely=0.3, height=int(
                    screen_height/20), anchor=CENTER)

                # PurchaseRate entry
                purchaseRateEntry_Var = StringVar()
                purchaseRateEntry = tk.Entry(rightBottom1_panel, textvariable=purchaseRateEntry_Var,
                                             font=("Dodge", 15, "bold"), width=int(screen_width/70), justify=RIGHT)
                purchaseRateEntry.place(relx=0.35, rely=0.48, height=int(
                    screen_height/20), anchor=CENTER)

                # SalesRate entry
                salesRateEntry_Var = StringVar()
                salesRateEntry = tk.Entry(rightBottom1_panel, textvariable=salesRateEntry_Var,
                                          font=("Dodge", 15, "bold"), width=int(screen_width/90), justify=RIGHT)
                salesRateEntry.place(relx=0.7, rely=0.48, height=int(
                    screen_height/20), anchor=CENTER)

                # Re-Order entry
                reOrderEntry_Var = StringVar()
                reOrderEntry = tk.Entry(rightBottom1_panel, textvariable=reOrderEntry_Var,
                                        font=("Dodge", 15, "bold"), width=int(screen_width/90), justify=RIGHT)
                reOrderEntry.place(relx=0.5, rely=0.7, height=int(
                    screen_height/20), anchor=CENTER)

                # Creating a AddStock button
                # Styling the AddStock Button
                addStock_btn_style = Style(rightBottom1_panel)
                addStock_btn_style.theme_use("default")
                addStock_btn_style.configure(
                    "AddStockButton.TButton", font=("Dodge", 16, "bold"), foreground="#B3C6E7", background="#2D361C", borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of minimize button
                addStock_btn_style.map("AddStockButton.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))], foreground=[("active", "!disabled", "#01102E")],
                                       background=[("active", "#656D4A")])

                addStock_btn = Button(
                    rightBottom1_panel, text="Add Stock", image=icon8, compound=LEFT, style="AddStockButton.TButton", command=lambda: addStock())
                addStock_btn.place(relx=0.83, rely=0.88, anchor=CENTER)

            def triggering_newStock():  # function for deleting the stocks widgets and triggers the function for adding new stock template

                # this prevents the function to be called twice by disabling the button
                stocksCreate_btn.configure(state=DISABLED)

                # Calling shrink_leftPanel() to shrink the left panel and also expand the right panel
                shrink_stocksLeftPanel()

                # this triggers the function for adding stock templete
                root.after(200, lambda: newStock())

            # function for destroying the label widget created by entered_fields() function
            def leaved_fields(event):

                # deleting the label
                fields_info.destroy()

            # function for creating and showing a label with some text when called by the mouse hover over table fields
            def entered_fields_B(event):

                # assigning the label as global variable
                global fields_info

                # creating and positioning the label
                fields_info = Label(rightBottom_panel, text="# Double click on the product name to view", font=("Dodge", 14, "bold"),
                                    background=rightBottom_label1_bG, foreground="#401414")
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            # function for creating and showing a label with some text when called by the mouse hover over table fields
            def entered_fields(event):

                # assigning the label as global variable
                global fields_info

                # creating and positioning the label
                fields_info = Label(rightBottom_panel, text="# Double click on the product name to view", font=("Dodge", 12, "bold"),
                                    background=rightBottom_label1_bG, foreground="#401414")
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            # function which wraps the text inside table fields
            def wrapLength(string, length=45):

                # this returns the textwrapped in it's field
                return "\n".join(textwrap.wrap(string, length))

            def shrink_stocksLeftPanel():

                def expand_stocksLeftPanel(event):

                    # Enable the disabled button
                    rightTop_panel_wrapBtn.configure(state=NORMAL)

                    # shrinking the widgets of right panel
                    right_panel.configure(height=int(screen_height/1.035),
                                          width=int(screen_width-(screen_width/4.6)))

                    # shrinking the widgets of rightTop panel
                    rightTop_panel.configure(height=int(screen_height/10),
                                             width=int(screen_width-(screen_width/4.6)))

                    rightTop_panel_label0.configure(
                        width=int(screen_width/7.55))

                    # deleting the profile picture on rightTop panel
                    rightTop_panel_profile.destroy()

                    # shrinking the widgets of rightBottom panel
                    rightBottom_panel.configure(
                        width=int(screen_width-(screen_width/4.6)))

                    rightBottom_panel_label_01.configure(
                        width=int(screen_width/8.3))

                    # expanding the widgets of left panel
                    left_panel.configure(height=int(
                        screen_height/1.035), width=int(screen_width/4.55))

                    # expanding the widgets of leftTop panel
                    leftTop_panel.configure(height=int(screen_height/3.05),
                                            width=int(screen_width/4.55))
                    # showing the wrap button
                    rightTop_panel_wrapBtn.lift(rightTop_panel_label0)

                    # Showing the profile picture again
                    leftTop_panel_bgImg.configure(image=img1)
                    # this changes the function assigned with the profile picture by mouse left-click
                    root.after(100, lambda: leftTop_panel_bgImg.bind(
                        "<Button-1>", change_profile))

                    # expanding the widgets of leftBottom panel
                    leftBottom_panel.configure(height=int(
                        screen_height/1.55), width=int(screen_width/4.55))

                    # Changing the button size and position to normal
                    option1.configure(text="    Dashboard")
                    option1.place(relx=0.5, rely=0.1, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option2.configure(text="    Invoices   ")
                    option2.place(relx=0.5, rely=0.24, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option3.configure(text="   Clients       ")
                    option3.place(relx=0.5, rely=0.38, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option4.configure(text="    Stocks      ")
                    option4.place(relx=0.5, rely=0.52, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)
                    option5.configure(text="   Settings    ")
                    option5.place(relx=0.5, rely=0.66, width=int(
                        screen_width/4.55), height=int(screen_height/12), anchor=N)

                    # shrinking the stocks table
                    stocksTable_header.configure(
                        width=int(screen_width-(screen_width/3)))
                    stocksTable_header_bgColor.place(
                        width=int(screen_width-(screen_width/3)))

                    # table rows
                    fields.place(width=int(screen_width/1.5))

                    # Changing back to the initial function assigned with the hover on table
                    root.after(100, lambda: fields.bind(
                        "<Enter>", entered_fields))

                # Calling the function to shrink left panel
                shrink_leftPanel()
                # this changes the function assigned with the profile picture by mouse left-click
                global unbindExpand
                unbindExpand = leftTop_panel_bgImg.bind(
                    "<Button-1>", expand_stocksLeftPanel)

                # expanding the stocks table
                stocksTable_header.configure(
                    width=int(screen_width-(screen_width/5.5)))
                stocksTable_header_bgColor.place(
                    width=int(screen_width-(screen_width/5.5)))

                # table rows
                fields.place(width=int(screen_width/1.222))

                # Changing the function assigned with the hover on table
                root.after(100, lambda: fields.bind(
                    "<Enter>", entered_fields_B))

            # Changing the wrap button function
            rightTop_panel_wrapBtn.configure(
                command=lambda: shrink_stocksLeftPanel())

            # Creating a label showing the icon and text
            rightBottom_panel_label1 = Label(
                rightBottom_panel, image=icon8, text="   Stocks", font=("Dodge", 16, "bold"), background=rightBottom_label1_bG, compound=LEFT)
            rightBottom_panel_label1.place(relx=0.12, rely=0.12, anchor=CENTER)

            # Creating a button to call new stocks template
            stocksCreate_btn_style = Style(rightBottom_panel)
            stocksCreate_btn_style.theme_use("default")
            stocksCreate_btn_style.configure(
                "CreateStocks.TButton", font=("Dodge", 10, "bold"), background="#0CB0A9", borderwidth=3, focuscolor="none", anchor=CENTER)

            # Changing the mapping style of background color button
            stocksCreate_btn_style.map("CreateStocks.TButton", foreground=[("active", "!disabled", "black")],
                                       background=[("active", "#61818D")])
            stocksCreate_btn = Button(
                rightBottom_panel, text="Add stock", style="CreateStocks.TButton", command=lambda: triggering_newStock())
            stocksCreate_btn.place(relx=0.15, rely=0.2, anchor=CENTER)

            # Creating a table showing the previously created stocks
            # Creating a frame for the stocks table header
            stocksTable_header = Frame(rightBottom_panel, height=int(screen_height/10),
                                       width=int(screen_width-(screen_width/3)))
            stocksTable_header.place(relx=0.5, rely=0.33, anchor=CENTER)

            # Background color for label stocks table header
            header_bgColor = "#9BA984"

            stocksTable_header_bgColor = Label(
                stocksTable_header, background=header_bgColor)
            stocksTable_header_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/10),
                                             width=int(screen_width-(screen_width/3)), anchor=CENTER)

            # Creating headings for the stocks table header
            stocksTable_heading1 = Label(
                stocksTable_header, text="No.", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            stocksTable_heading1.place(relx=0.08, rely=0.3, anchor=N)
            stocksTable_heading2 = Label(
                stocksTable_header, text="Product Name", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=W)
            stocksTable_heading2.place(relx=0.32, rely=0.3, anchor=N)
            stocksTable_heading3 = Label(
                stocksTable_header, text="Rate", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            stocksTable_heading3.place(relx=0.69, rely=0.3, anchor=N)
            stocksTable_heading4 = Label(
                stocksTable_header, text="Quantity", font=("Dodge", 12, "bold"), background=header_bgColor, anchor=CENTER)
            stocksTable_heading4.place(relx=0.9, rely=0.3, anchor=N)

            # Styling the stocks table fields
            fields_style = Style(rightBottom_panel)
            fields_style.theme_use("default")
            fields_style.configure(
                "Fields.Treeview", font=("Dodge", 12), borderwidth=0, highlightthickness=0, rowheight=120, anchor=CENTER)

            # Creating the stocks table columns and rows
            fields = Treeview(rightBottom_panel, selectmode=NONE,
                              style="Fields.Treeview")
            fields.place(relx=0.5, rely=0.35, width=int(
                screen_width/1.5), height=int(screen_height/2.8), anchor=N)

            fields["columns"] = ["1", "2", "3", "4"]
            fields.column("1", width=int(screen_width/1000), anchor=CENTER)
            fields.column("2", width=int(screen_width/6), anchor=CENTER)
            fields.column("3", width=int(screen_width/15), anchor=CENTER)
            fields.column("4", width=int(screen_width/60), anchor=CENTER)

            fields["show"] = ["headings"]

            # Creating new database for the new user
            user_inV = sqlite3.connect(
                str(inVoiceDB)+"in_voice.db")

            # Creating a cursor
            co = user_inV.cursor()

            # Creating a table productDetails if not exists
            co.execute("""CREATE TABLE IF NOT EXISTS productDetails (
                            productName TEXT,
                            productMRP REAL,
                            quantity INTEGER,
                            purchaseRate REAL,
                            salesRate REAL,
                            reOrderQuantity INTEGER
                            )""")

            # query the database
            co.execute(
                "SELECT *, oid FROM productDetails")
            stocks = co.fetchall()
            # print(len(stocks))

            if not len(stocks) == 0:

                for stock in stocks:

                    if int(stock[6]) % 2 == 0:

                        fields.insert("", "end",
                                      values=(str(stock[6]), wrapLength(str(stock[0])), str(stock[4]), str(stock[2])), tag="even")

                    else:

                        fields.insert("", "end",
                                      values=(str(stock[6]), wrapLength(str(stock[0])), str(stock[4]), str(stock[2])), tag="odd")

                # Changing intermediate background
                fields.tag_configure("even", background="#E8E8E4")

                # # this calls the function assigned with double-click mouse left button
                unBindStocks = fields.bind("<Double-1>", stockShow)

                # this calls the function assigned with the cursor entry and leaving over stocks table
                fields.bind("<Enter>", entered_fields)
                fields.bind("<Leave>", leaved_fields)

                # commit changes
                user_inV.commit()

                # close connection
                user_inV.close()

            elif len(stocks) == 0:
                # Creating a label to occupy the empty fields
                field_label1 = Label(fields, text="SORRY!", font=(
                    "Dodge", 17, "bold"), background="white", foreground="#401414", justify=CENTER)
                field_label1.place(relx=0.5, rely=0.4, anchor=CENTER)
                field_label2 = Label(fields, text="no product details to show", font=(
                    "Dodge", 14, "bold"), background="white", foreground="#401414", justify=CENTER)
                field_label2.place(relx=0.5, rely=0.6, anchor=CENTER)

            # To lift the frame over stocks table header
            stocksTable_header.lift(fields)

        def settings_btn():  # function

            # function for changing the currency symbol and value related to currencySelect combobox values
            def currencyValue(event):

                def currencyUpdate():  # function for updating the user typed value to database

                    co.execute("UPDATE updateCurrency SET  valueInIND = :valueInIND WHERE currrency = :currrency",
                               {
                                   "valueInIND": currencyUpdate_entry_Var.get(),

                                   "currrency": currencySelect_box.get()
                               })

                    # commit changes
                    user_inV.commit()

                    # close connection
                    user_inV.close()

                    # Disabling the currency update entry
                    currencyUpdate_entry.configure(state=DISABLED)

                    # Returning back to the main panel
                    root.after(300, lambda: dashboardTab())

                # Creating new database for the new user
                user_inV = sqlite3.connect(
                    str(inVoiceDB)+"in_voice.db")

                # Creating a cursor
                co = user_inV.cursor()

                # query the database
                co.execute(
                    "SELECT *, oid FROM updateCurrency WHERE currrency = " + "'" + str(currencySelect_box.get()) + "'")
                currencys = co.fetchall()

                if not len(currencys) == 0:
                    currency_value1 = ""
                    for currency in currencys:
                        currency_value1 += str(currency[1])

                    # Displaying the value according to the currency database
                    currencyUpdate_entry_Var.set(
                        "%.2f" % float(currency_value1))

                    # Enabling the currency update entry
                    currencyUpdate_entry.configure(state=NORMAL)

                    # Creating a button to set the new value to the database
                    # Styling the Update Button
                    Update_btn_style = Style(rightBottom_panel)
                    Update_btn_style.theme_use("default")
                    Update_btn_style.configure(
                        "UpdateButton.TButton", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background="#656D4A", borderwidth=3, focuscolor="none", justify=CENTER)
                    # Changing the mapping style of Update button
                    Update_btn_style.map("UpdateButton.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))], foreground=[("active", "!disabled", "#B3C6E7")],
                                         background=[("active", "#2D361C")])

                    Update_btn = Button(
                        rightBottom_panel, text="Update", compound=LEFT, style="UpdateButton.TButton", command=lambda: currencyUpdate())
                    Update_btn.place(relx=0.45, rely=0.85, width=int(
                        screen_width/12), anchor=CENTER)

                elif len(currencys) == 0:
                    return

            # function for checking the entry is valid number

            def updateCurrency(var, index, mode):

                # neglecting the empty value
                if currencyUpdate_entry_Var.get() == "":
                    return
                else:
                    try:  # if value is float or integer
                        float(currencyUpdate_entry_Var.get())

                    # if value is other than floats or integer
                    except (ValueError, TclError, FloatingPointError):
                        currencyUpdate_entry_Var.set("%.2f" % 0.00)

            # Creating a label showing the icon and text
            rightBottom_panel_label1 = Label(
                rightBottom_panel, image=icon9, text="   Settings", font=("Dodge", 16, "bold"), background=rightBottom_label1_bG, compound=LEFT)
            rightBottom_panel_label1.place(relx=0.12, rely=0.12, anchor=CENTER)

            # Background and Foreground color for label and the buttons in the leftBottom panel
            rightBottom_label1_fG = "#401414"

            # Currency entry label
            currencySelect_box_label = Label(
                rightBottom_panel, text="Update Currency", font=("Dodge", 14), background=rightBottom_label1_bG, foreground=rightBottom_label1_fG)
            currencySelect_box_label.place(relx=0.35, rely=0.25, anchor=CENTER)

            # Creating entries of invoice create panel
            # Styling the Combobox invoice create panel
            invoiceCreate_btn_style = Style(rightBottom_panel)
            invoiceCreate_btn_style.theme_use("default")
            invoiceCreate_btn_style.configure(
                "InvoiceSelect.TCombobox")
            # Changing the mapping style of Combobox invoice create panel
            invoiceCreate_btn_style.map("InvoiceSelect.TCombobox", fieldbackground=[("readonly", "!focus", "white"), ("readonly", "focus", "white")],
                                        selectbackground=[("readonly", "!focus", "none"), ("readonly", "focus", "none")], selectforeground=[("readonly", "focus", "#0A0908"), ("readonly", "!focus", rightBottom_label1_fG)])

            # Currency select
            currencySelect_box = Combobox(rightBottom_panel, font=("Dodge", 10, "bold"), style="InvoiceSelect.TCombobox",
                                          width=int(screen_width/40), state="readonly")

            currencySelect_box.place(relx=0.45, rely=0.35,
                                     height=int(screen_height/30), anchor=CENTER)

            # assigning values to dropdown box
            currencySelect_box["values"] = (" USD $",
                                            " EUR €",
                                            " INR ₹",
                                            " JPY ¥",
                                            " GBP £",
                                            " CHF",
                                            " CAD $",
                                            " AUD $",
                                            " NZD $",
                                            " ZAR R")
            currencySelect_box.current(2)

            # Creating new database for the new user
            user_inV = sqlite3.connect(
                str(inVoiceDB)+"in_voice.db")

            # Creating a cursor
            co = user_inV.cursor()

            # Creating a table updateCurrency
            co.execute("""CREATE TABLE IF NOT EXISTS updateCurrency (
                            currrency TEXT,
                            valueInIND REAL
                            )""")

            # query the database
            co.execute(
                "SELECT *, oid FROM updateCurrency WHERE currrency = " + "'" + str(currencySelect_box.get()) + "'")
            currencys = co.fetchall()

            currency_value = ""
            for currency in currencys:
                currency_value += str(currency[1])

            # CurrencyUpdate entry label
            currencyUpdate_entry_label = Label(
                rightBottom_panel, text="Currency Value", font=("Dodge", 14), background=rightBottom_label1_bG, foreground=rightBottom_label1_fG)
            currencyUpdate_entry_label.place(
                relx=0.35, rely=0.64, anchor=CENTER)

            # Creating a entry for updating currency values
            currencyUpdate_entry_Var = StringVar()
            currencyUpdate_entry_Var.set("%.2f" % float(currency_value))

            # global currencyUpdate_entry
            # Creating a entry for currencyUpdate
            currencyUpdate_entry = Entry(rightBottom_panel,
                                         font=("Dodge", 14, "bold"), foreground="black", textvariable=currencyUpdate_entry_Var, width=int(screen_width/150), state=DISABLED, justify=RIGHT)
            currencyUpdate_entry.place(
                relx=0.45, rely=0.7, width=int(screen_width/8), anchor=CENTER)

            # this triggers the function for checking the input is a integer or decimal
            currencyUpdate_entry_Var.trace_add("write", updateCurrency)

            # Assigning a function with currency select
            currencySelect_box.bind("<<ComboboxSelected>>", currencyValue)

            # commit changes
            user_inV.commit()

            # close connection
            user_inV.close()

        def shrink_leftPanel():  # function for shrinking the left panel and stretch the right panel

            # function for destroying the label widget created by entered_profile() function
            def leaved_profile(event):

                # deleting the label
                profile_info.destroy()

            # function for creating and showing a label with some text when called by the mouse hover over profile on rightTop panel
            def entered_profile(event):

                # Connecting to a database, if not exists creating one
                inVoice = sqlite3.connect("in_voice.db")

                # Creating a cursor
                co = inVoice.cursor()

                # query the database
                co.execute(
                    "SELECT * FROM usersAccount WHERE userId = " + "'" + inVoiceDB + "'")
                accounts = co.fetchall()
                # print(accounts)

                # converting tuples into separate strings
                show_firstName = ""
                for account in accounts:
                    show_firstName += str(account[0])

                show_secondName = ""
                for account in accounts:
                    show_secondName += str(account[1])

                show_emailId = ""
                for account in accounts:
                    show_emailId += str(account[2])

                profile_info_text = "   "+str(
                    show_firstName)+" "+str(show_secondName)+"    "+"\r\n"+"   "+str(show_emailId)+"    "
                # assigning the label as global variable
                global profile_info
                # creating and positioning the label
                profile_info = Label(rightBottom_panel, text=profile_info_text, font=("Dodge", 10, "bold"),
                                     background="#CDCBAB", foreground="#401414", justify=RIGHT, anchor=CENTER)
                profile_info.place(relx=0.95, rely=0.2, height=int(
                    screen_height/8.5), anchor=SE)

                # commit changes
                inVoice.commit()

                # close connection
                inVoice.close()

            # function for expanding the shrinked left panel and stretch the right panel
            def expand_leftPanel(event):

                # Enable the disabled button
                rightTop_panel_wrapBtn.configure(state=NORMAL)

                # shrinking the widgets of right panel
                right_panel.configure(height=int(screen_height/1.035),
                                      width=int(screen_width-(screen_width/4.6)))

                # shrinking the widgets of rightTop panel
                rightTop_panel.configure(height=int(screen_height/10),
                                         width=int(screen_width-(screen_width/4.6)))

                rightTop_panel_label0.configure(width=int(screen_width/7.55))

                # deleting the profile picture on rightTop panel
                rightTop_panel_profile.destroy()

                # shrinking the widgets of rightBottom panel
                rightBottom_panel.configure(
                    width=int(screen_width-(screen_width/4.6)))

                rightBottom_panel_label_01.configure(
                    width=int(screen_width/8.3))

                # expanding the widgets of left panel
                left_panel.configure(height=int(
                    screen_height/1.035), width=int(screen_width/4.55))

                # expanding the widgets of leftTop panel
                leftTop_panel.configure(height=int(screen_height/3.05),
                                        width=int(screen_width/4.55))
                # showing the wrap button
                rightTop_panel_wrapBtn.lift(rightTop_panel_label0)

                # Showing the profile picture again
                leftTop_panel_bgImg.configure(image=img1)
                # this changes the function assigned with the profile picture by mouse left-click
                root.after(100, lambda: leftTop_panel_bgImg.bind(
                    "<Button-1>", change_profile))

                # expanding the widgets of leftBottom panel
                leftBottom_panel.configure(height=int(
                    screen_height/1.55), width=int(screen_width/4.55))

                # Changing the button size and position to normal
                option1.configure(text="    Dashboard")
                option1.place(relx=0.5, rely=0.1, width=int(
                    screen_width/4.55), height=int(screen_height/12), anchor=N)
                option2.configure(text="    Invoices   ")
                option2.place(relx=0.5, rely=0.24, width=int(
                    screen_width/4.55), height=int(screen_height/12), anchor=N)
                option3.configure(text="   Clients       ")
                option3.place(relx=0.5, rely=0.38, width=int(
                    screen_width/4.55), height=int(screen_height/12), anchor=N)
                option4.configure(text="    Stocks      ")
                option4.place(relx=0.5, rely=0.52, width=int(
                    screen_width/4.55), height=int(screen_height/12), anchor=N)
                option5.configure(text="   Settings    ")
                option5.place(relx=0.5, rely=0.66, width=int(
                    screen_width/4.55), height=int(screen_height/12), anchor=N)

            # this prevents the function to be called twice by disabling the button
            rightTop_panel_wrapBtn.configure(state=DISABLED)

            # change the dimensions of all widgets in both panel
            # shrinking the widgets of left panel
            left_panel.configure(height=int(
                screen_height/1.035), width=int(screen_width/15))

            # shrinking the widgets of leftTop panel
            leftTop_panel.configure(height=int(screen_height/6.1),
                                    width=int(screen_width/15))

            # hiding the wrap button
            rightTop_panel_wrapBtn.lower()

            # Creating the extend button on changing profile picture
            leftTop_panel_bgImg.configure(image=icon11)
            # this changes the function assigned with the profile picture by mouse left-click
            global unbindExpand
            unbindExpand = leftTop_panel_bgImg.bind(
                "<Button-1>", expand_leftPanel)

            # shrinking the widgets of leftBottom panel
            leftBottom_panel.configure(height=int(screen_height/1.23),
                                       width=int(screen_width/15))

            # Changing the button size and position
            option1.configure(text="")
            option1.place(relx=0.5, rely=0, width=int(
                screen_width/4.55), height=int(screen_height/7.5), anchor=N)
            option2.configure(text="")
            option2.place(relx=0.5, rely=0.17, width=int(
                screen_width/4.55), height=int(screen_height/7.5), anchor=N)
            option3.configure(text="")
            option3.place(relx=0.5, rely=0.34, width=int(
                screen_width/4.55), height=int(screen_height/7.5), anchor=N)
            option4.configure(text="")
            option4.place(relx=0.5, rely=0.51, width=int(
                screen_width/4.55), height=int(screen_height/7.5), anchor=N)
            option5.configure(text="")
            option5.place(relx=0.5, rely=0.68, width=int(
                screen_width/4.55), height=int(screen_height/7.5), anchor=N)

            # expanding the widgets of right panel
            right_panel.configure(height=int(screen_height/1.035),
                                  width=int(screen_width-(screen_width/15.1)))

            # expanding the widgets of rightTop panel
            rightTop_panel.configure(height=int(screen_height/10),
                                     width=int(screen_width-(screen_width/15.1)))

            rightTop_panel_label0.configure(width=int(screen_width/6.4))

            # Showing the profile picture on the rightTop panel when leftTop panel is shrinked
            global rightTop_panel_profile
            rightTop_panel_profile = Label(
                rightTop_panel, image=img12, background=rightTop_panel_bG)
            rightTop_panel_profile.place(relx=0.8, rely=0.5, anchor=W)

            # this calls the function assigned with the curser entry and leaving over profile
            rightTop_panel_profile.bind("<Enter>", entered_profile)
            rightTop_panel_profile.bind("<Leave>", leaved_profile)

            # expanding the widgets of rightBottom panel
            rightBottom_panel.configure(
                width=int(screen_width-(screen_width/15.1)))
            rightBottom_panel_label_01.configure(width=int(screen_width/6.87))

        def change_profile(event):  # function for changing the profile by selecting a image

            # function for cropping and giving name to the resized user selected image
            def profileName(profile):

                # this crops the image by putting a mask
                bigsize = (profile.size[0] * 3, profile.size[1] * 3)
                mask = Image.new("L", bigsize, 0)
                ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
                mask = mask.resize(profile.size, Image.ANTIALIAS)
                mask = ImageChops.darker(mask, profile.split()[-1])
                profile.putalpha(mask)

                # naming the cropped image
                global n
                n += 1
                namingProfile = "profile_"+str(n)+".png"

                # Returning the cropped name as variable
                return namingProfile

            x = filedialog.askopenfilename(title="Choose a Image", filetype=[(
                "Both *.jpg and *.png", ("*.png", "*.jpg")), ("*.png only", "*.png"), ("*.jpg or *jpeg", "*.jpg")])

            # Opening and resizing the user selected image
            profile = Image.open(x).convert("RGBA")
            profile = profile.resize((150, 150), Image.ANTIALIAS)

            # Saving the resized image with a name got from the profileName() function
            pics = profileName(profile)
            profile.save(pics)

            # Assign the picture for the rightTop panel
            pic = Image.open(pics)
            pic = pic.resize((45, 45), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(pic)

            global img12
            img12 = pic

            # Opening the saved image and assigning it as an object of PhotoImage class
            pics = Image.open(pics)
            pics = ImageTk.PhotoImage(pics)

            # Changing the default image on the profile with modified user image
            leftTop_panel_bgImg.configure(image=pics)
            leftTop_panel_bgImg.image = pics

            # Assigning a global variable for inserting it into another function
            global img1
            img1 = pics

        def highlight_leftpanel_label():  # function for highlighting and disable the selected left label button

            # Styling the selected option
            left_panel_option_style = Style(leftBottom_panel)
            left_panel_option_style.theme_use("default")
            left_panel_option_style.configure("SelectedOption.TLabel", font=("Dogde", 14, "bold"),
                                              foreground="#FF5714", background="#FFD670", borderwidth=2, focuscolor="none", anchor=CENTER)

            left_panel_option_style.map("SelectedOption.TLabel", foreground=[("active", "!disabled", "red")],
                                        background=[("active", "#01102E")])

            # Setting the button state to unchangable and highlight the selected option
            if value == 2:
                option2.configure(
                    style="SelectedOption.TLabel", state=DISABLED)
                option3.configure(
                    style="Options.TLabel", state=NORMAL)
                option4.configure(
                    style="Options.TLabel", state=NORMAL)
                option5.configure(
                    style="Options.TLabel", state=NORMAL)
                option1.configure(
                    style="Options.TLabel", state=NORMAL)

                # Calling the function for invoice panel
                invoices_btn()

            if value == 3:
                option3.configure(
                    style="SelectedOption.TLabel", state=DISABLED)
                option4.configure(
                    style="Options.TLabel", state=NORMAL)
                option5.configure(
                    style="Options.TLabel", state=NORMAL)
                option1.configure(
                    style="Options.TLabel", state=NORMAL)
                option2.configure(
                    style="Options.TLabel", state=NORMAL)

                # Calling the function for clients panel
                clients_btn()

            if value == 4:
                option4.configure(
                    style="SelectedOption.TLabel", state=DISABLED)
                option5.configure(
                    style="Options.TLabel", state=NORMAL)
                option1.configure(
                    style="Options.TLabel", state=NORMAL)
                option2.configure(
                    style="Options.TLabel", state=NORMAL)
                option3.configure(
                    style="Options.TLabel", state=NORMAL)

                # Calling the function for stocks panel
                stocks_btn()

            if value == 5:
                option5.configure(
                    style="SelectedOption.TLabel", state=DISABLED)
                option1.configure(
                    style="Options.TLabel", state=NORMAL)
                option2.configure(
                    style="Options.TLabel", state=NORMAL)
                option3.configure(
                    style="Options.TLabel", state=NORMAL)
                option4.configure(
                    style="Options.TLabel", state=NORMAL)

                # Calling the function for settings panel
                settings_btn()

        #         -----------------------------------------
        # -------------------- Left Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for left left panel
        left_panel = Frame(root, height=int(screen_height/1.035),
                           width=int(screen_width/4.55))
        left_panel.place(relx=0, rely=1, anchor=SW)

        #         -----------------------------------------
        # -------------------- Left-Top Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for left-Top panel
        leftTop_panel = Frame(left_panel, height=int(screen_height/3.05),
                              width=int(screen_width/4.55))
        leftTop_panel.place(relx=0, rely=0, anchor=NW)

        # Background color for label and the buttons for change background color
        leftTop_panel_bG = "#401414"

        # Creating a label for displaying a background color of left-Top panel
        leftTop_panel_bgColor = Label(
            leftTop_panel, background=leftTop_panel_bG, width=int(screen_width/4.6))
        leftTop_panel_bgColor.place(
            relx=0.5, rely=0.5, height=int(screen_height/3), anchor=CENTER)

        # Creating the template for profile picture
        leftTop_panel_bgImg = Label(
            leftTop_panel, image=img1, background=leftTop_panel_bG)
        leftTop_panel_bgImg.place(relx=0.5, rely=0.5, anchor=CENTER)

        # this calls the function assigned with the profile picture by mouse left-click
        leftTop_panel_bgImg.bind("<Button-1>", change_profile)

        #          -----------------------------------------
        # -------------------- Left-Bottom Panel ---------------------
        #          -----------------------------------------

        # Creating a frame for left-bottom panel
        leftBottom_panel = Frame(left_panel, height=int(screen_height/1.55),
                                 width=int(screen_width/4.55))
        leftBottom_panel.place(relx=0, rely=1, anchor=SW)

        # Creating a label for displaying a background color of left-bottom panel
        leftBottom_panel_bgColor = Label(
            leftBottom_panel, background="#FF5714", width=int(screen_width/4.6))
        leftBottom_panel_bgColor.place(relx=0.5, rely=0.5, height=int(
            screen_height/1.045), anchor=CENTER)

        # Styling for left-bottom panel buttons
        leftBottom_panel_option_style = Style(leftBottom_panel)
        leftBottom_panel_option_style.theme_use("default")
        leftBottom_panel_option_style.configure(
            "Options.TLabel", font=("Dodge", 16, "bold"), foreground="#00000E", background="#FF5714", borderwidth=0, focuscolor="none", anchor=CENTER)
        # Changing the mapping style of left-bottom panel button
        leftBottom_panel_option_style.map("Options.TLabel", foreground=[("active", "!disabled", "#FF5714")],
                                          background=[("active", "#E9FF70")])

        # Creating a Button for the left-bottom panel selection
        option1 = Button(leftBottom_panel, text="    Dashboard", image=icon5, compound=LEFT,
                         style="Options.TLabel", command=lambda: dashboardTab())
        option1.place(relx=0.5, rely=0.1, width=int(
            screen_width/4.55), height=int(screen_height/12), anchor=N)
        option2 = Button(leftBottom_panel, text="    Invoices   ", image=icon6, compound=LEFT,
                         style="Options.TLabel", command=lambda: [invoicesTab(), dashboardTab()])
        option2.place(relx=0.5, rely=0.24, width=int(
            screen_width/4.55), height=int(screen_height/12), anchor=N)
        option3 = Button(leftBottom_panel, text="   Clients       ", image=icon7, compound=LEFT,
                         style="Options.TLabel", command=lambda: [clientsTab(), dashboardTab()])
        option3.place(relx=0.5, rely=0.38, width=int(
            screen_width/4.55), height=int(screen_height/12), anchor=N)
        option4 = Button(leftBottom_panel, text="    Stocks      ", image=icon8, compound=LEFT,
                         style="Options.TLabel", command=lambda: [stocksTab(), dashboardTab()])
        option4.place(relx=0.5, rely=0.52, width=int(
            screen_width/4.55), height=int(screen_height/12), anchor=N)
        option5 = Button(leftBottom_panel, text="   Settings    ", image=icon9, compound=LEFT,
                         style="Options.TLabel", command=lambda: [settingsTab(), dashboardTab()])
        option5.place(relx=0.5, rely=0.66, width=int(
            screen_width/4.55), height=int(screen_height/12), anchor=N)

        #         -----------------------------------------
        # -------------------- Right Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for right right-bottom panel
        right_panel = Frame(root, height=int(screen_height/1.035),
                            width=int(screen_width-(screen_width/4.6)))
        right_panel.place(relx=1, rely=1, anchor=SE)

        #         -----------------------------------------
        # -------------------- right-Top Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for right-Top panel inside right panel
        rightTop_panel = Frame(right_panel, height=int(screen_height/10),
                               width=int(screen_width-(screen_width/4.6)))
        rightTop_panel.place(relx=1, rely=0, anchor=NE)

        # Background color for label and the buttons for shrinking the left panel
        rightTop_panel_bG = "#01102E"

        # Creating a labels for label for displaying a background color of right-Top panel
        rightTop_panel_label0 = Label(
            rightTop_panel, background=rightTop_panel_bG, width=int(screen_width/7.55))
        rightTop_panel_label0.place(relx=0.5, rely=0.5, height=int(
            screen_height/10), anchor=CENTER)

        # Creating labels for displaying the app name on the right-Top panel
        rightTop_panel_label11 = Label(rightTop_panel, text="in", foreground="#B3C6E7",
                                       background=rightTop_panel_bG, font=("Magneto", 55, "bold"))
        rightTop_panel_label11.place(relx=0.4, rely=0.5, anchor=E)

        rightTop_panel_label12 = Label(rightTop_panel, text="Voice", foreground="#D6DDE8",
                                       background=rightTop_panel_bG, font=("Matura MT Script Capitals", 12, "bold"))
        rightTop_panel_label12.place(relx=0.445, rely=0.55, anchor=E)

        # Creating a label for displaying the user name
        rightTop_panel_label12 = Label(rightTop_panel, text="@ " + str(inVoiceDB), foreground="#B3C6E7",
                                       background=rightTop_panel_bG, font=("Dodge", 12, "bold"))
        rightTop_panel_label12.place(relx=0.85, rely=0.5, anchor=W)

        # Styling the wrap button
        rightTop_panel_wrapBtn_style = Style(rightTop_panel)
        rightTop_panel_wrapBtn_style.theme_use("default")
        rightTop_panel_wrapBtn_style.configure(
            "Wrap.TLabel", background=leftTop_panel_bG, borderwidth=0, focuscolor="none", anchor=CENTER)

        # Changing the mapping style of wrap button
        rightTop_panel_wrapBtn_style.map("Wrap.TLabel", foreground=[("active", "!disabled", "#FF5714")],
                                         background=[("active", leftTop_panel_bG)])

        # Creating a button for shrinking the left panel
        rightTop_panel_wrapBtn = Button(
            rightTop_panel, image=icon10, style="Wrap.TLabel", command=lambda: shrink_leftPanel())
        rightTop_panel_wrapBtn.place(
            relx=0, rely=0.07, width=int(screen_width/40), height=int(screen_height/20), anchor=NW)

        #         -----------------------------------------
        # -------------------- Right-Bottom Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for right rightBottom panel
        rightBottom_panel = Frame(right_panel, height=int(screen_height/1.151),
                                  width=int(screen_width-(screen_width/4.6)))
        rightBottom_panel.place(relx=1, rely=1, anchor=SE)

        # Creating a labels for displaying the application name
        rightBottom_panel_label0 = Label(
            rightBottom_panel, background="#B3C6E7", width=int(screen_width/4.6))
        rightBottom_panel_label0.place(relx=0.5, rely=0.5, height=int(
            screen_height/1.148), anchor=CENTER)

        # Background color for label and the buttons in the leftBottom panel
        rightBottom_label1_bG = "#F0EFF4"
        # Creating a labels for displaying the application name
        rightBottom_panel_label_01 = Label(
            rightBottom_panel, background=rightBottom_label1_bG, width=int(screen_width/8.3))
        rightBottom_panel_label_01.place(relx=0.5, rely=0.5, height=int(
            screen_height/1.3), anchor=CENTER)

        # calling this function changes the button background according to the mouse click
        highlight_leftpanel_label()

        # placing these widgets on top of another
        title_frame.lift()
        title_color.lift()
        close_button.lift()
        minnimize.lift()

    def signInPanel():  # function for opening the signIn window

        def closeSignInPanel():  # function for closing the signIn window

            # Reclaim the Faded buttons
            signIn_btn_style.configure(
                "SignInButton.TButton", background="#BF09D5", borderwidth=2)
            # Reclaim the Fading tabs
            client_btn.configure(style="ICSButton.TButton")
            stock_btn.configure(style="ICSButton.TButton")
            # Reclaim the Fading buttons label
            client_btnLabel.configure(style="ICSLabel.TLabel")
            stock_btnLabel.configure(style="ICSLabel.TLabel")

            # this closes the the signIn window
            root.after(100, lambda: signin.destroy())

            # refocusing
            root.grab_set()
            root.focus_set()

        def signUpPanel():  # function for opening a signUp window

            def closeSignUp():  # function for closing the signUp window

                # this closes the the signIn window
                root.after(100, lambda: signup.destroy())
                # Showing the signIn window again
                signin.deiconify()
                # refocusing
                root.grab_set()
                root.focus_set()
                signin.grab_set()
                signin.focus_set()

            def newAccount():  # function for creating new account if not exists

                accountCreating_msg = messagebox.askyesno(
                    title="Create Acoount", message="Are you sure, you want to create a account with the details you give?", parent=signup)

                # this creates the new account
                if accountCreating_msg == True:
                    # Connecting to a database, if not exists creating one
                    inVoice = sqlite3.connect("in_voice.db")

                    # Creating a cursor
                    co = inVoice.cursor()

                    # insert into table
                    co.execute("INSERT INTO usersAccount VALUES (:firstName, :lastName, :emailId, :mobileNumber, :userId, :passWord)",
                               {
                                   "firstName": signUp_entry1_var.get(),
                                   "lastName": signUp_entry2_var.get(),
                                   "emailId": signUp_entry3_var.get(),
                                   "mobileNumber": signUp_entry4_var.get(),
                                   "userId": signUp_entry5_var.get(),
                                   "passWord": signUp_entry6_var.get()
                               })

                    # commit changes
                    inVoice.commit()

                    # close connection
                    inVoice.close()

                    # Showing a message box with information of account has created
                    accountCreated_msg = messagebox.showinfo(
                        title="Account Created", message="Your account has been created as \r\n\nUserID :  "+str(signUp_entry5_var.get()), parent=signup)

                    if accountCreated_msg == "ok":

                        # Creating new database for the new user
                        user_inV = sqlite3.connect(
                            str(signUp_entry5_var.get())+"in_voice.db")

                        # Creating a cursor
                        co = user_inV.cursor()

                        # Creating a table userAccount
                        co.execute("""CREATE TABLE IF NOT EXISTS userAccount (
                                        userId TEXT,
                                        passWord TEXT              
                                        )""")
                        # insert into table
                        co.execute("INSERT INTO userAccount VALUES (:userId, :passWord)",
                                   {
                                       "userId": signUp_entry5_var.get(),
                                       "passWord": signUp_entry6_var.get()
                                   })

                        # commit changes
                        user_inV.commit()

                        # close connection
                        user_inV.close()

                        # this closes the signUp panel
                        closeSignUp()

                elif accountCreating_msg == False:
                    # Deleting the user typed password
                    signUp_entry6_var.set("")
                    signUp_entry7_var.set("")

                    # Changing the hint text
                    createBtn_info.destroy()

                    # Enabling all entries
                    signUp_entry1.configure(state=NORMAL)
                    signUp_entry2.configure(state=NORMAL)
                    signUp_entry3.configure(state=NORMAL)
                    signUp_entry4.configure(state=NORMAL)
                    signUp_entry5.configure(state=NORMAL)
                    signUp_entry6.configure(state=NORMAL)
                    signUp_entry7.configure(state=NORMAL)

            def keyGenerate():  # function for generating a random key

                def counter():  # function for decreasing the timer

                    global timing
                    timing -= 1

                    changesTimer.configure(
                        text="Valid for\n"+str(timing)+"s")

                    if timing != 0:
                        # this calls the function for countdown timer
                        root.after(1000, lambda: counter())
                    else:
                        # deleting the timer and the generated key
                        changesTimer.destroy()
                        key_info.destroy()
                        randomKey.destroy()

                        # Disabling the entry for typing key again
                        signUp_entry8.configure(state=DISABLED)

                        # Setting the timer to initial value
                        timing = 31

                        # Enabling the create button if the key matches
                        if signUp_entry8_var.get() == key:

                            # making the create account button clickable
                            createAccount.configure(state=NORMAL)
                            root.after(1000, lambda: keyHint.destroy())

                            # Showing hint
                            global createBtn_info
                            createBtn_info = Label(
                                signup, text="# Click 'Create' to create your account", font=("Dodge", 12, "bold"), background=signUp_bG, foreground="#22333B")
                            createBtn_info.place(
                                relx=0.8, rely=0.85, anchor=CENTER)

                        else:
                            # Deleting the user typed password
                            signUp_entry6_var.set("")
                            signUp_entry7_var.set("")

                            # Changing the hint text
                            keyHint.configure(
                                text="Sorry! key doesn't match try again")
                            root.after(5000, lambda: keyHint.destroy())

                            # Enabling all entries
                            signUp_entry1.configure(state=NORMAL)
                            signUp_entry2.configure(state=NORMAL)
                            signUp_entry3.configure(state=NORMAL)
                            signUp_entry4.configure(state=NORMAL)
                            signUp_entry5.configure(state=NORMAL)
                            signUp_entry6.configure(state=NORMAL)
                            signUp_entry7.configure(state=NORMAL)

                # Disabling the generateKey button
                generateKey.configure(state=DISABLED)

                # Connecting to a database, if not exists creating one
                inVoice = sqlite3.connect("in_voice.db")

                # Creating a cursor
                co = inVoice.cursor()

                # Creating a table usersAccount
                co.execute("""CREATE TABLE IF NOT EXISTS usersAccount (
                                firstName TEXT,
                                lastName TEXT,
                                emailId TEXT,
                                mobileNumber INTEGER,
                                userId TEXT,
                                passWord TEXT              
                                )""")

                # Querying database for checking the userId exists
                co.execute(
                    "SELECT * FROM usersAccount WHERE userId = " + "'" + signUp_entry5_var.get() + "'")
                accounts = co.fetchall()
                # print(accounts)

                # converting tuples into separate strings
                show_userID = ""
                for account in accounts:
                    show_userID += str(account[4])

                if signUp_entry5_var.get() == show_userID:

                    # if the userId exists in database shows this message
                    invalid_username = Label(signup, text="# userid exists", font=(
                        "Dodge", 12, "bold"), background=signUp_bG, foreground="#EF233C")
                    invalid_username.place(relx=0.72, rely=0.55, anchor=CENTER)

                    root.after(1500, lambda: invalid_username.destroy())

                    # Deleting the user typed password
                    signUp_entry6_var.set("")
                    signUp_entry7_var.set("")

                    # commit changes
                    inVoice.commit()

                    # close connection
                    inVoice.close()

                else:

                    # Enabling the entry for typing key and hiding the label
                    signUp_entry8.configure(state=NORMAL)
                    errorLabel2.configure(foreground=signUp_bG)

                    #  Disabling all entries
                    signUp_entry1.configure(state=DISABLED)
                    signUp_entry2.configure(state=DISABLED)
                    signUp_entry3.configure(state=DISABLED)
                    signUp_entry4.configure(state=DISABLED)
                    signUp_entry5.configure(state=DISABLED)
                    signUp_entry6.configure(state=DISABLED)
                    signUp_entry7.configure(state=DISABLED)

                    generateKey_label.destroy()

                    # Generating the random key with combination of numbers and letters
                    key = ""
                    for i in range(3):
                        key += str(random.choice(string.ascii_uppercase)
                                   )+str(random.choice(string.digits))+str(random.choice(string.ascii_uppercase))+"-"

                    key = key+str(random.choice(string.ascii_letters))

                    # print(key)
                    # label for key entry hint
                    keyHint = Label(signup, text="Hint: type key without hyphen", font=(
                        "Dodge", 10), background=signUp_bG, foreground="#22333B")
                    keyHint.place(relx=0.2, rely=0.97, anchor=CENTER)

                    # label for showing key is generated
                    key_info = Label(
                        signup, text="This is your KEY !", font=("Dodge", 14), background=signUp_bG, foreground="#22333B")
                    key_info.place(relx=0.8, rely=0.6, anchor=CENTER)

                    randomKey = Label(
                        signup, text=key, font=("Dodge", 13, "bold"), background=signUp_bG, foreground="#22333B")
                    randomKey.place(relx=0.8, rely=0.68, anchor=CENTER)

                    # Label showing timer
                    changesTimer = Label(signup, text="Valid for\n"+str(timing)+"s", font=(
                        "Dodge", 12, "bold"), background=signUp_bG, foreground="#22333B", justify=CENTER)
                    changesTimer.place(relx=0.55, rely=0.9)

                    # this calls the function for starting timer
                    counter()

            # function for destroying the label widget created by entered_generateKey() function
            def leaved_generateKey(event):

                # deleting the label
                generateKey_label.destroy()

            # function for creating and showing a label with some text of what the button is for
            def entered_generateKey(event):

                # assigning the label as global variable
                global generateKey_label
                # Creating a label to show the action of the button
                generateKey_label = Label(
                    signup, text="Generate key", font=("Dodge", 10), background=signUp_bG, foreground="#273C2C")
                generateKey_label.place(relx=0.55, rely=0.85, anchor=CENTER)

            def showingPassword():  # function for showing the hidden password

                def hidingPassword():  # function for hiding the visible password again to hidden

                    # this makes the password hidden again
                    signUp_entry6.configure(show="\u25CF")
                    signUp_entry7.configure(show="\u25CF")

                    # changing the button function to show it again when needed
                    root.after(50, lambda: showPassword.configure(
                        command=lambda: showingPassword()))

                # Making the characters in password entry visible
                signUp_entry6.configure(show="")
                signUp_entry7.configure(show="")

                # changing the button function to hide it again when needed
                root.after(50, lambda: showPassword.configure(
                    command=lambda: hidingPassword()))

            # function for add hypen automatically to the entry widget values
            def checkValidKey(var, index, mode):

                # function for deleting the key with mouse left click button
                def deletekeyEntry(event):

                    # this deletes and sets the key entry widget empty
                    signUp_entry8.delete(0, END)
                    signUp_entry8.unbind("<Button-1>", unbindingKeyDELETE)

                # Adding hypen for every third character
                if len(signUp_entry8_var.get()) == 3:
                    signUp_entry8.insert(END, "-")

                elif len(signUp_entry8_var.get()) == 7:
                    signUp_entry8.insert(END, "-")

                elif len(signUp_entry8_var.get()) == 11:
                    signUp_entry8.insert(END, "-")

                elif len(signUp_entry8_var.get()) == 13:
                    signup.focus_set()
                    # Adding a delete command to mouse left click
                    unbindingKeyDELETE = signUp_entry8.bind(
                        "<Button-1>", deletekeyEntry)

            # function for validating the entry is same as the password entry
            def checkConfirmPassword(var, index, mode):

                if signUp_entry1_var.get() == "" or signUp_entry2_var.get() == "" or signUp_entry3_var.get() == "" or signUp_entry4_var.get() == "":

                    # Showing error and preventing from typing
                    errorLabel1.configure(
                        text="# Fill your personel details first", foreground="#EF233C")
                    signUp_entry7_var.set("")

                # changing the text if userId is empty
                elif signUp_entry5_var.get() == "":

                    # Showing error and preventing from typing
                    errorLabel1.configure(
                        text="# Create your userId", foreground="#EF233C")
                    signUp_entry7_var.set("")

                elif signUp_entry6_var.get() == "":

                    # Showing error and preventing from typing
                    errorLabel2.configure(
                        text="# Create a password to proceed", foreground="#EF233C")
                    signUp_entry7_var.set("")

                elif signUp_entry6_var.get() != signUp_entry7_var.get():

                    # Showing error
                    errorLabel2.configure(
                        text="# password don't match", foreground="#EF233C")

                elif signUp_entry6_var.get() == signUp_entry7_var.get():

                    # Removing error
                    errorLabel2.configure(
                        text="# password matched", foreground="#38B000")

                    generateKey.configure(state=NORMAL)

            # function for validating the entry must be satisfied minimum length
            def checkPassword(var, index, mode):

                if signUp_entry1_var.get() == "" or signUp_entry2_var.get() == "" or signUp_entry3_var.get() == "" or signUp_entry4_var.get() == "":

                    # Showing error and preventing from typing
                    errorLabel1.configure(
                        text="# Fill your personel details first", foreground="#EF233C")
                    signUp_entry6_var.set("")

                else:
                    if signUp_entry5_var.get() == "":
                        # changing the text if userId is empty
                        errorLabel1.configure(
                            text="# Create your userId", foreground="#EF233C")
                        signUp_entry6_var.set("")

                    elif signUp_entry5_var.get().isalpha():
                        # if entry not a alphabet
                        errorLabel1.configure(
                            text="# Create your userId", foreground="#EF233C")
                        signUp_entry6_var.set("")

                    elif signUp_entry5_var.get().isdigit():
                        # if entry is a number
                        errorLabel1.configure(
                            text="# Create your userId", foreground="#EF233C")
                        signUp_entry6_var.set("")

                    elif len(signUp_entry5_var.get()) < 10:
                        errorLabel1.configure(
                            text="# Create your userId", foreground="#EF233C")
                        signUp_entry6_var.set("")

                    elif len(signUp_entry5_var.get()) > 15:
                        errorLabel1.configure(
                            text="# Create your userId", foreground="#EF233C")
                        signUp_entry6_var.set("")

                        # Creating a label for Showing condition
                        userPassword_info1 = Label(
                            signup, text="(minimum 8 characters)", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                        userPassword_info1.place(
                            relx=0.5, rely=0.7, anchor=CENTER)

                        # checking the input is character length
                        if len(signUp_entry6_var.get()) < 8:
                            # if entry not satisfies condition
                            userPassword_info1.configure(foreground=main_bG)

                            if len(signUp_entry6_var.get()) > 7:
                                userPassword_info1.configure(
                                    foreground=signUp_bG)

            # function for validating the entry must be combination of alphanumbers
            def checkUserId(var, index, mode):

                # Hiding the error label
                errorLabel1.configure(foreground=signUp_bG)

                # Creating a label for showing entry is invalid
                userUserId_info = Label(
                    signup, text="# UserId invalid", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userUserId_info.place(relx=0.58, rely=0.5, anchor=CENTER)
                # Showing condition
                userUserId_info1 = Label(
                    signup, text="(combination of both alphabets & numbers (10-15))", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userUserId_info1.place(relx=0.46, rely=0.6, anchor=CENTER)

                # checking the input is number
                # checking the input is number
                if not signUp_entry4_var.get().isdigit():
                    # if entry not a number
                    userUserId_info.configure(foreground="#EF233C")
                    signUp_entry5_var.set("")

                elif len(signUp_entry4_var.get()) > 10:
                    userUserId_info.configure(foreground=main_bG)
                    signUp_entry5_var.set("")

                elif len(signUp_entry4_var.get()) < 10:
                    userUserId_info.configure(foreground=main_bG)
                    signUp_entry5_var.set("")

                elif len(signUp_entry4_var.get()) == 10:

                    # checking the input is alphabet
                    if signUp_entry5_var.get().isalpha():
                        # if entry not a alphabet
                        userUserId_info.configure(foreground="#EF233C")

                    elif signUp_entry5_var.get().isdigit():
                        # if entry is a number
                        userUserId_info.configure(foreground="#EF233C")

                    else:
                        # if entry is combination of alphanumbers
                        userUserId_info.configure(foreground=signUp_bG)
                        if len(signUp_entry5_var.get()) < 10:
                            userUserId_info1.configure(foreground=main_bG)

                        elif len(signUp_entry5_var.get()) > 15:
                            signUp_entry5_var.set("")

            # function for validating the entry must be valid mobile number
            def checkMobileNumber(var, index, mode):

                # Creating label for showing the info about email
                userMobileNumber_info0 = Label(
                    signup, text="# fill this!", background=signUp_bG, foreground=signUp_bG, justify=CENTER)
                userMobileNumber_info0.place(
                    relx=0.38, rely=0.32, anchor=CENTER)

                # Creating a label for showing entry is invalid
                userMobileNumber_info = Label(
                    signup, text="# Invalid number", background=signUp_bG, foreground=signUp_bG, justify=CENTER)
                userMobileNumber_info.place(
                    relx=0.91, rely=0.42, anchor=CENTER)
                # Showing format
                userMobileNumber_info1 = Label(
                    signup, text="(should be 10 digits)", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userMobileNumber_info1.place(
                    relx=0.8, rely=0.3, anchor=CENTER)

                # checking the input is a valid email
                if not signUp_entry3_var.get().islower():

                    # if entry not a lowercase letter
                    userMobileNumber_info0.configure(foreground="#EF233C")
                    signUp_entry4_var.set("")

                elif signUp_entry3_var.get().isidentifier():

                    # if entry is not a symbol
                    userMobileNumber_info0.configure(foreground="#EF233C")
                    signUp_entry4_var.set("")

                elif len(signUp_entry3_var.get()) < 15:
                    userMobileNumber_info0.configure(foreground="#EF233C")
                    signUp_entry4_var.set("")

                elif not len(signUp_entry3_var.get()) < 15:

                    # if entry is a symbo
                    userMobileNumber_info0.configure(foreground=signUp_bG)

                    # checking the input is number
                    if not signUp_entry4_var.get().isdigit():
                        # if entry not a number
                        userMobileNumber_info.configure(foreground="#EF233C")
                        signUp_entry4_var.set("")

                    elif len(signUp_entry4_var.get()) > 10:
                        signUp_entry4_var.set(signUp_entry4_var.get()[-1])

                    elif len(signUp_entry4_var.get()) < 10:
                        userMobileNumber_info1.configure(foreground=main_bG)

            # function for validating the entry must be a valid email
            def checkEmail(var, index, mode):

                # Creating label for showing the info about lastname
                userEmail_info0 = Label(
                    signup, text="# fill this!", background=signUp_bG, foreground=signUp_bG, justify=CENTER)
                userEmail_info0.place(relx=0.85, rely=0.28, anchor=CENTER)

                # Creating a label for showing entry is invalid
                userEmail_info = Label(
                    signup, text="# Invalid email", background=signUp_bG, foreground=signUp_bG, justify=CENTER)
                userEmail_info.place(relx=0.35, rely=0.42, anchor=CENTER)
                # Showing format
                userEmail_info1 = Label(
                    signup, text="(like this: invoice123@gmail.com)", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userEmail_info1.place(relx=0.235, rely=0.3, anchor=CENTER)

                # checking the input is alphabet
                if not signUp_entry2_var.get().isalpha():
                    # if entry not a alphabet
                    userEmail_info0.configure(foreground="#EF233C")
                    signUp_entry3_var.set("")

                elif not signUp_entry2_var.get().istitle():
                    userEmail_info0.configure(foreground="#EF233C")
                    signUp_entry3_var.set("")

                elif signUp_entry2_var.get().isalpha():
                    # if entry is a alphabet
                    userEmail_info0.configure(foreground=signUp_bG)

                    # checking the input is a valid email
                    if not signUp_entry3_var.get().islower():
                        # if entry not a lowercase letter
                        userEmail_info.configure(foreground="#EF233C")

                    elif signUp_entry3_var.get().isidentifier():

                        # if entry is not a symbol
                        userEmail_info.configure(foreground="#EF233C")
                        userEmail_info1.configure(foreground=main_bG)

                    elif len(signUp_entry3_var.get()) < 15:
                        # if entry is a symbo
                        userEmail_info1.configure(foreground=main_bG)

            # function for validating the entry must be alphabets
            def checkLastName(var, index, mode):

                # Creating label for showing the info about firstname
                userLastName_info0 = Label(
                    signup, text="# fill this!", background=signUp_bG, foreground=signUp_bG, justify=CENTER)
                userLastName_info0.place(relx=0.35, rely=0.28, anchor=CENTER)

                # Creating a label for showing entry is invalid
                userLastName_info = Label(
                    signup, text="# Invalid name", background=signUp_bG, foreground=signUp_bG, justify=CENTER)
                userLastName_info.place(relx=0.91, rely=0.175, anchor=CENTER)
                # Showing minimum limit
                userLastName_info1 = Label(
                    signup, text="(atleast 1 character preferred Uppercase)", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userLastName_info1.place(relx=0.87, rely=0.15, anchor=CENTER)

                # checking the input is alphabet
                if not signUp_entry1_var.get().isalpha():
                    # if entry not a alphabet
                    userLastName_info0.configure(foreground="#EF233C")
                    signUp_entry2_var.set("")

                elif signUp_entry1_var.get().isalpha():

                    if not signUp_entry1_var.get().istitle():
                        userLastName_info0.configure(foreground="#EF233C")
                        signUp_entry2_var.set("")

                    elif len(signUp_entry1_var.get()) < 3:

                        userLastName_info0.configure(foreground=signUp_bG)
                        signUp_entry2_var.set("")

                    # checking the input is alphabet
                    elif not signUp_entry2_var.get().isalpha():
                        # if entry not a alphabet
                        userLastName_info.configure(foreground="#EF233C")
                        userLastName_info1.configure(foreground=main_bG)

                    elif not signUp_entry2_var.get().istitle():
                        userLastName_info1.configure(foreground=main_bG)

                    elif signUp_entry2_var.get().isalpha():
                        # if entry is a alphabet
                        userLastName_info.configure(
                            foreground=signUp_bG)

            # function for validating the entry must be alphabets

            def checkFirstName(var, index, mode):

                # Creating a label for showing entry is invalid
                userFirstName_info = Label(
                    signup, text="# Invalid name", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userFirstName_info.place(relx=0.35, rely=0.175, anchor=CENTER)
                # Showing minimum limit
                userFirstName_info1 = Label(
                    signup, text="(minimum 3 characters with a Uppercase)", background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
                userFirstName_info1.place(relx=0.3, rely=0.15, anchor=CENTER)

                # checking the input is alphabet
                if not signUp_entry1_var.get().isalpha():
                    # if entry not a alphabet
                    userFirstName_info.configure(foreground="#EF233C")

                elif signUp_entry1_var.get().isalpha():
                    # if entry is a alphabet
                    userFirstName_info.configure(foreground=signUp_bG)

                    if not signUp_entry1_var.get().istitle():
                        userFirstName_info1.configure(foreground="#EF233C")

                    elif len(signUp_entry1_var.get()) < 3:
                        userFirstName_info1.configure(foreground=main_bG)

            # minimizing the signIn window
            signin.withdraw()

            # Opening a new window for the signUp options
            signup = Toplevel()
            # focusing
            signup.grab_set()
            signup.focus_set()

            # To remove the toolbar of the signUp window
            signup.overrideredirect(True)

            # Setting the new window width, height and position on the user screen
            signup_window_width = int(screen_width/1.5)
            signup_window_height = int(screen_height/1.15)

            signup_screen_width = signup.winfo_screenwidth()
            signup_screen_height = signup.winfo_screenheight()

            signup_x_cordinate = int(
                (signup_screen_width/2) - (signup_window_width/2))
            signup_y_cordinate = int(
                (signup_screen_height/2) - (signup_window_height/2))

            signup.geometry("%dx%d+%d+%d" % (signup_window_width,
                                             signup_window_height, signup_x_cordinate, signup_y_cordinate))

            # signUp window background color
            signUp_bG = "#D4B0F9"
            # Setting background color for frame using label
            signUp_panel_label = Label(signup, background=signUp_bG)
            signUp_panel_label.place(relx=0.5, rely=0.5, height=int(
                signup_screen_height), width=int(signup_screen_width), anchor=CENTER)

            # Style for exit2 button
            exit2Button_style = Style(signup)
            exit2Button_style.theme_use("default")
            exit2Button_style.configure("EXIT2Button.TButton", font=("Dodge", 20, "bold"),
                                        foreground="#011932", background=signUp_bG, borderwidth=0, highlightthickness=0, relief=FLAT, focuscolor="none")

            # mouse hover style for exit2 Button
            exit2Button_style.map("EXIT2Button.TButton", foreground=[(
                "active", "!disabled", "#EF233C")], background=[("active", signUp_bG)])

            # Creating a button for closing the signUp window
            exit2Button = Button(
                signup, text="X", style="EXIT2Button.TButton", command=lambda: closeSignUp())
            exit2Button.place(relx=1, rely=0.01, width=int(
                signup_screen_width/30), anchor=NE)

            # Creating labels for the signUp window
            # signUp window foreground color
            signUp_fG = "#0A014F"

            # signUp label
            signUp_label1 = Label(signup, text="Create Account", font=(
                "Dodge", 25, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label1.place(relx=0.5, rely=0.06, anchor=CENTER)

            # FirstName label
            signUp_label2 = Label(signup, text="First Name", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label2.place(relx=0.1, rely=0.15, anchor=CENTER)

            # LastName label
            signUp_label3 = Label(signup, text="Last Name", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label3.place(relx=0.65, rely=0.15, anchor=CENTER)

            # EmailId label
            signUp_label4 = Label(signup, text="Email", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label4.place(relx=0.07, rely=0.3, anchor=CENTER)

            # MobileNumber label
            signUp_label5 = Label(signup, text="Mobile No.", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label5.place(relx=0.65, rely=0.3, anchor=CENTER)

            # Separater label
            signUp_label6 = Label(signup, text="- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -", font=(
                "Dodge", 14), background=signUp_bG, foreground=signUp_fG)
            signUp_label6.place(relx=0.5, rely=0.45, anchor=CENTER)

            # UserId label
            signUp_label7 = Label(signup, text="User Id", font=(
                "Dodge", 16, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label7.place(relx=0.3, rely=0.55, anchor=CENTER)

            # Password label
            signUp_label8 = Label(signup, text="Password", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label8.place(relx=0.3, rely=0.65, anchor=CENTER)

            # Re-Password label
            signUp_label9 = Label(signup, text="Re-type", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label9.place(relx=0.3, rely=0.75, anchor=CENTER)

            # Key label
            signUp_label10 = Label(signup, text="Key", font=(
                "Dodge", 14, "bold"), background=signUp_bG, foreground=signUp_fG)
            signUp_label10.place(relx=0.1, rely=0.85, anchor=CENTER)

            # Error labels
            errorLabel1 = Label(
                signup, text="# Fill your personel details first", font=("Dodge", 10, "bold"), background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
            errorLabel1.place(relx=0.75, rely=0.55, anchor=CENTER)

            errorLabel2 = Label(
                signup, text="# Create your password to proceed", font=("Dodge", 10, "bold"), background=signUp_bG, foreground=signUp_bG, justify=RIGHT)
            errorLabel2.place(relx=0.75, rely=0.75, anchor=CENTER)

            # Creating entries for the signUp window
            # FirstName entry
            signUp_entry1_var = StringVar()
            signUp_entry1 = Entry(
                signup, textvariable=signUp_entry1_var, font=("Dodge", 15, "bold"), justify=RIGHT)
            signUp_entry1.place(relx=0.22, rely=0.22, height=int(
                signup_screen_height/20), width=int(signup_screen_width/4), anchor=CENTER)

            # calling the trace method for checking entry is only alphabets
            signUp_entry1_var.trace_add("write", checkFirstName)

            # LastName entry
            signUp_entry2_var = StringVar()
            signUp_entry2 = Entry(
                signup, textvariable=signUp_entry2_var, font=("Dodge", 15, "bold"), justify=RIGHT)
            signUp_entry2.place(relx=0.78, rely=0.22, height=int(
                signup_screen_height/20), width=int(signup_screen_width/4), anchor=CENTER)

            # calling the trace method for checking entry is only alphabets
            signUp_entry2_var.trace_add("write", checkLastName)

            # Email entry
            signUp_entry3_var = StringVar()
            signUp_entry3 = Entry(
                signup, textvariable=signUp_entry3_var, font=("Dodge", 15, "bold"), justify=RIGHT)
            signUp_entry3.place(relx=0.22, rely=0.37, height=int(
                signup_screen_height/20), width=int(signup_screen_width/4), anchor=CENTER)

            # calling the trace method for checking entry is a valid email
            signUp_entry3_var.trace_add("write", checkEmail)

            # MobileNumber entry
            signUp_entry4_var = StringVar()
            signUp_entry4 = Entry(
                signup, textvariable=signUp_entry4_var, font=("Dodge", 15, "bold"), justify=RIGHT)
            signUp_entry4.place(relx=0.78, rely=0.37, height=int(
                signup_screen_height/20), width=int(signup_screen_width/4), anchor=CENTER)

            # calling the trace method for checking entry is a valid mobile number
            signUp_entry4_var.trace_add("write", checkMobileNumber)

            # UserId entry
            signUp_entry5_var = StringVar()
            signUp_entry5 = Entry(
                signup, textvariable=signUp_entry5_var, font=("Dodge", 15, "bold"), justify=RIGHT)
            signUp_entry5.place(relx=0.5, rely=0.55, height=int(
                signup_screen_height/20), width=int(signup_screen_width/6), anchor=CENTER)

            # calling the trace method for checking entry is a valid username
            signUp_entry5_var.trace_add("write", checkUserId)

            # Password entry
            signUp_entry6_var = StringVar()
            signUp_entry6 = Entry(
                signup, textvariable=signUp_entry6_var, font=("Dodge", 15, "bold"), show="\u25CF", justify=RIGHT)
            signUp_entry6.place(relx=0.5, rely=0.65, height=int(
                signup_screen_height/20), width=int(signup_screen_width/6), anchor=CENTER)

            # calling the trace method for checking the characters length entry
            signUp_entry6_var.trace_add("write", checkPassword)

            # Re-Password entry
            signUp_entry7_var = StringVar()
            signUp_entry7 = Entry(
                signup, textvariable=signUp_entry7_var, font=("Dodge", 15, "bold"), show="\u25CF", justify=RIGHT)
            signUp_entry7.place(relx=0.5, rely=0.75, height=int(
                signup_screen_height/20), width=int(signup_screen_width/6), anchor=CENTER)

            # calling the trace method for checking the password entrys match
            signUp_entry7_var.trace_add("write", checkConfirmPassword)

            # Key entry
            signUp_entry8_var = StringVar()
            signUp_entry8 = Entry(
                signup, textvariable=signUp_entry8_var, font=("Dodge", 15, "bold"), state=DISABLED, justify=RIGHT)
            signUp_entry8.place(relx=0.25, rely=0.92, height=int(
                signup_screen_height/20), width=int(signup_screen_width/4), anchor=CENTER)

            # calling the trace method for adding hypen with characters user type
            signUp_entry8_var.trace_add("write", checkValidKey)

            # Styling SignUp Button
            generateKey_style = Style()
            generateKey_style.theme_use("default")
            generateKey_style.configure("GenerateKey.TButton", background=signUp_bG,
                                        foreground=signin_fG, borderwidth=0, hightlightthickness=0, relief=FLAT, focuscolor="none")

            # mouse hover style for SignUp Button
            generateKey_style.map("GenerateKey.TButton", foreground=[(
                "active", "!disabled", "#4C1036")], background=[("active", signUp_bG)])

            # Creating button for showing typed password
            showPassword = Button(signup, image=icon4,
                                  style="GenerateKey.TButton", command=lambda: showingPassword())
            showPassword.place(relx=0.65, rely=0.65, anchor=CENTER)

            # Creating a button to send key to the user
            generateKey = Button(signup, image=icon3,
                                 style="GenerateKey.TButton", state=DISABLED, command=lambda: keyGenerate())
            generateKey.place(relx=0.5, rely=0.92, anchor=CENTER)

            # this calls the function assigned with the mouse hover over generateKey button
            generateKey.bind("<Enter>", entered_generateKey)
            generateKey.bind("<Leave>", leaved_generateKey)

            # Styling SignUp Button
            signUp_Button_style = Style(signup)
            signUp_Button_style.theme_use("default")
            signUp_Button_style.configure("SignUpButton.TButton", font=("Dodge", 18, "bold", "italic"),
                                          foreground="#F0EFF4", background="#4C1036", borderwidth=2, highlightthickness=0, focuscolor="none")

            # mouse hover style for SignUp_Button Button
            signUp_Button_style.map("SignUpButton.TButton", foreground=[(
                "active", "!disabled", "#F0EFF4")], background=[("active", "#72195A")])

            # Creating a button to create the account with the details entered
            createAccount = Button(signup, text="Create",
                                   style="SignUpButton.TButton", state=DISABLED, command=lambda: newAccount())
            createAccount.place(relx=0.9, rely=0.95, anchor=CENTER)

        def signingIn():  # function creates the user id on screen by replacing the signin button

            # Changing the invoice_btn, client_btn and stock_btn functions
            invoice_btn.configure(command=lambda: invoicesTab())
            client_btn.configure(command=lambda: clientsTab())
            stock_btn.configure(command=lambda: stocksTab())

            # Styling settings_btn Button
            settings_btn_style = Style(home)
            settings_btn_style.theme_use("default")
            settings_btn_style.configure(
                "SettingsAbout.TButton", background=main_bG, borderwidth=0, highlightthickness=0, focuscolor="none")
            # mouse hover style for settings_btn Button
            settings_btn_style.map("SettingsAbout.TButton", foreground=[(
                "active", "!disabled", "#F0EFF4")], background=[("active", main_bG)])

            # Creating a settings button
            settings_btn = Button(
                home, image=icon12, style="SettingsAbout.TButton", command=lambda: settingsTab())
            settings_btn.place(relx=0.1, rely=0.1, anchor=CENTER)

            # Creating a frame for the userId and log out button
            userDetails = Frame(home, width=int(
                screen_width/3), height=int(screen_height/6))
            userDetails.place(relx=1, rely=0, anchor=NE)

            # Setting background color for frame
            userDetails_label0 = Label(
                userDetails, background=main_bG, width=int(screen_width/2.5))
            userDetails_label0.place(relx=0.5, rely=0.5, height=int(
                screen_height/5), anchor=CENTER)

            # Showing the profile picture on the main panel
            rightTop_panel_profile = Label(
                userDetails, image=img12, background=main_bG)
            rightTop_panel_profile.place(relx=0.4, rely=0.5, anchor=CENTER)

            # Showing the logout button on the screen
            userDetails_label1 = Label(userDetails, text="@ "+str(inVoiceDB), font=(
                "Dodge", 14, "bold"), background=main_bG, foreground="#F0EFF4")
            userDetails_label1.place(relx=0.5, rely=0.5, anchor=W)

        def checkSignIn():  # function for checking the userid, password are valid and to login to the app

            # this prevents the function to called twice by disabling the button
            signIn_Button.configure(state=DISABLED)

            # Connecting to a database, if not exists creating one
            inVoice = sqlite3.connect("in_voice.db")

            # Creating a cursor
            co = inVoice.cursor()

            # query the database
            co.execute(
                "SELECT * FROM usersAccount WHERE userId = " + "'" + signIn_entry1_var.get() + "'")
            accounts = co.fetchall()
            # print(accounts)

            # converting tuples into separate strings
            show_userID = ""
            for account in accounts:
                show_userID += str(account[4])

            show_pwd = ""
            for account in accounts:
                show_pwd += str(account[5])

            # ----- making a condition using if-elif-else statements

            # this 'if' statement checks entry is empty or not
            if signIn_entry1_var.get() == "" or signIn_entry2_var.get() == "":
                messagebox.showerror(
                    title="Error", message="Field can't be empty", parent=signin)
                # If the any one entry is empty shows a error message
                signIn_Button.configure(state=NORMAL)

            # this elif statement checks the name entry value matches to the database
            elif signIn_entry1_var.get() == show_userID:

                # this if statement checks the password entry value matches to the database
                if signIn_entry2_var.get() == show_pwd:

                    global inVoiceDB
                    inVoiceDB = signIn_entry1_var.get()

                    # closing the signIn panel
                    root.after(300, lambda: closeSignInPanel())
                    root.after(250, lambda: aboutUs_btn.destroy())

                    # calling the function to show userId and log out button
                    root.after(400, lambda: signingIn())

                # this else statement works when the above if condition is false
                else:
                    messagebox.showerror(
                        title="Error", message="password is invalid", parent=signin)
                    signIn_Button.configure(state=NORMAL)

            # this else statement works when the above if and elif conditions are false
            else:
                messagebox.showerror(
                    title="Error", message="UserId is invalid", parent=signin)
                signIn_Button.configure(state=NORMAL)

            # commit changes
            inVoice.commit()

            # close connection
            inVoice.close()

        def showsPassword():  # function for showing the hidden password

            def hidesPassword():  # function for hiding the visible password again to hidden

                # this makes the password hidden again
                signIn_entry2.configure(show="\u25CF")

                # changing the button function to show it again when needed
                root.after(50, lambda: showsPwd.configure(
                    command=lambda: showsPassword()))

            # Making the characters in password entry visible
            signIn_entry2.configure(show="")

            # changing the button function to hide it again when needed
            root.after(50, lambda: showsPwd.configure(
                command=lambda: hidesPassword()))

        # Fading buttons
        signIn_btn_style.configure(
            "SignInButton.TButton", background="#723C70", borderwidth=1)
        # Fading tabs
        client_btn.configure(style="ICSButtonBlur.TButton")
        stock_btn.configure(style="ICSButtonBlur.TButton")
        # Fading buttons label
        client_btnLabel.configure(style="ICSLabelBlur.TLabel")
        stock_btnLabel.configure(style="ICSLabelBlur.TLabel")

        # Opening a new window for theIsignin options
        signin = Toplevel()
        signin.grab_set()
        signin.focus_set()

        # To remove the toolbar of the signIn window
        signin.overrideredirect(True)

        # Setting the new window width, height and position on the user screen
        signin_window_width = int(screen_width/3)
        signin_window_height = int(screen_height/1.2)

        signin_screen_width = signin.winfo_screenwidth()
        signin_screen_height = signin.winfo_screenheight()

        signin_x_cordinate = int(
            (signin_screen_width/2) - (signin_window_width/2))
        signin_y_cordinate = int(
            (signin_screen_height/2) - (signin_window_height/2))

        signin.geometry("%dx%d+%d+%d" % (signin_window_width,
                                         signin_window_height, signin_x_cordinate, signin_y_cordinate))

        # signIn window background color
        signin_bG = "#D4B0F9"
        # Setting background color for frame using label
        signIn_panel_label = Label(signin, background=signin_bG)
        signIn_panel_label.place(relx=0.5, rely=0.5, height=int(
            signin_screen_height), width=int(signin_screen_width), anchor=CENTER)

        # Style for exit button
        exitButton_style = Style(signin)
        exitButton_style.theme_use("default")
        exitButton_style.configure("EXITButton.TButton", font=("Dodge", 20, "bold"),
                                   foreground="#011932", background=signin_bG, borderwidth=0, highlightthickness=0, relief=FLAT, focuscolor="none")

        # mouse hover style for exitButton Button
        exitButton_style.map("EXITButton.TButton", foreground=[(
            "active", "!disabled", "#EF233C")], background=[("active", signin_bG)])

        # Creating a button for closing the signIn window
        exitButton = Button(
            signin, text="X", style="EXITButton.TButton", command=lambda: closeSignInPanel())
        exitButton.place(relx=1, rely=0.01, width=int(
            signin_screen_width/30), anchor=NE)

        # Creating labels for the signIn window
        # signIn window foreground color
        signin_fG = "#0A014F"

        # signIn label
        signIn_label1 = Label(signin, image=icon2,
                              background=signin_bG, foreground=signin_fG)
        signIn_label1.place(relx=0.5, rely=0.2, anchor=CENTER)

        # userID label
        signIn_label2 = Label(signin, text="User ID", font=(
            "Dodge", 14, "bold"), background=signin_bG, foreground=signin_fG)
        signIn_label2.place(relx=0.3, rely=0.38, anchor=CENTER)

        # password label
        signIn_label2 = Label(signin, text="Password", font=(
            "Dodge", 14, "bold"), background=signin_bG, foreground=signin_fG)
        signIn_label2.place(relx=0.33, rely=0.53, anchor=CENTER)

        # sigup label
        signIn_label3 = Label(signin, text="don't have an account?", font=(
            "Dodge", 12), background=signin_bG, foreground=signin_fG)
        signIn_label3.place(relx=0.4, rely=0.85, anchor=CENTER)

        # Creating entries for the signIn window
        # userID entry
        signIn_entry1_var = StringVar()
        signIn_entry1 = Entry(
            signin, textvariable=signIn_entry1_var, font=("Dodge", 15, "bold"), justify=RIGHT)
        signIn_entry1.place(relx=0.5, rely=0.45, height=int(
            signin_screen_height/20), width=int(signin_screen_width/5), anchor=CENTER)

        # password entry
        signIn_entry2_var = StringVar()
        signIn_entry2 = Entry(
            signin, textvariable=signIn_entry2_var, font=("Dodge", 15, "bold"), show="\u25CF", justify=RIGHT)
        signIn_entry2.place(relx=0.5, rely=0.6, height=int(
            signin_screen_height/20), width=int(signin_screen_width/5), anchor=CENTER)

        # Styling SignUp Button
        showsPwd_style = Style()
        showsPwd_style.theme_use("default")
        showsPwd_style.configure("ShowsPwd.TButton", background=signin_bG,
                                 foreground=signin_fG, borderwidth=0, hightlightthickness=0, relief=FLAT, focuscolor="none")

        # mouse hover style for SignUp Button
        showsPwd_style.map("ShowsPwd.TButton", foreground=[(
            "active", "!disabled", "#4C1036")], background=[("active", signin_bG)])

        # Creating button for showing typed password
        showsPwd = Button(signin, image=icon4,
                          style="ShowsPwd.TButton", command=lambda: showsPassword())
        showsPwd.place(relx=0.85, rely=0.6, anchor=CENTER)

        # Styling signIn_Button Button
        signIn_Button_style = Style(signin)
        signIn_Button_style.theme_use("default")
        signIn_Button_style.configure("SignInButton.TButton", font=("Dodge", 16, "bold", "italic"),
                                      foreground="#F0EFF4", background="#4C1036", borderwidth=2, highlightthickness=0, focuscolor="none")

        # mouse hover style for signIn_Button Button
        signIn_Button_style.map("SignInButton.TButton", foreground=[(
            "active", "!disabled", "#F0EFF4")], background=[("active", "#72195A")])

        # Creating button for signing in with the userID and password
        signIn_Button = Button(signin, text="Sign In",
                               style="SignInButton.TButton", command=lambda: checkSignIn())
        signIn_Button.place(relx=0.5, rely=0.75, height=int(
            signin_screen_height/20), width=int(signin_screen_width/12), anchor=CENTER)

        # Styling SignUp Button
        signUp_Button_style = Style()
        signUp_Button_style.theme_use("default")
        signUp_Button_style.configure("SignUpButton.TLabel", font=("Dodge", 14, "bold", "underline"), background=signin_bG,
                                      foreground=signin_fG, borderwidth=0, hightlightthickness=0, relief=FLAT, focuscolor="none")

        # mouse hover style for SignUp Button
        signUp_Button_style.map("SignUpButton.TLabel", foreground=[(
            "active", "!disabled", "#4C1036")], background=[("active", signin_bG)])

        # Creating button for Signup
        signUp_Button = Button(signin, text="Sign Up",
                               style="SignUpButton.TLabel", command=lambda: signUpPanel())
        signUp_Button.place(relx=0.7, rely=0.85, height=int(
            signin_screen_height/20), width=int(signin_screen_width/12), anchor=CENTER)

    def aboutUs():  # function for displaying the aboutUs screen

        def closeAboutUs():  # function for closing aboutUs screen

            # deleting the aboutUs panel
            about_panel_back.destroy()
            about_panel.destroy()
            # enabling the signIn button
            signIn_btn.lift()

            # changing the button function back to normal
            root.after(100, lambda: aboutUs_btn.configure(
                text="About Us", command=lambda: aboutUs()))

        # this changes the button text and function
        root.after(100, lambda: aboutUs_btn.configure(
            text="back", command=lambda: closeAboutUs()))

        # disabling the signIn button
        signIn_btn.lower()

        # aboutUs colors
        aboutUs_bG = "#1E0905"
        aboutUs_fG = "#F0EFF4"

        # Creating a frame for aboutUs information
        about_panel_back = Canvas(home, width=int(screen_width/1.2),
                                  height=int(screen_height/2), highlightthickness=0, background=aboutUs_bG)
        about_panel_back.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Creating a frame for aboutUs information
        about_panel = Frame(home, width=int(screen_width/1.6),
                            height=int(screen_height/2))
        about_panel.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Giving background a color
        about_panel_label0 = Label(
            about_panel, background=aboutUs_bG, width=int(screen_width/1.5))
        about_panel_label0.place(relx=0.5, rely=0.5, height=int(
            screen_height/2), anchor=CENTER)

        about_panel_outline = Canvas(
            about_panel, width=int(screen_width/1.4), height=int(screen_height/2.2), background=aboutUs_bG)
        about_panel_outline.place(
            relx=0.5, rely=0.5, anchor=CENTER)

        # labels for aboutUs
        about_panel_label1 = Label(
            about_panel, text="Version                 :  ", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label1.place(relx=0.3, rely=0.2, anchor=CENTER)

        about_panel_label11 = Label(
            about_panel, text="1 . 0 . 1", font=("Dodge", 15, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label11.place(relx=0.5, rely=0.2, anchor=W)

        about_panel_label2 = Label(
            about_panel, text="Developed by     :  ", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label2.place(relx=0.3, rely=0.4, anchor=CENTER)

        about_panel_label21 = Label(
            about_panel, text="Mahendra Kumara", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label21.place(relx=0.5, rely=0.4, anchor=W)

        about_panel_label3 = Label(
            about_panel, text="Released on        :  ", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label3.place(relx=0.3, rely=0.6, anchor=CENTER)

        about_panel_label31 = Label(
            about_panel, text="06-03-2022", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label31.place(relx=0.5, rely=0.6, anchor=W)

        about_panel_label4 = Label(
            about_panel, text="Published by     :  ", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label4.place(relx=0.3, rely=0.8, anchor=CENTER)

        about_panel_label41 = Label(
            about_panel, text="Programming with Maurya", font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        about_panel_label41.place(relx=0.5, rely=0.8, anchor=W)

    # function for changing back the look of stock_btn while leaving
    def leaved_stocksButton(event):

        # Clear fade out
        invoice_btn.configure(style="ICSButton.TButton")
        client_btn.configure(style="ICSButton.TButton")
        # Shrinking the client button
        stock_btn.place(relx=0.8, rely=0.7, height=int(
            screen_height/3), width=int(screen_width/5), anchor=CENTER)

        # Fading buttons label
        invoice_btnLabel.configure(style="ICSLabel.TLabel")
        client_btnLabel.configure(style="ICSLabel.TLabel")
        # Shrinking the stocks button label
        stock_btnLabel.place(relx=0.5, rely=0.72, width=int(
            screen_width/5.3), anchor=CENTER)

    # function for changing the look of stock_btn while hovering
    def entered_stocksButton(event):

        # Fading out
        invoice_btn.configure(style="ICSButtonBlur.TButton")
        client_btn.configure(style="ICSButtonBlur.TButton")
        # scaling the stocks button
        stock_btn.place(relx=0.8, rely=0.7, height=int(
            screen_height/2.3), width=int(screen_width/4.3), anchor=CENTER)

        # Fading buttons label
        invoice_btnLabel.configure(style="ICSLabelBlur.TLabel")
        client_btnLabel.configure(style="ICSLabelBlur.TLabel")
        # Scaling the stocks button label
        stock_btnLabel.place(relx=0.5, rely=0.72, width=int(
            screen_width/4.8), anchor=CENTER)

    # function for changing back the look of client_btn while leaving
    def leaved_clientButton(event):

        # Clear fade out
        invoice_btn.configure(style="ICSButton.TButton")
        stock_btn.configure(style="ICSButton.TButton")
        # Shrinking the client button
        client_btn.place(relx=0.2, rely=0.7, height=int(
            screen_height/3), width=int(screen_width/5), anchor=CENTER)

        # Fading buttons label
        invoice_btnLabel.configure(style="ICSLabel.TLabel")
        stock_btnLabel.configure(style="ICSLabel.TLabel")
        # Shrinking the client button label
        client_btnLabel.place(relx=0.5, rely=0.72, width=int(
            screen_width/5.3), anchor=CENTER)

    # function for changing the look of client_btn while hovering
    def entered_clientButton(event):

        # Fading out
        invoice_btn.configure(style="ICSButtonBlur.TButton")
        stock_btn.configure(style="ICSButtonBlur.TButton")
        # scaling the client button
        client_btn.place(relx=0.2, rely=0.7, height=int(
            screen_height/2.3), width=int(screen_width/4.3), anchor=CENTER)

        # Fading buttons label
        invoice_btnLabel.configure(style="ICSLabelBlur.TLabel")
        stock_btnLabel.configure(style="ICSLabelBlur.TLabel")
        # Scaling the client button label
        client_btnLabel.place(relx=0.5, rely=0.72, width=int(
            screen_width/4.8), anchor=CENTER)

    # function for changing back the look of invoice_btn while leaving
    def leaved_invoiceButton(event):

        # Clear fade out buttons
        client_btn.configure(style="ICSButton.TButton")
        stock_btn.configure(style="ICSButton.TButton")
        # Shrinking the invoice button
        invoice_btn.place(relx=0.5, rely=0.7, height=int(
            screen_height/2.7), width=int(screen_width/4.7), anchor=CENTER)

        # Clear fade out labels
        client_btnLabel.configure(style="ICSLabel.TLabel")
        stock_btnLabel.configure(style="ICSLabel.TLabel")
        # Shrinking the invoice button label
        invoice_btnLabel.place(relx=0.5, rely=0.7, width=int(
            screen_width/5), anchor=CENTER)

    # function for changing the look of invoice_btn while hovering
    def entered_invoiceButton(event):

        # Fading buttons
        client_btn.configure(style="ICSButtonBlur.TButton")
        stock_btn.configure(style="ICSButtonBlur.TButton")
        # scaling the invoice button
        invoice_btn.place(relx=0.5, rely=0.7, height=int(
            screen_height/2.3), width=int(screen_width/4.3), anchor=CENTER)

        # Fading buttons label
        client_btnLabel.configure(style="ICSLabelBlur.TLabel")
        stock_btnLabel.configure(style="ICSLabelBlur.TLabel")
        # Scaling the invoice button label
        invoice_btnLabel.place(relx=0.5, rely=0.7, width=int(
            screen_width/4.8), anchor=CENTER)

    # function for destroying the label widget created by entered_close() function
    def leaved_close(event):

        # deleting the label
        close_label.destroy()

    # function for creating and showing a label with some text when called by the mouse hover over close_button
    def entered_close(event):

        # assigning the label as global variable
        global close_label

        # creating and positioning the label
        close_label = Label(
            root, text="Close", background="#F8FFE5", foreground="black", borderwidth=1, width=5)
        valuex = (screen_width-80+int(event.x))
        valuey = int(event.y)+15
        close_label.place(x=valuex, y=valuey)

    def minimize():  # function which minimizes the root window and creates a button to call it again

        def maximize():  # function for getting the minimized window back

            # Getting the minimized window in fullscreen with no toolbar
            root.deiconify()
            root.state("zoomed")
            root.overrideredirect(True)

            # this deletes the widgets created by minimize() function
            root2.destroy()

        # To replace the removed the toolbar of the root window
        root.overrideredirect(False)
        # this minimizes the window
        root.withdraw()

        # creating a new window and removing the toolbar for the maximize button
        root2 = Toplevel()
        root2.overrideredirect(True)

        # Setting the window width, height and position on the user screen
        root2_window_width = 40
        root2_window_height = 40

        root2_screen_width = root2.winfo_screenwidth()
        root2_screen_height = root2.winfo_screenheight()

        root2_x_cordinate = int((root2_screen_width) - (root2_window_width+50))
        root2_y_cordinate = int(
            (root2_screen_height) - (root2_window_height+60))

        root2.geometry("%dx%d+%d+%d" % (root2_window_width,
                                        root2_window_height, root2_x_cordinate, root2_y_cordinate))

        # Creating a exit button
        # Styling the exit Button
        max_button_style = Style(root2)
        max_button_style.theme_use("default")
        max_button_style.configure(
            "Maximize.TButton", background="#00000E", borderwidth=0, focuscolor="none")
        # Changing the mapping style of exit button
        max_button_style.map("Maximize.TButton", foreground=[("active", "!disabled", "#011932")],
                             background=[("active", "black")])

        # Creating the maximize button and positioning it on the screen
        max_button = Button(root2, image=icon1, style="Maximize.TButton",
                            command=lambda: maximize())
        max_button.place(relx=0.488, rely=0.488, anchor=CENTER)

    # To make the window fullscreen and non-resizable
    root.wm_state("zoomed")

    # # Setting the background color of the root window
    # background_color = Canvas(root, width=screen_width,
    #                           height=screen_height, background="purple", borderwidth=0, highlightthickness=0)  # 01102E
    # background_color.grid()

    #     -----------------------------------------
    # -------------------- Title Bar ---------------------
    #     -----------------------------------------

    # Creating a new frame for the title bar and positioning it on root window
    title_frame = Frame(root, width=screen_width, height=int(screen_height/24))
    title_frame.place(relx=0.5, rely=0, anchor=N)

    # Setting the background color of the frame by creating a label widget
    title_color = Label(title_frame, width=screen_width,
                        background="#011932", borderwidth=1)
    title_color.place(relx=0.5, rely=0.5,
                      height=int(screen_height/22), anchor=CENTER)

    #       -----------------------------------------
    # -------------------- Exit Button ---------------------
    #       -----------------------------------------

    # Styling the exit Button
    close_button_style = Style(title_frame)
    close_button_style.theme_use("default")
    close_button_style.configure("Close.TButton", font=("Dodge", 14, "bold"),
                                 foreground="#B3C6E7", background="#011932", borderwidth=0, focuscolor="none")
    # Changing the mapping style of exit button
    close_button_style.map("Close.TButton", foreground=[("active", "!disabled", "#011932")],
                           background=[("active", "#EF233C")])

    # Creating a exit button and positioning it on the title bar
    close_button = Button(title_frame, text="X", style="Close.TButton",
                          command=lambda: root.destroy())
    close_button.place(relx=0.998, rely=0.5, width=int(screen_width/27),
                       height=int(screen_height/28), anchor=E)

    # this calls the function assigned with the exit button entry and leaving
    close_button.bind("<Enter>", entered_close)
    close_button.bind("<Leave>", leaved_close)

    #         -----------------------------------------
    # -------------------- Minimize Button ---------------------
    #         -----------------------------------------

    # Creating a minimize button and displaying it as icon
    # Styling the minimize Button
    minnimize_button_style = Style(title_frame)
    minnimize_button_style.theme_use("default")
    minnimize_button_style.configure(
        "Minimize.TButton", foreground="#B3C6E7", background="#011932", borderwidth=0, focuscolor="none")

    # Changing the mapping style of minimize button
    minnimize_button_style.map("Minimize.TButton", foreground=[("active", "!disabled", "red")],
                               background=[("active", "#01102E")])

    # Setting the minimize button a image and positioning it on the title bar
    minnimize = Button(title_frame,  style="Minimize.TButton",
                       command=lambda: minimize(), image=icon)
    minnimize.place(relx=0.015, rely=0.5, width=int(
        screen_width/35), height=int(screen_height/25), anchor=CENTER)

    #         -----------------------------------------
    # -------------------- Main Panel ---------------------
    #         -----------------------------------------

    # Creating a frame for main panel
    home = Frame(root, height=int(screen_height/1.035),
                 width=int(screen_width))
    home.place(relx=0.5, rely=1, anchor=S)

    # main panel background color
    main_bG = "#1E0905"

    # Creating a labels for displaying the application name
    main_panel_label0 = Label(
        home, background=main_bG, width=int(screen_width))
    main_panel_label0.place(relx=0.5, rely=0.5, height=int(
        screen_height), anchor=CENTER)

    # Styling signIn_btn Button
    signIn_btn_style = Style(home)
    signIn_btn_style.theme_use("default")
    signIn_btn_style.configure("SignInAbout.TButton", font=("Dodge", 16, "bold", "italic"),
                               foreground="#F0EFF4", background="#BF09D5", borderwidth=2, highlightthickness=0, focuscolor="none")

    # mouse hover style for signIn_btn Button
    signIn_btn_style.map("SignInAbout.TButton", foreground=[(
        "active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

    # Creating a signIn button
    signIn_btn = Button(home, text="Sign In",
                        style="SignInAbout.TButton", command=lambda: signInPanel())
    signIn_btn.place(relx=0.9, rely=0.1, anchor=CENTER)

    # Creating the About Us button
    aboutUs_btn = Button(home, text="About Us",
                         style="SignInAbout.TButton", command=lambda: aboutUs())
    aboutUs_btn.place(relx=0.1, rely=0.1, anchor=CENTER)

    # Creating labels for displaying the app name on the main panel
    home_appName1 = Label(home, text="in", foreground="#B3C6E7",
                          background=main_bG, font=("Magneto", 100, "bold"))
    home_appName1.place(relx=0.5, rely=0.2, anchor=CENTER)

    home_appName2 = Label(home, text="Voice", foreground="#D6DDE8",
                          background=main_bG, font=("Matura MT Script Capitals", 25, "bold"))
    home_appName2.place(relx=0.55, rely=0.3, anchor=CENTER)

    # Styling for invoice, client, stocks Button
    ICS_btn_style = Style(home)
    ICS_btn_style.theme_use("default")
    ICS_btn_style.configure("ICSButton.TButton", font=("Dodge", 30, "bold", "italic"),
                            foreground="#F0EFF4", background="#F72585", borderwidth=2, focuscolor="none", higlightthickness=0, anchor=N)
    # Blur style
    ICS_btn_style.configure("ICSButtonBlur.TButton", font=("Dodge", 30, "bold", "italic"),
                            foreground="#E598AE", background="#B7094C", borderwidth=1, focuscolor="none", higlightthickness=0, anchor=N)
    # mouse hover style for invoice, client, stocks Button
    ICS_btn_style.map("ICSButton.TButton", foreground=[(
        "active", "!disabled", "#F0EFF4")], background=[("active", "#F72585")])

    # Creating a button for opening invoices tab
    invoice_btn = Button(home, text="\rInvoices",
                         style="ICSButton.TButton", command=lambda: signInPanel())
    invoice_btn.place(relx=0.5, rely=0.7, height=int(
        screen_height/2.7), width=int(screen_width/4.7), anchor=CENTER)

    # this calls the function assigned with the mouse hover over invoice entry
    invoice_btn.bind("<Enter>", entered_invoiceButton)
    invoice_btn.bind("<Leave>", leaved_invoiceButton)

    # Creating a button for opening Clients tab
    client_btn = Button(home, text="\rClients",
                        style="ICSButton.TButton", command=lambda: signInPanel())
    client_btn.place(relx=0.2, rely=0.7, height=int(
        screen_height/3), width=int(screen_width/5), anchor=CENTER)

    # this calls the function assigned with the mouse hover over invoice entry
    client_btn.bind("<Enter>", entered_clientButton)
    client_btn.bind("<Leave>", leaved_clientButton)

    # Creating a button for opening Stocks tab
    stock_btn = Button(home, text="\rStocks",
                       style="ICSButton.TButton", command=lambda: signInPanel())
    stock_btn.place(relx=0.8, rely=0.7, height=int(
        screen_height/3), width=int(screen_width/5), anchor=CENTER)

    # this calls the function assigned with the mouse hover over invoice entry
    stock_btn.bind("<Enter>", entered_stocksButton)
    stock_btn.bind("<Leave>", leaved_stocksButton)

    # Styling for invoice, client, stocks labels
    ICS_label_style = Style(home)
    ICS_label_style.theme_use("default")
    ICS_label_style.configure("ICSLabel.TLabel", font=("Dodge", 12, "bold", "italic"), foreground="#E598AE", background="#832161",
                              borderwidth=2, focuscolor="none", higlightthickness=0, relief=SUNKEN, justify=CENTER, anchor=CENTER)
    # Blur style
    ICS_label_style.configure("ICSLabelBlur.TLabel", font=("Dodge", 12, "bold", "italic"),
                              foreground="#E598AE", background="#602453", borderwidth=1, focuscolor="none", higlightthickness=0, relief=SUNKEN, justify=CENTER, anchor=CENTER)

    # Creating label for invoice button
    invoice_btnLabel = Label(
        invoice_btn, text="\nCREATE,    VIEW   & \r\nMODIFY   invoices\n", style="ICSLabel.TLabel")
    invoice_btnLabel.place(relx=0.5, rely=0.7, width=int(
        screen_width/5), anchor=CENTER)

    # Creating label for client button
    client_btnLabel = Label(
        client_btn, text="\nADD,    VIEW   & \r\nEDIT   client's details\n", style="ICSLabel.TLabel")
    client_btnLabel.place(relx=0.5, rely=0.72, width=int(
        screen_width/5.3), anchor=CENTER)

    # Creating label for stocks button
    stock_btnLabel = Label(
        stock_btn, text="\n    ADD   & \r\nUPDATE   stocks \n", style="ICSLabel.TLabel")
    stock_btnLabel.place(relx=0.5, rely=0.72, width=int(
        screen_width/5.3), anchor=CENTER)

    # placing these widgets on top of another
    title_frame.lift()
    title_color.lift()
    close_button.lift()
    minnimize.lift()


def starting():  # function which creates and runs the countdown

    def triggering_main():  # function for deleting widgets and triggering the main() function

        # this calls the main function
        root.after(100, lambda: main())

        # this deletes the background image and the text on it
        root.after(110, lambda: background_img.destroy())

    def timer_dot3():  # this function is for positioning dots in second position

        global dots
        dots = ". ."
        background_img.itemconfigure(
            change_text, text=txt1 + str(txt2) + txt3 + dots)

    def timer_dot2():  # this function is for positioning dots in first position

        global dots
        dots = " .."
        background_img.itemconfigure(
            change_text, text=txt1 + str(txt2) + txt3 + dots)

    def timer_dot1():  # this function is for positioning dots in final position

        global dots
        dots = ".. "
        background_img.itemconfigure(
            change_text, text=txt1 + str(txt2) + txt3 + dots)

    def timer():  # this function changes the timer count

        global txt2
        txt2 -= 1
        background_img.itemconfigure(
            change_text, text=txt1 + str(txt2) + txt3 + dots)

        if txt2 == 0:
            background_img.destroy()

        else:
            root.after(1000, lambda: timer())

    # Creating and Positioning the timer over image
    change_text = background_img.create_text(
        335, 245, text=txt1 + str(txt2) + txt3 + dots, fill="#D6DDE8", font=("Dongle", 9))

    # this calls the function for changing the countdown
    root.after(1000, lambda: timer())

    # this calls the function for changing the dots position
    root.after(200, lambda: timer_dot2())
    root.after(400, lambda: timer_dot3())
    root.after(600, lambda: timer_dot1())
    root.after(800, lambda: timer_dot2())
    root.after(1000, lambda: timer_dot3())
    root.after(1200, lambda: timer_dot1())
    root.after(1400, lambda: timer_dot2())
    root.after(1600, lambda: timer_dot3())
    root.after(1800, lambda: timer_dot1())
    root.after(2000, lambda: timer_dot2())
    root.after(2200, lambda: timer_dot3())
    root.after(2400, lambda: timer_dot1())
    root.after(2600, lambda: timer_dot2())
    root.after(2800, lambda: timer_dot3())
    root.after(3000, lambda: timer_dot1())
    root.after(3200, lambda: timer_dot2())
    root.after(3400, lambda: timer_dot3())
    root.after(3600, lambda: timer_dot1())
    root.after(3800, lambda: timer_dot2())
    root.after(4000, lambda: timer_dot3())
    root.after(4200, lambda: timer_dot1())
    root.after(4400, lambda: timer_dot2())
    root.after(4600, lambda: timer_dot3())
    root.after(4800, lambda: timer_dot1())
    root.after(4990, lambda: timer_dot2())

    # this calls the function for triggering the main() function
    root.after(5010, lambda: triggering_main())


def my_name2():  # function which creates the name

    # Creating and Positioning another text over image
    background_img.create_text(65, 250, text="Mahendra Kumara",
                               fill="#01102E", font=("Playball", 8, "bold", "italic"))

    # calling the function for creating countdown
    root.after(800, lambda: starting())


def my_name1():  # function which creates the name tile

    # Creating and Positioning another text over image
    background_img.create_text(30, 235, text="designed by", fill="#00000E", font=(
        "Dongle", 7))

    # Calling the function for another name
    root.after(400, lambda: my_name2())


def logo2():  # function which creates the logo2

    # Creating and Positioning another text over image
    background_img.create_text(260, 160, text="Voice", fill="#D6DDE8", font=(
        "Matura MT Script Capitals", 18, "bold"))

    # Calling the function for name
    root.after(800, lambda: my_name1())


def logo1():  # function which creates the logo1

    # Creating and Positioning the text over image
    background_img.create_text(
        250, 100, text="in", fill="#B3C6E7", font=("Magneto", 80, "bold"))

    # Calling the another function for logo
    root.after(400, lambda: logo2())


# Setting a background size of the canvas widget
background_img = Canvas(root, width=window_width,
                        height=window_height, highlightthickness=0)
# highlightthickness=0 removes the border around the image
background_img.grid()

# Placing a background image in canvas widgets
img = Image.open(
    "Images/launcher.jpg")
img = img.resize((window_width, window_height), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Positioning the image over canvas
background_img.create_image(0, 0, anchor=NW,
                            image=img)
# Calling the function for displaying logo
root.after(500, lambda: logo1())


root.mainloop()

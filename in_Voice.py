# ---- in Voice ---- a in-voice application designed and developed by Kumara


# Importing everything tkinter and tkinter.ttk modules for creating the GUI
from tkinter import *
from tkinter.ttk import *

# Importing the required modules from Pillow library to work with imagefiles
from PIL import ImageTk, Image, ImageChops, ImageDraw

# Importing the class messagebox to create a messagebox, filedialog to permit User to select Image files for their profile
from tkinter import messagebox, filedialog, scrolledtext

# Importing tkinter as variable for special purposes
import tkinter as tk

# Importing random and string modules for generating numbers and string in random order
import random
import string

# Importing the datatime module to work with date and times
from datetime import datetime, timedelta

# Importing the textwrap module to Wrap text strings to multiple lines
import textwrap

# Importing Calendar Class from tkcalendar module for working with calendars
from tkcalendar import Calendar

# Importing babel.numbers module to make the calendars working after converting this app into .exe file
from babel.numbers import *

# Importing the autocomplete entry from the ttkwidgets module
from ttkwidgets.autocomplete import AutocompleteEntry

# Importing a custom module to work with database through Class and its methods
from inVoiceDB import UserCredential, UserDetail, CurrencyRate, DueDate, InVoiceDetail, ClientDetail, ProductDetail, UserPreference, wordDocGenerator


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

root = Tk()

# Giving Title to the root-Window
root.title("in Voice")

# Removing the default toolbar of the root-Window which is provided by OS
root.overrideredirect(True)

# Assigning the width and height for the root-Window while launching
window_width = 400
window_height = 260

# Getting the fullscreen resolution of the display where the root-Window is running
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculating the X, Y coordinates for placing the root-Window to the center of the screen from every axis
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

# Setting the width, height and positioning the root-Window using the calculated X, Y coordinates
root.geometry("%dx%d+%d+%d" % (window_width,
              window_height, x_cordinate, y_cordinate))

# Assigning the path to the App's main logo to a variable
path_to_logo = "Images/logo.png"

# Setting a image as icon for taskbar using iconphoto() method
root.iconphoto(False, PhotoImage(file=path_to_logo))

#         -----------------------------------------
# -------------------- Images & Icons ---------------------
#         -----------------------------------------

# Assigning the root directory for all the Images & Icons
img_DIR = "./Images/"

# Opening a image for --- Logo --- and assigning it into a variable
logo = Image.open(path_to_logo).convert("RGBA")

# Opening a cropped image for --- Logo --- and assigning it into a variable
cropped_logo = Image.open(f"{img_DIR}logo_C.png").convert("RGBA")

# Opening a image for --- Show Password --- button and assigning it into a variable
showHide_icon = Image.open(f"{img_DIR}show.png").convert("RGBA")

# Opening a image for --- Generate Key --- button and assigning it into a variable
key_icon = Image.open(f"{img_DIR}key.png").convert("RGBA")

# Opening a image for --- Settings --- button and assigning it into a variable
controls_icon = Image.open(f"{img_DIR}control.png").convert("RGBA")

# Opening a image for --- Dashboard --- link and assigning it into a variable
dashboard_icon = Image.open(f"{img_DIR}dashboard.png").convert("RGBA")

# Opening a image for --- InVoice --- link and assigning it into a variable
inVoice_icon = Image.open(f"{img_DIR}invoice.png").convert("RGBA")

# Opening a image for --- Clients --- link and assigning it into a variable
clients_icon = Image.open(f"{img_DIR}clients.png").convert("RGBA")

# Opening a image for --- Stocks --- link and assigning it into a variable
stocks_icon = Image.open(f"{img_DIR}stocks.png").convert("RGBA")

# Opening a image for --- Settings --- link and assigning it into a variable
settings_icon = Image.open(f"{img_DIR}settings.png").convert("RGBA")

# Opening a image for --- Wrap --- Button and assigning it into a variable
wrap_icon = Image.open(f"{img_DIR}fold.png").convert("RGBA")

# Opening a image for --- Shrinked Left Panel --- label and assigning it into a variable
menu_icon = Image.open(f"{img_DIR}menu.png").convert("RGBA")

# Opening a image for --- Calendar --- Button and assigning it into a variable
calendar_icon = Image.open(f"{img_DIR}calendar.png").convert("RGBA")

# Opening a image for --- Edit --- Buttons and assigning it into a variable
edit_icon = Image.open(f"{img_DIR}edit.png").convert("RGBA")

# Opening a image for --- Delete --- Buttons and assigning it into a variable
delete_icon = Image.open(f"{img_DIR}trash.png").convert("RGBA")


# Assigning the latest resampling filter if available, else assigning the old filter
resampling_filter = Image.Resampling.LANCZOS if (
    Image.Resampling.LANCZOS) else Image.LANCZOS

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Function which creates the structure of the --- `(in Voice)` --- Home-Screen
def inVoice_HomeScreen():

    # Function to show/hide Title Bar's Button INFO while mouse-hovering
    def titleBar_INFO(event):

        # Making the Title Bar's Button INFO a global variable so it can be accessed everywhere
        global titleBar_btn_INFO

        # Getting the type of the event by id_number
        event_ID = int(getattr(event, "__dict__")["type"])

        # Checking if the Event-Enter is on Close(X) Button
        if (event_ID == 7 and event.widget["text"] == "X"):

            # Creating a label to show INFO about Close(X) Button
            titleBar_btn_INFO = Label(root, text="Close", font=("Dodge", 10, "bold"),
                                      background=main_bG, foreground="#000000", borderwidth=1, width=5)

            # Calculating the X, Y coordinates for placing the Close(X) Button's INFO
            x_axis = (screen_width-80+int(event.x))
            y_axis = int(event.y)+15

            # Positioning the Close(X) Button's INFO using the calculated X, Y coordinates
            titleBar_btn_INFO.place(x=x_axis, y=y_axis)

        # Checking if the Event-Enter is on Minimize Button
        elif (event_ID == 7 and event.widget["text"] == "-"):

            # Creating a label to show INFO about Minimize Button
            titleBar_btn_INFO = Label(root, text="minimize", font=("Dodge", 9, "bold"),
                                      background=main_bG, foreground="#000000", width=7.5)

            # Calculating the X, Y coordinates for placing the Minimize Button's INFO
            x_axis = int(event.x)+5
            y_axis = int(event.y)+20

            # Positioning the Minimize Button's INFO using the calculated X, Y coordinates
            titleBar_btn_INFO.place(x=x_axis, y=y_axis)

        elif (event_ID == 8):

            # Destroying the Title Bar's Button INFO when mouseevent is <Leave>
            titleBar_btn_INFO.destroy()

    # >>

    # Function which is operated by Close(X) Button and that creates a confirmation message before Quitting
    def closeInVoiceAPP():

        # Disabling the Close(X) Button after clicked, for preventing the function to be called twice
        close_X_btn.configure(state=DISABLED)

        # Showing a confirmation dialog with some message
        button_click = messagebox.askquestion("in Voice",
                                              "Are you sure, you want to exit?")

        if (button_click == "yes"):

            # Clearing the --- `(in Voice)` --- cache folder and its files
            UserCredential.createHiddenDIR(
                UserCredential, "./.__appcache__", "clearCache")

            # Closing the --- `(in Voice)` ---
            root.after(500, lambda: root.destroy())

        else:

            # Re-enabling the Close(X) Button
            close_X_btn.configure(state=NORMAL)

    # >>

    # Function which is operated by the Minimize Button to minimize the Application and displaying it as a logo on the lower-left corner of screen
    def minimizeInvoiceAPP():

        # Function which makes the Application back to fullscreen when the root-Window is maximized
        def maximizeInvoiceAPP(event):

            if (root.state() == "zoomed"):

                # Removing the default toolbar again
                root.after(10, lambda: root.overrideredirect(True))

                # Re-enabling the Minimize Button
                minimize_btn.configure(state=NORMAL)

                # Removing the 'maximizeInvoiceAPP' function assigned with the root-Window
                root.unbind("<Map>", minimize_state)

        # >>

        # Disabling the Minimize Button after clicked, for preventing the function to be called twice
        minimize_btn.configure(state=DISABLED)

        # Minimizing the root-Window as a icon to the Taskbar
        root.overrideredirect(False)
        root.iconify()

        # Assigning a function to track the changes made on the size of root-Window
        minimize_state = root.bind("<Map>", maximizeInvoiceAPP)

        # -------------------------------------------------------------------------------------------- `(in Voice)` Minimized State -StyleEnds----

    # >>

    # Function which is operated by the AboutUs Button to Show the AboutUs Panel
    def aboutUsPanel():

        # Function which is operated by the AboutUs Button to Hide the AboutUs Panel
        def closeAboutUsPanel():

            # Disabling the AboutUs Button after clicked, for preventing the function to be called twice
            aboutUs_btn.configure(state=DISABLED)

            # Destroying all the widgets created in the AboutUs panel
            aboutUs_frame.destroy()

            # Showing the SignIn Button again
            signIn_btn.lift()

            # Changing the AboutUs Button text and function back to default
            root.after(100, lambda: aboutUs_btn.configure(text="About Us",
                                                          state=NORMAL, command=lambda: aboutUsPanel()))

        # >>

        # ------------------------------------- `(in Voice)` AboutUs Panel -StyleStarts----------------------------------------------------

        # Disabling the AboutUs Button after clicked, for preventing the function to be called twice
        aboutUs_btn.configure(state=DISABLED)

        # Changing the AboutUs Button text and function assigned to it
        root.after(100, lambda: aboutUs_btn.configure(text="back",
                                                      state=NORMAL, command=lambda: closeAboutUsPanel()))

        # Hiding the SignIn Button when AboutUs Panel is open
        signIn_btn.lower()

        # Assigning the common colors used in AboutUs Panel
        aboutUs_bG = "#F4F4F4"
        aboutUs_fG = "#1E0905"

        # Creating a frame for the AboutUs Panel
        aboutUs_frame = Frame(home_frame, width=int(screen_width),
                              height=int(screen_height/2))
        aboutUs_frame.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Creating a label to set a background color for the AboutUs Panel
        aboutUs_bgColor = Label(aboutUs_frame, background=main_bG,
                                width=int(screen_width/1.5))
        aboutUs_bgColor.place(relx=0.5, rely=0.5,
                              height=int(screen_height/2), anchor=CENTER)

        # Creating a outline for the informations in the AboutUs Panel
        aboutUs_outline = Canvas(aboutUs_frame, width=int(screen_width/1.4),
                                 height=int(screen_height/2.2), background=aboutUs_bG, highlightbackground="#969696")
        aboutUs_outline.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Creating the LEFT-side labels to show titles of information in AboutUs Panel
        aboutUs_L_label1 = Label(aboutUs_frame, text="Version                 :  ",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_L_label1.place(relx=0.3, rely=0.2, anchor=CENTER)

        aboutUs_L_label2 = Label(aboutUs_frame, text="Developed by     :  ",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_L_label2.place(relx=0.3, rely=0.4, anchor=CENTER)

        aboutUs_L_label3 = Label(aboutUs_frame, text="Released on        :  ",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_L_label3.place(relx=0.3, rely=0.6, anchor=CENTER)

        aboutUs_L_label4 = Label(aboutUs_frame, text="Published by     :  ",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_L_label4.place(relx=0.3, rely=0.8, anchor=CENTER)

        # Creating the Right-side labels to show the information in AboutUs Panel
        aboutUs_R_label1 = Label(aboutUs_frame, text="1 . 1 . 0",
                                 font=("Dodge", 15, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_R_label1.place(relx=0.5, rely=0.2, anchor=W)

        aboutUs_R_label2 = Label(aboutUs_frame, text="Mahendra Kumara",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_R_label2.place(relx=0.5, rely=0.4, anchor=W)

        aboutUs_R_label3 = Label(aboutUs_frame, text="06-03-2022",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_R_label3.place(relx=0.5, rely=0.6, anchor=W)

        aboutUs_R_label4 = Label(aboutUs_frame, text="Programming with Maurya",
                                 font=("Dodge", 14, "bold"), foreground=aboutUs_fG, background=aboutUs_bG)
        aboutUs_R_label4.place(relx=0.5, rely=0.8, anchor=W)

        # -------------------------------------------------------------------------------------------- `(in Voice)` AboutUs Panel -StyleEnds----

    # >>

    # Function for styling the Tab-Buttons while mouse-hovering
    def TAB_hoveringEffect(event):

        # Getting the type of the event by id_number
        event_ID = int(getattr(event, "__dict__")["type"])

        # Checking if the Event is <Enter>
        if (event_ID == 7):

            # Fading the Tab-Buttons and its labels
            inVoiceTAB_btn.configure(style="TAB-Blur.TButton")
            clientTAB_btn.configure(style="TAB-Blur.TButton")
            stockTAB_btn.configure(style="TAB-Blur.TButton")
            ##
            inVoiceTAB_btnLabel.configure(style="TAB-Blur.TLabel")
            clientTAB_btnLabel.configure(style="TAB-Blur.TLabel")
            stockTAB_btnLabel.configure(style="TAB-Blur.TLabel")

            if (event.widget["text"] == "\rInVoices"):

                # Clearing the fade-out on InVoice Tab-Button and its label
                inVoiceTAB_btn.configure(style="TAB.TButton")
                inVoiceTAB_btnLabel.configure(style="TAB.TLabel")

                # Scaling the InVoice Tab-Button and its label
                inVoiceTAB_btn.place(relx=0.5, rely=0.7,
                                     height=int(screen_height/2.3), width=int(screen_width/4.3), anchor=CENTER)
                inVoiceTAB_btnLabel.place(relx=0.5, rely=0.7,
                                          width=int(screen_width/4.8), anchor=CENTER)

            if (event.widget["text"] == "\rClients"):

                # Clearing the fade-out on Client Tab-Button and its label
                clientTAB_btn.configure(style="TAB.TButton")
                clientTAB_btnLabel.configure(style="TAB.TLabel")

                # Scaling the Client Tab-Button and its label
                clientTAB_btn.place(relx=0.2, rely=0.7,
                                    height=int(screen_height/2.3), width=int(screen_width/4.3), anchor=CENTER)
                clientTAB_btnLabel.place(relx=0.5, rely=0.72,
                                         width=int(screen_width/4.8), anchor=CENTER)

            if (event.widget["text"] == "\rStocks"):

                # Clearing the fade-out on Stock Tab-Button and its label
                stockTAB_btn.configure(style="TAB.TButton")
                stockTAB_btnLabel.configure(style="TAB.TLabel")

                # Scaling the Stock Tab-Button and its label
                stockTAB_btn.place(relx=0.8, rely=0.7,
                                   height=int(screen_height/2.3), width=int(screen_width/4.3), anchor=CENTER)
                stockTAB_btnLabel.place(relx=0.5, rely=0.72,
                                        width=int(screen_width/4.8), anchor=CENTER)

        # Checking if the Event is <Leave>
        elif (event_ID == 8):

            # Clearing the fade-out on Tab-Buttons and its labels
            inVoiceTAB_btn.configure(style="TAB.TButton")
            clientTAB_btn.configure(style="TAB.TButton")
            stockTAB_btn.configure(style="TAB.TButton")
            ##
            inVoiceTAB_btnLabel.configure(style="TAB.TLabel")
            clientTAB_btnLabel.configure(style="TAB.TLabel")
            stockTAB_btnLabel.configure(style="TAB.TLabel")

            # Re-scaling the Tab-Buttons to original size
            inVoiceTAB_btn.place(relx=0.5, rely=0.7,
                                 height=int(screen_height/2.7), width=int(screen_width/4.7), anchor=CENTER)
            clientTAB_btn.place(relx=0.2, rely=0.7,
                                height=int(screen_height/3), width=int(screen_width/5), anchor=CENTER)
            stockTAB_btn.place(relx=0.8, rely=0.7,
                               height=int(screen_height/3), width=int(screen_width/5), anchor=CENTER)

            # Re-scaling the Tab-Button's labels to original size
            inVoiceTAB_btnLabel.place(relx=0.5, rely=0.7,
                                      width=int(screen_width/5), anchor=CENTER)
            clientTAB_btnLabel.place(relx=0.5, rely=0.72,
                                     width=int(screen_width/5.3), anchor=CENTER)
            stockTAB_btnLabel.place(relx=0.5, rely=0.72,
                                    width=int(screen_width/5.3), anchor=CENTER)

    # >>

    # Function which creates the SignIn Panel and also creates the Button to create SignUp Panel
    def signInPanel():

        # Function which is operated by the SignIn Panel's Close-Button to close the SignIn-Window and its Widgets
        def closeSignInPanel():

            # Clearing the fade-out on all the Buttons in the Main Panel
            signIn_btn_style.configure("SignInAbout.TButton",
                                       background="#BF09D5", borderwidth=2)
            inVoiceTAB_btn.configure(style="TAB.TButton")
            clientTAB_btn.configure(style="TAB.TButton")
            stockTAB_btn.configure(style="TAB.TButton")
            ##
            inVoiceTAB_btnLabel.configure(style="TAB.TLabel")
            clientTAB_btnLabel.configure(style="TAB.TLabel")
            stockTAB_btnLabel.configure(style="TAB.TLabel")

            # Closing the SignIn-Window along with its widgets
            root.after(100, lambda: sign_In.destroy())

            # Re-focusing the root-Window again
            root.grab_set()
            root.focus_set()

        # >>

        # Function which is operated by the SignIn Panel's SignUp-Button to create the SignUp Panel
        def signUpPanel():

            # Function which is operated by the SignUp Panel's Close-Button to close the SignUp-Window and its Widgets
            def closeSignUpPanel():

                # Destroying all the child widgets created in the SignUp-Window
                for child in sign_Up.winfo_children():

                    child.destroy()

                # Closing the SignUp-Window along with its widgets
                root.after(100, lambda: sign_Up.destroy())

                # Showing the SignIn-Window again
                sign_In.deiconify()

                # Re-focusing the root-Window and SignIn-Window again
                root.grab_set()
                root.focus_set()
                sign_In.grab_set()
                sign_In.focus_set()

            # >>

            # Function for validating the Entries in the SignUp Panel
            def entry_Validator(entryW, signUp_var):

                # Checking if the value got is from FirstName Entry
                if (str(signUp_var) == "firstName"):

                    # Creating a label to show invalid-INFO about FirstName Entry
                    invalid_info = Label(sign_Up, text="(minimum 3 letters starts with Uppercase)",
                                         background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
                    invalid_info.place(relx=0.3, rely=0.15, anchor=CENTER)

                    # Confirming the input is alphabet
                    if (not signUp_var.get().isalpha()):

                        # Marking around the Entry in red if input is not a alphabet
                        entryW.configure(highlightbackground=error_fG,
                                         highlightcolor=error_fG)

                    # Confirming the input starts with UpperCase and has minimum 3 letters
                    elif (signUp_var.get()[0].isupper() and len(signUp_var.get()) > 2):

                        # Re-Marking and Hiding the invalid-INFO
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)
                        invalid_info.configure(foreground=signIn_bG)

                    else:

                        # Re-Marking the Entry to normal
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)

                        # Showing invalid-INFO if input doesn't either starts with UpperCase and has minimum 3 letters
                        invalid_info.configure(foreground=error_fG)

                # Checking if the value got is from LastName Entry
                if (str(signUp_var) == "lastName"):

                    # Creating a label to show invalid-INFO about LastName Entry
                    invalid_info = Label(sign_Up, text="(atleast 1 character preferred Uppercase)",
                                         background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
                    invalid_info.place(relx=0.87, rely=0.15, anchor=CENTER)

                    # Confirming the FirstName Entry is filled
                    if (signUp_firstName_var.get().isalpha() and signUp_firstName_var.get()[0].isupper() and len(signUp_firstName_var.get()) > 2):

                        # Removing red color Highlighting from the LastName Entry
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)

                        # Confirming the input is alphabet
                        if (not signUp_var.get().isalpha()):

                            # Marking around the Entry in red if input is not a alphabet
                            entryW.configure(highlightbackground=error_fG,
                                             highlightcolor=error_fG)

                        # Confirming the input starts with UpperCase
                        elif (signUp_var.get().isalpha() and signUp_var.get()[0].isupper()):

                            # Removing red color Highlighting from the LastName Entry and also Hiding the invalid-INFO
                            entryW.configure(highlightbackground=signIn_bG,
                                             highlightcolor=focus_color)
                            invalid_info.configure(foreground=signIn_bG)
                        else:

                            # Showing invalid-INFO if input is not a alphabet
                            invalid_info.configure(foreground=error_fG)
                    else:

                        # Highlighting the FirstName and LastName Entries in red
                        signUp_firstName.configure(highlightbackground=error_fG,
                                                   highlightcolor=error_fG)
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=error_fG)

                        # Setting the LastName Entry value to nothing
                        signUp_var.set("")

                # Checking if the value got is from Email Entry
                if (str(signUp_var) == "email"):

                    # Creating a label to show invalid-INFO about Email Entry
                    invalid_info = Label(sign_Up, text="(like this: invoice123@gmail.com)",
                                         background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
                    invalid_info.place(relx=0.235, rely=0.3, anchor=CENTER)

                    # Confirming the LastName Entry is filled
                    if (signUp_lastName_var.get().isalpha() and signUp_lastName_var.get()[0].isupper()):

                        # Removing red color Highlighting from the Email Entry
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)

                        # Confirming the input is in LowerCase
                        if (not signUp_var.get().islower()):

                            # Marking around the Entry in red if input is not LowerCase
                            entryW.configure(highlightbackground=error_fG,
                                             highlightcolor=error_fG)

                        # Confirming the input has atleast one symbol
                        elif (signUp_var.get().isidentifier()):

                            # Marking around the Entry in red if input doesn't have a symbol
                            entryW.configure(highlightbackground=error_fG,
                                             highlightcolor=error_fG)
                            invalid_info.configure(foreground=error_fG)

                        elif (len(signUp_var.get()) < 15):

                            # Showing invalid-INFO if input is less than 15
                            invalid_info.configure(foreground=error_fG)
                    else:

                        # Highlighting the LastName and Email Entries in red
                        signUp_lastName.configure(highlightbackground=error_fG,
                                                  highlightcolor=error_fG)
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=error_fG)

                        # Setting the Email Entry value to nothing
                        signUp_var.set("")

                # Checking if the value got is from MobileNumber Entry
                if (str(signUp_var) == "mobileNumber"):

                    # Creating a label to show invalid-INFO about MobileNumber Entry
                    invalid_info = Label(sign_Up, text="(should be a 10 digit number)",
                                         background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
                    invalid_info.place(relx=0.8, rely=0.3, anchor=CENTER)

                    # Confirming the Email Entry is filled
                    if (signUp_email_var.get().islower() and (not signUp_email_var.get().isidentifier()) and len(signUp_email_var.get()) > 14):

                        # Removing red color Highlighting from the MobileNumber Entry
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)

                        # Confirming the input is a Integer
                        if (not signUp_var.get().isdigit()):

                            # Marking around the Entry in red if input is not a Integer
                            entryW.configure(highlightbackground=error_fG,
                                             highlightcolor=error_fG)

                            # Setting the MobileNumber Entry value to nothing
                            signUp_var.set("")

                        elif (len(signUp_var.get()) > 10):

                            # Showing invalid-INFO and also Re-setting the MobileNumber Entry value if input is greater than 10
                            invalid_info.configure(foreground=error_fG)
                            signUp_var.set(signUp_var.get()[-1])

                        elif (len(signUp_var.get()) < 10):

                            # Showing invalid-INFO if input is less than 10
                            invalid_info.configure(foreground=error_fG)
                    else:

                        # Highlighting the Email and MobileNumber Entries in red
                        signUp_email.configure(highlightbackground=error_fG,
                                               highlightcolor=error_fG)
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=error_fG)

                        # Setting the MobileNumber Entry value to nothing
                        signUp_var.set("")

                # Checking if the value got is from UserId Entry
                if (str(signUp_var) == "userId"):

                    # Hiding the error label beside UserId
                    errorLabel1.configure(foreground=signIn_bG)

                    # Creating a label to show invalid-INFO about UserId Entry
                    invalid_info = Label(sign_Up, text="(combination of both alphabets & numbers (10-20))",
                                         background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
                    invalid_info.place(relx=0.46, rely=0.6, anchor=CENTER)

                    # Confirming the MobileNumber Entry is filled
                    if (signUp_mobileNumber_var.get().isdigit() and len(signUp_mobileNumber_var.get()) == 10):

                        # Removing red color Highlighting from the UserId Entry
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)

                        # Confirming the input is combination of both alphabets and numbers
                        if (signUp_var.get().isalpha() and signUp_var.get().isdigit()):

                            # Marking around the Entry in red if input is not combination of both alphabets and numbers
                            entryW.configure(highlightbackground=error_fG,
                                             highlightcolor=error_fG)

                        elif (len(signUp_var.get()) > 20):

                            # Showing invalid-INFO and also Re-setting the UserId Entry if input is greater than 20
                            invalid_info.configure(foreground=error_fG)
                            signUp_var.set("")

                        elif (len(signUp_var.get()) < 10):

                            # Showing invalid-INFO if input is lesser than 10
                            invalid_info.configure(foreground=error_fG)
                    else:

                        # Highlighting the MobileNumber and UserId Entries in red
                        signUp_mobileNumber.configure(highlightbackground=error_fG,
                                                      highlightcolor=error_fG)
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=error_fG)

                        # Setting the UserId Entry value to nothing
                        signUp_var.set("")

                # Checking if the value got is from Password Entry
                if (str(signUp_var) == "password"):

                    # Hiding the error label beside Password and also resetting the Confirm-Password Entry
                    errorLabel2.configure(foreground=signIn_bG)
                    signUp_pwdC_var.set(
                        "") if (signUp_pwdC_var.get() != "") else ""

                    # Creating a label to show invalid-INFO about Password Entry
                    invalid_info = Label(sign_Up, text="(contains atleast 8 characters)",
                                         background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
                    invalid_info.place(relx=0.5, rely=0.7, anchor=CENTER)

                    # Confirming the Personal details Entries are filled
                    if (signUp_firstName_var.get() == "" or signUp_lastName_var.get() == "" or signUp_email_var.get() == "" or signUp_mobileNumber_var.get() == ""):

                        # Showing the error label beside UserId and preventing from typing
                        errorLabel1.configure(
                            text="# Fill your personel details first", foreground=error_fG)
                        signUp_var.set("")

                    else:

                        # Confirming the UserId Entry is filled
                        if (not signUp_userID_var.get().isalpha() and not signUp_userID_var.get().isdigit() and (len(signUp_userID_var.get()) >= 10 and len(signUp_userID_var.get()) <= 20)):

                            # Hiding the error label beside UserId
                            errorLabel1.configure(foreground=signIn_bG)

                            # Removing red color Highlighting from the Password Entry
                            entryW.configure(highlightbackground=signIn_bG,
                                             highlightcolor=focus_color)

                            # Confirming the input is greater than the minimum length
                            if (len(signUp_var.get()) < 8):

                                # Marking around the Entry in red if input is less than minimum length
                                entryW.configure(highlightbackground=error_fG,
                                                 highlightcolor=error_fG)

                                # Showing invalid-INFO if input is lesser than minimum length
                                invalid_info.configure(foreground=error_fG)
                        else:

                            # Showing the error label beside UserId
                            errorLabel1.configure(
                                text="# Create your userId", foreground=error_fG)

                            # Highlighting the UserId and Password Entries in red
                            signUp_userID.configure(highlightbackground=error_fG,
                                                    highlightcolor=error_fG)
                            entryW.configure(highlightbackground=signIn_bG,
                                             highlightcolor=error_fG)

                            # Setting the Password Entry value to nothing
                            signUp_var.set("")

                # Checking if the value got is from Confirm-Password Entry
                if (str(signUp_var) == "confirmPassword"):

                    # Confirming the Personal details Entries are filled
                    if (signUp_firstName_var.get() == "" or signUp_lastName_var.get() == "" or signUp_email_var.get() == "" or signUp_mobileNumber_var.get() == ""):

                        # Showing the error label beside UserId and preventing from typing
                        errorLabel1.configure(
                            text="# Fill your personel details first", foreground=error_fG)
                        signUp_var.set("")

                    # Confirming the UserId Entry is filled
                    elif (not signUp_userID_var.get().isalpha() and not signUp_userID_var.get().isdigit() and (len(signUp_userID_var.get()) >= 10 and len(signUp_userID_var.get()) <= 20)):

                        # Hiding the error label beside UserId
                        errorLabel1.configure(foreground=signIn_bG)

                        # Removing red color Highlighting from the Confirm-Password Entry
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=focus_color)

                        # Checking the values of both Password Entries is matched
                        if (len(signUp_pwd_var.get()) >= 8 and signUp_pwd_var.get() == signUp_var.get()):

                            # Hiding the error label beside Password and making it a matched label
                            errorLabel2.configure(
                                text="# password matched", foreground="#38B000")

                            # Enabling the Generate-Key Button to generate random key
                            generateKey_btn.configure(
                                cursor="hand2", state=NORMAL)

                        # Confirming the Password Entry is filled
                        elif (len(signUp_pwd_var.get()) < 8):

                            # Showing the error label beside Password and preventing from typing
                            errorLabel2.configure(
                                text="# Create a password to proceed", foreground=error_fG)
                            signUp_var.set("")

                        else:

                            # Showing the error label beside Password
                            errorLabel2.configure(
                                text="# password don't match", foreground=error_fG)
                    else:

                        # Showing the error label beside UserId
                        errorLabel1.configure(
                            text="# Create your userId", foreground=error_fG)

                        # Highlighting the UserId and Confirm-Password Entries in red
                        signUp_userID.configure(highlightbackground=error_fG,
                                                highlightcolor=error_fG)
                        entryW.configure(highlightbackground=signIn_bG,
                                         highlightcolor=error_fG)

                        # Setting the Confirm-Password Entry value to nothing
                        signUp_var.set("")

            # >>

            # Function for adding hypen (-) automatically to the Key Entry while entering values
            def keyValidator(key_Entry, key_Var):

                # Function for deleting the entire key with a single mouse left click button
                def deleteAllEntry(event):

                    # Deleting the key in entry widget and also unbinding the click event assigned to it
                    key_Entry.delete(0, END)
                    key_Entry.unbind("<Button-1>", clickToDELETE)

                # >>

                # Adding hypen for every third character
                if (len(key_Var.get()) == 3):
                    key_Entry.insert(END, "-")

                elif (len(key_Var.get()) == 7):
                    key_Entry.insert(END, "-")

                elif (len(key_Var.get()) == 11):
                    key_Entry.insert(END, "-")

                elif (len(key_Var.get()) == 13):

                    # Changing focus to SignUp-Window
                    sign_Up.focus_set()

                    # Assigning a delete function to mouse left click
                    clickToDELETE = key_Entry.bind("<Button-1>",
                                                   deleteAllEntry)

            # >>

            # Function to show/hide SignUp Panel's Generate-Key Button INFO while mouse-hovering
            def generateKey_INFO(event):

                # Function for changing the destroyer timer for Generated Key and also destroys the Generated Key after timers ends
                def keyDestroyer(timing, timerTime, gereratedkey, keyLabels):

                    # Decreasing the Timer time in seconds
                    timing -= 1

                    # Updating the time in the Destroyer Timer
                    timerTime.configure(
                        text="Valid for\n"+str(timing)+"s")

                    # Checking if the time not reaches to zero
                    if (timing != 0):

                        # Calling the function to reduce the timer to destroy the Generated Key
                        root.after(1000, lambda: keyDestroyer(
                            timing, timerTime, gereratedkey, [keyLabels[1], keyLabels[2], keyLabels[0]]))

                    else:

                        # Destroying the Timer and the Generated key when the Timer reaches zero
                        timerTime.destroy()
                        keyLabels[1].destroy()
                        keyLabels[2].destroy()

                        # Disabling the entry for typing Key again
                        signUp_key.configure(state=DISABLED)

                        # Enabling the Create button if the Generated Key and Entered Key matches
                        if (signUp_key_var.get() == gereratedkey):

                            # Enabling the Create-Account Button and destroying the Hint for Key Entry
                            createAccount_btn.configure(
                                cursor="hand2", state=NORMAL)
                            root.after(1000, lambda: keyLabels[0].destroy())

                            # Creating a label to show CreateAccount Button's INFO
                            global createBtn_info
                            createBtn_info = Label(sign_Up, text="# Click 'Create' to create your account",
                                                   font=("Dodge", 12, "bold"), background=signIn_bG, foreground="#38B000")
                            createBtn_info.place(
                                relx=0.8, rely=0.85, anchor=CENTER)

                            # Assigning the same function of Create-Account Button to <Enter> key
                            global ENTERtoCreateAccount
                            ENTERtoCreateAccount = sign_Up.bind(
                                "<Return>", lambda *_: createNewAccount())

                        else:

                            # Resetting both the Password Entries if the Generated Key and Entered Key doesn't match
                            signUp_pwd_var.set("")
                            signUp_pwdC_var.set("")

                            # Showing Error-INFO on the Key Entry's Hint
                            keyLabels[0].configure(
                                text="Sorry! key doesn't match try again", foreground=error_fG)
                            root.after(5000, lambda: keyLabels[0].destroy())

                            # Enabling all entries in the SignUp Panel
                            signUp_firstName.configure(state=NORMAL)
                            signUp_lastName.configure(state=NORMAL)
                            signUp_email.configure(state=NORMAL)
                            signUp_mobileNumber.configure(state=NORMAL)
                            signUp_userID.configure(state=NORMAL)
                            signUp_pwd.configure(state=NORMAL)
                            signUp_pwdC.configure(state=NORMAL)

                # >>

                # Function for generating a random key only if the UserId is unique
                def keyGenerate():

                    # Disabling the Generate-Key Button after clicked, for preventing the function to be called twice
                    generateKey_btn.configure(cursor="arrow", state=DISABLED)

                    # Opening the --- `(in Voice)` --- Database
                    appDB = UserCredential()

                    # Querying the 'userCredentials' table in --- `(in Voice)` --- main database and picking the matched record
                    existingUser = appDB.getUser(signUp_userID_var.get())

                    # Closing the connection with the Database
                    appDB.closeDB()

                    if (existingUser is None):

                        # Enabling the entry for typing key and hiding the matched label
                        signUp_key.configure(state=NORMAL)
                        errorLabel2.configure(foreground=signIn_bG)

                        # Disabling all entries in the SignUp Panel except the Entry for Key
                        signUp_firstName.configure(state=DISABLED)
                        signUp_lastName.configure(state=DISABLED)
                        signUp_email.configure(state=DISABLED)
                        signUp_mobileNumber.configure(state=DISABLED)
                        signUp_userID.configure(state=DISABLED)
                        signUp_pwd.configure(state=DISABLED)
                        signUp_pwdC.configure(state=DISABLED)

                        # Generating the random key with combination of numbers and letters
                        key = ""
                        for i in range(3):
                            key += str(random.choice(string.ascii_uppercase))+str(random.choice(
                                string.digits))+str(random.choice(string.ascii_uppercase))+"-"

                        key = key+str(random.choice(string.ascii_letters))

                        # Creating a label for showing Hint for Key Entry
                        keyHint = Label(sign_Up, text="Hint: type key without hyphen",
                                        font=("Dodge", 10), background=signIn_bG, foreground="#22333B")
                        keyHint.place(relx=0.2, rely=0.97, anchor=CENTER)

                        # Creating a label to show INFO for the generated key
                        key_info = Label(sign_Up, text="This is your KEY !",
                                         font=("Dodge", 14), background=signIn_bG, foreground="#4C1036")
                        key_info.place(relx=0.8, rely=0.6, anchor=CENTER)

                        # Creating a label for showing the generated key
                        randomKey = Label(sign_Up, text=key, font=("Dodge", 13, "bold"),
                                          background=signIn_bG, foreground="#38B000")
                        randomKey.place(relx=0.8, rely=0.68, anchor=CENTER)

                        # Setting the initial value for Countdown Timer
                        timeInSec = 31

                        # Creating a label to show the timer for key to disappear
                        changesTimer = Label(sign_Up, text="Valid for\n"+str(timeInSec)+"s",
                                             font=("Dodge", 12, "bold"), background=signIn_bG, foreground="#000040", justify=CENTER)
                        changesTimer.place(relx=0.55, rely=0.9)

                        # Calling the function to start the timer to destroy the Generated Key
                        keyDestroyer(timeInSec, changesTimer, key,
                                     [keyHint, key_info, randomKey])

                    else:
                        # Creating a label to show invalid-INFO about UserId
                        invalid_username = Label(sign_Up, text="# userid exists",
                                                 font=("Dodge", 12, "bold"), background=signIn_bG, foreground=error_fG)
                        invalid_username.place(relx=0.72, rely=0.55,
                                               anchor=CENTER)

                        # Destroying the invalid-INFO about UserId
                        root.after(1500, lambda: invalid_username.destroy())

                        # Resetting both the Password Entries
                        signUp_pwd_var.set("")
                        signUp_pwdC_var.set("")

                # >>

                # Making the SignUp Panel's Generate-Key Button INFO a global variable so it can be accessed everywhere
                global generateKey_btn_INFO

                # Getting the type of the event by id_number
                event_ID = int(getattr(event, "__dict__")["type"])

                # Checking if the Event is <Enter>
                if (event_ID == 7):

                    # Assigning a function to Generate-Key Button
                    event.widget.configure(command=lambda: keyGenerate())

                    # Creating a label to show INFO about Generate-Key Button
                    generateKey_btn_INFO = Label(sign_Up, text="Generate key",
                                                 font=("Dodge", 10, "bold"), background=signIn_bG, foreground="#360015")
                    generateKey_btn_INFO.place(relx=0.55, rely=0.85,
                                               anchor=CENTER)

                # Checking if the Event is <Leave>
                elif (event_ID == 8):

                    # Destroying the SignUp Panel's Generate-Key Button INFO when mouseevent is <Leave>
                    generateKey_btn_INFO.destroy()

            # >>

            # Function which operated by the CreateAccount Button in the SignUp Panel to create mew account with a confirmation message
            def createNewAccount():

                # Function which Sets up the Database for the New User with some default(predefined) data populated tables
                def setting_userDB(details):

                    # Starting the loop by assigning new values to the variables
                    status, object = "Create", UserDetail

                    while(status != "Completed"):

                        # Creating new table and Database for the New User
                        userDB = object(details[0])

                        if (status == "Create"):

                            # Creating a new account with details provided by User
                            userDB.create(
                                details[0],
                                details[1],
                                details[2],
                                details[3]
                            )

                            # Changing the values of the variables
                            status, object = "Preference", UserPreference

                        elif (status == "Preference"):

                            # Creating a new table for holding the User Preferences for --- `(in Voice)` ---
                            userDB.createDefault()

                            # Changing the values of the variables
                            status, object = "Currency", CurrencyRate

                        elif (status == "Currency"):

                            # Creating a new table for holding the Currency Exchange Rate of Specific Countries
                            userDB.update("create")

                            # Changing the values of the variables
                            status, object = "DueDate", DueDate

                        elif (status == "DueDate"):

                            # Creating a new table for holding the default values for Due Dates
                            userDB.add()

                            # Changing the values of the variables
                            status, object = "Completed", None

                        # Commiting and Closing the connection with the Database
                        userDB.closeDB()

                # >>

                # Disabling the CreateAccount Button after clicked, for preventing the function to be called twice
                createAccount_btn.configure(cursor="arrow", state=DISABLED)

                # Removing the <Enter> key to Create Account
                sign_Up.unbind("<Return>", ENTERtoCreateAccount)

                # Showing a confirmation dialogbox with some message
                confimation_msg = messagebox.askyesno(title="Create Account",
                                                      message="Are you sure, you want to create a account with the details you provided?", parent=sign_Up)

                # Destroying CreateAccount Button's INFO
                createBtn_info.destroy()

                # If clicked 'yes' creates a new account with details provided
                if (confimation_msg == True):

                    # Creating a label to show SignUp-Window's closing INFO
                    closing_INFO = Label(sign_Up, text="Window will close in few seconds...", font=("Dodge", 10, "bold"),
                                         background=signIn_bG, foreground="#E75E76")
                    root.after(300,
                               lambda: closing_INFO.place(relx=0.985, rely=0.03, anchor=NE))

                    # Destroying the Exit Button in the SignUp-Window to prevent any errors while working with Database
                    root.after(200, lambda: exit_btn2.destroy())

                    # Opening the --- `(in Voice)` --- Database
                    appDB = UserCredential()

                    # Creating a new account with details provided
                    appDB.createUser(
                        signUp_firstName_var.get(),
                        signUp_lastName_var.get(),
                        signUp_email_var.get(),
                        signUp_mobileNumber_var.get(),
                        signUp_userID_var.get(),
                        signUp_pwd_var.get()
                    )

                    # Commiting and Closing the connection with the Database
                    appDB.closeDB()

                    # Showing a message box with information of account has created
                    accountCreated_msg = messagebox.showinfo(title="Create Account",
                                                             message=f"Your account has been created as \r\n\nUserID :  {signUp_userID_var.get()}", parent=sign_Up)

                    if (accountCreated_msg == "ok"):

                        # -------------- Setting Up the Database for the New User ----------------
                        setting_userDB([
                            signUp_userID_var.get(),
                            signUp_email_var.get(),
                            signUp_firstName_var.get(),
                            signUp_lastName_var.get()
                        ])

                        # Resetting all the entry fields in the SignUp Panel
                        signUp_firstName_var.set(""),
                        signUp_lastName_var.set(""),
                        signUp_email_var.set(""),
                        signUp_mobileNumber_var.set(""),
                        signUp_userID_var.set(""),
                        signUp_pwd_var.set(""),

                        # Closing the SignUp-Window
                        closeSignUpPanel()

                elif (confimation_msg == False):

                    # Resetting both the Password Entries
                    signUp_pwd_var.set("")
                    signUp_pwdC_var.set("")

                    # Enabling all entries in the SignUp Panel
                    signUp_firstName.configure(state=NORMAL)
                    signUp_lastName.configure(state=NORMAL)
                    signUp_email.configure(state=NORMAL)
                    signUp_mobileNumber.configure(state=NORMAL)
                    signUp_userID.configure(state=NORMAL)
                    signUp_pwd.configure(state=NORMAL)
                    signUp_pwdC.configure(state=NORMAL)

            # >>

            # ------------------------------------- `(in Voice)` SignUp Panel -StyleStarts----------------------------------------------------

            # Hiding the SignIn-Window
            sign_In.withdraw()

            #         ------------------------------------------------
            # -------------------- `(in Voice)` SignUp Panel ---------------------
            #         ------------------------------------------------

            # Creating a new window as SignUp-Window for placing the SignUp Panel widgets and also removing the default toolbar provided by OS
            sign_Up = Toplevel(root, background=signIn_bG,
                               highlightcolor="#E3DBDB", highlightthickness=2)
            sign_Up.overrideredirect(True)

            # Calculating the width and height of the SignUp-Window by using the users fullscreen resolution
            signup_window_width = int(screen_width/1.5)
            signup_window_height = int(screen_height/1.15)

            # Calculating the X, Y coordinates for placing the SignUp-Window to the center of the screen from every axis
            signup_x_cordinate = int(
                (screen_width/2) - (signup_window_width/2))
            signup_y_cordinate = int(
                (screen_height/2) - (signup_window_height/2))

            # Setting the width, height and positioning the SignUp-Window using the calculated X, Y coordinates
            sign_Up.geometry("%dx%d+%d+%d" % (signup_window_width,
                                              signup_window_height, signup_x_cordinate, signup_y_cordinate))

            # Setting the custom Logo for SignUp-Window using iconphoto() method
            sign_Up.iconphoto(False, PhotoImage(file=path_to_logo))

            # Making the SignUp-Window focused
            sign_Up.grab_set()
            sign_Up.focus_set()

            # Creating a Exit Button for closing the SignUp-Window
            exit_btn2 = Button(sign_Up, text="X", style="Exit_X.TButton",
                               command=lambda: closeSignUpPanel())
            exit_btn2.place(relx=1, rely=0.01,
                            width=int(screen_width/30), anchor=NE)

            # Creating all the Entries for the SignUp Panel -----------------------------------

            # Assigning the common colors for Focused Entry and for invalid-INFO
            focus_color = "#4C1036"
            error_fG = "#EF233C"

            # FirstName Entry
            signUp_firstName_var = StringVar(sign_Up, name="firstName")
            signUp_firstName = tk.Entry(sign_Up, textvariable=signUp_firstName_var,
                                        font=("Dodge", 14, "bold"), highlightthickness=1, highlightcolor=focus_color, justify=RIGHT)
            signUp_firstName.place(relx=0.22, rely=0.22,
                                   height=int(screen_height/20), width=int(screen_width/4), anchor=CENTER)

            # Assigning a function to validate the value entered in the FirstName Entry must only be alphabets
            signUp_firstName_var.trace_add("write",
                                           lambda *_, entry=signUp_firstName, var=signUp_firstName_var: entry_Validator(entryW=entry, signUp_var=var))

            # LastName Entry
            signUp_lastName_var = StringVar(sign_Up, name="lastName")
            signUp_lastName = tk.Entry(sign_Up, textvariable=signUp_lastName_var,
                                       font=("Dodge", 14, "bold"), highlightthickness=1, justify=RIGHT)
            signUp_lastName.place(relx=0.78, rely=0.22,
                                  height=int(screen_height/20), width=int(screen_width/4), anchor=CENTER)

            # Assigning a function to validate the value entered in the LastName Entry must only be alphabets
            signUp_lastName_var.trace_add("write",
                                          lambda *_, entry=signUp_lastName, var=signUp_lastName_var: entry_Validator(entryW=entry, signUp_var=var))

            # Email Entry
            signUp_email_var = StringVar(sign_Up, name="email")
            signUp_email = tk.Entry(sign_Up, textvariable=signUp_email_var,
                                    font=("Dodge", 14, "bold"), highlightthickness=1, justify=RIGHT)
            signUp_email.place(relx=0.22, rely=0.37,
                               height=int(screen_height/20), width=int(screen_width/4), anchor=CENTER)

            # Assigning a function to validate the Email Entry
            signUp_email_var.trace_add("write",
                                       lambda *_, entry=signUp_email, var=signUp_email_var: entry_Validator(entryW=entry, signUp_var=var))

            # MobileNumber Entry
            signUp_mobileNumber_var = StringVar(sign_Up, name="mobileNumber")
            signUp_mobileNumber = tk.Entry(sign_Up, textvariable=signUp_mobileNumber_var,
                                           font=("Dodge", 14, "bold"), highlightthickness=1, justify=RIGHT)
            signUp_mobileNumber.place(relx=0.78, rely=0.37,
                                      height=int(screen_height/20), width=int(screen_width/4), anchor=CENTER)

            # Assigning a function to validate the MobileNumber Entry
            signUp_mobileNumber_var.trace_add("write",
                                              lambda *_, entry=signUp_mobileNumber, var=signUp_mobileNumber_var: entry_Validator(entryW=entry, signUp_var=var))

            # UserId Entry
            signUp_userID_var = StringVar(sign_Up, name="userId")
            signUp_userID = tk.Entry(sign_Up, textvariable=signUp_userID_var,
                                     font=("Dodge", 14, "bold"), highlightthickness=1, justify=RIGHT)
            signUp_userID.place(relx=0.5, rely=0.55,
                                height=int(screen_height/20), width=int(screen_width/6), anchor=CENTER)

            # Assigning a function to validate the UserId Entry
            signUp_userID_var.trace_add("write",
                                        lambda *_, entry=signUp_userID, var=signUp_userID_var: entry_Validator(entryW=entry, signUp_var=var))

            # Password Entry
            signUp_pwd_var = StringVar(sign_Up, name="password")
            signUp_pwd = tk.Entry(sign_Up, textvariable=signUp_pwd_var,
                                  font=("Dodge", 14, "bold"), highlightthickness=1, show="\u25CF", justify=RIGHT)
            signUp_pwd.place(relx=0.5, rely=0.65,
                             height=int(screen_height/20), width=int(screen_width/6), anchor=CENTER)

            # Assigning a function to validate the Password Entry
            signUp_pwd_var.trace_add("write",
                                     lambda *_, entry=signUp_pwd, var=signUp_pwd_var: entry_Validator(entryW=entry, signUp_var=var))

            # Confirm-Password Entry
            signUp_pwdC_var = StringVar(sign_Up, name="confirmPassword")
            signUp_pwdC = tk.Entry(sign_Up, textvariable=signUp_pwdC_var,
                                   font=("Dodge", 14, "bold"), highlightthickness=1, show="\u25CF", justify=RIGHT)
            signUp_pwdC.place(relx=0.5, rely=0.75,
                              height=int(screen_height/20), width=int(screen_width/6), anchor=CENTER)

            # Assigning a function to validate the Confirm-Password Entry
            signUp_pwdC_var.trace_add("write",
                                      lambda *_, entry=signUp_pwdC, var=signUp_pwdC_var: entry_Validator(entryW=entry, signUp_var=var))

            # Key Entry
            signUp_key_var = StringVar()
            signUp_key = tk.Entry(sign_Up, textvariable=signUp_key_var,
                                  font=("Dodge", 14, "bold"), highlightthickness=1, state=DISABLED, justify=RIGHT)
            signUp_key.place(relx=0.25, rely=0.92,
                             height=int(screen_height/20), width=int(screen_width/4), anchor=CENTER)

            # Assigning a function to adding hyphen between characters in the Key Entry
            signUp_key_var.trace_add("write",
                                     lambda *_, keyE=signUp_key, keyV=signUp_key_var: keyValidator(key_Entry=keyE, key_Var=keyV))

            # -----------------------------------------------------------------------

            # Creating all the labels for the Entries in the SignUp Panel -----------------------------------

            # SignUp Title label
            signUp_title = Label(sign_Up, text="Create Account", font=("Dodge", 21, "bold"),
                                 background=signIn_bG, foreground=signIn_fG)
            signUp_title.place(relx=0.5, rely=0.06, anchor=CENTER)

            # FirstName label
            signUp_firstName_L = Label(sign_Up, text="First Name", font=("Dodge", 12, "bold"),
                                       background=signIn_bG, foreground=signIn_fG)
            signUp_firstName_L.place(relx=0.1, rely=0.15, anchor=CENTER)

            # LastName label
            signUp_lastName_L = Label(sign_Up, text="Last Name", font=("Dodge", 12, "bold"),
                                      background=signIn_bG, foreground=signIn_fG)
            signUp_lastName_L.place(relx=0.65, rely=0.15, anchor=CENTER)

            # Email label
            signUp_email_L = Label(sign_Up, text="Email", font=("Dodge", 12, "bold"),
                                   background=signIn_bG, foreground=signIn_fG)
            signUp_email_L.place(relx=0.07, rely=0.3, anchor=CENTER)

            # MobileNumber label
            signUp_mobileNumber_L = Label(sign_Up, text="Mobile No.", font=("Dodge", 12, "bold"),
                                          background=signIn_bG, foreground=signIn_fG)
            signUp_mobileNumber_L.place(relx=0.65, rely=0.3, anchor=CENTER)

            # Dot-Separator label
            separator = 0.05
            while (separator < 0.98):

                # Creating a label with dots and positioning it on the SignUp Panel
                signUp_separater = Label(sign_Up, text="- -- -", font=("Dodge", 12),
                                         background=signIn_bG, foreground=signIn_fG)
                signUp_separater.place(relx=separator, rely=0.45,
                                       anchor=CENTER)

                # Increasing the X axis value
                separator += 0.05

            # UserId label
            signUp_userID_L = Label(sign_Up, text="User Id", font=("Dodge", 12, "bold"),
                                    background=signIn_bG, foreground=signIn_fG)
            signUp_userID_L.place(relx=0.3, rely=0.55, anchor=CENTER)

            # Password label
            signUp_pwd_L = Label(sign_Up, text="Password", font=("Dodge", 12, "bold"),
                                 background=signIn_bG, foreground=signIn_fG)
            signUp_pwd_L.place(relx=0.3, rely=0.65, anchor=CENTER)

            # Confirm-Password label
            signUp_pwdC_L = Label(sign_Up, text="Confirm-Password", font=("Dodge", 12, "bold"),
                                  background=signIn_bG, foreground=signIn_fG)
            signUp_pwdC_L.place(relx=0.26, rely=0.75, anchor=CENTER)

            # Key label
            signUp_key_L = Label(sign_Up, text="Key", font=("Dodge", 12, "bold"),
                                 background=signIn_bG, foreground=signIn_fG)
            signUp_key_L.place(relx=0.1, rely=0.85, anchor=CENTER)

            # Error labels
            errorLabel1 = Label(sign_Up, text="# Fill your personel details first",
                                font=("Dodge", 10, "bold"), background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
            errorLabel1.place(relx=0.75, rely=0.55, anchor=CENTER)

            errorLabel2 = Label(sign_Up, text="# Create your password to proceed",
                                font=("Dodge", 10, "bold"), background=signIn_bG, foreground=signIn_bG, justify=RIGHT)
            errorLabel2.place(relx=0.75, rely=0.75, anchor=CENTER)

            # -----------------------------------------------------------------------

            # Resizing the -- Generate Key -- image and converting it into a object to display on a widget
            global generateKey_obj
            generateKey_obj = ImageTk.PhotoImage(key_icon.resize((40, 40),
                                                                 resampling_filter))

            # Creating Show-Password Button to show/hide the password in the SignUp Panel
            showPwd_btn = Button(sign_Up, image=showHide_obj, style="Pwd_&_Key.TButton",
                                 cursor="hand2", command=lambda: showPassword("Hidden", showPwd_btn, signUp_pwd, signUp_pwdC))
            showPwd_btn.place(relx=0.65, rely=0.65, anchor=CENTER)

            # Creating a Generate-Key Button to generate random key like a captcha
            generateKey_btn = Button(sign_Up, image=generateKey_obj, style="Pwd_&_Key.TButton",
                                     state=DISABLED)
            generateKey_btn.place(relx=0.5, rely=0.92, anchor=CENTER)

            # Assigning a function to show/hide Generate-Key Button INFO while hovering
            generateKey_btn.bind("<Enter>", generateKey_INFO)
            generateKey_btn.bind("<Leave>", generateKey_INFO)

            # Styling the Create-Account Button
            createAccount_btn_style = Style(sign_Up)
            createAccount_btn_style.theme_use("default")
            createAccount_btn_style.configure("createAccount.TButton", font=("Dodge", 16, "bold", "italic"),
                                              foreground="#F0EFF4", background="#4C1036", borderwidth=2, highlightthickness=2, focuscolor="none")
            # Mouse Hovering style for Create-Account Button
            createAccount_btn_style.map("createAccount.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                        background=[("active", "#72195A")])

            # Creating a Create-Account Button to create new account with the details entered
            createAccount_btn = Button(sign_Up, text="Create", style="createAccount.TButton",
                                       state=DISABLED, command=lambda: createNewAccount())
            createAccount_btn.place(relx=0.9, rely=0.95, anchor=CENTER)

            # -------------------------------------------------------------------------------------------- `(in Voice)` SignUp Panel -StyleEnds----

        # >>

        # Function to show/hide password entered in the Password Entry
        def showPassword(status, showBtn, passwordE1, passwordE2=None):

            # Showing the Password if status is 'Hidden'
            if (status == "Hidden"):

                # Looking for the Confirm-Password Entry to confirm it is from SignUp-Window
                if (passwordE2 is not None):

                    # Making the Password Entries in SignUp-Window visible
                    passwordE1.configure(show="")
                    passwordE2.configure(show="")

                else:
                    # Making the Password Entry in SignIn-Window visible
                    passwordE1.configure(show="")

                # Changing the status to 'Visible'
                newStatus = "Visible"

            # Hiding the Password if status is 'Visible'
            elif (status == "Visible"):

                # Looking for the Confirm-Password Entry to confirm it is from SignUp-Window
                if (passwordE2 is not None):

                    # Making the Password Entries in SignUp-Window back to hidden
                    passwordE1.configure(show="\u25CF")
                    passwordE2.configure(show="\u25CF")

                else:
                    # Making the Password Entry in SignIn-Window back to hidden
                    passwordE1.configure(show="\u25CF")

                # Changing the status to 'Hidden'
                newStatus = "Hidden"

            # Changing the Show-Password Buttons function to show/hide
            root.after(50, lambda: showBtn.configure(
                command=lambda: showPassword(newStatus, showBtn, passwordE1, passwordE2)))

        # >>

        # Function which is operated by the SignIn Panel's SignIn Button for checking the credentials are valid before sending the login request
        def credentialsValidator(userid_E, password_E):

            # Function to show/hide Log-Out Button while mouse-hovering over the User-Profile Section
            def changelogOutVisiblity(event, frame=None, settings_btn=None):

                # Function which is operated by the Log-Out Button to logout the User and redirecting to `(in Voice)` Home-Screen
                def logOutUser():

                    # Re-Setting the new functions assigned for the Tab-Buttons in the Main Panel to default
                    inVoiceTAB_btn.configure(command=lambda: signInPanel())
                    clientTAB_btn.configure(command=lambda: signInPanel())
                    stockTAB_btn.configure(command=lambda: signInPanel())

                    # Removing the function assigning with all Tab-Button's labels
                    inVoiceTAB_btnLabel.unbind("<Button-1>")
                    clientTAB_btnLabel.unbind("<Button-1>")
                    stockTAB_btnLabel.unbind("<Button-1>")

                    # Assigning new functions with all Tab-Button's labels
                    inVoiceTAB_btnLabel.bind(
                        "<Button-1>", lambda *_: signInPanel())
                    clientTAB_btnLabel.bind(
                        "<Button-1>", lambda *_: signInPanel())
                    stockTAB_btnLabel.bind(
                        "<Button-1>", lambda *_: signInPanel())

                    # Destroying the User's Dashboard and its widgets
                    root.after(800, lambda: settings_btn.destroy())
                    root.after(450, lambda: logOut_btn.destroy())
                    root.after(850, lambda: frame.destroy())

                    # Showing the AboutUs Button again
                    root.after(850, lambda: aboutUs_btn.place(
                        relx=0.1, rely=0.1, anchor=CENTER))

                # >>

                # Making the Log-Out Button a global variable so it can be accessed everywhere
                global logOut_btn

                # Getting the type of the event by id_number
                event_ID = int(getattr(event, "__dict__")["type"])

                # Checking if the Event is <Enter>
                if (event_ID == 7):

                    #     ----------------------------
                    # ---------- Log-Out Button ----------
                    #     ----------------------------

                    # Styling the Log-Out Button
                    logOut_btn_style = Style(home_frame)
                    logOut_btn_style.theme_use("default")
                    logOut_btn_style.configure("Log-Out.TButton", font=("Dodge", 11, "bold", "italic"),
                                               background="#F0EFF4", foreground="#EF233C", width=7, borderwidth=0, highlightthickness=0, focuscolor="none")
                    # Mouse Hovering style for Log-Out Button
                    logOut_btn_style.map("Log-Out.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                         background=[("active", "#E75E76")])

                    # Creating a Log-Out Button to Signout the signIned User
                    logOut_btn = Button(frame, text="log-out", style="Log-Out.TButton",
                                        cursor="hand2", command=lambda: logOutUser())
                    logOut_btn.place(relx=0.9, rely=0.95, anchor=SE)

                # Checking if the Event is <Leave>
                elif (event_ID == 8):

                    # Destroying the Log-Out Button when mouseevent is <Leave>
                    logOut_btn.destroy()

            # >>

            # Function for changing the `(in Voice)` Home-Screen --into--> loggedIn User's Dashboard with their UserId and Profile showing
            def loggingIn(activeUser):

                # Assigning the logged in UserId to a global variable so it can be accessed everywhere
                global loggedInUser
                loggedInUser = activeUser["userId"]

                # ------------------------------------- `(in Voice)` User Dashboard -StyleStarts----------------------------------------------------

                # Assigning new functions for the Tab-Buttons in the Main Panel
                inVoiceTAB_btn.configure(
                    command=lambda: workSpace(inVoiceTAB_btn))
                clientTAB_btn.configure(
                    command=lambda: workSpace(clientTAB_btn))
                stockTAB_btn.configure(
                    command=lambda: workSpace(stockTAB_btn))

                # Removing the function assigning with all Tab-Button's labels
                inVoiceTAB_btnLabel.unbind("<Button-1>")
                clientTAB_btnLabel.unbind("<Button-1>")
                stockTAB_btnLabel.unbind("<Button-1>")

                # Assigning new functions with all Tab-Button's labels
                inVoiceTAB_btnLabel.bind(
                    "<Button-1>", lambda *_: workSpace(inVoiceTAB_btn))
                clientTAB_btnLabel.bind(
                    "<Button-1>", lambda *_: workSpace(clientTAB_btn))
                stockTAB_btnLabel.bind(
                    "<Button-1>", lambda *_: workSpace(stockTAB_btn))

                #     --------------------------------
                # ------------ Settings Button ------------
                #     --------------------------------

                # Styling the Settings Button
                settings_btn_style = Style(home_frame)
                settings_btn_style.theme_use("default")
                settings_btn_style.configure("Settings.TButton", background=main_bG,
                                             borderwidth=0, highlightthickness=0, focuscolor="none")
                # Mouse Hovering style for Settings Button
                settings_btn_style.map("Settings.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                       background=[("active", main_bG)])

                # Resizing the -- Settings -- image and converting it into a object to display on a widget
                global controls_obj
                controls_obj = ImageTk.PhotoImage(controls_icon.resize((65, 65),
                                                                       resampling_filter))

                # Creating a Settings Button
                settings_btn = Button(home_frame, text="Settings", image=controls_obj, style="Settings.TButton",
                                      cursor="hand2", command=lambda: workSpace(settings_btn))  # settingsTab()
                settings_btn.place(relx=0.1, rely=0.1, anchor=CENTER)

                #     --------------------------------
                # ------------ User-Profile Section ------------
                #     --------------------------------

                # Creating a frame for the User-Profile Section
                userProfile_frame = Frame(home_frame, width=int(screen_width/3),
                                          height=int(screen_height/6))
                userProfile_frame.place(relx=0.98, rely=0.02, anchor=NE)

                # Assigning the functions to show/hide Log-Out Button while hovering User-Profile Section
                userProfile_frame.bind("<Enter>", lambda event: changelogOutVisiblity(event,
                                                                                      userProfile_frame, settings_btn))
                userProfile_frame.bind("<Leave>",
                                       lambda event: changelogOutVisiblity(event))

                # Creating a label to set a background color for the User-Profile Section
                userProfile_bgColor = Label(userProfile_frame, background=main_bG,
                                            width=int(screen_width/2.5))
                userProfile_bgColor.place(relx=0.5, rely=0.5,
                                          height=int(screen_height/5), anchor=CENTER)

                # Opening and Resizing the -- User's Profile -- picture and converting it into a object to display on a widget
                global profile_obj1
                profile_obj1 = ImageTk.PhotoImage(
                    (Image.open(activeUser["profile"]).convert("RGBA")).resize((45, 45), resampling_filter))

                # Creating a label to place the User's profile picture on the User-Profile Section
                global home_userProfile
                home_userProfile = Label(userProfile_frame, image=profile_obj1,
                                         background=main_bG)
                home_userProfile.place(relx=0.4, rely=0.5, anchor=CENTER)

                # Creating a label to show the userId on the User-Profile Section
                userId_label = Label(userProfile_frame, text=f"@ {loggedInUser}",
                                     font=("Dodge", 14, "bold"), background=main_bG, foreground="#360015")
                userId_label.place(relx=0.5, rely=0.5, anchor=W)

                # Opening the CurrencyRate Table in the User's Database
                currencyObj = CurrencyRate(loggedInUser)

                # Updating the records in the 'currencyRates' table with new Currency Exchange Rates
                home_frame.after(40, lambda: currencyObj.update())

                # Commiting and Closing the connection with the Database and removing the mouse arrow loading effect
                home_frame.after(80,
                                 lambda: [currencyObj.closeDB(), home_frame.configure(cursor="arrow")])

                # -------------------------------------------------------------------------------------------- `(in Voice)` User Dashboard -StyleEnds----

            # >>

            # Disabling the SignIn Button after clicked, for preventing the function to be called twice
            sign_In_Button.configure(state=DISABLED)

            # Checking if none of the Credential Entries are empty
            if (userid_E.get() == "" or password_E.get() == ""):

                # Showing a error message
                messagebox.showerror(
                    title="Log-In :Error", message="UserId or Password is empty", parent=sign_In)

                # Re-enabling the SignIn Button
                sign_In_Button.configure(state=NORMAL)

            else:

                # Opening the --- `(in Voice)` --- Database
                appDB = UserCredential()

                # Querying the 'userCredentials' table in the --- `(in Voice)` --- main database and picking the matched record
                validUser = appDB.getUser(userid_E.get())

                # Closing the connection with the Database
                appDB.closeDB()

                # Assigning the password from the matched record to variable, if got a matched record
                validPwd = validUser[5] if (validUser is not None) else None

                if (validPwd is None or validPwd != password_E.get()):

                    # Showing a error message when any one of the credential is invalid or doesn't matched to the record in the Database
                    messagebox.showerror(
                        title="Log-In :Error", message="Invalid Credentials", parent=sign_In)

                    # Re-enabling the SignIn Button
                    sign_In_Button.configure(state=NORMAL)

                elif (validPwd is not None and validPwd == password_E.get()):

                    # Closing the SignIn-Window along with its widgets
                    root.after(400, lambda: closeSignInPanel())
                    root.after(300, lambda: aboutUs_btn.place_forget())

                    # Opening the User's Database
                    userObj = UserDetail(validUser[4])

                    # Querying the 'userDetails' table in the User's database and picking the matched record
                    loggingInUser = userObj.get()

                    # Closing the connection with the Database
                    userObj.closeDB()

                    # Making the mouse arrow loading to indicate processing something
                    home_frame.after(400, home_frame.configure(cursor="watch"))

                    # Calling the function to logging in to the --- `(in Voice)` --- as a User
                    root.after(410, lambda: loggingIn(loggingInUser))

        # >>

        # ------------------------------------- `(in Voice)` SignIn Panel -StyleStarts----------------------------------------------------

        # Fading the all Buttons in the Main Panel
        signIn_btn_style.configure("SignInAbout.TButton",
                                   background="#723C70", borderwidth=1)
        inVoiceTAB_btn.configure(style="TAB-Blur.TButton")
        clientTAB_btn.configure(style="TAB-Blur.TButton")
        stockTAB_btn.configure(style="TAB-Blur.TButton")
        ##
        inVoiceTAB_btnLabel.configure(style="TAB-Blur.TLabel")
        clientTAB_btnLabel.configure(style="TAB-Blur.TLabel")
        stockTAB_btnLabel.configure(style="TAB-Blur.TLabel")

        # Assigning the common colors used in SignIn Panel
        signIn_bG = "#EDE8E7"
        signIn_fG = "#0A014F"

        #         ------------------------------------------------
        # -------------------- `(in Voice)` SignIn Panel ---------------------
        #         ------------------------------------------------

        # Creating a new window as SignIn-Window for placing the SignIn Panel widgets and also removing the default toolbar provided by OS
        sign_In = Toplevel(root, background=signIn_bG,
                           highlightcolor="#E3DBDB", highlightthickness=2)
        sign_In.overrideredirect(True)

        # Calculating the width and height of the SignIn-Window by using the users fullscreen resolution
        signin_window_width = int(screen_width/3)
        signin_window_height = int(screen_height/1.2)

        # Calculating the X, Y coordinates for placing the SignIn-Window to the center of the screen from every axis
        signin_x_cordinate = int((screen_width/2) - (signin_window_width/2))
        signin_y_cordinate = int((screen_height/2) - (signin_window_height/2))

        # Setting the width, height and positioning the SignIn-Window using the calculated X, Y coordinates
        sign_In.geometry("%dx%d+%d+%d" % (signin_window_width,
                                          signin_window_height, signin_x_cordinate, signin_y_cordinate))

        # Setting the custom Logo for SignUp-Window using iconphoto() method
        sign_In.iconphoto(False, PhotoImage(file=path_to_logo))

        # Making the SignIn-Window focused
        sign_In.grab_set()
        sign_In.focus_set()

        # Styling the Exit Button
        exit_btn_style = Style(sign_In)
        exit_btn_style.theme_use("default")
        exit_btn_style.configure("Exit_X.TButton", font=("Dodge", 20, "bold"), foreground="#011932",
                                 background=signIn_bG, borderwidth=0, highlightthickness=0, relief=FLAT, focuscolor="none")
        # Mouse Hovering style for Exit Button
        exit_btn_style.map("Exit_X.TButton", foreground=[("active", "!disabled", "#EF233C")],
                           background=[("active", signIn_bG)])

        # Creating a Exit Button for closing the SignIn-Window
        exit_btn1 = Button(sign_In, text="X", style="Exit_X.TButton",
                           command=lambda: closeSignInPanel())
        exit_btn1.place(relx=1, rely=0.01,
                        width=int(screen_width/30), anchor=NE)

        # Resizing the cropped -- logo -- image and converting it into a object to display on a widget
        global logo_C_obj
        logo_C_obj = ImageTk.PhotoImage(cropped_logo.resize((150, 150),
                                                            resampling_filter))

        # Creating a label to display the APP's logo on the SignIn Panel
        signIn_logo_L = Label(sign_In, image=logo_C_obj,
                              background=signIn_bG)
        signIn_logo_L.place(relx=0.5, rely=0.2, anchor=CENTER)

        # Creating all the Entries for the SignIn Panel -----------------------

        # UserId Entry
        signIn_userID_var = StringVar()
        signIn_userID = Entry(sign_In, textvariable=signIn_userID_var,
                              font=("Dodge", 14, "bold"), justify=RIGHT)
        signIn_userID.place(relx=0.5, rely=0.45, height=int(screen_height/20),
                            width=int(screen_width/5), anchor=CENTER)

        # Password Entry
        signIn_pwd_var = StringVar()
        signIn_pwd = Entry(sign_In, textvariable=signIn_pwd_var,
                           font=("Dodge", 14, "bold"), show="\u25CF", justify=RIGHT)
        signIn_pwd.place(relx=0.5, rely=0.6, height=int(screen_height/20),
                         width=int(screen_width/5), anchor=CENTER)

        #     --------------------------------
        # --------- Show-Password Button ---------
        #     --------------------------------

        # Styling the Show-Password Button
        showPwd_style = Style(sign_In)
        showPwd_style.theme_use("default")
        showPwd_style.configure("Pwd_&_Key.TButton", background=signIn_bG,
                                borderwidth=0, hightlightthickness=0, relief=FLAT, focuscolor="none")
        # Mouse Hovering style for Show-Password Button
        showPwd_style.map("Pwd_&_Key.TButton", foreground=[("active", "!disabled", "#4C1036")],
                          background=[("active", signIn_bG)])

        # Resizing the -- Show Password -- image and converting it into a object to display on a widget
        global showHide_obj
        showHide_obj = ImageTk.PhotoImage(showHide_icon.resize((30, 30),
                                                               resampling_filter))

        # Creating a Show-Password Button to show/hide the password in the SignIn Panel
        showPwd = Button(sign_In, image=showHide_obj, style="Pwd_&_Key.TButton",
                         cursor="hand2", command=lambda: showPassword("Hidden", showPwd, signIn_pwd))
        showPwd.place(relx=0.85, rely=0.6, anchor=CENTER)

        # -------------------------------------------------

        # Creating all the labels for the Entries in the SignIn Panel -----------------------

        # Label for UserId Entry
        signIn_userID_L = Label(sign_In, text="User ID", font=("Dodge", 12, "bold"),
                                background=signIn_bG, foreground=signIn_fG)
        signIn_userID_L.place(relx=0.21, rely=0.38, anchor=W)

        # Label for Password Entry
        signIn_pwd_L = Label(sign_In, text="Password", font=("Dodge", 12, "bold"),
                             background=signIn_bG, foreground=signIn_fG)
        signIn_pwd_L.place(relx=0.21, rely=0.53, anchor=W)

        # -------------------------------------------------

        #     ------------------------
        # --------- SignIn Button ---------
        #     ------------------------

        # Styling the SignIn Button
        sign_In_Button_style = Style(sign_In)
        sign_In_Button_style.theme_use("default")
        sign_In_Button_style.configure("SignIn.TButton", font=("Dodge", 15, "bold", "italic"),
                                       foreground="#F0EFF4", background="#72195A", borderwidth=2, highlightthickness=2, focuscolor="none")
        # Mouse Hovering style for SignIn Button
        sign_In_Button_style.map("SignIn.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                 background=[("active", "#A92767")])

        # Creating a SignIn Button for users to login with the userID and password
        sign_In_Button = Button(sign_In, text="Sign In", style="SignIn.TButton",
                                command=lambda: credentialsValidator(signIn_userID_var, signIn_pwd_var))
        sign_In_Button.place(relx=0.5, rely=0.75, height=int(screen_height/20),
                             width=int(screen_width/12), anchor=CENTER)

        # Assigning the same function of SignIn Button to <Enter> key
        sign_In.bind("<Return>", lambda *_, userid=signIn_userID_var,
                     password=signIn_pwd_var: credentialsValidator(userid, password))

        #     ------------------------
        # --------- SignUp Button ---------
        #     ------------------------

        # Creating a label to display some additional Info before SignUp Button
        signIn_signUp_L = Label(sign_In, text="don't have an account?", font=("Dodge", 11),
                                background=signIn_bG, foreground=signIn_fG)
        signIn_signUp_L.place(relx=0.45, rely=0.88, anchor=CENTER)

        # Styling the SignUp Button
        signIn_signUpBtn_style = Style()
        signIn_signUpBtn_style.theme_use("default")
        signIn_signUpBtn_style.configure("SignUp.TLabel", font=("Dodge", 13, "bold", "underline"),
                                         background=signIn_bG, foreground=signIn_fG, borderwidth=0, hightlightthickness=0, relief=FLAT, focuscolor="none")
        # Mouse Hovering style for SignUp Button
        signIn_signUpBtn_style.map("SignUp.TLabel", foreground=[("active", "!disabled", "#4C1036")],
                                   background=[("active", signIn_bG)])

        # Creating a SignUp Button to create the SignUp Panel
        signIn_signUpBtn = Button(sign_In, text="Sign Up", style="SignUp.TLabel",
                                  command=lambda: signUpPanel())
        signIn_signUpBtn.place(relx=0.76, rely=0.88,
                               height=int(screen_height/20), width=int(screen_width/12), anchor=CENTER)

        # -------------------------------------------------------------------------------------------- `(in Voice)` SignIn Panel -StyleEnds----

    # >>

    # Function for creating the WorkSpace layout of the --- `(in Voice)` ---
    def workSpace(linkSelected, leftPanelShrinked=False):

        # Function for returning back to the User's Dashboard
        def dashboardTab():

            # Destroying the `(in Voice)` WorkSpace and its child widgets
            root.after(100, lambda: workSpace_leftFrame.destroy())
            root.after(120, lambda: workSpace_rightFrame.destroy())

        # >>

        # Function which is operated by clicking on the User profile picture to update with a new the User's profile picture
        def profilePictureUpdater(event):

            # Opening a dialogbox for User to pick a image file and returning its file path
            imagePath = filedialog.askopenfilename(title="Choose a Image", filetype=[(
                "Both *.jpg and *.png", ("*.png", "*.jpg")), ("*.png only", "*.png"), ("*.jpg or *jpeg", "*.jpg")])

            # Confirming the Selected image file is a valid one
            if (imagePath.lower().endswith(".png") or imagePath.lower().endswith(".jpeg") or imagePath.lower().endswith(".jpg")):

                # Opening the image file using the returned file path and Resizing it to fit the Profile Picture Frame
                profilePic = Image.open(imagePath).convert("RGBA")
                minimumSize = min(profilePic.size)
                profilePic = profilePic.resize(
                    (minimumSize, minimumSize), resampling_filter)

                # Creating a mask as same as the size of the image and used it to crop the new image to Circle
                bigger_3x = (profilePic.size[0] * 3, profilePic.size[1] * 3)
                mask = Image.new("L", bigger_3x, 0)
                ImageDraw.Draw(mask).ellipse((0, 0) + bigger_3x, fill=255)
                mask = mask.resize(profilePic.size, resampling_filter)
                mask = ImageChops.darker(mask, profilePic.split()[-1])
                profilePic.putalpha(mask)

                # Generating the path to cropped image and Saving it on the path
                timeNow = datetime.now()
                pathToTempPic = f"./.__appcache__/{timeNow.year}_{timeNow.month}_{timeNow.day}_{timeNow.strftime('%H%M%S')}.png"
                profilePic.save(pathToTempPic)

                # Opening the User's Database
                userObj = UserDetail(loggedInUser)

                # Updating the Profile Picture in the User's database with the new picture
                userObj.updateProfilePicture(pathToTempPic)

                # Closing the connection with the Database
                userObj.closeDB()

                # Resizing the -- New User's Profile -- picture and converting it into a object to display on the
                leftTopProfile_obj = profilePic.resize((150, 150),
                                                       resampling_filter)
                leftTopProfile_obj = ImageTk.PhotoImage(leftTopProfile_obj)

                # Changing the Profile picture on Left-Top Panel User's Profile with new one
                leftTop_profile.configure(image=leftTopProfile_obj)
                leftTop_profile.image = leftTopProfile_obj

                # Opening and Resizing the -- New User's Profile -- picture and converting it into a object to display on the
                homeProfile_obj = profilePic.resize((45, 45),
                                                    resampling_filter)
                homeProfile_obj = ImageTk.PhotoImage(homeProfile_obj)

                # Changing the Profile picture on User Dashboard's User Profile Section with new one
                home_userProfile.configure(image=homeProfile_obj)
                home_userProfile.image = homeProfile_obj

        # >>

        # Function which is operated by the Wrap Button of WorkSpace's Left-Top Panel to shrink the WorkSpace's Left Panel by expanding the WorkSpace's Right Panel
        def leftPanelShrinker():

            # Function which is operated by the (Menu)Extend-Button for expanding the shrinked Left Panel by shrinking the Right Panel
            def leftPanelExpander(event):

                # Enabling and Showing the Wrap Button
                panelWrap_btn.configure(state=NORMAL)
                panelWrap_btn.lift(leftTop_bgColor)

                # --------------------- WorkSpace's Right Panel (Shrinked) -StyleStarts----------------------------------

                # Shrinking the Right Panel, Right-Top Panel and its background Color
                workSpace_rightFrame.configure(height=int(screen_height/1.035),
                                               width=int(screen_width-(screen_width/4.6)))
                rightTop_frame.configure(height=int(screen_height/10),
                                         width=int(screen_width-(screen_width/4.6)))
                rightTop_bgColor.configure(width=int(screen_width/7.55))

                # Destorying the User's Profile Picture on the Right-Top Panel
                rightTop_profile.destroy()

                # Shrinking the Right-Bottom Panel and its background Color
                rightBottom_frame.configure(
                    width=int(screen_width-(screen_width/4.6)))
                rightBottom_innerbgColor.configure(width=int(screen_width/8.3))

                # Confirming the Tab-Link Button selected is not 'Settings' Button
                if (selectedLinkName != "Settings"):

                    # Shrinking the Table Header on the Right-Bottom Panel
                    tableHeader.configure(
                        width=int(screen_width-(screen_width/3)))
                    tableHeader_bgColor.place(
                        width=int(screen_width-(screen_width/3)))

                    # Shrinking the Table Fields on the Right-Bottom Panel
                    tableFields.place(width=int(screen_width/1.5))

                # ----------------------------------------------------- WorkSpace's Right Panel (Shrinked) -StyleEnds----

                # --------------------- WorkSpace's Left Panel (Expanded) -StyleStarts----------------------------------

                # Expanding the Left and Left-Top Panels
                workSpace_leftFrame.configure(height=int(screen_height/1.035),
                                              width=int(screen_width/4.55))
                leftTop_frame.configure(height=int(screen_height/3.05),
                                        width=int(screen_width/4.55))

                # Opening and Resizing the -- User's Profile -- picture and converting it into a object to display on a widget
                global profile_obj2
                profile_obj2 = ImageTk.PhotoImage(
                    (Image.open(currentUser["profile"]).convert("RGBA")).resize((150, 150), resampling_filter))

                # Changing the image of the User's Profile Picture label to back to display User Profile
                leftTop_profile.configure(image=profile_obj2)

                # Removing the function assigning with User's Profile Picture label
                leftTop_profile.unbind("<Button-1>")

                # Assigning again the function to update the User's Profile Picture by mouse left-click
                root.after(100, lambda: leftTop_profile.bind(
                    "<Button-1>", profilePictureUpdater))

                # Expanding the Left-Bottom Panel
                leftBottom_frame.configure(height=int(screen_height/1.55),
                                           width=int(screen_width/4.55))

                # Expanding the Tab-Link Buttons to normal
                tabLink1.configure(compound=LEFT)
                tabLink1.place(relx=0.5, rely=0.1, width=int(screen_width/4.55),
                               height=int(screen_height/12), anchor=N)
                tabLink2.configure(compound=LEFT, command=lambda: [
                    dashboardTab(), workSpace(tabLink2)
                ])
                tabLink2.place(relx=0.5, rely=0.24, width=int(screen_width/4.55),
                               height=int(screen_height/12), anchor=N)
                tabLink3.configure(compound=LEFT, command=lambda: [
                    dashboardTab(), workSpace(tabLink3)
                ])
                tabLink3.place(relx=0.5, rely=0.38, width=int(screen_width/4.55),
                               height=int(screen_height/12), anchor=N)
                tabLink4.configure(compound=LEFT, command=lambda: [
                    dashboardTab(), workSpace(tabLink4)
                ])
                tabLink4.place(relx=0.5, rely=0.52, width=int(screen_width/4.55),
                               height=int(screen_height/12), anchor=N)
                tabLink5.configure(compound=LEFT, command=lambda: [
                    dashboardTab(), workSpace(tabLink5)
                ])
                tabLink5.place(relx=0.5, rely=0.66, width=int(screen_width/4.55),
                               height=int(screen_height/12), anchor=N)

                # ----------------------------------------------------- WorkSpace's Left Panel (Expanded) -StyleEnds----

            # >>

            # Function to show/hide User INFO while mouse-hovering over the User's Profile Picture on the Right-Top Panel
            def userProfile_INFO(event, fullName="", email=""):

                # Making the User INFO a global variable so it can be accessed everywhere
                global rightTop_profile_INFO

                # Getting the type of the event by id_number
                event_ID = int(getattr(event, "__dict__")["type"])

                # Checking if the Event is <Enter>
                if (event_ID == 7):

                    profile_info_text = f"   {fullName}    \r\n   {email}    "

                    # Creating a label to show INFO about LoggedIn User
                    rightTop_profile_INFO = Label(rightBottom_frame, text=profile_info_text, font=("Dodge", 10, "bold"),
                                                  background="#FFD670", foreground=leftTop_bG, justify=RIGHT, anchor=CENTER)
                    rightTop_profile_INFO.place(relx=0.95, rely=0.2,
                                                height=int(screen_height/8.5), anchor=SE)

                # Checking if the Event is <Leave>
                elif (event_ID == 8):

                    # Destroying the User INFO when mouseevent is <Leave>
                    rightTop_profile_INFO.destroy()

            # >>

            # Disabling and Hiding the Wrap Button after clicked, for preventing the function to be called twice
            panelWrap_btn.configure(state=DISABLED)
            panelWrap_btn.lower()

            # ---------------------------- WorkSpace's Left Panel (Shrinked) -StyleStarts-------------------------------------------

            # Shrinking the Left and Left-Top Panels
            workSpace_leftFrame.configure(height=int(screen_height/1.035),
                                          width=int(screen_width/15))
            leftTop_frame.configure(height=int(screen_height/6.1),
                                    width=int(screen_width/15))

            # Resizing the -- Menu -- image and converting it into a object to display on a widget
            global menu_obj
            menu_obj = ImageTk.PhotoImage(menu_icon.resize((40, 40),
                                                           resampling_filter))

            # Changing the image of the User's Profile Picture label to Extend-Button
            leftTop_profile.configure(image=menu_obj)

            # Removing the function assigning with User's Profile Picture label
            leftTop_profile.unbind("<Button-1>")

            # Assigning new function to User's Profile Picture label which extends the Left Panel back to Default
            leftTop_profile.bind("<Button-1>", leftPanelExpander)

            # Shrinking the Left-Bottom Panel
            leftBottom_frame.configure(height=int(screen_height/1.23),
                                       width=int(screen_width/15))

            # Shrinking the Tab-Link Buttons and also Hiding the text on it
            tabLink1.configure(compound=NONE)
            tabLink1.place(relx=0.5, rely=0, width=int(screen_width/4.55),
                           height=int(screen_height/7.5), anchor=N)
            tabLink2.configure(compound=NONE, command=lambda: [
                               dashboardTab(), workSpace(tabLink2, True)
                               ])
            tabLink2.place(relx=0.5, rely=0.17, width=int(screen_width/4.55),
                           height=int(screen_height/7.5), anchor=N)
            tabLink3.configure(compound=NONE, command=lambda: [
                               dashboardTab(), workSpace(tabLink3, True)
                               ])
            tabLink3.place(relx=0.5, rely=0.34, width=int(screen_width/4.55),
                           height=int(screen_height/7.5), anchor=N)
            tabLink4.configure(compound=NONE, command=lambda: [
                               dashboardTab(), workSpace(tabLink4, True)
                               ])
            tabLink4.place(relx=0.5, rely=0.51, width=int(screen_width/4.55),
                           height=int(screen_height/7.5), anchor=N)
            tabLink5.configure(compound=NONE, command=lambda: [
                               dashboardTab(), workSpace(tabLink5, True)
                               ])
            tabLink5.place(relx=0.5, rely=0.68, width=int(screen_width/4.55),
                           height=int(screen_height/7.5), anchor=N)

            # ------------------------------------------------------------------- WorkSpace's Left Panel (Shrinked) -StyleEnds----

            # ---------------------------- WorkSpace's Right Panel (Expanded) -StyleStarts-------------------------------------------

            # Expanding the Right Panel, Right-Top Panel and its background Color
            workSpace_rightFrame.configure(height=int(screen_height/1.035),
                                           width=int(screen_width-(screen_width/15.1)))
            rightTop_frame.configure(height=int(screen_height/10),
                                     width=int(screen_width-(screen_width/15.1)))
            rightTop_bgColor.configure(width=int(screen_width/6.4))

            # Opening the User's Database
            userObj = UserDetail(loggedInUser)

            # Querying the 'userDetails' table in the User's database and picking the matched record
            currentUser = userObj.get()

            # Closing the connection with the Database
            userObj.closeDB()

            # Opening and Resizing the -- New User's Profile -- picture and converting it into a object to display on a widget
            global rightTopProfile_obj
            rightTopProfile_obj = ImageTk.PhotoImage(
                (Image.open(currentUser["profile"]).convert("RGBA")).resize((45, 45), resampling_filter))

            # Creating a label to show the User's Profile Picture on the Right-Top Panel
            rightTop_profile = Label(rightTop_frame, image=rightTopProfile_obj,
                                     background=rightTop_bG)
            rightTop_profile.place(relx=0.8, rely=0.5, anchor=W)

            # Assigning a function to show/hide User INFO while hovering the User's Profile Picture on the Right-Top Panel
            rightTop_profile.bind("<Enter>",
                                  lambda event, fullName=currentUser["fullName"], email=currentUser["email"]: userProfile_INFO(event, fullName, email))
            rightTop_profile.bind("<Leave>",
                                  lambda event: userProfile_INFO(event))

            # Expanding the Right-Bottom Panel and its background Color
            rightBottom_frame.configure(
                width=int(screen_width-(screen_width/15.1)))
            rightBottom_innerbgColor.configure(width=int(screen_width/6.87))

            # Confirming the Tab-Link Button selected is not 'Settings' Button
            if (selectedLinkName != "Settings"):

                # Expanding the Table Header on the Right-Bottom Panel
                tableHeader.configure(
                    width=int(screen_width-(screen_width/5.5)))
                tableHeader_bgColor.place(
                    width=int(screen_width-(screen_width/5.5)))

                # Expanding the Table Fields on the Right-Bottom Panel
                tableFields.place(width=int(screen_width/1.222))

            # ------------------------------------------------------------------- WorkSpace's Right Panel (Expanded) -StyleEnds----

        # >>

        # Function to wrap the lenght of text inside Right-Bottom Panel Table Fields
        def wrapTextLength(content, charLength=45):

            # returning the wrappedtext to it's field
            return "\n".join(textwrap.wrap(content, charLength))

        # Function to get the default Currency symbols from the user preferences in User's Database
        def defaultCurrencyGrappler():

            # Opening the CurrencyRates Table in the User's Database
            currencyObj = CurrencyRate(loggedInUser)

            # Querying the 'currencyRates' table in the User's database and picking all the records of currency
            all_currencies = currencyObj.all()

            # Closing the connection with the Database
            currencyObj.closeDB()

            # Confirming the Currency Rates are not empty
            if (all_currencies != []):

                # Opening the User Preferences Table in the User's Database
                preferenceObj = UserPreference(loggedInUser)

                # Querying the 'userPreferences' table in the User's database and picking the preferences
                preferences = preferenceObj.all()

                # Closing the connection with the Database
                preferenceObj.closeDB()

                # Checking the User preference is empty or not
                preferCurrencyCode = preferences[0] if (
                    preferences is not None) else "INR"

                for item in all_currencies:

                    # Confirming the Currency code in preference and record matches
                    if (item[0] == preferCurrencyCode):

                        # Assigning the matched Currency list as a symbol to return as a response
                        currencyUsed = item

            return currencyUsed

        # >>

        # Function to show/hide Table Fields INFO while mouse-hovering over the Table Fields on the Right-Bottom Panel
        def tableFields_INFO(event, buttonText):

            # Making the User INFO a global variable so it can be accessed everywhere
            global fields_info

            # Getting the type of the event by id_number
            event_ID = int(getattr(event, "__dict__")["type"])

            # Parsing the New or Add Button text to get the active Tab name
            currentTabName = buttonText.replace(
                "Add", "").replace("New", "").replace(" ", "")

            # Checking if the Event is <Enter>
            if (event_ID == 7):

                # Creating a label to show INFO about LoggedIn User
                fields_info = Label(rightBottom_frame, text=f"# Double click on the {currentTabName} to view or edit", font=("Dodge", 12, "bold"),
                                    background=rightBottom_innerbG, foreground=leftTop_bG)
                fields_info.place(relx=0.9, rely=0.9, anchor=SE)

            # Checking if the Event is <Leave>
            elif (event_ID == 8):

                # Destroying the Table Fields INFO INFO when mouseevent is <Leave>
                fields_info.destroy()

        # >>

        # Function to disable the Left-Top Panel's Menu-Button and also limits the Tab-Link Buttons to asking for confirmation before switching Tabs
        def leftPanelExpand_disabler(label=""):

            # Function which is operated by the Tab-Link Buttons to ask for confirmation before switching Tabs
            def tabLink_limiter(clickedLinkName):

                # Showing a confirmation dialog with some message
                confimation_msg = messagebox.askquestion(
                    "in Voice: ", "Are you sure you want to, Discard Changes?") if (label != "") else "yes"

                if (confimation_msg == "yes"):

                    if (clickedLinkName == "InVoices"):

                        # Calling the function to destroy the widgets of Create-InVoice Panel
                        dashboardTab()

                        # Re-setting the Close(X) Button to default
                        close_X_btn.configure(
                            command=lambda: closeInVoiceAPP())

                        # Calling the function to redirect to InVoices's WorkSpace
                        workSpace(tabLink2)

                    elif (clickedLinkName == "Clients"):

                        # Calling the function to destroy the widgets of Add-Client Panel
                        dashboardTab()

                        # Calling the function to redirect to Clients's WorkSpace
                        workSpace(tabLink3)

                    elif (clickedLinkName == "Stocks"):

                        # Calling the function to destroy the widgets of Add-Stock Panel
                        dashboardTab()

                        # Calling the function to redirect to Stocks's WorkSpace
                        workSpace(tabLink4)

                    elif (clickedLinkName == "Settings"):

                        # Calling the function to destroy the widgets of Create-Setting Panel
                        dashboardTab()

                        # Calling the function to redirect to Settings's WorkSpace
                        workSpace(tabLink5)

                    else:

                        # Calling the function to return to User's Dashboard
                        dashboardTab()

            # >>

            # Removing the function assigning with User's Profile Picture label
            leftTop_profile.unbind("<Button-1>")
            leftTop_profile.configure(cursor="arrow")

            # Enabling and Assigning new function to Tab-Link Buttons to ask for confirmation before switching Tabs
            tabLink1.configure(style="Tab-Links.TLabel", state=NORMAL,
                               command=lambda: tabLink_limiter(tabLink1["text"].replace(" ", "")))
            tabLink2.configure(style="Tab-Links.TLabel", state=NORMAL,
                               command=lambda: tabLink_limiter(tabLink2["text"].replace(" ", "")))
            tabLink3.configure(style="Tab-Links.TLabel", state=NORMAL,
                               command=lambda: tabLink_limiter(tabLink3["text"].replace(" ", "")))
            tabLink4.configure(style="Tab-Links.TLabel", state=NORMAL,
                               command=lambda: tabLink_limiter(tabLink4["text"].replace(" ", "")))
            tabLink5.configure(style="Tab-Links.TLabel", state=NORMAL,
                               command=lambda: tabLink_limiter(tabLink5["text"].replace(" ", "")))

        # >>

        # Function which is operated by New-InVoice Button to create the Create-InVoice Panel which is like a template for creating new invoice
        def createNewInVoicePanel(request=""):

            # Function to populate the dropdown and entry widgets in the Create-InVoice Panel with some predefined data from User's Database
            def populate_Box_or_Entry(object, widget, label):

                # Opening the Table in the User's Database
                user_DataBase = object(loggedInUser)

                # Confirming the request is from Client-Select Combobox
                if (label == "Client"):

                    # Querying the 'clientDetails' table in the User's database and picking all the clients
                    all_clients = user_DataBase.all()

                    # Confirming the Client details are not empty
                    if (all_clients != []):

                        # Creating a List with only the Client names
                        client_names = []
                        for name in all_clients:

                            client_names.append(name[0])

                        # Assigning the Clients name List as values to the Client-Select Combobox
                        widget.configure(values=client_names)

                # >>

                # Confirming the request is from InVoice-Number Entry
                elif (label == "InVoice No."):

                    # Querying the 'inVoiceDetails' table in the User's database and picking all the invoices
                    all_inVoices = user_DataBase.all()

                    # Generating the inVoice's uniqueId
                    number = 1
                    generated_no = f"inV#00{number}"

                    # Confirming the InVoice Details are not empty
                    if (all_inVoices != []):

                        for invoice in all_inVoices:

                            # Checking the generated inVoice's uniqueId already exists
                            while (generated_no == invoice[0]):

                                # Generating new inVoice's uniqueId if exists
                                number += 1
                                if (len(str(number)) < 2):
                                    generated_no = f"inV#00{number}"

                                elif (len(str(number)) < 3):
                                    generated_no = f"inV#0{number}"

                                else:
                                    generated_no = f"inV#{number}"

                    # Assigning the generated inVoice's uniqueId as the value of InVoice-Number Entry
                    widget.set(generated_no)

                # >>

                # Confirming the request is from Currency-Select Combobox or DueDate-Select Combobox
                elif (label == "Currency" or label == "Due"):

                    # Opening the User Preferences Table in the User's Database
                    preferenceObj = UserPreference(loggedInUser)

                    # Querying the 'userPreferences' table in the User's database and picking the record
                    preferences = preferenceObj.all()

                    # Creating a empty List to append the queryed records from tables in User's database
                    newList = []

                    # Confirming the request is from Currency-Select Combobox
                    if (label == "Currency"):

                        # Querying the 'currencyRates' table in the User's database and picking all the currencies
                        all_currencies = user_DataBase.all()

                        # Confirming the Currency Rates are not empty
                        if (all_currencies != []):

                            # Checking the User preference is empty or not
                            prefer = preferences[0] if (
                                preferences is not None) else "INR"

                            for item in all_currencies:

                                # Filling the new list with records from database tables
                                newList.append(f" {item[0]} {item[2]}" if (
                                    item[0] != "CHF") else f" {item[0]}")

                                # Confirming the Currency code in preference and record matches
                                if (item[0] == prefer):

                                    # Setting the default exchange value for Currency-Select Combobox
                                    widget["textvariable"] = item[4]

                                    # Settings the default Currency Symbols in labels of Create-InVoice Panel
                                    productsTable_heading4_sym.configure(
                                        text=item[2])
                                    productsTable_heading5_sym.configure(
                                        text=item[2])
                                    totalAmount_symbol.configure(text=item[2])

                            # Assigning the Currency Code and Symbol from the Database as values to the Currency-Select Combobox
                            widget.configure(values=newList)

                    # Confirming the request is from DueDate-Select Combobox
                    elif (label == "Due"):

                        # Querying the 'dueDates' table in the User's database and picking all the records
                        all_duedates = user_DataBase.all()

                        # Confirming the Due Dates are not empty
                        if (all_duedates != []):

                            for day in all_duedates:

                                if (day[0] != "Nil"):

                                    newList.append(f" {day[0]} days")

                                else:
                                    newList.append(f" {day[0]}")

                            # Assigning the Due Days from the Database as values to the DueDate-Select Combobox
                            widget.configure(values=newList)

                            # Checking the User preference is empty or not
                            prefer = preferences[1] if (
                                preferences is not None) else "Nil"

                    # Iterating through the List created and assigning the default option for the Combobox
                    for item in newList:

                        if (item.find(prefer) == 1):

                            # Setting the default option for Combobox
                            widget.current(newList.index(item))

                            if (label == "Due"):

                                # Calling the function to create a Paid-Amount Entry according to the preference
                                dueValueCalculator()

                    # Commiting and Closing the connection with the Database
                    preferenceObj.closeDB()

                # >>

                # Confirming the request is from Customer-Message Box
                elif (label == "Customer-Message"):

                    # Querying the 'clientDetails' table in the User's database and picking all the clients
                    all_clients = user_DataBase.all()

                    # Confirming the Client details are not empty
                    if (all_clients != []):

                        # Picking the message for the picked client name
                        messageContent = [client[8] for client in all_clients if (
                            client[0] == clientSelect_box.get())]

                        # Setting the default message for Customer-Message Box according to the Client
                        widget.delete(1.0, END)
                        widget.insert(INSERT, messageContent[0])

                # Confirming the request is from Tax-Percentage Entry
                elif (label == "Tax (%)"):

                    # Querying the 'userPreferences' table in the User's database and picking all the User preferences
                    preferences = user_DataBase.all()

                    # Confirming the User Preferences are not empty
                    if (preferences != [] and label == "Tax (%)"):

                        # Setting the default tax percentage in the Tax-Percentage Entry
                        widget.set(preferences[2])

                # Closing the connection with the Database
                user_DataBase.closeDB()

            # >>

            # Function for updating the Currency Exchange Value whenever the Currency-Select Combobox's selection changes
            def currencyValueChanger(event, currencySelect, tablerows):

                # Opening the CurrencyRates Table in the User's Database
                currencyObj = CurrencyRate(loggedInUser)

                # Querying the 'currencyRates' table in the User's database and picking all the records of currency
                all_currencies = currencyObj.all()

                # Closing the connection with the Database
                currencyObj.closeDB()

                # Confirming the Currency Rates are not empty
                if (all_currencies != []):

                    for item in all_currencies:

                        # Converting the Code in same format of values in Currency-Select Combobox
                        code_fromDB = f" {item[0]} {item[2]}" if (
                            item[0] != "CHF") else f" {item[0]}"

                        # Changing the Symbols according to the selection in Currency-Select Combobox
                        symbol = f"{item[2]}" if (
                            item[0] != "CHF") else f"  {item[2]}"

                        # Confirming the Currency code in database and matches with the selection
                        if (code_fromDB == currencySelect.get()):

                            # Setting the new exchange value for Currency-Select Combobox
                            currencySelect["textvariable"] = item[4]

                            # Setting the picked option as new default for Combobox
                            currencySelect.current(all_currencies.index(item))

                            # Changing the Currency Symbols in labels of Create-InVoice Panel
                            productsTable_heading4_sym.configure(text=symbol)
                            productsTable_heading5_sym.configure(text=symbol)
                            totalAmount_symbol.configure(text=symbol)

                            for row in tablerows:

                                # Updating the Product Rate in all rows according to the Currency selected
                                productPriceChanger(
                                    row[1],
                                    row[4],
                                    row[2]
                                )

                                # Updating the Product Total Rate in all rows according to the Currency selected
                                rateEntryValidator(
                                    row[3],
                                    row[4],
                                    row[5],
                                    tablerows
                                )

                                # Calling the function to calculate and update the subtotal and total amount of the InVoice
                                totalAmountCalculator(tablerows)

            # >>

            # Function which is operated by the Calendar Button to open a Calendar to pick User's desired date
            def openCalendar():

                # Function which is operated by the SET Button to change date in the Date Entry with User picked date from the Calendar
                def setCustomDate():

                    # Changing the value of Date Entry with User picked date
                    dateEntry_Var.set(f"{month_calendar.get_date()} ")

                    # Destroying the Month-Calendar and its SET Button
                    setDate_btn.destroy()
                    month_calendar.destroy()

                    # Enabling and Showing the Calendar Button again
                    calendarButton.configure(state=NORMAL)
                    calendarButton.lift()

                # >>

                # Disabling and Hiding the Calendar Button after clicked, for preventing the function to be called twice
                calendarButton.configure(state=DISABLED)
                calendarButton.lower()

                # Creating the Month-Calendar for Users to pick their desired date and displaying it on the Create-InVoice Panel
                month_calendar = Calendar(createInVoice_frame, date_pattern="y-mm-dd", selectmode="day",
                                          year=todaysDate.year, month=todaysDate.month, day=todaysDate.day)
                month_calendar.place(relx=0.66, rely=0.365, anchor=CENTER)

                # Styling the Set-Date Button
                setDate_btn_style = Style()
                setDate_btn_style.theme_use("default")
                setDate_btn_style.configure("SET.TButton", font=("Dodge", 12, "bold"), foreground=createInVoice_innerfG,
                                            borderwidth=0, width=6, focuscolor="none", relief=FLAT, highlightthickness=0)
                # Mouse Hovering style for Set-Date Button
                setDate_btn_style.map("SET.TButton", foreground=[(
                    "active", "!disabled", "#011932")], background=[("active", "#B9B5B0")])

                # Creating the Set-Date Button to change date in the Date Entry with User picked date from the Month-Calendar
                setDate_btn = Button(createInVoice_frame, text="Set", style="SET.TButton",
                                     command=lambda: setCustomDate())
                setDate_btn.place(relx=0.73, rely=0.505, anchor=CENTER)

            # >>

            # Function for Creating a Paid-Amount Entry according to the selected option in DueDate-Select Combobox
            def dueValueCalculator(event=None):

                def paidAmountValidator(var, index, mode):

                    # Confirming the Paid-Amount Entry is not empty
                    if (paidAmountEntry_Var.get() != ""):

                        try:

                            # Converting the entry value to a float, if value not either integer or float throws a exception
                            float(paidAmountEntry_Var.get())

                            # Checking the tax entered is not exceed Total Amount
                            if (float(paidAmountEntry_Var.get()) > float(totalAmountEntry["text"])):

                                # Showing a error message
                                messagebox.showerror(
                                    "in Voice", "Amount paid can't be greater than the Total Amount")

                                # Re-setting the Paid-Amount Entry to zero if value exceeds Total Amount
                                paidAmountEntry_Var.set("%.2f" % 0)

                        except (ValueError, TclError, FloatingPointError):

                            # Re-setting the Rate Entry to zero if is not either integer or float
                            paidAmountEntry_Var.set("%.2f" % 0)

                # >>

                # Making the Paid-Amount Entry and labels the global variable so it can be accessed everywhere
                global paidAmountEntry, paidAmountEntry_label

                if (event is None):

                    # Creating Paid-Amount Entry for entering the paid amount
                    paidAmountEntry_Var = StringVar(createInVoice_frame,
                                                    value="%.2f" % 0)
                    paidAmountEntry = tk.Entry(createInVoice_frame, textvariable=paidAmountEntry_Var, font=("Dodge", 12, "bold"),
                                               width=int(screen_width/70), disabledbackground="#FFFFFF", disabledforeground="#0A0908", justify=CENTER)

                    # Assigning a function to validate the input is valid number
                    paidAmountEntry_Var.trace_add("write", paidAmountValidator)

                    # PaidAmount-Entry label
                    paidAmountEntry_label = Label(createInVoice_frame, text="Amount Paid", font=("Dodge", 13, "bold"),
                                                  background=createInVoice_innerbG, foreground=createInVoice_innerfG)

                    # Adding the Widgets related to Paid-Amount Entry to All-Boxes list
                    all_Boxes.append((
                        paidAmountEntry,
                        paidAmountEntry_Var,
                        paidAmountEntry_label["text"]
                    ))

                    if(dueSelect_box.get() != " Nil"):

                        # Displaying the Paid-Amount Entry and PaidAmount-Entry label
                        paidAmountEntry.place(relx=0.6, rely=0.125,
                                              height=int(screen_height/23), anchor=CENTER)
                        paidAmountEntry_label.place(relx=0.6, rely=0.075,
                                                    anchor=CENTER)

                        # Assigning a function for deleting the pre-occupied value in the PaidAmount-Entry
                        paidAmountEntry.bind("<Button-1>",
                                             lambda event, box=paidAmountEntry, index=0: deletePrefilledContent(event, box, index))

                elif(event is not None and dueSelect_box.get() == " Nil"):

                    # Hiding the Paid-Amount Entry and labels when DueDate-Select Combobox value is not 'Nil'
                    paidAmountEntry.place_forget()
                    paidAmountEntry_label.place_forget()

                elif(event is not None and dueSelect_box.get() != " Nil"):

                    # Displaying the Paid-Amount Entry and PaidAmount-Entry label
                    paidAmountEntry.place(relx=0.6, rely=0.125,
                                          height=int(screen_height/23), anchor=CENTER)
                    paidAmountEntry_label.place(relx=0.6, rely=0.075,
                                                anchor=CENTER)

                    # Assigning a function for deleting the pre-occupied value in the Paid-Amount Entry
                    paidAmountEntry.bind("<Button-1>",
                                         lambda event, box=paidAmountEntry, index=0: deletePrefilledContent(event, box, index))

            # >>

            # Function for adding new rows inside the Product-Details table
            def addNewRow(itemNo=0, allRows=[]):

                # ------------------------------------- Product-Details Table (row) -StyleStarts-------------------------------------------

                # Increasing the row count
                itemNo += 1

                # ---------------------
                #      Item Number
                # ---------------------

                # Creating a label for displaying the Item Number
                itemNumberEntry = Label(productsTable_body_frame, text=itemNo, font=("Dodge", 14, "bold"),
                                        background=productsTable_bgColor, anchor=CENTER)
                itemNumberEntry.grid(row=itemNo, column=0,
                                     padx=(40, 0), pady=(20, 6))

                # -----------------------
                #   Product Description
                # -----------------------

                # Styling the Product Description Entry
                productEntry_style = Style(productsTable_body_frame)
                productEntry_style.theme_use("default")
                productEntry_style.map("ProductDescription.TEntry", foreground=[("disabled", "#0A0908")], background=[("disabled", "#FFFFFF")],
                                       fieldbackground=[("disabled", "#FFFFFF")])

                # Opening the ProductDetails Table in the User's Database
                productObj = ProductDetail(loggedInUser)

                # Querying the 'productDetails' table in the User's database and picking all the products
                products = productObj.all()

                # Closing the connection to the database
                productObj.closeDB()

                # Creating a empty python List
                description = []

                # Confirming the products from the 'productDetails' table are not empty
                if (products != []):

                    for product in products:

                        description.append(product[0])

                # Creating a entry for Product Description
                productEntry_Var = StringVar(productsTable_body_frame)
                productEntry = AutocompleteEntry(productsTable_body_frame, textvariable=productEntry_Var, font=("Dodge", 12, "bold"),
                                                 width=int(screen_width/45), completevalues=description, style="ProductDescription.TEntry")
                productEntry.grid(row=itemNo, column=1, ipady=6,
                                  padx=(50, 0), pady=(20, 6))

                # ---------------------
                #       Quantity
                # ---------------------

                # Creating a entry for Product Quantity
                quantityEntry_Var = StringVar(productsTable_body_frame,
                                              value=0)
                quantityEntry = tk.Entry(productsTable_body_frame, textvariable=quantityEntry_Var, font=("Dodge", 14, "bold"),
                                         width=int(screen_width/180), disabledbackground="#FFFFFF", disabledforeground="#0A0908", justify=RIGHT)
                quantityEntry.grid(row=itemNo, column=2, ipady=6,
                                   padx=(250, 0), pady=(20, 6))

                # ---------------------
                #         Rate
                # ---------------------

                # Creating a entry for Product rate (price per item)
                rateEntry_Var = StringVar(productsTable_body_frame,
                                          value="%.2f" % 0)
                rateEntry = tk.Entry(productsTable_body_frame, textvariable=rateEntry_Var, font=("Dodge", 14, "bold"),
                                     width=int(screen_width/150), disabledbackground="#FFFFFF", disabledforeground="#0A0908", justify=RIGHT)
                rateEntry.grid(row=itemNo, column=3, ipady=6,
                               padx=(70, 0), pady=(20, 6))

                # ---------------------
                #       Amount
                # ---------------------

                # Creating a entry for Product's Total Amount
                amountEntry_Var = StringVar(productsTable_body_frame,
                                            value="%.2f" % 0)
                amountEntry = tk.Entry(productsTable_body_frame, textvariable=amountEntry_Var, font=("Dodge", 14, "bold"), width=int(screen_width/120),
                                       disabledbackground="#FFFFFF", disabledforeground="#0A0908", borderwidth=1, cursor="arrow", state=DISABLED, justify=RIGHT)
                amountEntry.grid(row=itemNo, column=4, ipady=6,
                                 padx=(50, 50), pady=(20, 6))

                # Assigning a function to scroll the Product-Details Table canvas widget along with the mouse wheel
                itemNumberEntry.bind("<MouseWheel>", scrollProductsDetail)
                productEntry.bind("<MouseWheel>", scrollProductsDetail)
                quantityEntry.bind("<MouseWheel>", scrollProductsDetail)
                rateEntry.bind("<MouseWheel>", scrollProductsDetail)
                amountEntry.bind("<MouseWheel>", scrollProductsDetail)

                fields = (
                    itemNumberEntry,
                    productEntry_Var,
                    quantityEntry,
                    quantityEntry_Var,
                    rateEntry_Var,
                    amountEntry_Var,
                    productEntry,
                    rateEntry
                )

                # Adding the fields in the current row to a python list
                allRows.append(fields)

                # Assigning a function to the Product Description Entry which fills the price fields related to the product name entered
                productEntry_Var.trace_add("write",
                                           lambda *_, product=productEntry_Var, rate=rateEntry_Var, quantity=quantityEntry: productPriceChanger(product, rate, quantity))

                # Assigning a function to validate the Product Quantity Entry and also calculate the total cost of product in each row
                quantityEntry_Var.trace_add("write",
                                            lambda *_, product=productEntry_Var, quantity=quantityEntry_Var, rate=rateEntry_Var, amount=amountEntry_Var, tablerows=allRows: quantityEntryValidator(product, quantity, rate, amount, tablerows))

                # Assigning a function to validate the Product Rate Entry and also calculate the total cost of product in each row
                rateEntry_Var.trace_add("write",
                                        lambda *_, quantity=quantityEntry_Var, rate=rateEntry_Var, amount=amountEntry_Var, tablerows=allRows: rateEntryValidator(quantity, rate, amount, tablerows))

                # Assigning a function with Currency-Select Combobox to update the values and symbols of currency in some widgets
                currencySelect_box.bind("<<ComboboxSelected>>",
                                        lambda event, dropdown=currencySelect_box, tablerows=allRows: currencyValueChanger(event, dropdown, tablerows))

                # Changing the arguments of the function assigned with the Add-Row Button
                addRowButton.configure(
                    command=lambda: addNewRow(itemNo, allRows))

                return allRows

                # ---------------------------------------------------------------------------- Product-Details Table (row) -StyleEnds----

            # >>

            # Function for making the whole canvas wigdet scrollable
            def onFrameConfigure(productsTable_canvas):

                # Setting the scrollable area of canvas to all
                productsTable_canvas.configure(
                    scrollregion=productsTable_canvas.bbox("all"))

            # >>

            # Function which scrolls the fields on the Product-Details Table along with the mouse wheel
            def scrollProductsDetail(event):

                # Moving the canvas along with the mouse wheel rotatation
                productsTable_body_canvas.yview_scroll(int(-1*(event.delta/120)),
                                                       "units")

            # >>

            # Function for deleting the pre-occupied message in a widget with a mouse left-click
            def deletePrefilledContent(event, widget, index):

                # Deleting the pre-occupied message and also removing the function to assigned to the widget mouse left-click
                widget.delete(index, END)
                widget.unbind("<Button-1>")

            # >>

            # Function for getting the rate of the product by its name and setting the rate to Rate Entry
            def productPriceChanger(product_Var, rate_Var, quantity_Entry):

                # Function for deleting the values in Quantity Entry when mouse double-click is pressed
                def delete_entry(event):

                    # Re-setting the values in Quantity Entry to zero and also removing the double-click delete functionality
                    quantity_Entry.delete(0, END)
                    quantity_Entry.unbind("<Double-1>")

                # >>

                # Opening the ProductDetails Table in the User's Database
                productObj = ProductDetail(loggedInUser)

                # Querying the 'productDetails' table in the User's Database and picking only the matched product
                product = productObj.get(filterby="productName",
                                         productName=product_Var.get())

                # Closing the connection to the database
                productObj.closeDB()

                # Confirming the product from the 'productDetails' table are not empty
                if (product is not None):

                    # Converting the products price(INR) to their default selected Currency value
                    INR_to_userPrefer = float(
                        product[4])/float(currencySelect_box["textvariable"])

                    # Setting the rate of the product in user selected Currency
                    rate_Var.set("%.2f" % INR_to_userPrefer)

                else:

                    # Resetting the Rate Entry when there is no matched product in Database
                    rate_Var.set("%.2f" % 0)

                # Assigning a function to clear Quantity Entry with mouse Double-Click
                quantity_Entry.bind("<Double-1>", delete_entry)

            # >>

            # Function for validating the value of Quantity Entry is Integer and also calls the function to calculate total amount for each product
            def quantityEntryValidator(product_Var, quantity_Var, rate_Var, amount_Var, tablerows):

                # Checking the Product Entry is empty
                if (product_Var.get() == ""):

                    # Re-setting the Quantity Entry to empty
                    quantity_Var.set("")

                else:

                    # Confirming the Quantity Entry is not empty
                    if (quantity_Var.get() != ""):

                        try:

                            # Converting the entry value to a Integer, if value not integer throws a exception
                            int(quantity_Var.get())

                            # Calculating the total amount for products in each row
                            row_totalAmount = float(
                                quantity_Var.get()) * float(rate_Var.get())

                            # Setting the values for Amount Entry
                            amount_Var.set("%.2f" % row_totalAmount)

                            # Calling the function to calculate total amount for all the products
                            totalAmountCalculator(tablerows)

                        except ValueError:

                            # Re-setting the Quantity Entry to zero if is not a integer
                            quantity_Var.set(0)

            # >>

            # Function for validating the value of Rate Entry is float and also calls the function to calculate total amount for each product
            def rateEntryValidator(quantity_Var, rate_Var, amount_Var, tablerows):

                # Confirming the Rate Entry is not empty
                if (rate_Var.get() != ""):

                    try:

                        # Converting the entry value to a float, if value not either integer or float throws a exception
                        float(rate_Var.get())

                        # Calculating the total amount for products in each row
                        row_totalAmount = float(
                            quantity_Var.get()) * float(rate_Var.get())

                        # Setting the values for Amount Entry
                        amount_Var.set("%.2f" % row_totalAmount)

                        # Calling the function to calculate total amount for all the products
                        totalAmountCalculator(tablerows)

                    # Re-setting the Rate Entry to zero if is not either integer or float
                    except (ValueError, TclError, FloatingPointError):

                        rate_Var.set("%.2f" % 0)

                else:

                    # Re-setting the Rate Entry to zero if Rate Entry is empty
                    rate_Var.set("%.2f" % 0)

            # >>

            # Function for validating the value of TaxPercentage-Entry is Integer and also calculate the total amount by adding the tax
            def taxEntryValidator(var, index, mode):

                # Checking the TaxPercentage-Entry is empty
                if (taxEntry_box_Var.get() == ""):

                    taxCalculated = 0
                else:

                    try:

                        # Converting the entry value to a Integer, if value not integer throws a exception
                        int(taxEntry_box_Var.get())

                        # Calculating the tax for the SubTotal amount and setting it to TaxPercentage-Entry label
                        taxCalculated = float(
                            subtotalEntry["text"]) * (int(taxEntry_box_Var.get())/100)

                        # Checking the tax entered is not exceed 100
                        if (len(taxEntry_box_Var.get()) > 2):

                            # Showing a error message
                            messagebox.showerror(
                                "in Voice", "Percentage value must be a integer less than 100")

                            # Re-setting the TaxPercentage-Entry to zero if value exceeds 100
                            taxEntry_box_Var.set(0)
                            taxCalculated = 0

                    except ValueError:

                        # Re-setting the TaxPercentage-Entry to zero if is not a integer
                        taxEntry_box_Var.set(0)
                        taxCalculated = 0

                # Calling the function to calculate total amount for all the products
                totalAmountCalculator(tax=taxCalculated)

            # >>

            # Function to calculate and update the subtotal and total amount of the InVoice
            def totalAmountCalculator(tablerows=None, tax=None):

                if (tax is None):

                    subTotal = 0
                    for row in tablerows:

                        # Calculating the SubTotal by adding all the product totals
                        subTotal += float(row[5].get())

                    # Assigning the calculated SubTotal as new value to SubTotal-Entry label
                    subtotalEntry["text"] = "%.2f" % subTotal

                    # Calculating the tax for the SubTotal amount
                    taxCalculated = subTotal * \
                        (float(taxEntry_box_Var.get() if (
                            taxEntry_box_Var.get() != "") else 0)/100)

                    if (request != "view"):

                        # Changing the arguments of the function assigned with the Save-InVoice Button
                        saveInVoice_btn.configure(
                            command=lambda: saveInVoice(tablerows))

                        # Changing the function assigned with the Close(X) Button
                        close_X_btn.configure(
                            command=lambda: save_CloseInVoiceApp(tablerows))

                else:

                    # Calculating the tax for the SubTotal amount
                    taxCalculated = tax
                    subTotal = float(subtotalEntry["text"])

                # Setting the calculated tax to TaxPercentage-Entry label
                calculatedTaxEntry["text"] = "%.2f" % taxCalculated

                # Calculating the total amount including tax
                totalAmountEntry["text"] = "%.2f" % round(
                    subTotal + (float(calculatedTaxEntry["text"])), 1)

            # >>

            # Function to convert the default prices to and from INR for saving to Database
            def convertPrice_to_INR(price, request):

                # Confirming the request is 'convert' to INR
                if (request == "convert"):

                    # Converting the price from User's default preference to INR
                    convertedPrice = "%.2f" % (
                        float(price) * float(currencySelect_box["textvariable"]))

                elif (request == "revert"):

                    # Converting the price from INR to User's default preference
                    convertedPrice = "%.2f" % (
                        float(price) / float(currencySelect_box["textvariable"]))

                return float(convertedPrice)

            # >>

            # Function to reduce/refill the product quantity according to the number purchased
            def productQuantityUpdator(purchasedItems, previousItems):

                # Opening the ProductDetails Table in the User's Database
                productObj = ProductDetail(loggedInUser)

                if (previousItems != []):

                    for item1, item2 in zip(purchasedItems, previousItems):

                        # Querying the 'productDetails' table in the User's Database and picking only the matched product
                        productInList = productObj.get(filterby="productName",
                                                       productName=item1[1])

                        if (item1 != item2):

                            # Calculating the products remaining using the total product quantity in stocks Table and bought quantity
                            product_left = productInList[2] - \
                                (int(item1[2] - item2[2]))

                            # Updating the product quantity remaining
                            productObj.update(productInList[0],
                                              productInList[0],
                                              float(productInList[1]),
                                              int(product_left),
                                              float(productInList[3]),
                                              float(productInList[4]),
                                              int(productInList[5]),
                                              getBy="productName"
                                              )

                            # Checking the products remaining goes below the re-order quantity
                            if (product_left > 0 and product_left <= productInList[5]):

                                # Calculating the Re-filling quantity
                                refilling_quantity = int(productInList[5]) * 5

                                # Re-filling the product when it reach below the re-order quantity
                                productObj.update(productInList[0],
                                                  productInList[0],
                                                  float(productInList[1]),
                                                  int(refilling_quantity),
                                                  float(productInList[3]),
                                                  float(productInList[4]),
                                                  int(productInList[5]),
                                                  getBy="productName"
                                                  )

                else:

                    for item in purchasedItems:

                        # Querying the 'productDetails' table in the User's Database and picking only the matched product
                        productInList = productObj.get(filterby="productName",
                                                       productName=item[1])

                        # Calculating the products remaining using the total product quantity in stocks Table and bought quantity
                        product_left = productInList[2] - int(item[2])

                        # Updating the product quantity remaining
                        productObj.update(productInList[0],
                                          productInList[0],
                                          float(productInList[1]),
                                          int(product_left),
                                          float(productInList[3]),
                                          float(productInList[4]),
                                          int(productInList[5]),
                                          getBy="productName"
                                          )

                        # Checking the products remaining goes below the re-order quantity
                        if (product_left > 0 and product_left <= productInList[5]):

                            # Calculating the Re-filling quantity
                            refilling_quantity = int(productInList[5]) * 5

                            # Re-filling the product when it reach below the re-order quantity
                            productObj.update(productInList[0],
                                              productInList[0],
                                              float(productInList[1]),
                                              int(refilling_quantity),
                                              float(productInList[3]),
                                              float(productInList[4]),
                                              int(productInList[5]),
                                              getBy="productName"
                                              )

                # Closing the connection to the database
                productObj.closeDB()

                return True

            # >>

            # Function for saving the new InVoice to the User's Database and also as a word document
            def saveInVoice(tablerows=None, afterSave="", inVoiceID=None):

                # Checking all the important entries other than the fields in Product-Details Table are filled
                if (tablerows is None or clientSelect_box.get() == ""):

                    # Showing a error message
                    messagebox.showerror("in Voice",
                                         "Client and Product details can't be empty")

                    # Changing value of error response
                    response = False

                else:

                    # Creating a list to collect the Currency Code and Symbol
                    selectedCurrency = []

                    # Splitting the Currency Code from the selected option of Currency-Select Combobox and adding it to currency list
                    selectedCurrency.append(
                        currencySelect_box.get().split(" ")[1])

                    # Getting the Currency symbol and adding it to currency list
                    selectedCurrency.append(totalAmount_symbol["text"])

                    # Getting the selected option from Due-Select Combobox
                    selectedDue = dueSelect_box.get().split(" ")

                    # Parsing the date-object from the string of User picked or today's date
                    pickedDate = datetime.strptime(dateEntry_Var.get().split(" ")[0],
                                                   "%Y-%m-%d").date()

                    # Calculating the Due-Date and Balance-Amount from the selected value of Due-Select Combobox
                    if (selectedDue[1] != "Nil"):

                        # Calculating the Due-Date by counting the days picked with Date picked
                        dueDate = pickedDate + \
                            timedelta(days=int(selectedDue[1]))

                        # Converting the value got from Paid-Amount Entry to float
                        amountPaid = float(paidAmountEntry.get()) if (
                            paidAmountEntry.get() != "") else float(0)

                        # Calculating the Balance-Amount by reducing the Paid-Amount from the Total amount
                        balanceAmount = float(
                            totalAmountEntry["text"]) - amountPaid

                    else:

                        # Assigning the pickedDate as dueDate if selection is 'Nil'
                        dueDate = pickedDate

                        # Setting the Balance-Amount to zero
                        balanceAmount = float(0)

                    # Converting the value got from Tax-Percentage Entry to integer
                    taxIn_percent = int(taxEntry_box.get()) if (
                        taxEntry_box.get() != "") else 0

                    # Assigning empty variables to track the product details
                    count = 0
                    productsPicked = []
                    productsPicked_UC = []

                    for row in tablerows:

                        # Increasing the iteration count
                        count += 1

                        # Checking for the first and in-between product details is empty
                        if ((len(tablerows) != count and row[1].get() == "" and tablerows[count][1].get() != "") or (count == 1 and row[1].get() == "")
                            or (len(tablerows) != count and row[3].get() == "" and tablerows[count][3].get() != "") or (count == 1 and row[3].get() == "")
                                or (len(tablerows) != count and float(row[4].get())*1 == 0 and float(tablerows[count][4].get())*1 != 0) or (count == 1 and float(row[4].get())*1 == 0)):

                            # Showing a error message
                            messagebox.showerror(
                                "in Voice", "Product details can't be empty")

                            # Changing value of return response
                            response = False
                            break

                        # Checking for the first and in-between quantity is zero
                        elif ((len(tablerows) != count and int(row[3].get()) == 0 and int(tablerows[count][3].get()) != 0) or (count == 1 and int(row[3].get()) == 0)):

                            # Showing a error message
                            messagebox.showerror(
                                "in Voice", "Product quantity can't be zero")

                            # Changing value of return response
                            response = False
                            break

                        elif (row[1].get() != "" and row[3].get() != "" and int(row[3].get()) != 0 and float(row[4].get())*1 != 0):

                            # Opening the ProductDetails Table in the User's Database
                            productObj = ProductDetail(loggedInUser)

                            # Querying the 'productDetails' table in the User's Database and picking only the matched product
                            productExists = productObj.get(filterby="productName",
                                                           productName=row[1].get())

                            # Closing the connection to the database
                            productObj.closeDB()

                            if (productExists is None):

                                # Showing a error message
                                messagebox.showerror(
                                    "in Voice", f"Product: '{row[1].get()}' doesn't exists in stocks")

                                # Changing value of return response
                                response = False
                                break

                            else:

                                # Calculating the products remaining using the total product quantity in stocks Table and requested quantity
                                product_remains = productExists[2] - int(
                                    row[3].get())

                                # Checking the products remaining goes zero or below zero quantity
                                if (product_remains <= 0):

                                    # Showing a error message
                                    messagebox.showerror(
                                        "in Voice", f"Product: '{row[1].get()}' is probably Out-of-Stock to perform this request, because the order quantity({row[3].get()}) is more than the stock left({productExists[2]})")

                                    # Changing value of return response
                                    response = False
                                    break

                                else:

                                    # Calling the function to convert prices to INR
                                    rate_per_product = convertPrice_to_INR(
                                        row[4].get(), "convert")
                                    price_per_products = convertPrice_to_INR(
                                        row[5].get(), "convert")

                                    # Making a tuple with details about picked product
                                    product_pick = (str(row[0]["text"]),
                                                    str(row[1].get()),
                                                    int(row[3].get()),
                                                    rate_per_product,
                                                    price_per_products)

                                    # Creating a python list with the list of tuples created by product details
                                    productsPicked.append(product_pick)

                                    # Making a tuple with unconverted prices of the picked product
                                    productpick_UC = (str(row[0]["text"]),
                                                      str(row[1].get()),
                                                      int(row[3].get()),
                                                      float(row[4].get()),
                                                      float(row[5].get()))

                                    # Creating a python list with the list of tuples created with product details of unconverted price
                                    productsPicked_UC.append(productpick_UC)

                                    # Changing value of return response
                                    response = True

                    # Checking the value of response returned from loop to make further progress
                    if (response):

                        # Calling the function to convert prices to INR before saving
                        subTotal_C = convertPrice_to_INR(
                            subtotalEntry["text"], "convert")
                        calculatedTax_C = convertPrice_to_INR(
                            calculatedTaxEntry["text"], "convert")
                        totalAmount_C = convertPrice_to_INR(
                            totalAmountEntry["text"], "convert")
                        balanceAmount_C = convertPrice_to_INR(
                            balanceAmount, "convert")

                        # Checking the after-save request is from Close(X) Button or Save-InVoice Button
                        button_click = messagebox.askyesno(
                            "in Voice", "Before pressing 'yes', make sure the data are correct") if (afterSave != "quit") else afterSave

                        # Validating the value of request as 'yes' and starting the saving process
                        if (button_click):

                            # Opening the InVoiceDetails Table in the User's Database
                            inVoiceObj = InVoiceDetail(loggedInUser)

                            if (request != "view" and inVoiceID is None):

                                # Adding InVoice data into 'inVoiceDetails' table in the User's Database
                                inVoiceObj.create(inVoiceNumberEntry_Var.get(),
                                                  clientSelect_box.get(),
                                                  selectedCurrency[0],
                                                  selectedCurrency[1],
                                                  pickedDate,
                                                  dueDate,
                                                  productsPicked,
                                                  customernoteEntry.get(
                                                      1.0, "end-1c"),
                                                  taxIn_percent,
                                                  subTotal_C,
                                                  calculatedTax_C,
                                                  totalAmount_C,
                                                  balanceAmount_C
                                                  )

                                # Creating a empty list
                                previousRecord = []

                            elif (request == "view" and inVoiceID is not None):

                                # Querying the 'inVoiceDetails' table in the User's database and picking the matched inVoice's product details
                                previousRecord = inVoiceObj.get(inVoiceID)[6]

                                # Updating a existing product details to the Table
                                inVoiceObj.update(inVoiceID,
                                                  clientSelect_box.get(),
                                                  selectedCurrency[0],
                                                  selectedCurrency[1],
                                                  pickedDate,
                                                  dueDate,
                                                  productsPicked,
                                                  customernoteEntry.get(
                                                      1.0, "end-1c"),
                                                  taxIn_percent,
                                                  subTotal_C,
                                                  calculatedTax_C,
                                                  totalAmount_C,
                                                  balanceAmount_C
                                                  )

                            # Saving and Closing the connection to the database
                            inVoiceObj.closeDB()

                            # Opening the ClientDetail Table in the User's Database
                            clientObj = ClientDetail(loggedInUser)

                            # Getting the index of Client name selected
                            clientIndex = str(clientSelect_box["values"].index(
                                clientSelect_box.get()) + 1)

                            # Generating a word document with the InVoice data
                            wordDocGenerator(inVoiceNumberEntry_Var.get(),
                                             clientObj.get(clientIndex),
                                             pickedDate,
                                             dueDate,
                                             selectedCurrency[1],
                                             productsPicked_UC,
                                             float(subtotalEntry["text"]),
                                             float(calculatedTaxEntry["text"]),
                                             float(totalAmountEntry["text"]),
                                             float("%.2f" % (balanceAmount)),
                                             customernoteEntry.get(
                                                 1.0, "end-1c")
                                             )

                            # Closing the connection with the Database
                            clientObj.closeDB()

                            # Calling the function to reduce the product quantity according to the number purchased
                            updated = productQuantityUpdator(
                                productsPicked, previousRecord)

                            if (updated):

                                # Re-setting the Close(X) Button to default
                                close_X_btn.configure(
                                    command=lambda: closeInVoiceAPP())

                                if (afterSave != "quit"):

                                    # Calling the function to redirect to `(in Voice)` WorkSpace
                                    redirectToWorkSpace(tabLink2)

                        else:

                            # Changing value of return response
                            response = False

                return response

            # >>

            # Function for which is operated by Close(X) Button and that asks for confirmation to save the InVoice before Quitting
            def save_CloseInVoiceApp(tablerows, inVoiceId=None):

                # Disabling the Close(X) Button after clicked, for preventing the function to be called twice
                close_X_btn.configure(state=DISABLED)

                # Showing a confirmation dialog with some message
                button_click = messagebox.askyesnocancel("in Voice",
                                                         "Save & Close, Do you want to save the invoice?")

                # Confirming the answer is either 'yes' or 'no'
                if (button_click or button_click is False):

                    # Confirming the answer is only 'yes'
                    if (button_click):

                        # Calling the function to save the InVoice in the User's Database
                        responsed = saveInVoice(
                            tablerows, afterSave="quit", inVoiceID=inVoiceId)

                    if (button_click is False or responsed):

                        # Clearing the --- `(in Voice)` --- cache folder and its files
                        UserCredential.createHiddenDIR(
                            UserCredential, "./.__appcache__", "clearCache")

                        # Closing the --- `(in Voice)` ---
                        root.after(500, lambda: root.destroy())

                    elif (responsed is False):

                        # Re-enabling the Close(X) Button when Save request failed
                        close_X_btn.configure(state=NORMAL)

                else:

                    # Re-enabling the Close(X) Button when 'cancel' is pressed
                    close_X_btn.configure(state=NORMAL)

            # >>

            # Function which is operated by Edit-InVoice Button to edit the inVoice details queried from the Database
            def editInVoice(allBoxes, ProductsData, inVoiceID):

                # Disabling the Edit-InVoice Button after clicked, for preventing the function to be called twice
                editInVoice_btn.configure(state=DISABLED)

                # Calling the function to limit the Tab-Link Buttons by asking for confirmation before switching Tabs
                leftPanelExpand_disabler("Update")

                # Showing again the hidden buttons in the View-InVoice Panel
                calendarButton.lift()
                addRowButton.lift()

                # Enabing back the comboboxes and entries in the View-InVoice Panel
                for box in allBoxes:

                    # Re-settings the state and cursor of the Comboboxes to default
                    if (box[1] is None and box[2] != "Customer-Message"):
                        box[0].configure(cursor="hand2", state="readonly")

                    # Re-settings the state and cursor of specific Entries to default
                    if (box[2] == "Customer-Message" or box[2] == "Amount Paid" or box[2] == "Tax (%)"):
                        box[0].configure(cursor="xterm", state=NORMAL)

                # Destroying the Delete-InVoice Button created to delete this inVoice details
                deleteInVoice_btn.destroy()

                # Removing the mouse left-click delete functions assigned to the Widgets in the View-InVoice Panel
                customernoteEntry.unbind("<Button-1>")
                taxEntry_box.unbind("<Button-1>")
                paidAmountEntry.unbind("<Button-1>")

                # Enabling back the Entries in all the rows of Product-Details Table
                for entry in ProductsData:

                    entry[2].configure(cursor="xterm", state=NORMAL)
                    entry[6].configure(cursor="xterm", state=NORMAL)
                    entry[7].configure(cursor="xterm", state=NORMAL)

                # Enabling and changing the arguments of the function assigned with the Edit-InVoice Button and also changing the text on the button to 'Save'
                createInVoice_frame.after(200, lambda: editInVoice_btn.configure(text="Update", image=inVoice_obj, state=NORMAL,
                                                                                 command=lambda: saveInVoice(ProductsData, "Update", inVoiceID)))

                # Changing the function assigned with the Close(X) Button
                close_X_btn.configure(
                    command=lambda: save_CloseInVoiceApp(ProductsData, inVoiceID))

            # >>

            # Function which is operated by Delete-InVoice Button to delete the inVoice details from the Database
            def deleteInVoice(inVoiceID):

               # Showing a confirmation dialog with some message
                deleteRequest = messagebox.askyesno(
                    "in Voice", "Delete InVoice, Are you sure you want to delete inVoice details?")

                if (deleteRequest):

                    # Opening the InVoiceDetail Table in the User's Database
                    user_DataBase = InVoiceDetail(loggedInUser)

                    # Deleting a specific inVoice from the Table
                    user_DataBase.delete(inVoiceID)

                    # Commiting and Closing the connection with the Database
                    user_DataBase.closeDB()

                    # Calling the function to redirect to `(in Voice)` WorkSpace
                    redirectToWorkSpace(tabLink2)

            # >>

            # ------------------------------------- Create-InVoice Panel -StyleStarts----------------------------------------------------

            # Creating a frame for the Create-InVoice Panel and positioning it on Right-Bottom Panel
            createInVoice_frame = Frame(workSpace_rightFrame, height=int(screen_height/1.044),
                                        width=int(screen_width-(screen_width/15.1)))
            createInVoice_frame.place(relx=1, rely=1, anchor=SE)

            # Creating a label to set a background color for the Create-InVoice Panel
            createInVoice_bgColor = Label(createInVoice_frame, background="#B3C6E7",
                                          width=int(screen_width/4.6))
            createInVoice_bgColor.place(relx=0.5, rely=0.5,
                                        height=int(screen_height/1), anchor=CENTER)

            # Assigning the common colors for Create-InVoice Panel
            createInVoice_innerbG = "#F0EFF4"
            createInVoice_innerfG = leftTop_bG

            # Creating a label to set a background color for the Inner Create-InVoice Panel
            createInVoice_innerbgColor = Label(createInVoice_frame, background=createInVoice_innerbG,
                                               width=int(screen_width/6.75))
            createInVoice_innerbgColor.place(relx=0.5, rely=0.5,
                                             height=int(screen_height/1.1), anchor=CENTER)

            # Creating a empty list to contain the Entries and Comboboxes in the Create-InVoice Panel
            all_Boxes = []

            #        -------------------------------------
            # -------------- Client-Select Combobox ---------------
            #        -------------------------------------

            # Styling all the Create Panel Comboboxes
            createPanel_selectBox_style = Style(createInVoice_frame)
            createPanel_selectBox_style.theme_use("default")
            createPanel_selectBox_style.configure("CreatePanel-Select.TCombobox", arrowsize=18,
                                                  background=tableHeader_bG)
            # Mouse Hovering style for Create Panel Comboboxes
            createPanel_selectBox_style.map("CreatePanel-Select.TCombobox", background=[("readonly", "focus", tableHeader_bG)], foreground=[("disabled", "!focus", "#0A0908")],
                                            selectbackground=[("readonly", "!focus", "none"), ("readonly", "focus", "none")], selectforeground=[("readonly", "focus", "#0A0908"), ("readonly", "!focus", createInVoice_innerfG)],
                                            fieldbackground=[("readonly", "!focus", "#FFFFFF"), ("readonly", "focus", "#FFFFFF")], arrowsize=[("disabled", "!focus", 0)])

            # Creating the Client-Select Combobox to pick the Client from the dropdown
            clientSelect_box = Combobox(createInVoice_frame, font=("Dodge", 10, "bold"), style="CreatePanel-Select.TCombobox",
                                        cursor="hand2", width=int(screen_width/25), state="readonly")
            clientSelect_box.place(relx=0.09, rely=0.125,
                                   height=int(screen_height/25), anchor=W)

            # Client-Combobox label
            clientSelect_box_label = Label(createInVoice_frame, text="Client", font=("Dodge", 14),
                                           background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            clientSelect_box_label.place(relx=0.13, rely=0.075, anchor=CENTER)

            # Calling the function to populate the Client-Select Combobox
            populate_Box_or_Entry(
                object=ClientDetail,
                widget=clientSelect_box,
                label=clientSelect_box_label["text"]
            )

            # Adding the Widgets related to Client-Select Combobox to All-Boxes list
            all_Boxes.append((
                clientSelect_box,
                None,
                clientSelect_box_label["text"]
            ))

            #        -------------------------------------
            # -------------- InVoice-Number Entry ---------------
            #        -------------------------------------

            # Creating the InVoice-Number Entry to hold the generated inVoice number
            inVoiceNumberEntry_Var = StringVar(createInVoice_frame)
            inVoiceNumberEntry = tk.Entry(createInVoice_frame, textvariable=inVoiceNumberEntry_Var, font=("Dodge", 13, "bold"), width=int(screen_width/80),
                                          disabledbackground="#FFFFFF", disabledforeground="#0A0908", highlightbackground=tableHeader_bG, highlightthickness=2, borderwidth=0, cursor="arrow", state=DISABLED, justify=RIGHT)
            inVoiceNumberEntry.place(relx=0.85, rely=0.125,
                                     height=int(screen_height/25), anchor=CENTER)

            # InVoice-Entry label
            inVoiceNumberEntry_label = Label(createInVoice_frame, text="InVoice No.", font=("Dodge", 14),
                                             background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            inVoiceNumberEntry_label.place(
                relx=0.83, rely=0.075, anchor=CENTER)

            # Calling the function to populate the InVoice-Entry with unique InVoice number
            populate_Box_or_Entry(
                object=InVoiceDetail,
                widget=inVoiceNumberEntry_Var,
                label=inVoiceNumberEntry_label["text"]
            )

            # Adding the Widgets related to InVoice-Number Entry to All-Boxes list
            all_Boxes.append((
                inVoiceNumberEntry,
                inVoiceNumberEntry_Var,
                inVoiceNumberEntry_label["text"]
            ))

            #        -------------------------------------
            # ------------- Currency-Select Combobox ---------------
            #        -------------------------------------

            # Creating the Currency-Select Combobox to pick the Currency from the dropdown
            currencySelect_box = Combobox(createInVoice_frame, font=("Dodge", 10, "bold"), style="CreatePanel-Select.TCombobox",
                                          cursor="hand2", width=int(screen_width/40), state="readonly")
            currencySelect_box.place(relx=0.09, rely=0.275,
                                     height=int(screen_height/30), anchor=W)

            # Currency-Combobox label
            currencySelect_box_label = Label(createInVoice_frame, text="Currency", font=("Dodge", 14),
                                             background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            currencySelect_box_label.place(relx=0.14, rely=0.225,
                                           anchor=CENTER)

            # Adding the Widgets related to Currency-Select Combobox to All-Boxes list
            all_Boxes.append((
                currencySelect_box,
                None,
                currencySelect_box_label["text"]
            ))

            #       ---------------------------------
            # ---------------- Date Entry ----------------
            #       ---------------------------------

            # Getting the today's date and assigning it to a variable
            todaysDate = datetime.today().date()

            # Creating the Date Entry and Setting the Today's date as default value
            dateEntry_Var = StringVar(createInVoice_frame, f"{todaysDate} ")
            dateEntry = tk.Entry(createInVoice_frame, textvariable=dateEntry_Var, font=("Dodge", 12, "bold"), width=int(screen_width/80),
                                 disabledbackground="#FFFFFF", disabledforeground="#0A0908", borderwidth=1, cursor="arrow", state=DISABLED, justify=RIGHT)
            dateEntry.place(relx=0.5, rely=0.275,
                            height=int(screen_height/25), anchor=CENTER)

            # Styling the Calendar Button
            calendarButton_style = Style()
            calendarButton_style.theme_use("default")
            calendarButton_style.configure("Calendar.TButton", font=("Playball", 16, "italic"), background=createInVoice_innerbG,
                                           foreground=createInVoice_innerfG, borderwidth=0, width=6, focuscolor="none", relief=FLAT, highlightthickness=0)
            # Mouse Hovering style for Calendar Button
            calendarButton_style.map("Calendar.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                     background=[("active", "#D3D3D2")])

            # Resizing the -- Calendar -- image and converting it into a object to display on a widget
            global calendar_obj
            calendar_obj = ImageTk.PhotoImage(calendar_icon.resize((35, 35),
                                                                   resampling_filter))

            # Creating a Calendar Button for Users to open Month-Calendar and pick their desired date instead of current date in Date Entry
            calendarButton = Button(createInVoice_frame, image=calendar_obj, style="Calendar.TButton",
                                    cursor="hand2", command=lambda: openCalendar())
            calendarButton.place(relx=0.59, rely=0.275, anchor=CENTER)

            # Date-Entry label
            dateEntry_label = Label(createInVoice_frame, text="Date", font=("Dodge", 14),
                                    background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            dateEntry_label.place(relx=0.47, rely=0.225, anchor=CENTER)

            # Adding the Widgets related to Date Entry to All-Boxes list
            all_Boxes.append((
                dateEntry,
                dateEntry_Var,
                dateEntry_label["text"]
            ))

            #        -------------------------------------
            # ------------- DueDate-Select Combobox ---------------
            #        -------------------------------------

            # Creating a DueDate-Select Combobox to pick the number of days from the dropdown
            dueSelect_box = Combobox(createInVoice_frame, font=("Dodge", 10, "bold"), style="CreatePanel-Select.TCombobox",
                                     cursor="hand2", width=int(screen_width/80), state="readonly")
            dueSelect_box.place(relx=0.8, rely=0.275,
                                height=int(screen_height/30), anchor=W)

            # DueDate-Combobox label
            dueSelect_box_label = Label(createInVoice_frame, text="Due", font=("Dodge", 14),
                                        background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            dueSelect_box_label.place(relx=0.82, rely=0.225, anchor=CENTER)

            # Calling the function to populate the Currency-Select Combobox and also setting the default value
            populate_Box_or_Entry(
                object=DueDate,
                widget=dueSelect_box,
                label=dueSelect_box_label["text"]
            )

            # Assigning a function to DueDate-Select Combobox to track the selection
            dueSelect_box.bind("<<ComboboxSelected>>",
                               lambda event: dueValueCalculator(event))

            # Adding the Widgets related to DueDate-Select Combobox to All-Boxes list
            all_Boxes.append((
                dueSelect_box,
                None,
                dueSelect_box_label["text"]
            ))

            #        -------------------------------------
            # ------------- Product-Details Table ---------------
            #        -------------------------------------

            # Creating a frame for the Product-Details Table Header
            productsTableHeader = Frame(createInVoice_frame, height=int(screen_height/10),
                                        width=int(screen_width-(screen_width/5.5)))
            productsTableHeader.place(relx=0.5, rely=0.425, anchor=CENTER)

            # Creating a label to set a background color for the Product-Details Table Header
            productsTableHeader_bgColor = Label(productsTableHeader,
                                                background=tableHeader_bG)
            productsTableHeader_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/10),
                                              width=int(screen_width-(screen_width/5.5)), anchor=CENTER)

            # Creating the headings for the Product-Details Table Header
            productsTable_heading1 = Label(productsTableHeader, text="#", font=("Dodge", 14, "bold"),
                                           background=tableHeader_bG, anchor=CENTER)
            productsTable_heading1.place(relx=0.04, rely=0.3, anchor=N)
            productsTable_heading2 = Label(productsTableHeader, text="Description", font=("Dodge", 14, "bold"),
                                           background=tableHeader_bG, anchor=CENTER)
            productsTable_heading2.place(relx=0.2, rely=0.3, anchor=N)
            productsTable_heading3 = Label(productsTableHeader, text="Qty", font=("Dodge", 14, "bold"),
                                           background=tableHeader_bG, anchor=CENTER)
            productsTable_heading3.place(relx=0.6, rely=0.3, anchor=N)
            productsTable_heading4_sym = Label(productsTableHeader, font=("Dodge", 14, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
            productsTable_heading4_sym.place(relx=0.778, rely=0.3, anchor=N)
            productsTable_heading4 = Label(productsTableHeader, text="Rate", font=("Dodge", 14, "bold"),
                                           background=tableHeader_bG, anchor=CENTER)
            productsTable_heading4.place(relx=0.738, rely=0.3, anchor=N)
            productsTable_heading5_sym = Label(productsTableHeader, font=("Dodge", 14, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
            productsTable_heading5_sym.place(relx=0.96, rely=0.3, anchor=N)
            productsTable_heading5 = Label(productsTableHeader, text="Amount", font=("Dodge", 14, "bold"),
                                           background=tableHeader_bG, anchor=CENTER)
            productsTable_heading5.place(relx=0.9, rely=0.3, anchor=N)

            # Creating a frame for the Product-Details Table Body
            productsTable_body = Frame(createInVoice_frame, height=int(screen_height/7),
                                       width=int(screen_width-(screen_width/5.5)))
            productsTable_body.place(relx=0.5, rely=0.575, anchor=CENTER)

            # Creating a label to set a background color for the Product-Details Table Body
            productsTable_body_bgColor = Label(productsTable_body,
                                               background="#C2C5AA")
            productsTable_body_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/7),
                                             width=int(screen_width-(screen_width/5.5)), anchor=CENTER)

            # Assigning a common background color for Product-Details Table Body
            productsTable_bgColor = "#C2C5AA"

            # Creating a canvas widget for making a scrollable table
            productsTable_body_canvas = Canvas(productsTable_body, background=productsTable_bgColor, height=int(screen_height/7),
                                               width=int(screen_width-(screen_width/5.5)), borderwidth=0, highlightthickness=0)
            productsTable_body_canvas.pack(side=LEFT, fill=BOTH, expand=True)

            # Creating a frame to place the Entry fields
            productsTable_body_frame = Frame(productsTable_body_canvas,
                                             width=int(screen_width-(screen_width/5.5)))

            # Creating a label to set a background color for the Product-Details Table Entry fields frame
            productsTable_field_bgColor = Label(productsTable_body_frame,
                                                background=productsTable_bgColor)
            productsTable_field_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height*20),
                                              width=int(screen_width-(screen_width/5.5)), anchor=CENTER)

            # Creating scrollbar to scroll the fields in the Product-Details Table
            productsTable_scrollbar = Scrollbar(productsTable_body, orient="vertical",
                                                command=productsTable_body_canvas.yview)
            productsTable_body_canvas.configure(
                yscrollcommand=productsTable_scrollbar.set)

            # Placing the frame created for the Entry fields on the canvas widget
            productsTable_body_canvas.create_window((4, 4), window=productsTable_body_frame,
                                                    anchor=S)
            productsTable_body_frame.bind("<Configure>",
                                          lambda event, productsTable_body_canvas=productsTable_body_canvas: onFrameConfigure(productsTable_body_canvas))

            # Assigning a function to scroll the Product-Details Table canvas widget along with the mouse wheel
            productsTable_body_canvas.bind(
                "<MouseWheel>", scrollProductsDetail)
            productsTable_field_bgColor.bind(
                "<MouseWheel>", scrollProductsDetail)

            #      -----------------------------------
            # -------------- Add-Row Button ---------------
            #      -----------------------------------

            # Styling the Add-Row Button
            addRowButton_style = Style(createInVoice_frame)
            addRowButton_style.theme_use("default")
            addRowButton_style.configure("Add-Row.TButton", font=("Dodge", 10, "bold", "italic"), foreground="#B3C6E7",
                                         background="#073B4C", borderwidth=3, focuscolor="none", justify=CENTER)
            # Mouse Hovering style for Add-Row Button
            addRowButton_style.map("Add-Row.TButton", font=[("active", "!disabled", ("Dodge", 11, "bold"))],
                                   foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

            # Creating a Add-Row Button to add new row in the Products-Details Table
            addRowButton = Button(createInVoice_frame, text="Add row", style="Add-Row.TButton",
                                  command=lambda: addNewRow(itemNo=1))
            addRowButton.place(relx=0.1, rely=0.675, anchor=CENTER)

            #      ------------------------------------
            # ------------ Customer-Message Box ---------------
            #      ------------------------------------

            # Creating a Customer-Message Box for sending short message to their clients
            customernoteEntry = scrolledtext.ScrolledText(createInVoice_frame, font=("Dodge", 12, "italic"),
                                                          width=int(screen_width/35), height=int(screen_height/120), wrap=WORD)
            customernoteEntry.place(relx=0.1, rely=0.895, anchor=SW)
            customernoteEntry.insert(INSERT, "Your message here!")

            # Assigning a function to DueDate-Select Combobox to track the selection for populate the Customer-Message Box with the default value
            clientSelect_box.bind("<<ComboboxSelected>>",
                                  lambda event, object=ClientDetail, widget=customernoteEntry, label="Customer-Message": populate_Box_or_Entry(object, widget, label))

            # Assigning a function for deleting the pre-occupied message in the Customer-Message Box
            customernoteEntry.bind("<Button-1>",
                                   lambda event, box=customernoteEntry, index=1.0: deletePrefilledContent(event, box, index))

            # Adding the Widgets related to Customer-Message Box to All-Boxes list
            all_Boxes.append((
                customernoteEntry,
                None,
                "Customer-Message"
            ))

            #      ----------------------------------
            # ------------ SubTotal-Entry ---------------
            #      ----------------------------------

            # Assigning a common value for Amount Entries in Create-InVoice Panel
            initial_amount = "%.2f" % 0

            # Creating a SubTotal-Entry label to show the Subtotal value of all the products
            subtotalEntry = Label(createInVoice_frame, text=initial_amount, font=("Dodge", 12, "bold"),
                                  background=createInVoice_innerbG, foreground="#0A0908")
            subtotalEntry.place(relx=0.85, rely=0.735, anchor=CENTER)

            # SubTotal-Entry label
            subtotalEntry_label = Label(createInVoice_frame, text="Subtotal", font=("Dodge", 12),
                                        background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            subtotalEntry_label.place(relx=0.71, rely=0.735, anchor=CENTER)

            #    ----------------------------------------------
            # ------- Tax-Percentage Entry & Calculated-Tax -------
            #    ----------------------------------------------

            # Creating a Tax-Percentage Entry for User to manually change tax value
            taxEntry_box_Var = StringVar()
            taxEntry_box = tk.Entry(createInVoice_frame, textvariable=taxEntry_box_Var, font=("Dodge", 12, "bold"),
                                    width=int(screen_width/280), disabledbackground="#FFFFFF", disabledforeground="#0A0908", borderwidth=2, justify=RIGHT)
            taxEntry_box.place(relx=0.74, rely=0.785,
                               height=int(screen_height/25), anchor=CENTER)

            # TaxPercentage-Entry label
            taxEntry_label = Label(createInVoice_frame, text="Tax (%)", font=("Dodge", 11),
                                   background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            taxEntry_label.place(relx=0.7, rely=0.785, anchor=CENTER)

            # Calling the function to populate the Tax-Percentage Entry with the default value
            populate_Box_or_Entry(
                object=UserPreference,
                widget=taxEntry_box_Var,
                label=taxEntry_label["text"]
            )

            # Assigning a function for deleting the pre-occupied tax value in the Tax-Percentage Entry
            taxEntry_box.bind("<Button-1>",
                              lambda event, box=taxEntry_box, index=0: deletePrefilledContent(event, box, index))

            # Assigning a function to validate the Tax-Percentage Entry and also calculate the total amount by adding the tax
            taxEntry_box_Var.trace_add("write", taxEntryValidator)

            # Creating a Calculated-Tax label to show the calculated tax for the subtotal
            calculatedTaxEntry = Label(createInVoice_frame, text=initial_amount, font=("Dodge", 12, "bold"),
                                       background=createInVoice_innerbG, foreground="#0A0908")
            calculatedTaxEntry.place(relx=0.85, rely=0.785, anchor=CENTER)

            # Adding the Widgets related to Tax-Percentage Entry to All-Boxes list
            all_Boxes.append((
                taxEntry_box,
                taxEntry_box_Var,
                taxEntry_label["text"]
            ))

            #       ------------------------------------
            # -------------- Total-Amount Entry ---------------
            #       ------------------------------------

            # Creating a Total-Amount's symbol label for showing the currency in which amount is calculated
            totalAmount_symbol = Label(createInVoice_frame, font=("Dodge", 16, "bold"),
                                       background=createInVoice_innerbG, foreground=createInVoice_innerfG)
            totalAmount_symbol.place(relx=0.938, rely=0.865, anchor=E)

            # Creating a frame for the Total Amount Entry
            totalAmount_frame = tk.Frame(createInVoice_frame, height=int(screen_height/15),
                                         width=int(screen_width-(screen_width/1.3)), highlightbackground=createInVoice_innerfG, highlightthickness=2)
            totalAmount_frame.place(relx=0.78, rely=0.865, anchor=CENTER)

            # Styling the Total-Amount Entry
            totalAmountEntry_style = Style(createInVoice_frame)
            totalAmountEntry_style.theme_use("default")
            totalAmountEntry_style.configure("totalAmount.TLabel", font=("Dodge", 8, "bold"),
                                             background=createInVoice_innerbG, foreground="#0A0908", anchor=CENTER)

            # Creating a Total-Amount Entry label to showing total amount including tax
            totalAmountEntry = Label(createInVoice_frame, text=initial_amount, font=("Dodge", 15, "bold"),
                                     style="totalAmount.TLabel")
            totalAmountEntry.place(relx=0.872, rely=0.865, anchor=E)

            # TotalAmount-Entry label
            totalAmountEntry_label = Label(totalAmount_frame, text="Total", font=("Dodge", 14, "bold"),
                                           foreground="#B3C6E7", background=createInVoice_innerfG, anchor=CENTER)
            totalAmountEntry_label.place(relx=0, rely=0.5, height=int(screen_height/15),
                                         width=int(screen_width-(screen_width/1.08)), anchor=W)

            # Calling the function to populate the Currency-Select Combobox and also setting the default Currency Symbols in the Create-InVoice Panel
            populate_Box_or_Entry(
                object=CurrencyRate,
                widget=currencySelect_box,
                label=currencySelect_box_label["text"]
            )

            if (request != "view"):

                # Calling the function to add the very first row to the Product-Details Table
                root.after(100, lambda: addNewRow())

                #       ------------------------------------
                # -------------- Save-InVoice Button ---------------
                #       ------------------------------------

                # Styling the Save-InVoice Button
                saveInVoice_btn_style = Style(createInVoice_frame)
                saveInVoice_btn_style.theme_use("default")
                saveInVoice_btn_style.configure("Save-InVoice.TButton", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background="#2D361C",
                                                borderwidth=3, focuscolor="none", justify=CENTER)
                # Mouse Hovering style for Save-InVoice Button
                saveInVoice_btn_style.map("Save-InVoice.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))],
                                          foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

                # Creating a Save-InVoice Button to save the created InVoice
                saveInVoice_btn = Button(createInVoice_frame, text="Save", image=inVoice_obj, compound=LEFT,
                                         style="Save-InVoice.TButton", command=lambda: saveInVoice())
                saveInVoice_btn.place(relx=0.5, rely=0.895, anchor=CENTER)

            # Checking the request to view the existing inVoice detail
            elif (request == "view"):

                # Getting the inVoice details according to the field selection
                inVoiceID = tableFields.item(
                    tableFields.focus())["values"][0]

                # ------------------------------------- View-InVoice Panel -StyleStarts---------------------------------------

                # Opening the InVoiceDetails Table in the User's Database
                inVoiceObj = InVoiceDetail(loggedInUser)

                # Querying the 'inVoiceDetails' table in the User's database and picking the matched inVoice details
                inVoiceRecord = inVoiceObj.get(inVoiceID)

                # Closing the connection with the Database
                inVoiceObj.closeDB()

                if (inVoiceRecord is not None):

                    # Opening the CurrencyRates Table in the User's Database
                    currencyObj = CurrencyRate(loggedInUser)

                    # Querying the 'currencyRates' table in the User's database and picking all the records of currency
                    all_currencies = currencyObj.all()

                    # Closing the connection with the Database
                    currencyObj.closeDB()

                    # Setting the exchange value for Currency-Select Combobox according to the Currency Code
                    currencySelect_box["textvariable"] = [
                        item[4] for item in all_currencies if item[0] == inVoiceRecord[2]][0] if (all_currencies != []) else 1

                    # Settings the default Currency Symbols in labels of View-InVoice Panel
                    productsTable_heading4_sym.configure(text=inVoiceRecord[3])
                    productsTable_heading5_sym.configure(text=inVoiceRecord[3])
                    totalAmount_symbol.configure(text=inVoiceRecord[3])

                    # Creating a empty list for holding the widgets created on every row inside the Product-Details Table
                    rowsInTable = []

                    row_count = 0
                    for field in inVoiceRecord[6]:

                        # Creating the new rows according to the number of products
                        rowsInTable = addNewRow(row_count, rowsInTable)

                        # Populating the rows inside the Product-Details Table with values from the queryed InVoice
                        rowsInTable[row_count][1].set(field[1])
                        rowsInTable[row_count][3].set(field[2])
                        rowsInTable[row_count][4].set(
                            convertPrice_to_INR(field[3], "revert"))

                        # Disabling the Entries in all the rows of Product-Details Table
                        rowsInTable[row_count][2].configure(
                            cursor="arrow", state=DISABLED)
                        rowsInTable[row_count][6].configure(
                            cursor="arrow", state=DISABLED)
                        rowsInTable[row_count][7].configure(
                            cursor="arrow", state=DISABLED)

                        # Increasing the iteration count
                        row_count += 1

                    # Iterating through each boxes in the Create-InVoice Panel to populate them with the values from the queryed InVoice
                    for box in all_Boxes:

                        # Hiding the buttons in the View-InVoice Panel
                        calendarButton.lower()
                        addRowButton.lower()

                        # Confirming the widgets are a valid Combobox
                        if (box[1] is None):

                            # Settings the default value for Client-Select Combobox
                            if (box[2] == "Client"):
                                box[0].current(
                                    box[0]["values"].index(inVoiceRecord[1]))

                            # Settings the default value for Currency-Select Combobox
                            if (box[2] == "Currency"):

                                currency_used = f" {inVoiceRecord[2]} {inVoiceRecord[3]}" if (
                                    inVoiceRecord[2] != "CHF") else f" {inVoiceRecord[2]}"
                                box[0].current(
                                    box[0]["values"].index(currency_used))

                            # Settings the default value for DueDate-Select Combobox
                            if (box[2] == "Due"):

                                # Calculating the due days from the date picked
                                date_past = datetime.strptime(inVoiceRecord[4].split(" ")[0],
                                                              "%Y-%m-%d").date()

                                date_future = datetime.strptime(inVoiceRecord[5].split(" ")[0],
                                                                "%Y-%m-%d").date()
                                days_till = (date_future - date_past).days

                                # Gererating a string of text according to the remaining day count
                                due_in_days = f" {days_till} days" if (
                                    days_till != 0) else f" Nil"
                                box[0].current(
                                    box[0]["values"].index(due_in_days))

                            # Settings the default value for Customer-Message Box
                            if (box[2] == "Customer-Message"):

                                # Deleting and Inserting the saved message
                                box[0].configure(state=NORMAL)
                                box[0].delete(1.0, END)
                                box[0].insert(INSERT, inVoiceRecord[7])

                        # Confirming the widgets are a valid Entry
                        if (box[1] is not None):

                            # Settings the default value for InVoice-Number Entry
                            if (box[2] == "InVoice No."):
                                box[1].set(inVoiceRecord[0])

                            # Settings the default value for Date Entry
                            if (box[2] == "Date"):
                                box[1].set(f"{inVoiceRecord[4]} ")

                            # Settings the default value for Paid-Amount Entry
                            if (box[2] == "Amount Paid"):
                                box[1].set(convertPrice_to_INR(
                                    inVoiceRecord[11]-inVoiceRecord[12], "revert"))

                            # Settings the default value for Tax-Percentage Entry
                            if (box[2] == "Tax (%)"):
                                box[1].set(inVoiceRecord[8])

                        # Disabling all the Comboboxes and Entries in the View-InVoice Panel
                        box[0].configure(cursor="arrow", state=DISABLED)

                    #       ------------------------------------
                    # -------------- Edit-InVoice Button ---------------
                    #       ------------------------------------

                    # Styling the Edit-InVoice Button
                    editInVoice_btn_style = Style(createInVoice_frame)
                    editInVoice_btn_style.theme_use("default")
                    editInVoice_btn_style.configure("Edit-InVoice.TButton", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background="#2D361C",
                                                    borderwidth=3, width=6, focuscolor="none", justify=CENTER)
                    # Changing the mapping style of Edit-InVoice Button
                    editInVoice_btn_style.map("Edit-InVoice.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))],
                                              foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

                    # Resizing the -- Edit -- image and converting it into a object to display on a widget
                    global edit_obj
                    edit_obj = ImageTk.PhotoImage(edit_icon.resize((30, 30),
                                                                   resampling_filter))

                    # Creating a Edit-InVoice Button for editing existing the inVoice details
                    editInVoice_btn = Button(createInVoice_frame, text="edit", image=edit_obj, compound=LEFT,
                                             style="Edit-InVoice.TButton", command=lambda: editInVoice(all_Boxes, rowsInTable, inVoiceID))
                    editInVoice_btn.place(relx=0.5, rely=0.895, anchor=CENTER)

                    #       ------------------------------------
                    # -------------- Delete-InVoice Button ---------------
                    #       ------------------------------------

                    # Styling the Delete-InVoice Button
                    deleteInVoice_btn_style = Style()
                    deleteInVoice_btn_style.theme_use("default")
                    deleteInVoice_btn_style.configure("Delete-InVoice.TButton", background=createInVoice_innerbG, foreground=createInVoice_innerfG,
                                                      borderwidth=0, focuscolor="none", relief=FLAT, highlightthickness=0)
                    # Mouse Hovering style for Delete-InVoice Button
                    deleteInVoice_btn_style.map("Delete-InVoice.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                                background=[("active", createInVoice_innerbG)])

                    # Resizing the -- Delete -- image and converting it into a object to display on a widget
                    global delete_obj
                    delete_obj = ImageTk.PhotoImage(delete_icon.resize((30, 30),
                                                                       resampling_filter))

                    # Adding a delete button for deleting the InVoice details
                    deleteInVoice_btn = Button(createInVoice_innerbgColor, image=delete_obj, style="Delete-InVoice.TButton",
                                               cursor="hand2", command=lambda: deleteInVoice(inVoiceID))
                    deleteInVoice_btn.place(relx=0.99, rely=0.04, anchor=E)

                # ------------------------------------------------------------------------------- View-InVoice Panel -StyleEnds----

            # -------------------------------------------------------------------------------------------- Create-InVoice Panel -StyleEnds----

        # >>

        # Function which is operated by Add-Client Button to open the Add-Client Panel which is like a template for adding new client
        def addNewClientPanel(request=""):

            # Function to validate the entries in Add, View or Delete Client Panel
            def clientsEntryValidator():

                # Changing value of response
                response = False

                # Checking the important entries are not empty
                if (nameEntry_Var.get() == "" or addressEntry1_Var.get() == "" or cityEntry_Var.get() == "" or pincodeEntry_Var.get() == "" or contactEntry_Var.get() == "" or emailEntry_Var.get() == ""):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Make sure the fields with asterisk are filled")

                # Checking the characters in Client name, address1 and city entries has a minimum length of 3
                elif (len(nameEntry_Var.get()) < 3 or len(addressEntry2_Var.get()) < 3 or len(cityEntry_Var.get()) < 3):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "ClientName, Address Line1, City should have minimum 3 characters")

                # Checking the characters in Client address1 entry has a minimum length of 5
                elif (len(addressEntry1_Var.get()) < 5):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Address Line1 should have minimum 5 characters")

                # Confirming the City Entry is a alphabet
                elif (not cityEntry_Var.get().isalpha()):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "City name must be alphabets")

                # Confirming the PinCode and Contact Entry is a valid number
                elif (not pincodeEntry_Var.get().isdigit() or not contactEntry_Var.get().isdigit()):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Pincode and Contact must contain numbers only")

                    # Resetting the entries if value is not a integer
                    pincodeEntry_Var.set("")
                    contactEntry_Var.set("")

                # Checking the PinCode digit length is exactly 6
                elif (len(pincodeEntry_Var.get()) > 6 or len(pincodeEntry_Var.get()) < 6):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Pin code must be 6 digit number")

                # Validating the email field has a perfect email
                elif (emailEntry_Var.get().isdigit() or emailEntry_Var.get().isalpha()):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Enter a valid emailId")

                    # Resetting the entry if value is not a integer
                    emailEntry_Var.set("")

                # Limiting the character length of email field from 14 to 35
                elif (not len(emailEntry_Var.get()) > 14 or len(emailEntry_Var.get()) > 35):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "email may have 15-40 characters")

                # Checking the Contact number length is exactly 10
                elif (len(contactEntry_Var.get()) > 10 or len(contactEntry_Var.get()) < 10):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Contact must be 10 digits")

                    # Resetting the entry if value is not a integer
                    contactEntry_Var.set("")

                else:

                    # Changing value of response
                    response = True

                return response

            # >>

            # Function which adds or updates the Client Details to the User's Database with a confirmation message
            def saveClientChanges(buttonClicked, request, clientID=None):

                # Disabling the clicked Button for preventing the function to be called twice
                buttonClicked.configure(state=DISABLED)

                # Calling the function to validate the Entries
                validated = clientsEntryValidator()

                if (validated):

                    # Showing a confirmation dialog with some message
                    saveRequest = messagebox.askyesno(
                        "in Voice", f"{request} Client, Are you sure you want to save changes?")

                    if (saveRequest):

                        # Opening the ClientDetail Table in the User's Database
                        clientObj = ClientDetail(loggedInUser)

                        if (request == "ADD"):

                            # Inserting a new client details to the Table
                            clientObj.add(nameEntry_Var.get(),
                                          emailEntry_Var.get(),
                                          contactEntry_Var.get(),
                                          addressEntry1_Var.get(),
                                          addressEntry2_Var.get(),
                                          addressEntry3_Var.get(),
                                          cityEntry_Var.get(),
                                          pincodeEntry_Var.get(),
                                          customernoteEntry.get(
                                1.0, "end-1c")
                            )

                        elif (request == "UPDATE"):

                            # Updating a existing client details to the Table
                            clientObj.update(clientID,
                                             nameEntry_Var.get(),
                                             emailEntry_Var.get(),
                                             contactEntry_Var.get(),
                                             addressEntry1_Var.get(),
                                             addressEntry2_Var.get(),
                                             addressEntry3_Var.get(),
                                             cityEntry_Var.get(),
                                             pincodeEntry_Var.get(),
                                             customernoteEntry.get(
                                                 1.0, "end-1c")
                                             )

                        # Commiting and Closing the connection with the Database
                        clientObj.closeDB()

                        # Calling the function to redirect to `(in Voice)` WorkSpace
                        redirectToWorkSpace(tabLink3)

                else:

                    # Re-enabling the clicked Button
                    buttonClicked.configure(state=NORMAL)

            # >>

            # Function which is operated by Edit-Client Button to edit the client details queried from the Database
            def editClient(allEntries, clientData, clientID):

                # Disabling the Edit-Client Button after clicked, for preventing the function to be called twice
                editClient_btn.configure(state=DISABLED)

                # Calling the function to limit the Tab-Link Buttons by asking for confirmation before switching Tabs
                leftPanelExpand_disabler("Update")

                # Showing and Filling the entries
                item = 0
                for entry in allEntries:

                    # Showing the entries
                    entry[0].lift()

                    # Filling the entries with client details from Database
                    entry[1].set(clientData[item])
                    item += 1

                # Destroying the labels and delete button created to show the client details
                nameLabel.destroy()
                emailLabel.destroy()
                contactLabel.destroy()
                address1Label.destroy()
                address2Label.destroy()
                address3Label.destroy()
                cityLabel.destroy()
                pincodeLabel.destroy()
                deleteClient_btn.destroy()

                # Enabling the Customer-Message Box
                customernoteEntry.configure(state=NORMAL, cursor="xterm")

                # Removing the function assigned to the Customer-Message Box's mouse left-click
                customernoteEntry.unbind("<Button-1>")

                # Enabling and changing the function and text of Edit-Client Button
                addClient_frame.after(200, lambda: editClient_btn.configure(text="Update", image=clients_obj, state=NORMAL,
                                                                            command=lambda: saveClientChanges(editClient_btn, "UPDATE", clientID)))

            # >>

            # Function which is operated by Delete-Client Button to delete the client details from the Database
            def deleteClient(clientID):

               # Showing a confirmation dialog with some message
                deleteRequest = messagebox.askyesno(
                    "in Voice", "Delete Client, Are you sure you want to delete client details?")

                if (deleteRequest):

                    # Opening the ClientDetail Table in the User's Database
                    user_DataBase = ClientDetail(loggedInUser)

                    # Deleting a specific client from the Table
                    user_DataBase.delete(clientID)

                    # Commiting and Closing the connection with the Database
                    user_DataBase.closeDB()

                    # Calling the function to redirect to `(in Voice)` WorkSpace
                    redirectToWorkSpace(tabLink3)

            # >>

            # Function for deleting the pre-occupied message in Customer-Message Box with a mouse left-click
            def deleteMessageBoxContent(event):

                # Deleting the pre-occupied message and also removing the function to assigned to the Customer-Message Box's mouse left-click
                customernoteEntry.delete(1.0, END)
                customernoteEntry.unbind("<Button-1>")

            # >>

            # ------------------------------------- Add-Client Panel -StyleStarts----------------------------------------------------

            # Creating a frame for the Add-Client Panel and positioning it on Right-Bottom Panel
            addClient_frame = Frame(rightBottom_frame, height=int(screen_height/1.144),
                                    width=int(screen_width-(screen_width/15.1)))
            addClient_frame.place(relx=1, rely=1, anchor=SE)

            # Creating a label to set a background color for the Add-Client Panel
            addClient_bgColor = Label(addClient_frame, background="#B3C6E7",
                                      width=int(screen_width/4.6))
            addClient_bgColor.place(relx=0.5, rely=0.5,
                                    height=int(screen_height/1.14), anchor=CENTER)

            # Assigning the common colors for Add-Client Panel
            addClient_innerbG = "#F0EFF4"
            addClient_innerfG = leftTop_bG
            required_fG = "#EF233C"

            # Creating a label to set a background color for the Inner Add-Client Panel
            addClient_innerbgColor = Label(addClient_frame, background=addClient_innerbG,
                                           width=int(screen_width/6.75))
            addClient_innerbgColor.place(relx=0.5, rely=0.5,
                                         height=int(screen_height/1.24), anchor=CENTER)

            # Assigning a empty list to collect all the entries
            clientPanelEntries = []

            #        -------------------------------------
            # -------------- Client-Name Entry ---------------
            #        -------------------------------------

            # Creating a Client-Name Entry
            nameEntry_Var = StringVar(addClient_frame)
            nameEntry = tk.Entry(addClient_frame, textvariable=nameEntry_Var, font=("Dodge", 13, "bold"),
                                 width=int(screen_width/35), justify=RIGHT)
            nameEntry.place(relx=0.35, rely=0.15,
                            height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((nameEntry, nameEntry_Var))

            # ClientName-Asterisk label
            nameAsterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                 background=addClient_innerbG, foreground=required_fG)
            nameAsterisk.place(relx=0.15, rely=0.13)

            # ClientName-Entry label
            nameEntry_label = Label(addClient_frame, text="Client Name", font=("Dodge", 15),
                                    background=addClient_innerbG, foreground=addClient_innerfG, justify=RIGHT)
            nameEntry_label.place(relx=0.1, rely=0.15, anchor=CENTER)

            #        -------------------------------------
            # -------------- Client-Email Entry ---------------
            #        -------------------------------------

            # Creating a Client-Email Entry
            emailEntry_Var = StringVar(addClient_frame)
            emailEntry = tk.Entry(addClient_frame, textvariable=emailEntry_Var, font=("Dodge", 13, "bold"),
                                  width=int(screen_width/50), justify=RIGHT)
            emailEntry.place(relx=0.8, rely=0.15,
                             height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((emailEntry, emailEntry_Var))

            # ClientEmail-Asterisk label
            emailAsterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                  background=addClient_innerbG, foreground=required_fG)
            emailAsterisk.place(relx=0.63, rely=0.13)

            # ClientEmail-Entry label
            emailEntry_label = Label(addClient_frame, text="Email", font=("Dodge", 15),
                                     background=addClient_innerbG, foreground=addClient_innerfG)
            emailEntry_label.place(relx=0.6, rely=0.15, anchor=CENTER)

            #        -------------------------------------
            # -------------- Client-Contact Entry ---------------
            #        -------------------------------------

            # Creating a Client-Contact Entry
            contactEntry_Var = StringVar(addClient_frame)
            contactEntry = tk.Entry(addClient_frame, textvariable=contactEntry_Var, font=("Dodge", 13, "bold"),
                                    width=int(screen_width/70), justify=RIGHT)
            contactEntry.place(relx=0.772, rely=0.28,
                               height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((contactEntry, contactEntry_Var))

            # ClientContact-Asterisk label
            contactAsterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                    background=addClient_innerbG, foreground=required_fG)
            contactAsterisk.place(relx=0.64, rely=0.26)

            # ClientContact-Entry label
            contactEntry_label = Label(addClient_frame, text="Contact", font=("Dodge", 15),
                                       background=addClient_innerbG, foreground=addClient_innerfG, justify=RIGHT)
            contactEntry_label.place(relx=0.6, rely=0.28, anchor=CENTER)

            #        -------------------------------------
            # -------------- Client-Address Entry ---------------
            #        -------------------------------------

            # ClientAddress label
            addressEntry_label = Label(addClient_frame, text="Address", font=("Dodge", 15),
                                       background=addClient_innerbG, foreground=addClient_innerfG, justify=RIGHT)
            addressEntry_label.place(relx=0.1, rely=0.25, anchor=CENTER)

            #   --------------------------
            #        Address Line - 1
            #   --------------------------

            # Creating a Client-Address1 Entry
            addressEntry1_Var = StringVar(addClient_frame)
            addressEntry1 = tk.Entry(addClient_frame, textvariable=addressEntry1_Var, font=("Dodge", 13, "bold"),
                                     width=int(screen_width/35), justify=RIGHT)
            addressEntry1.place(relx=0.35, rely=0.31,
                                height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((addressEntry1, addressEntry1_Var))

            # ClientAddress1-Asterisk label
            address1Asterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                     background=addClient_innerbG, foreground=required_fG)
            address1Asterisk.place(relx=0.12, rely=0.29)

            # ClientAddress1-Entry label
            addressEntry1_label = Label(addClient_frame, text="line 1", font=("Dodge", 13),
                                        background=addClient_innerbG, foreground=addClient_innerfG)
            addressEntry1_label.place(relx=0.15, rely=0.31, anchor=CENTER)

            #   --------------------------
            #        Address Line - 2
            #   --------------------------

            # Creating a Client-Address2 Entry
            addressEntry2_Var = StringVar(addClient_frame)
            addressEntry2 = tk.Entry(addClient_frame, textvariable=addressEntry2_Var, font=("Dodge", 13, "bold"),
                                     width=int(screen_width/35), justify=RIGHT)
            addressEntry2.place(relx=0.35, rely=0.41,
                                height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((addressEntry2, addressEntry2_Var))

            # ClientAddress2-Asterisk label
            address2Asterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                     background=addClient_innerbG, foreground=required_fG)
            address2Asterisk.place(relx=0.12, rely=0.39)

            # ClientAddress2-Entry label
            addressEntry2_label = Label(addClient_frame, text="line 2", font=("Dodge", 13),
                                        background=addClient_innerbG, foreground=addClient_innerfG)
            addressEntry2_label.place(relx=0.15, rely=0.41, anchor=CENTER)

            #   --------------------------
            #        Address Line - 3
            #   --------------------------

            # Creating a Client-Address3 Entry
            addressEntry3_Var = StringVar(addClient_frame)
            addressEntry3 = tk.Entry(addClient_frame, textvariable=addressEntry3_Var, font=("Dodge", 13, "bold"),
                                     width=int(screen_width/35), justify=RIGHT)
            addressEntry3.place(relx=0.35, rely=0.51,
                                height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((addressEntry3, addressEntry3_Var))

            # ClientAddress3-Optional label
            address3Optional = Label(addClient_frame, text="(optional)",
                                     background=addClient_innerbG, foreground="#0A014F")
            address3Optional.place(relx=0.13, rely=0.53)

            # ClientAddress3-Entry label
            addressEntry3_label = Label(addClient_frame, text="Website", font=("Dodge", 13),
                                        background=addClient_innerbG, foreground=addClient_innerfG)
            addressEntry3_label.place(relx=0.15, rely=0.51, anchor=CENTER)

            #        -------------------------------------
            # -------------- Client-City Entry ---------------
            #        -------------------------------------

            # Creating a Client-City Entry
            cityEntry_Var = StringVar(addClient_frame)
            cityEntry = tk.Entry(addClient_frame, textvariable=cityEntry_Var, font=("Dodge", 13, "bold"),
                                 width=int(screen_width/50), justify=RIGHT)
            cityEntry.place(relx=0.308, rely=0.66,
                            height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((cityEntry, cityEntry_Var))

            # ClientCity-Asterisk label
            cityAsterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                 background=addClient_innerbG, foreground=required_fG)
            cityAsterisk.place(relx=0.125, rely=0.64)

            # ClientCity-Entry label
            cityEntry_label = Label(addClient_frame, text="City", font=("Dodge", 15),
                                    background=addClient_innerbG, foreground=addClient_innerfG)
            cityEntry_label.place(relx=0.105, rely=0.66, anchor=CENTER)

            #        -------------------------------------
            # -------------- Client-PinCode Entry ---------------
            #        -------------------------------------

            # Creating a Client-PinCode Entry
            pincodeEntry_Var = StringVar(addClient_frame)
            pincodeEntry = tk.Entry(addClient_frame, textvariable=pincodeEntry_Var, font=("Dodge", 13, "bold"),
                                    width=int(screen_width/90), justify=RIGHT)
            pincodeEntry.place(relx=0.268, rely=0.77,
                               height=int(screen_height/20), anchor=CENTER)
            clientPanelEntries.append((pincodeEntry, pincodeEntry_Var))

            # ClientPinCode-Asterisk label
            pincodeAsterisk = Label(addClient_frame, text="*", font=("Dodge", 16, "bold"),
                                    background=addClient_innerbG, foreground=required_fG)
            pincodeAsterisk.place(relx=0.145, rely=0.75)

            # ClientPinCode-Entry label
            pincodeEntry_label = Label(addClient_frame, text="Pin Code", font=("Dodge", 15),
                                       background=addClient_innerbG, foreground=addClient_innerfG)
            pincodeEntry_label.place(relx=0.105, rely=0.77, anchor=CENTER)

            #      ------------------------------------
            # ------------ Customer-Message Box ---------------
            #      ------------------------------------

            # Creating a Customer-Message Box for sending short message to their clients
            customernoteEntry = scrolledtext.ScrolledText(addClient_frame, font=("Dodge", 11, "italic", "bold"),
                                                          width=int(screen_width/35), height=int(screen_height/100), wrap=WORD)
            customernoteEntry.place(relx=0.65, rely=0.7, anchor=SW)
            customernoteEntry.insert(INSERT, "Your message here!")

            # Assigning a function for deleting the pre-occupied message in the Customer-Message Box
            customernoteEntry.bind("<Button-1>", deleteMessageBoxContent)

            # Customer-Message Box Optional label
            customernoteOptional = Label(addClient_frame, text="(optional)",
                                         background=addClient_innerbG, foreground="#0A014F")
            customernoteOptional.place(relx=0.7, rely=0.43)

            # Customer-Message Box Label
            customernoteEntry_label = Label(addClient_frame, text="Customer Note", font=("Dodge", 15),
                                            background=addClient_innerbG, foreground=addClient_innerfG)
            customernoteEntry_label.place(relx=0.63, rely=0.44, anchor=CENTER)

            if (request != "view"):

                #     -----------------------------
                # ------------ Note Labels ------------
                #     -----------------------------

                # Note label
                note_label = Label(addClient_frame, text="Note: field with asterisk            must be filled", font=("Dodge", 11, "bold"),
                                   background=addClient_innerbG, foreground="#0A014F")
                note_label.place(relx=0.2, rely=0.9)

                # Note-Asterisk label
                noteAsterisk_label = Label(addClient_frame, text="*", font=("Dodge", 17, "bold"),
                                           background=addClient_innerbG, foreground=required_fG)
                noteAsterisk_label.place(relx=0.34, rely=0.9)

                #       ------------------------------------
                # -------------- Add-Client Button ---------------
                #       ------------------------------------

                # Styling the Add-Client Button
                addClient_btn_style = Style(addClient_frame)
                addClient_btn_style.theme_use("default")
                addClient_btn_style.configure("Add-Client.TButton", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background="#2D361C",
                                              borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of Add-Client Button
                addClient_btn_style.map("Add-Client.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))],
                                        foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

                # Resizing the -- Clients -- image and converting it into a object to display on a widget
                global client_btn_obj
                client_btn_obj = ImageTk.PhotoImage(clients_icon.resize((30, 30),
                                                                        resampling_filter))

                # Creating a Add-Client Button to add the client to Database
                addClient_btn = Button(addClient_frame, text="Add Client", image=client_btn_obj, compound=LEFT,
                                       style="Add-Client.TButton", command=lambda: saveClientChanges(addClient_btn, request="ADD"))
                addClient_btn.place(relx=0.81, rely=0.86, anchor=CENTER)

            # Checking the request to view the existing client detail
            elif (request == "view"):

                # Getting the client details according to the field selection
                clientNumber = tableFields.item(
                    tableFields.focus())["values"][0]

                # ------------------------------------- View-Client Panel -StyleStarts---------------------------------------

                # Opening the ClientDetail Table in the User's Database
                clientObj = ClientDetail(loggedInUser)

                # Querying the 'clientDetails' table in the User's database and picking the matched client details
                clientRecord = clientObj.get(clientNumber)

                # Closing the connection with the Database
                clientObj.closeDB()

                if (clientRecord is not None):

                    # Hiding the entries and Customer-Message box
                    for entry in clientPanelEntries:

                        # Hiding the entries
                        entry[0].lower()

                    # Filling and Disabling the Customer-Message Box
                    customernoteEntry.delete(1.0, END)
                    customernoteEntry.insert(INSERT, clientRecord[8])
                    customernoteEntry.configure(state=DISABLED, cursor="arrow")

                    # Name label value
                    nameLabel = Label(addClient_frame, text=clientRecord[0], font=("Dodge", 13, "bold"),
                                      wraplength=350, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    nameLabel.place(relx=0.22, rely=0.15, anchor=W)

                    # Email label value
                    emailLabel = Label(addClient_frame, text=clientRecord[1], font=("Dodge", 13, "bold"),
                                       wraplength=300, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    emailLabel.place(relx=0.7, rely=0.15, anchor=W)

                    # Contact label value
                    contactLabel = Label(addClient_frame, text=clientRecord[2], font=("Dodge", 13, "bold"),
                                         wraplength=300, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    contactLabel.place(relx=0.7, rely=0.28, anchor=W)

                    # Address1 label value
                    address1Label = Label(addClient_frame, text=clientRecord[3], font=("Dodge", 13, "bold"),
                                          wraplength=350, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    address1Label.place(relx=0.22, rely=0.31, anchor=W)

                    # Address2 label value
                    address2Label = Label(addClient_frame, text=clientRecord[4], font=("Dodge", 13, "bold"),
                                          wraplength=350, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    address2Label.place(relx=0.22, rely=0.41, anchor=W)

                    # Address3 label value
                    optionalAddress = clientRecord[5] if (
                        clientRecord[5] != "") else "Nil"
                    address3Label = Label(addClient_frame, text=optionalAddress, font=("Dodge", 13, "bold"),
                                          wraplength=350, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    address3Label.place(relx=0.22, rely=0.51, anchor=W)

                    # City label value
                    cityLabel = Label(addClient_frame, text=clientRecord[6], font=("Dodge", 13, "bold"),
                                      wraplength=350, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    cityLabel.place(relx=0.22, rely=0.66, anchor=W)

                    # PinCode label value
                    pincodeLabel = Label(addClient_frame, text=clientRecord[7], font=("Dodge", 13, "bold"),
                                         wraplength=350, background=addClient_innerbG, foreground=addClient_innerfG, justify=LEFT)
                    pincodeLabel.place(relx=0.22, rely=0.77, anchor=W)

                    #       ------------------------------------
                    # -------------- Edit-Client Button ---------------
                    #       ------------------------------------

                    # Styling the Edit-Client Button
                    editClient_btn_style = Style(addClient_frame)
                    editClient_btn_style.theme_use("default")
                    editClient_btn_style.configure("Edit-Client.TButton", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background="#2D361C",
                                                   borderwidth=3, width=6, focuscolor="none", justify=CENTER)
                    # Changing the mapping style of Edit-Client Button
                    editClient_btn_style.map("Edit-Client.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))],
                                             foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

                    # Resizing the -- Edit -- image and converting it into a object to display on a widget
                    global edit_obj
                    edit_obj = ImageTk.PhotoImage(edit_icon.resize((30, 30),
                                                                   resampling_filter))

                    # Creating a Edit-Client Button for editing existing the client details
                    editClient_btn = Button(addClient_frame, text="edit", image=edit_obj, compound=LEFT,
                                            style="Edit-Client.TButton", command=lambda: editClient(clientPanelEntries, clientRecord, clientNumber))
                    editClient_btn.place(relx=0.81, rely=0.86, anchor=CENTER)

                    #       ------------------------------------
                    # -------------- Delete-Client Button ---------------
                    #       ------------------------------------

                    # Styling the Delete-Client Button
                    deleteClient_btn_style = Style()
                    deleteClient_btn_style.theme_use("default")
                    deleteClient_btn_style.configure("Delete-Client.TButton", background=addClient_innerbG, foreground=addClient_innerfG,
                                                     borderwidth=0, focuscolor="none", relief=FLAT, highlightthickness=0)
                    # Mouse Hovering style for Delete-Client Button
                    deleteClient_btn_style.map("Delete-Client.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                               background=[("active", addClient_innerbG)])

                    # Resizing the -- Delete -- image and converting it into a object to display on a widget
                    global delete_obj
                    delete_obj = ImageTk.PhotoImage(delete_icon.resize((30, 30),
                                                                       resampling_filter))

                    # Adding a delete button for deleting the client details
                    deleteClient_btn = Button(addClient_frame, image=delete_obj, style="Delete-Client.TButton",
                                              cursor="hand2", command=lambda: deleteClient(clientNumber))
                    deleteClient_btn.place(
                        relx=0.95, rely=0.082, anchor=CENTER)

                # ------------------------------------------------------------------------------- View-Client Panel -StyleEnds----

            # -------------------------------------------------------------------------------------------- Add-Client Panel -StyleEnds----

        # >>

        # Function which is operated by Add-Product Button to open the Add-Product Panel which is like a template for adding new Products to Stocks
        def addNewProductPanel(request=""):

            # Function to validate the entries in Add, View or Delete Product Panel
            def stocksEntryValidator(request):

                # Changing value of response
                response = False

                # Checking the Product name exists in the ProductDetails Table
                productExists = [name[0] for name in products if (
                    name[0] == nameEntry_Var.get())] if (products != []) else []

                # Checking the important entries are not empty
                if (nameEntry_Var.get() == "" or quantityEntry_Var.get() == "" or salesRateEntry_Var.get() == "" or reOrderEntry_Var.get() == ""):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Make sure the fields with asterisk are filled")

                elif ((request == "ADD" and productExists != []) or (request == "UPDATE" and productExists != [] and productExists[0] != productRecord[0])):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Product name should be Unique!")

                # Checking the characters in Product name has a minimum length of 3
                elif (len(nameEntry_Var.get()) < 3):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Product Name should atleast have minimum 3 characters")

                # Confirming the Quantity Entry is a valid number
                elif (not quantityEntry_Var.get().isdigit() or not reOrderEntry_Var.get().isdigit()):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Quantity must be a whole number")

                    # Resetting the entries if value is not a integer
                    quantityEntry_Var.set(0)
                    reOrderEntry_Var.set(0)

                # Confirming the Quantity Entry is not zero
                elif (int(quantityEntry_Var.get()) <= 0 or int(reOrderEntry_Var.get()) <= 0):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Quantity can't be zero number")

                # Confirming the Re-Order Quantity Entry is greater than 2
                elif (int(reOrderEntry_Var.get()) < 2):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Re-Order Quantity can't be less than 2")

                # Confirming the Quantity is greater than Re-Order Quantity
                elif (int(quantityEntry_Var.get()) <= int(reOrderEntry_Var.get())):

                    # Showing a error message
                    messagebox.showerror(
                        "in Voice", "Quantity must be atleast 1 in count greater than Re-Order Quantity")

                else:

                    try:

                        # Converting the Sales-Rate Entry value to float
                        float(salesRateEntry_Var.get())

                        if (MRPEntry_Var.get() != "" or purchaseRateEntry_Var.get() != ""):

                            try:
                                # Converting the MRP Entry and Purchase-Rate Entry value to float
                                float(MRPEntry_Var.get())
                                float(purchaseRateEntry_Var.get())

                                # Changing value of response
                                response = True

                            except (ValueError, TclError, FloatingPointError):

                                # Showing a error message
                                messagebox.showerror(
                                    "in Voice", "Rate must be valid number or decimal")

                                # Resetting the MRP Entry and Purchase-Rate Entry values
                                MRPEntry_Var.set(0)
                                purchaseRateEntry_Var.set(0)

                        else:

                            # Changing value of response
                            response = True

                    except (ValueError, TclError, FloatingPointError):

                        # Showing a error message
                        messagebox.showerror(
                            "in Voice", "Rate must be valid number or decimal")

                        # Resetting the Sales-Rate Entry value
                        salesRateEntry_Var.set(0)

                return response

            # >>

            # Function for converting the User enter price values into INR for saving it to Database
            def convertCurrency_to_INR(prices, currencyUsed, request):

                if (request == "convert"):

                    # Converting the User enter price values into INR
                    MRP_value = float("%.2f" %
                                      (float(prices[0]) * float(currencyUsed)))
                    purchase_value = float("%.2f" %
                                           (float(prices[1]) * float(currencyUsed)))
                    sales_value = float("%.2f" %
                                        (float(prices[2]) * float(currencyUsed)))

                    return [MRP_value, purchase_value, sales_value]

                elif (request == "revert"):

                    # Converting the User enter price values into INR
                    MRP_value = float("%.2f" %
                                      (float(prices[1]) / float(currencyUsed)))
                    purchase_value = float("%.2f" %
                                           (float(prices[3]) / float(currencyUsed)))
                    sales_value = float("%.2f" %
                                        (float(prices[4]) / float(currencyUsed)))

                    return [prices[0], MRP_value, prices[2], purchase_value, sales_value, prices[5]]

            # >>

            # Function which adds or updates the Product Details to the User's Database with a confirmation message
            def saveProductChanges(buttonClicked, request, allEntries, productID=None):

                # Disabling the clicked Button for preventing the function to be called twice
                buttonClicked.configure(state=DISABLED)

                # Calling the function to validate the Entries
                validated = stocksEntryValidator(request)

                if (validated):

                    # Converting the MRP and Purchase-Rate Entry values to float
                    MRP_value = float(MRPEntry_Var.get()) if (
                        MRPEntry_Var.get() != "") else float(0)
                    purchase_value = float(purchaseRateEntry_Var.get()) if (
                        purchaseRateEntry_Var.get() != "") else float(0)

                    # Calling the function to convert the User enter prices into INR
                    convertedPrices = convertCurrency_to_INR([MRP_value,
                                                             purchase_value,
                                                             salesRateEntry_Var.get()],
                                                             defaultCurrency[4],
                                                             "convert")

                    # Showing a confirmation dialog with some message
                    saveRequest = messagebox.askyesno(
                        "in Voice", f"{request} Product, Are you sure you want to save changes?")

                    if (saveRequest):

                        # Opening the ProductDetails Table in the User's Database
                        productObj = ProductDetail(loggedInUser)

                        if (request == "ADD"):

                            # Inserting a new client details to the Table
                            productObj.add(nameEntry_Var.get(),
                                           convertedPrices[0],
                                           int(quantityEntry_Var.get()),
                                           convertedPrices[1],
                                           convertedPrices[2],
                                           int(reOrderEntry_Var.get())
                                           )

                            # Querying the 'productDetails' table in the User's database and picking all the products
                            products = productObj.all()

                            # Enabling the In-Stocks Box to update the new product
                            inStocksBox.configure(state=NORMAL)

                            # Deleting the Out of Stocks message if the added product is the very first one
                            if (len(products) - 1 == 0):

                                inStocksBox.delete(1.0, END)
                                inStocksBox.configure(
                                    font=("Dodge", 11, "italic", "bold"))

                            # Updating the newly added product to the In-Stocks Box
                            inStocksBox.insert(
                                INSERT, f"\n  - {products[len(products) - 1][0]},\n")

                            # Disabling the In-Stocks Box to prevent the User to edit the contents
                            inStocksBox.configure(state=DISABLED)

                            # Resetting the entries in Add-Product Panel
                            for var in allEntries:
                                var[1].set("")

                            # Re-enabling the clicked Button
                            buttonClicked.configure(state=NORMAL)

                            # Commiting and Closing the connection with the Database
                            productObj.closeDB()

                        elif (request == "UPDATE"):

                            # Updating a existing product details to the Table
                            productObj.update(productID,
                                              nameEntry_Var.get(),
                                              convertedPrices[0],
                                              int(quantityEntry_Var.get()),
                                              convertedPrices[1],
                                              convertedPrices[2],
                                              int(reOrderEntry_Var.get())
                                              )

                            # Commiting and Closing the connection with the Database
                            productObj.closeDB()

                            # Calling the function to redirect to `(in Voice)` WorkSpace
                            redirectToWorkSpace(tabLink4)
                else:

                    # Re-enabling the clicked Button
                    buttonClicked.configure(state=NORMAL)

            # >>

            # Function which is operated by Edit-Product Button to edit the product details queried from the Database
            def editProduct(allEntries, productID):

                # Disabling the Edit-Product Button after clicked, for preventing the function to be called twice
                editProduct_btn.configure(state=DISABLED)

                # Calling the function to limit the Tab-Link Buttons by asking for confirmation before switching Tabs
                leftPanelExpand_disabler("Update")

                # Re-enabling all the entries
                for entry in allEntries:

                    # Making entries editable again
                    entry[0].configure(borderwidth=1, cursor="xterm",
                                       justify=RIGHT, state=NORMAL)

                # Destroying the Delete-Product Button
                deleteProduct_btn.destroy()

                # Enabling and changing the function and text of Edit-Product Button
                addProduct_frame.after(200, lambda: editProduct_btn.configure(text="Update", image=stocks_obj, state=NORMAL,
                                                                              command=lambda: saveProductChanges(editProduct_btn, "UPDATE", allEntries, productID)))

            # >>

            # Function which is operated by Delete-Product Button to delete the product details from the Database
            def deleteProduct(productID):

               # Showing a confirmation dialog with some message
                deleteRequest = messagebox.askyesno(
                    "in Voice", "Delete Product, Are you sure you want to delete product details?")

                if (deleteRequest):

                    # Opening the ProductDetail Table in the User's Database
                    productObj = ProductDetail(loggedInUser)

                    # Deleting a specific product from the Table
                    productObj.delete(productID)

                    # Commiting and Closing the connection with the Database
                    productObj.closeDB()

                    # Calling the function to redirect to `(in Voice)` WorkSpace
                    redirectToWorkSpace(tabLink4)

            # >>

            # ------------------------------------- Add-Product Panel -StyleStarts----------------------------------------------------

            # Creating a frame for the Add-Product Panel and positioning it on Right-Bottom Panel
            addProduct_frame = Frame(rightBottom_frame, height=int(screen_height/1.144),
                                     width=int(screen_width-(screen_width/15.1)))
            addProduct_frame.place(relx=1, rely=1, anchor=SE)

            # Creating a label to set a background color for the Add-Product Panel
            addProduct_bgColor = Label(addProduct_frame, background="#B3C6E7",
                                       width=int(screen_width/4.6))
            addProduct_bgColor.place(relx=0.5, rely=0.5,
                                     height=int(screen_height/1.14), anchor=CENTER)

            # Assigning the common colors for Add-Product Panel
            addProduct_innerbG = "#F0EFF4"
            addProduct_innerfG = leftTop_bG
            required_fG = "#EF233C"

            # Creating a label to set a background color for the Inner Add-Product Panel
            addProduct_innerbgColor = Label(addProduct_frame, background=addProduct_innerbG,
                                            width=int(screen_width/6.75))
            addProduct_innerbgColor.place(relx=0.5, rely=0.5,
                                          height=int(screen_height/1.235), anchor=CENTER)

            # Assigning a empty list to collect all the entries
            productPanelEntries = []

            # Calling the function to get the default currency code, symbol and exchange-rate
            defaultCurrency = defaultCurrencyGrappler()

            #      ------------------------------------
            # ------------ In-Stocks Box ---------------
            #      ------------------------------------

            # Creating a In-Stocks Box for showing the available products in Stocks
            inStocksBox = Text(addProduct_innerbgColor, font=("Dodge", 11, "italic", "bold"), height=int(screen_height/100),
                               highlightbackground="#647050", highlightthickness=1, borderwidth=0, wrap=WORD)
            inStocksBox.place(relx=1, rely=1, width=int(screen_width/3.75),
                              height=int(screen_height/1.5), anchor=SE)

            # Creating and assigning the X, Y scrollbars to scroll the In-Stocks Box when content exceeds visibility
            scrollbar_H = Scrollbar(inStocksBox, orient=HORIZONTAL)
            scrollbar_V = Scrollbar(inStocksBox, orient=VERTICAL)
            inStocksBox.configure(xscrollcommand=scrollbar_H.set,
                                  yscrollcommand=scrollbar_V.set)

            # Opening the ProductDetails Table in the User's Database
            productObj = ProductDetail(loggedInUser)

            # Querying the 'productDetails' table in the User's database and picking all the products
            products = productObj.all()

            # Closing the connection to the database
            productObj.closeDB()

            # In-Stocks Box label
            inStocksBox_label = tk.Label(addProduct_innerbgColor, text="In-STOCKs", font=("Dongle", 13, "bold"),
                                         background=tableHeader_bG, foreground=addProduct_innerfG, highlightbackground="#647050", highlightthickness=1, anchor=CENTER)
            inStocksBox_label.place(relx=1, rely=0, width=int(screen_width/3.75),
                                    height=int(screen_height/7), anchor=NE)

            #        -------------------------------------
            # -------------- Product-Name Entry ---------------
            #        -------------------------------------

            # Creating a Product-Name Entry
            nameEntry_Var = StringVar(addProduct_frame)
            nameEntry = tk.Entry(addProduct_frame, textvariable=nameEntry_Var, font=("Dodge", 12, "bold"),
                                 width=int(screen_width/30), justify=RIGHT)
            nameEntry.place(relx=0.42, rely=0.13,
                            height=int(screen_height/20), anchor=CENTER)
            productPanelEntries.append((nameEntry, nameEntry_Var))

            # ProductName-Asterisk label
            nameAsterisk = Label(addProduct_frame, text="*", font=("Dodge", 15, "bold"),
                                 background=addProduct_innerbG, foreground=required_fG)
            nameAsterisk.place(relx=0.195, rely=0.11)

            # ProductName-Entry label
            nameEntry_label = Label(addProduct_frame, text="Product Name", font=("Dodge", 14),
                                    background=addProduct_innerbG, foreground=addProduct_innerfG, justify=RIGHT)
            nameEntry_label.place(relx=0.14, rely=0.13, anchor=CENTER)

            #        -------------------------------------
            # -------------- Product-MRP Entry ---------------
            #        -------------------------------------

            # Creating a Product-MRP Entry
            MRPEntry_Var = StringVar()
            MRPEntry = tk.Entry(addProduct_frame, textvariable=MRPEntry_Var, font=("Dodge", 12, "bold"),
                                width=int(screen_width/70), justify=RIGHT)
            MRPEntry.place(relx=0.33, rely=0.26,
                           height=int(screen_height/20), anchor=CENTER)
            productPanelEntries.append((MRPEntry, MRPEntry_Var))

            # ProductMRP-Entry symbol
            MRPEntry_sym = Label(addProduct_frame, text=defaultCurrency[2], font=("Dodge", 13, "bold"),
                                 background=addProduct_innerbG, foreground=addProduct_innerfG)
            MRPEntry_sym.place(relx=0.243, rely=0.26, anchor=CENTER)

            # ProductMRP-Entry label
            MRPEntry_label = Label(addProduct_frame, text="M.R.P", font=("Dodge", 14),
                                   background=addProduct_innerbG, foreground=addProduct_innerfG)
            MRPEntry_label.place(relx=0.16, rely=0.26, anchor=CENTER)

            #        -------------------------------------
            # -------------- Product-Quantity Entry ---------------
            #        -------------------------------------

            # Creating a Product-Quantity Entry
            quantityEntry_Var = StringVar()
            quantityEntry = tk.Entry(addProduct_frame, textvariable=quantityEntry_Var, font=("Dodge", 12, "bold"),
                                     width=int(screen_width/90), justify=RIGHT)
            quantityEntry.place(relx=0.316, rely=0.39,
                                height=int(screen_height/20), anchor=CENTER)
            productPanelEntries.append((quantityEntry, quantityEntry_Var))

            # ProductQuantity-Asterisk label
            quantityAsterisk = Label(addProduct_frame, text="*", font=("Dodge", 15, "bold"),
                                     background=addProduct_innerbG, foreground=required_fG)
            quantityAsterisk.place(relx=0.195, rely=0.37)

            # ProductQuantity-Entry label
            quantityEntry_label = Label(addProduct_frame, text="Quantity", font=("Dodge", 15),
                                        background=addProduct_innerbG, foreground=addProduct_innerfG, justify=RIGHT)
            quantityEntry_label.place(relx=0.152, rely=0.39, anchor=CENTER)

            #        -------------------------------------
            # -------------- Purchase-Rate Entry ---------------
            #        -------------------------------------

            # Creating a Purchase-Rate Entry
            purchaseRateEntry_Var = StringVar()
            purchaseRateEntry = tk.Entry(addProduct_frame, textvariable=purchaseRateEntry_Var, font=("Dodge", 12, "bold"),
                                         width=int(screen_width/70), justify=RIGHT)
            purchaseRateEntry.place(relx=0.33, rely=0.52,
                                    height=int(screen_height/20), anchor=CENTER)
            productPanelEntries.append(
                (purchaseRateEntry, purchaseRateEntry_Var))

            # PurchaseRate-Entry symbol
            purchaseRateEntry_sym = Label(addProduct_frame, text=defaultCurrency[2], font=("Dodge", 13, "bold"),
                                          background=addProduct_innerbG, foreground=addProduct_innerfG)
            purchaseRateEntry_sym.place(relx=0.243, rely=0.52, anchor=CENTER)

            # PurchaseRate-Entry label
            purchaseRateEntry_label = Label(addProduct_frame, text="Purchase Rate", font=("Dodge", 15),
                                            background=addProduct_innerbG, foreground=addProduct_innerfG)
            purchaseRateEntry_label.place(relx=0.14, rely=0.52, anchor=CENTER)

            #        -------------------------------------
            # -------------- Sales-Rate Entry ---------------
            #        -------------------------------------

            # Creating a Sales-Rate Entry
            salesRateEntry_Var = StringVar()
            salesRateEntry = tk.Entry(addProduct_frame, textvariable=salesRateEntry_Var, font=("Dodge", 12, "bold"),
                                      width=int(screen_width/70), justify=RIGHT)
            salesRateEntry.place(relx=0.33, rely=0.65,
                                 height=int(screen_height/20), anchor=CENTER)
            productPanelEntries.append((salesRateEntry, salesRateEntry_Var))

            # SalesRate-Asterisk label
            salesRateAsterisk = Label(addProduct_frame, text="*", font=("Dodge", 15, "bold"),
                                      background=addProduct_innerbG, foreground=required_fG)
            salesRateAsterisk.place(relx=0.195, rely=0.63)

            # SalesRate-Entry symbol
            salesRateEntry_sym = Label(addProduct_frame, text=defaultCurrency[2], font=("Dodge", 13, "bold"),
                                       background=addProduct_innerbG, foreground=addProduct_innerfG)
            salesRateEntry_sym.place(relx=0.243, rely=0.65, anchor=CENTER)

            # SalesRate-Entry label
            salesRateEntry_label = Label(addProduct_frame, text="Sales Rate", font=("Dodge", 15),
                                         background=addProduct_innerbG, foreground=addProduct_innerfG, justify=RIGHT)
            salesRateEntry_label.place(relx=0.145, rely=0.65, anchor=CENTER)

            #        -------------------------------------
            # -------------- Re-Order Quantity Entry ---------------
            #        -------------------------------------

            # Creating a Re-Order Quantity Entry
            reOrderEntry_Var = StringVar()
            reOrderEntry = tk.Entry(addProduct_frame, textvariable=reOrderEntry_Var, font=("Dodge", 12, "bold"),
                                    width=int(screen_width/90), justify=RIGHT)
            reOrderEntry.place(relx=0.316, rely=0.78,
                               height=int(screen_height/20), anchor=CENTER)
            productPanelEntries.append((reOrderEntry, reOrderEntry_Var))

            # Re-Order Asterisk label
            reOrderAsterisk = Label(addProduct_frame, text="*", font=("Dodge", 15, "bold"),
                                    background=addProduct_innerbG, foreground=required_fG)
            reOrderAsterisk.place(relx=0.21, rely=0.76)

            # Re-Order Quantity-Entry label
            reOrderEntry_label = Label(addProduct_frame, text="Re-Order Quantity", font=("Dodge", 15),
                                       background=addProduct_innerbG, foreground=addProduct_innerfG, justify=RIGHT)
            reOrderEntry_label.place(relx=0.13, rely=0.78, anchor=CENTER)

            if (request != "view"):

                # Confirming the Stocks is not empty
                if (products != []):

                    for product in products:

                        # Populating the In-Stocks Box with the products available in the 'productDetails' table
                        inStocksBox.insert(INSERT, f"\n  - {product[0]},\n")

                else:

                    # Populating the In-Stocks Box with a no stock message
                    inStocksBox.insert(INSERT, f"\n\n\t -  Out of Stocks  -")
                    inStocksBox.configure(font=("Dongle", 15, "bold"))

                # Disabling the In-Stocks Box to prevent the User to edit the contents
                inStocksBox.configure(cursor="arrow", state=DISABLED)

                #     -----------------------------
                # ------------ Note Labels ------------
                #     -----------------------------

                # Note label
                note_label = Label(addProduct_frame, text="Note: field with asterisk        must be filled", font=("Dodge", 11, "bold"),
                                   background=addProduct_innerbG, foreground="#0A014F")
                note_label.place(relx=0.15, rely=0.9)

                # Note-Asterisk label
                noteAsterisk_label = Label(addProduct_frame, text="*", font=("Dodge", 16, "bold"),
                                           background=addProduct_innerbG, foreground=required_fG)
                noteAsterisk_label.place(relx=0.29, rely=0.9)

                #       ------------------------------------
                # -------------- Add-Product Button ---------------
                #       ------------------------------------

                # Styling the Add-Product Button
                addProduct_btn_style = Style(addProduct_frame)
                addProduct_btn_style.theme_use("default")
                addProduct_btn_style.configure("Add-Product.TButton", font=("Dodge", 13, "bold"), foreground="#B3C6E7", background="#2D361C",
                                               borderwidth=3, focuscolor="none", justify=CENTER)
                # Changing the mapping style of Add-Product Button
                addProduct_btn_style.map("Add-Product.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))],
                                         foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

                # Creating a Add-Product Button to add the Product to Database
                addProduct_btn = Button(addProduct_frame, text="Add Product", image=stocks_obj, compound=LEFT,
                                        style="Add-Product.TButton", command=lambda: saveProductChanges(addProduct_btn, request="ADD", allEntries=productPanelEntries))
                addProduct_btn.place(relx=0.55, rely=0.89, anchor=CENTER)

            # Checking the request to view the existing product detail
            elif (request == "view"):

                # Getting the product details according to the field selection
                productNumber = tableFields.item(
                    tableFields.focus())["values"][0]

                # ------------------------------------- View-Product Panel -StyleStarts---------------------------------------

                # Opening the ProductDetail Table in the User's Database
                productObj = ProductDetail(loggedInUser)

                # Querying the 'productDetails' table in the User's database and picking the matched product details
                productRecord = productObj.get(filterby="oid",
                                               productName=productNumber)

                # Closing the connection with the Database
                productObj.closeDB()

                if (productRecord is not None):

                    # Calling the function to create a converted list of the queryed product in INR prices into User default Currency
                    convertedRecords = convertCurrency_to_INR(productRecord,
                                                              defaultCurrency[4],
                                                              "revert")

                    # Populating and disabling the entries
                    for entry, product in zip(productPanelEntries, convertedRecords):

                        # Populating the entries
                        entry[1].set(product)

                        # Disabling the entries
                        entry[0].configure(disabledbackground=addProduct_innerbG, disabledforeground="#0A0908",
                                           borderwidth=0, cursor="arrow", justify=LEFT, state=DISABLED)

                    # Populating the In-Stocks Box with the product important details in the 'productDetails' table
                    inStocksBox.insert(
                        INSERT, f"\n\t  Product ID      -  {productNumber}\n")
                    inStocksBox.insert(
                        INSERT, f"\n\t  Item left          -  {productRecord[2]}\n")
                    inStocksBox.insert(
                        INSERT, f"\n\t  Sales Price    -  {convertedRecords[4]}\n\n")

                    # Inserting separator with dots
                    for i in range(inStocksBox["width"]-40):
                        inStocksBox.insert(INSERT, " -")
                    inStocksBox.insert(
                        INSERT, f"\n\n\n\t\tOther Products\t\n\n")

                    for product in products:

                        if (product[0] != productRecord[0]):

                            # Populating the In-Stocks Box with the products available in the 'productDetails' table except the picked one
                            inStocksBox.insert(
                                INSERT, f"\n  - {product[0]},\n")

                    # Disabling the In-Stocks Box to prevent the User to edit the contents
                    inStocksBox.configure(cursor="arrow", state=DISABLED)

                    #       ------------------------------------
                    # -------------- Edit-Product Button ---------------
                    #       ------------------------------------

                    # Styling the Edit-Product Button
                    editProduct_btn_style = Style(addProduct_frame)
                    editProduct_btn_style.theme_use("default")
                    editProduct_btn_style.configure("Edit-Product.TButton", font=("Dodge", 14, "bold"), foreground="#B3C6E7", background="#2D361C",
                                                    borderwidth=3, width=6, focuscolor="none", justify=CENTER)
                    # Changing the mapping style of Edit-Product Button
                    editProduct_btn_style.map("Edit-Product.TButton", font=[("pressed", "!disabled", ("Dodge", 12, "bold", "italic"))],
                                              foreground=[("active", "!disabled", "#01102E")], background=[("active", "#656D4A")])

                    # Resizing the -- Edit -- image and converting it into a object to display on a widget
                    global edit_obj
                    edit_obj = ImageTk.PhotoImage(edit_icon.resize((30, 30),
                                                                   resampling_filter))

                    # Creating a Edit-Product Button for editing existing the Product details
                    editProduct_btn = Button(addProduct_frame, text="edit", image=edit_obj, compound=LEFT,
                                             style="Edit-Product.TButton", command=lambda: editProduct(productPanelEntries, productNumber))
                    editProduct_btn.place(relx=0.48, rely=0.89, anchor=CENTER)

                    #       ------------------------------------
                    # -------------- Delete-Product Button ---------------
                    #       ------------------------------------

                    # Styling the Delete-Product Button
                    deleteProduct_btn_style = Style()
                    deleteProduct_btn_style.theme_use("default")
                    deleteProduct_btn_style.configure("Delete-Product.TButton", background=addProduct_innerbG, foreground=addProduct_innerfG,
                                                      borderwidth=0, focuscolor="none", relief=FLAT, highlightthickness=0)
                    # Mouse Hovering style for Delete-Product Button
                    deleteProduct_btn_style.map("Delete-Product.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                                                background=[("active", addProduct_innerbG)])

                    # Resizing the -- Delete -- image and converting it into a object to display on a widget
                    global delete_obj
                    delete_obj = ImageTk.PhotoImage(delete_icon.resize((30, 30),
                                                                       resampling_filter))

                    # Adding a delete button for deleting the Product details
                    deleteProduct_btn = Button(addProduct_frame, image=delete_obj, style="Delete-Product.TButton",
                                               cursor="hand2", command=lambda: deleteProduct(productNumber))
                    deleteProduct_btn.place(
                        relx=0.65, rely=0.1, anchor=CENTER)

                # ------------------------------------------------------------------------------- View-Product Panel -StyleEnds----

            # -------------------------------------------------------------------------------------------- Add-Product Panel -StyleEnds----

        # >>

        # Function for redirecting to the `(in Voice)` WorkSpace
        def redirectToWorkSpace(currentTabLink):

            # Re-settings the new functions assigned to Tab-Link Buttons to default
            tabLink1.configure(command=lambda: dashboardTab())
            tabLink2.configure(command=lambda: [dashboardTab(),
                                                workSpace(tabLink2)])
            tabLink3.configure(command=lambda: [dashboardTab(),
                                                workSpace(tabLink3)])
            tabLink4.configure(command=lambda: [dashboardTab(),
                                                workSpace(tabLink4)])
            tabLink5.configure(command=lambda: [dashboardTab(),
                                                workSpace(tabLink5)])

            # Calling the function to destroy the widgets of Add, View or Delete Panel
            root.after(200, lambda: dashboardTab())

            # Calling the function to open the `(in Voice)` WorkSpace
            root.after(200, workSpace(currentTabLink))

        # >>

        # ------------------------------------- `(in Voice)` WorkSpace -StyleStarts----------------------------------------------------

        #         -----------------------------------------------
        # -------------------- WorkSpace's Left Panel ---------------------
        #         -----------------------------------------------

        # Creating a frame for the WorkSpace's Left Panel and positioning it on Main Panel
        workSpace_leftFrame = Frame(home_frame, height=int(screen_height/1.035),
                                    width=int(screen_width/4.55))
        workSpace_leftFrame.place(relx=0, rely=1, anchor=SW)

        #         -----------------------------------------
        # -------------------- Left-Top Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for the Left-Top Panel and positioning it on WorkSpace's Left Panel
        leftTop_frame = Frame(workSpace_leftFrame, height=int(screen_height/3.05),
                              width=int(screen_width/4.55))
        leftTop_frame.place(relx=0, rely=0, anchor=NW)

        # Assigning a common background color for Left-Top Panel
        leftTop_bG = "#360015"

        # Creating a label to set a background color for the Left-Top Panel
        leftTop_bgColor = Label(leftTop_frame, background=leftTop_bG,
                                width=int(screen_width/4.6))
        leftTop_bgColor.place(relx=0.5, rely=0.5,
                              height=int(screen_height/3), anchor=CENTER)

        # Opening the User's Database
        userObj = UserDetail(loggedInUser)

        # Querying the 'userDetails' table in the User's database and picking the matched record
        pathToProfile = userObj.get()["profile"]

        # Closing the connection with the Database
        userObj.closeDB()

        # Opening and Resizing the -- User's Profile -- picture and converting it into a object to display on a widget
        global profile_obj2
        profile_obj2 = ImageTk.PhotoImage(
            (Image.open(pathToProfile).convert("RGBA")).resize((150, 150), resampling_filter))

        # Creating a label as a template for holding the User's Profile Picture
        leftTop_profile = Label(leftTop_frame, image=profile_obj2,
                                background=leftTop_bG, cursor="hand2")
        leftTop_profile.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Assigning a function to update the User's Profile Picture by mouse left-click
        leftTop_profile.bind("<Button-1>", profilePictureUpdater)

        #     -----------------------------
        # ------------ Wrap Button ------------
        #     -----------------------------

        # Styling the Wrap Button
        panelWrap_btn_style = Style(leftTop_frame)
        panelWrap_btn_style.theme_use("default")
        panelWrap_btn_style.configure("Wrap.TLabel", background=leftTop_bG,
                                      borderwidth=0, focuscolor="none", anchor=CENTER)
        # Mouse Hovering style for Wrap Button
        panelWrap_btn_style.map("Wrap.TLabel", foreground=[("active", "!disabled", "#D6DDE8")],
                                background=[("active", "#7A4559")])

        # Opening, resize and Setting image variable for ---  fold icon  ---
        global wrap_obj
        wrap_obj = wrap_icon.resize((25, 25), resampling_filter)
        wrap_obj = ImageTk.PhotoImage(wrap_obj)

        # Creating a button for shrinking the left panel
        panelWrap_btn = Button(leftTop_frame, image=wrap_obj, style="Wrap.TLabel",
                               cursor="hand2", command=lambda: leftPanelShrinker())
        panelWrap_btn.place(relx=0.99, rely=0.01, width=int(screen_width/40),
                            height=int(screen_height/20), anchor=NE)

        #          -----------------------------------------
        # -------------------- Left-Bottom Panel ---------------------
        #          -----------------------------------------

        # Creating a frame for the Left-Bottom Panel and positioning it on WorkSpace's Left Panel
        leftBottom_frame = Frame(workSpace_leftFrame, height=int(screen_height/1.55),
                                 width=int(screen_width/4.55))
        leftBottom_frame.place(relx=0, rely=1, anchor=SW)

        # Assigning a common background color for Left-Bottom Panel
        leftBottom_bG = "#FF5714"

        # Creating a label to set a background color for the Left-Bottom panel
        leftBottom_bgColor = Label(leftBottom_frame, background=leftBottom_bG,
                                   width=int(screen_width/4.6))
        leftBottom_bgColor.place(relx=0.5, rely=0.5,
                                 height=int(screen_height/1.045), anchor=CENTER)

        #     --------------------------------
        # ------------ Tab-Link Buttons ------------
        #     --------------------------------

        # Creating and Styling all the Tab-Link Buttons in the Left-Bottom panel
        leftBottom_tabLink_style = Style(leftBottom_frame)
        leftBottom_tabLink_style.theme_use("default")
        leftBottom_tabLink_style.configure("Tab-Links.TLabel", font=("Dodge", 16, "bold"),
                                           foreground="#00000E", background=leftBottom_bG, borderwidth=0, focuscolor="none", anchor=CENTER)
        # Mouse Hovering style for all Tab-Link Buttons
        leftBottom_tabLink_style.map("Tab-Links.TLabel", foreground=[("active", "!disabled", leftBottom_bG)],
                                     background=[("active", "#E9FF70")])

        # Resizing and Converting all the icons into objects to display on the buttons
        global dashboard_obj, inVoice_obj, clients_obj, stocks_obj, settings_obj

        # Dashboard Icon
        dashboard_obj = ImageTk.PhotoImage(dashboard_icon.resize((30, 30),
                                                                 resampling_filter))
        # Dashboard Tab-Link Button
        tabLink1 = Button(leftBottom_frame, text="    Dashboard", image=dashboard_obj, compound=LEFT,
                          style="Tab-Links.TLabel", state=NORMAL, command=lambda: dashboardTab())
        tabLink1.place(relx=0.5, rely=0.1, width=int(screen_width/4.55),
                       height=int(screen_height/12), anchor=N)

        # InVoice Icon
        inVoice_obj = ImageTk.PhotoImage(inVoice_icon.resize((30, 30),
                                                             resampling_filter))
        # InVoice Tab-Link Button
        tabLink2 = Button(leftBottom_frame, text="    InVoices   ", image=inVoice_obj, compound=LEFT,
                          style="Tab-Links.TLabel", state=NORMAL, command=lambda: [dashboardTab(), workSpace(tabLink2)])
        tabLink2.place(relx=0.5, rely=0.24, width=int(screen_width/4.55),
                       height=int(screen_height/12), anchor=N)

        # Clients Icon
        clients_obj = ImageTk.PhotoImage(clients_icon.resize((40, 40),
                                                             resampling_filter))
        # Clients Tab-Link Button
        tabLink3 = Button(leftBottom_frame, text="   Clients       ", image=clients_obj, compound=LEFT,
                          style="Tab-Links.TLabel", state=NORMAL, command=lambda: [dashboardTab(), workSpace(tabLink3)])
        tabLink3.place(relx=0.5, rely=0.38, width=int(screen_width/4.55),
                       height=int(screen_height/12), anchor=N)

        # Stocks Icon
        stocks_obj = ImageTk.PhotoImage(stocks_icon.resize((30, 30),
                                                           resampling_filter))
        # Stocks Tab-Link Button
        tabLink4 = Button(leftBottom_frame, text="    Stocks      ", image=stocks_obj, compound=LEFT,
                          style="Tab-Links.TLabel", state=NORMAL, command=lambda: [dashboardTab(), workSpace(tabLink4)])
        tabLink4.place(relx=0.5, rely=0.52, width=int(screen_width/4.55),
                       height=int(screen_height/12), anchor=N)

        # Settings Icon
        settings_obj = ImageTk.PhotoImage(settings_icon.resize((35, 35),
                                                               resampling_filter))
        # Settings Tab-Link Button
        tabLink5 = Button(leftBottom_frame, text="   Settings    ", image=settings_obj, compound=LEFT,
                          style="Tab-Links.TLabel", state=NORMAL, command=lambda: [dashboardTab(), workSpace(tabLink5)])
        tabLink5.place(relx=0.5, rely=0.66, width=int(screen_width/4.55),
                       height=int(screen_height/12), anchor=N)

        # Styling the Selected Tab-Link Button
        selected_tabLink_style = Style(leftBottom_frame)
        selected_tabLink_style.theme_use("default")
        selected_tabLink_style.configure("SelectedTab-Link.TLabel", font=("Dogde", 14, "bold"),
                                         foreground="#FF5714", background="#FFD670", borderwidth=2, focuscolor="none", anchor=CENTER)
        # Mouse Hovering style for Selected Tab-Link Button
        selected_tabLink_style.map("SelectedTab-Link.TLabel", foreground=[("active", "!disabled", "#FF0000")],
                                   background=[("active", "#01102E")])

        #         -----------------------------------------------
        # -------------------- WorkSpace's Right Panel ---------------------
        #         -----------------------------------------------

        # Creating a frame for the WorkSpace's Right Panel and positioning it on Main Panel
        workSpace_rightFrame = Frame(home_frame, height=int(screen_height/1.035),
                                     width=int(screen_width-(screen_width/4.6)))
        workSpace_rightFrame.place(relx=1, rely=1, anchor=SE)

        #         -----------------------------------------
        # -------------------- Right-Top Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for the Right-Top Panel and positioning it on WorkSpace's Right Panel
        rightTop_frame = Frame(workSpace_rightFrame, height=int(screen_height/10),
                               width=int(screen_width-(screen_width/4.6)))
        rightTop_frame.place(relx=1, rely=0, anchor=NE)

        # Assigning a common background color for Right-Top Panel
        rightTop_bG = "#01102E"

        # Creating a label to set a background color for the Right-Top Panel
        rightTop_bgColor = Label(rightTop_frame, background=rightTop_bG,
                                 width=int(screen_width/7.55))
        rightTop_bgColor.place(relx=0.5, rely=0.5,
                               height=int(screen_height/10), anchor=CENTER)

        # Creating labels for displaying the APP's name on the Right-Top Panel
        appName_Lhalf = Label(rightTop_frame, text="in", foreground="#B3C6E7",
                              background=rightTop_bG, font=("Magneto", 55, "bold"))
        appName_Lhalf.place(relx=0.4, rely=0.5, anchor=E)

        appName_Rhalf = Label(rightTop_frame, text="Voice", foreground="#D6DDE8",
                              background=rightTop_bG, font=("Matura MT Script Capitals", 12, "bold"))
        appName_Rhalf.place(relx=0.445, rely=0.55, anchor=E)

        # Creating a label to show the userId on the Right-Top Panel
        rightTop_userId = Label(rightTop_frame, text=f"@ {loggedInUser}", foreground="#B3C6E7",
                                background=rightTop_bG, font=("Dodge", 12, "bold"))
        rightTop_userId.place(relx=0.95, rely=0.51, anchor=E)

        #         -----------------------------------------
        # -------------------- Right-Bottom Panel ---------------------
        #         -----------------------------------------

        # Creating a frame for the Right-Bottom Panel and positioning it on WorkSpace's Right Panel
        rightBottom_frame = Frame(workSpace_rightFrame, height=int(screen_height/1.151),
                                  width=int(screen_width-(screen_width/4.6)))
        rightBottom_frame.place(relx=1, rely=1, anchor=SE)

        # Creating a label to set a background color for the Right-Bottom Panel
        rightBottom_bgColor = Label(rightBottom_frame, background="#B3C6E7",
                                    width=int(screen_width/4.6))
        rightBottom_bgColor.place(relx=0.5, rely=0.5,
                                  height=int(screen_height/1.148), anchor=CENTER)

        # Assigning a common background color for Right-Bottom Panel
        rightBottom_innerbG = "#F0EFF4"

        # Creating a label to set a background color for the Inner Right-Bottom Panel
        rightBottom_innerbgColor = Label(rightBottom_frame, background=rightBottom_innerbG,
                                         width=int(screen_width/8.3))
        rightBottom_innerbgColor.place(relx=0.5, rely=0.5,
                                       height=int(screen_height/1.3), anchor=CENTER)

        # Creating a label to show the current active Tab's Title with a icon
        rightBottom_title = Label(rightBottom_frame, font=("Dodge", 16, "bold"),
                                  background=rightBottom_innerbG, compound=LEFT)
        rightBottom_title.place(relx=0.12, rely=0.12, anchor=CENTER)

        # Parsing the Selected Button text to Confirm which Tab-Link Button to apply styles
        selectedLinkName = linkSelected["text"].replace(
            "\r", "").replace(" ", "")

        # Confirming the Tab-Link Button selected is not 'Settings' Button
        if (selectedLinkName != "Settings"):

            # Styling the New and Add Buttons on the Right-Bottom Panel
            newADD_btn_style = Style(rightBottom_frame)
            newADD_btn_style.theme_use("default")
            newADD_btn_style.configure("New_Add.TButton", font=("Dodge", 10, "bold"), background="#0CB0A9",
                                       borderwidth=3, focuscolor="none", anchor=CENTER)
            # Mouse Hovering style for New and Add Buttons
            newADD_btn_style.map("New_Add.TButton", foreground=[("active", "!disabled", "#000000")],
                                 background=[("active", "#61818D")])

            # Creating the New and Add Button to create the templates related to the Tab-Link Button
            newADD_btn = Button(rightBottom_frame, style="New_Add.TButton")
            newADD_btn.place(relx=0.15, rely=0.2, anchor=CENTER)

            # ---------------------------- Right-Bottom Panel's Table -StyleStarts-------------------------------------------

            # Creating a frame for the Table Header
            tableHeader = Frame(rightBottom_frame, height=int(screen_height/10),
                                width=int(screen_width-(screen_width/3)))
            tableHeader.place(relx=0.5, rely=0.33, anchor=CENTER)

            # Assigning a common background color for the Table Header
            tableHeader_bG = "#9BA984"

            # Creating a label to set a background color for the Table Header
            tableHeader_bgColor = Label(tableHeader, background=tableHeader_bG)
            tableHeader_bgColor.place(relx=0.5, rely=0.5, height=int(screen_height/10),
                                      width=int(screen_width-(screen_width/3)), anchor=CENTER)

            # Styling all the Table Fields
            tableFields_style = Style(rightBottom_frame)
            tableFields_style.theme_use("default")
            tableFields_style.configure("Table-Fields.Treeview", font=("Dodge", 12),
                                        borderwidth=0, highlightthickness=0, rowheight=120, anchor=CENTER)

            # Creating the Table Fields which holds the columns and rows
            tableFields = Treeview(rightBottom_frame, selectmode=NONE,
                                   style="Table-Fields.Treeview")
            tableFields.place(relx=0.5, rely=0.35, width=int(screen_width/1.5),
                              height=int(screen_height/2.8), anchor=N)

            # Showing the partition made by each heading on the Table Header
            tableFields["show"] = ["headings"]

            # Changing the background color of even rows
            tableFields.tag_configure("even", background="#EAF4F4")
            tableFields.tag_configure("odd", background="#B8D3C8")

            # Creating a label to occupy the empty Table Fields if the records from the Database-Table is empty
            emptyField_INFO1 = Label(tableFields, font=("Dodge", 17, "bold"),
                                     background="#FFFFFF", foreground=leftTop_bG, justify=CENTER)
            emptyField_INFO2 = Label(tableFields, text="no records available to show", font=("Dodge", 14, "bold"),
                                     background="#FFFFFF", foreground=leftTop_bG, justify=CENTER)

            # Calling the function to get the default currency code, symbol and exchange-rate
            defaultCurrency = defaultCurrencyGrappler()

            # Confirming which Tab-Link Button to apply the disable and the Selected styles
            if (selectedLinkName == "InVoices"):

                # Disabling and Styling the InVoices Tab-Link Button
                tabLink2.configure(
                    style="SelectedTab-Link.TLabel", state=DISABLED)

                # Changing the Title and the icon of the tab relavent to the Selected Tab
                rightBottom_title.configure(
                    text=f"   {selectedLinkName}", image=inVoice_obj)

                # Assigning a function to the New-InVoice Button to open the Create-InVoice Panel
                newADD_btn.configure(text=f"New InVoice", command=lambda: [
                    workSpace_leftFrame.after(200, lambda: [
                        leftPanelExpand_disabler("New"),
                        createNewInVoicePanel()
                    ]),
                    workSpace_leftFrame.after(100, lambda: leftPanelShrinker())
                ])

                # Creating the headings for the InVoices-Table Header
                inVoicesTable_heading1 = Label(tableHeader, text="No.", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading1.place(relx=0.05, rely=0.3, anchor=N)
                inVoicesTable_heading2 = Label(tableHeader, text="Clients", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=W)
                inVoicesTable_heading2.place(relx=0.2, rely=0.3, anchor=N)
                inVoicesTable_heading3 = Label(tableHeader, text="Date", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading3.place(relx=0.43, rely=0.3, anchor=N)
                inVoicesTable_heading4 = Label(tableHeader, text="Due date", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading4.place(relx=0.565, rely=0.3, anchor=N)
                inVoicesTable_heading5_sym = Label(tableHeader, text=defaultCurrency[2], font=("Dodge", 12, "bold"),
                                                   background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading5_sym.place(
                    relx=0.743, rely=0.3, anchor=N)
                inVoicesTable_heading5 = Label(tableHeader, text="Amount", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading5.place(relx=0.69, rely=0.3, anchor=N)
                inVoicesTable_heading6_sym = Label(tableHeader, text=defaultCurrency[2], font=("Dodge", 12, "bold"),
                                                   background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading6_sym.place(
                    relx=0.878, rely=0.3, anchor=N)
                inVoicesTable_heading6 = Label(tableHeader, text="Balance", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading6.place(relx=0.825, rely=0.3, anchor=N)
                inVoicesTable_heading7 = Label(tableHeader, text="Status", font=("Dodge", 12, "bold"),
                                               background=tableHeader_bG, anchor=CENTER)
                inVoicesTable_heading7.place(relx=0.945, rely=0.3, anchor=N)

                # Creating the columns and rows for the InVoices-Table Fields
                tableFields["columns"] = ["1", "2", "3", "4", "5", "6", "7"]
                tableFields.column("1",
                                   width=int(screen_width/2000), anchor=CENTER)
                tableFields.column("2",
                                   width=int(screen_width/10), anchor=CENTER)
                tableFields.column("3",
                                   width=int(screen_width/60), anchor=CENTER)
                tableFields.column("4",
                                   width=int(screen_width/60), anchor=CENTER)
                tableFields.column("5",
                                   width=int(screen_width/60), anchor=CENTER)
                tableFields.column("6",
                                   width=int(screen_width/60), anchor=CENTER)
                tableFields.column("7",
                                   width=int(screen_width/2000), anchor=CENTER)

                # Opening the InVoices Table in the User's Database
                inVoiceObj = InVoiceDetail(loggedInUser)

                # Querying the 'inVoiceDetails' table in the User's database and picking the matched record
                all_inVoices = inVoiceObj.all()

                # Closing the connection with the Database
                inVoiceObj.closeDB()

                # Confirming the 'inVoiceDetails' table is not empty
                if (all_inVoices != []):

                    iter_count = 0
                    for inVoice in all_inVoices:

                        # Checking the InVoice oid is even or odd
                        ODD_or_EVEN = "even" if (
                            iter_count % 2 == 0) else "odd"
                        iter_count += 1

                        # Assigning Due-Date to 'Nil' if don't have one
                        due_date = "Nil" if (
                            inVoice[4] == inVoice[5]) else inVoice[5]

                        # Collecting the amount to pay and balance amount to convert it to a two decimal digit number
                        amount_to_pay = "Nil" if (
                            int(inVoice[12]) == 0) else "%.2f" % (float(inVoice[12]) / float(defaultCurrency[4]))
                        total_amount = "%.2f" % (
                            float(inVoice[11]) / float(defaultCurrency[4]))

                        # Filling columns and rows of the InVoices-Table Fields with the data from User's Database
                        tableFields.insert("", "end", tag=ODD_or_EVEN, values=(
                            str(inVoice[0]),
                            wrapTextLength(str(inVoice[1])),
                            str(inVoice[4]),
                            str(due_date),
                            str(total_amount),
                            str(amount_to_pay),
                            str(inVoice[13])
                        ))

                else:

                    # Showing the Empty-INFO on the InVoices-Table Fields if the records from the 'inVoiceDetails' table is empty
                    emptyField_INFO1.configure(text="Oops, SORRY!")
                    emptyField_INFO1.place(relx=0.5, rely=0.4, anchor=CENTER)
                    emptyField_INFO2.configure(
                        text="no inVoice records available to show")
                    emptyField_INFO2.place(relx=0.5, rely=0.6, anchor=CENTER)

                # Assigning a function to the InVoices-Table Fields for opening the Update-InVoices Panel on mouse double-click
                tableFields.bind("<Double-1>", lambda event: [
                    workSpace_leftFrame.after(200, lambda: [
                        leftPanelExpand_disabler(),
                        createNewInVoicePanel(request="view")
                    ]),
                    workSpace_leftFrame.after(100, lambda: leftPanelShrinker())
                ])

            else:

                if (selectedLinkName == "Clients"):

                    # Disabling and Styling the Clients Tab-Link Button
                    tabLink3.configure(
                        style="SelectedTab-Link.TLabel", state=DISABLED)

                    # Changing the Title and the icon of the tab relavent to the Selected Tab
                    rightBottom_title.configure(
                        text=f"   {selectedLinkName}", image=clients_obj)

                    # Assigning a function to the Add-Client Button to open the Add-Client Panel
                    newADD_btn.configure(text=f"Add Client", command=lambda: [
                        workSpace_leftFrame.after(200, lambda: [
                            leftPanelExpand_disabler("New"),
                            addNewClientPanel()
                        ]),
                        workSpace_leftFrame.after(
                            100, lambda: leftPanelShrinker())
                    ])

                    # Creating the headings for the Clients-Table Header
                    clientsTable_heading1 = Label(tableHeader, text="No.", font=("Dodge", 12, "bold"),
                                                  background=tableHeader_bG, anchor=CENTER)
                    clientsTable_heading1.place(relx=0.08, rely=0.3, anchor=N)
                    clientsTable_heading2 = Label(tableHeader, text="Client Name", font=("Dodge", 12, "bold"),
                                                  background=tableHeader_bG, anchor=W)
                    clientsTable_heading2.place(relx=0.32, rely=0.3, anchor=N)
                    clientsTable_heading3 = Label(tableHeader, text="Email", font=("Dodge", 12, "bold"),
                                                  background=tableHeader_bG, anchor=CENTER)
                    clientsTable_heading3.place(relx=0.69, rely=0.3, anchor=N)
                    clientsTable_heading4 = Label(tableHeader, text="Contact", font=("Dodge", 12, "bold"),
                                                  background=tableHeader_bG, anchor=CENTER)
                    clientsTable_heading4.place(relx=0.9, rely=0.3, anchor=N)

                    # Opening the Clients Table in the User's Database
                    clientObj = ClientDetail(loggedInUser)

                    # Querying the 'clientDetails' table in the User's database and picking the matched record
                    all_clients = clientObj.all()

                    # Closing the connection with the Database
                    clientObj.closeDB()

                    # Confirming the 'clientDetails' table is not empty
                    if (all_clients != []):

                        iter_count = 0
                        for client in all_clients:

                            # Checking the Clients oid is even or odd
                            ODD_or_EVEN = "even" if (
                                iter_count % 2 == 0) else "odd"
                            iter_count += 1

                            # Filling columns and rows of the Clients-Table Fields with the data from User's Database
                            tableFields.insert("", "end", tag=ODD_or_EVEN, values=(
                                str(client[9]),
                                wrapTextLength(str(client[0]), 45),
                                wrapTextLength(str(client[1]), 25),
                                str(client[2])
                            ))

                        # Assigning a function to the Clients-Table Fields for opening the Update-Client Panel on mouse double-click
                        tableFields.bind("<Double-1>", lambda event: [
                            workSpace_leftFrame.after(200, lambda: [
                                leftPanelExpand_disabler(),
                                addNewClientPanel(request="view")
                            ]),
                            workSpace_leftFrame.after(
                                100, lambda: leftPanelShrinker())
                        ])

                    else:

                        # Showing the Empty-INFO on the Clients-Table Fields if the records from the 'clientDetails' table is empty
                        emptyField_INFO1.configure(text="Oops!")
                        emptyField_INFO1.place(
                            relx=0.5, rely=0.4, anchor=CENTER)
                        emptyField_INFO2.configure(
                            text="no Client details available to show")
                        emptyField_INFO2.place(
                            relx=0.5, rely=0.6, anchor=CENTER)

                elif (selectedLinkName == "Stocks"):

                    # Disabling and Styling the Stocks Tab-Link Button
                    tabLink4.configure(
                        style="SelectedTab-Link.TLabel", state=DISABLED)

                    # Changing the Title and the icon of the tab relavent to the Selected Tab
                    rightBottom_title.configure(
                        text=f"   {selectedLinkName}", image=stocks_obj)

                    # Assigning a function to the Add-Product Button to open the Add-Product Panel
                    newADD_btn.configure(text=f"Add Product", command=lambda: [
                        workSpace_leftFrame.after(200, lambda: [
                            leftPanelExpand_disabler("New"),
                            addNewProductPanel()
                        ]),
                        workSpace_leftFrame.after(
                            100, lambda: leftPanelShrinker())
                    ])

                    # Creating the headings for the Stocks-Table Header
                    stocksTable_heading1 = Label(tableHeader, text="No.", font=("Dodge", 12, "bold"),
                                                 background=tableHeader_bG, anchor=CENTER)
                    stocksTable_heading1.place(relx=0.08, rely=0.3, anchor=N)
                    stocksTable_heading2 = Label(tableHeader, text="Product Name", font=("Dodge", 12, "bold"),
                                                 background=tableHeader_bG, anchor=W)
                    stocksTable_heading2.place(relx=0.32, rely=0.3, anchor=N)
                    stocksTable_heading3_sym = Label(tableHeader, text=defaultCurrency[2], font=("Dodge", 12, "bold"),
                                                     background=tableHeader_bG, anchor=CENTER)
                    stocksTable_heading3_sym.place(
                        relx=0.735, rely=0.3, anchor=N)
                    stocksTable_heading3 = Label(tableHeader, text="Rate", font=("Dodge", 12, "bold"),
                                                 background=tableHeader_bG, anchor=CENTER)
                    stocksTable_heading3.place(relx=0.69, rely=0.3, anchor=N)
                    stocksTable_heading4 = Label(tableHeader, text="Quantity", font=("Dodge", 12, "bold"),
                                                 background=tableHeader_bG, anchor=CENTER)
                    stocksTable_heading4.place(relx=0.9, rely=0.3, anchor=N)

                    # Opening the Products(Stocks) Table in the User's Database
                    productObj = ProductDetail(loggedInUser)

                    # Querying the 'productDetails' table in the User's database and picking the matched record
                    productsInStock = productObj.all()

                    # Closing the connection with the Database
                    productObj.closeDB()

                    # Confirming the 'productDetails' table is not empty
                    if (productsInStock != []):

                        iter_count = 0
                        for product in productsInStock:

                            # Checking the Products oid is even or odd
                            ODD_or_EVEN = "even" if (
                                iter_count % 2 == 0) else "odd"
                            iter_count += 1

                            # Converting the Product Sales price to user prefered default currency
                            sales_rate = "%.2f" % (
                                float(product[4]) / float(defaultCurrency[4]))

                            # Filling columns and rows of the Products(Stocks)-Table Fields with the data from User's Database
                            tableFields.insert("", "end", tag=ODD_or_EVEN, values=(
                                str(product[6]),
                                wrapTextLength(str(product[0])),
                                sales_rate,
                                str(product[2]),
                            ))

                        # Assigning a function to the Stocks-Table Fields for opening the Update-Stock Panel on mouse double-click
                        tableFields.bind("<Double-1>", lambda event: [
                            workSpace_leftFrame.after(200, lambda: [
                                leftPanelExpand_disabler(),
                                addNewProductPanel(request="view")
                            ]),
                            workSpace_leftFrame.after(
                                100, lambda: leftPanelShrinker())
                        ])

                    else:

                        # Showing the Empty-INFO on the Products(Stocks)-Table Fields if the records from the 'productDetails' table is empty
                        emptyField_INFO1.configure(text="Out of Stock!")
                        emptyField_INFO1.place(
                            relx=0.5, rely=0.4, anchor=CENTER)
                        emptyField_INFO2.configure(
                            text="Seems to be no products are added to the Stocks")
                        emptyField_INFO2.place(
                            relx=0.5, rely=0.6, anchor=CENTER)

                # Creating the columns and rows for the Clients-Table Fields and Stocks-Table Fields
                tableFields["columns"] = ["1", "2", "3", "4"]
                tableFields.column("1",
                                   width=int(screen_width/1000), anchor=CENTER)
                tableFields.column("2",
                                   width=int(screen_width/6), anchor=CENTER)
                tableFields.column("3",
                                   width=int(screen_width/15), anchor=CENTER)
                tableFields.column("4",
                                   width=int(screen_width/60), anchor=CENTER)

            # Assigning a function to show/hide Table Fields INFO while mouse-hovering over the Table Fields on the Right-Bottom Panel
            tableFields.bind("<Enter>",
                             lambda event, button=newADD_btn["text"]: tableFields_INFO(event, button))
            tableFields.bind("<Leave>",
                             lambda event, button=newADD_btn["text"]: tableFields_INFO(event, button))

            # Lifting the Table Header frame over default table header
            tableHeader.lift(tableFields)

            # ------------------------------------------------------------------- Right-Bottom Panel's Table -StyleEnds----

        # If the Tab-Link Button selected is 'Settings' Button then creating the Settings Panel
        elif (selectedLinkName == "Settings"):

            # Disabling and Styling the Settings Tab-Link Button
            tabLink5.configure(style="SelectedTab-Link.TLabel", state=DISABLED)

            # Changing the Title and the icon of the tab relavent to the Selected Tab
            rightBottom_title.configure(
                text=f"   {selectedLinkName}", image=settings_obj)

            # Calling the function to create the Settings Panel
            workSpace_rightFrame.after(
                50, lambda: settingsTab(rightBottom_innerbgColor))

        # Lifting these widgets on top of other widgets
        title_frame.lift()
        title_bgColor.lift()
        close_X_btn.lift()
        minimize_btn.lift()

        # Checking if the WorkSpace's Left Panel is shrinked or not
        if (leftPanelShrinked):

            # Calling the function to shrink the WorkSpace's Left Panel
            leftPanelShrinker()

        # -------------------------------------------------------------------------------------------- `(in Voice)` WorkSpace -StyleEnds----

    # >>

    # Function to create the Settings Panel for user to change their preference and credentials
    def settingsTab(frame_S):

        # Function for displaying the Success Message after changes made to the Database
        def showSuccessMessage(prefer, passWd):

            # Confirming the Preferences or Password is changed
            if (prefer or passWd):

                if (prefer and passWd):

                    # Assigning a Success message
                    message = "# All the changes on the preferences and credentials where saved!"

                elif (prefer and passWd is False):

                    # Assigning a Success message
                    message = "# All the changes made on the preferences where saved!"

                elif (prefer is False and passWd):

                    # Assigning a Success message
                    message = "# Your credentials has been changed successfully!"

                # Showing a success message
                settings_INFO.configure(text=message, foreground="#01102E")

        # >>

        # Function for updating the new defaults and passwords to the User's Database
        def saveChangesMade(defaultValues):

            # Disabling the Save-Changes Button after clicked, for preventing the function to be called twice
            saveChanges_btn.configure(state=DISABLED)

            # Assigning a variable for controlling the saving process according to its value
            updatePreference = False
            updatePassword = False

            # Checking all the default values and modified values are the same
            for item in defaultValues:

                if (item[1] != item[0].get()):

                    # Changing the value of variable
                    updatePreference = True
                    break

            # Checking the Update User Preference request
            if (updatePreference):

                # Collecting and Converting the values to desired format
                currency_code = currencySelect_S.get().split(" ")[1]
                due_picked = dueSelect_S.get().split(" ")[1]
                tax_entered = int(taxEntry_S_Var.get()) if (
                    taxEntry_S_Var.get() != "") else 0

                # Opening the User Preferences Table in the User's Database
                preferenceObj = UserPreference(loggedInUser)

                # Updating the record in the 'userPreferences' table with the new ones
                preferenceObj.updateDefault(
                    currency_code, due_picked, tax_entered)

                # Closing the connection with the Database
                preferenceObj.closeDB()

                # Creating a new list of default values occupied on the Settings Panel before modifications
                newDefaultValues = [
                    (currencySelect_S, currencySelect_S.get()),
                    (dueSelect_S, dueSelect_S.get()),
                    (taxEntry_S_Var, taxEntry_S_Var.get())
                ]

                # Updating the arguments of function assigned with Save-Changes Button
                saveChanges_btn.configure(
                    command=lambda: saveChangesMade(newDefaultValues))

            # Checking the password entries are not empty
            if (new_passWrd_var.get() != "" or new_passWrdC_var.get() != ""):

                # Confirming the both password entries are filled
                if (new_passWrd_var.get() != "" and new_passWrdC_var.get() != ""):

                    # Opening the --- `(in Voice)` --- Database
                    appDB = UserCredential()

                    # Querying the 'userCredentials' table in --- `(in Voice)` --- main database and picking the matched record
                    userOldPwd = appDB.getUser(loggedInUser)[5]

                    # Checking for the length of the passwords is minimum of 8
                    if (len(new_passWrd_var.get()) < 8):

                        # Resetting the value of Confirm-Password Entry
                        new_passWrdC_var.set("")

                        # Showing a error message
                        settings_INFO.configure(
                            text="# Password should contain a minimum of 8 characters", foreground=err_fG)

                    elif (userOldPwd == new_passWrd_var.get()):

                        # Resetting the value of Confirm-Password Entry
                        new_passWrd_var.set("")
                        new_passWrdC_var.set("")

                        # Showing a error message
                        settings_INFO.configure(
                            text="# Password might be different from the existing one", foreground=err_fG)

                    elif (new_passWrd_var.get() != new_passWrdC_var.get()):

                        # Highlighting the password fields to indicate error
                        new_passWrd.configure(highlightbackground=err_fG)
                        new_passWrdC.configure(highlightbackground=err_fG)

                        # Resetting the value of Confirm-Password Entry
                        new_passWrdC_var.set("")

                        # Showing a error message
                        settings_INFO.configure(
                            text="# Passwords doesn't match, Try again!", foreground=err_fG)

                    elif (len(new_passWrd_var.get()) >= 8 and userOldPwd != new_passWrd_var.get() and new_passWrd_var.get() == new_passWrdC_var.get()):

                        # Updating the value of password field with new value
                        appDB.changePassword(loggedInUser,
                                             new_passWrd_var.get())

                        # Resetting the value of Confirm-Password Entry
                        new_passWrd_var.set("")
                        new_passWrdC_var.set("")

                        # Changing the value of variable
                        updatePassword = True

                    # Closing the connection with the Database
                    appDB.closeDB()

                else:

                    # Highlighting the password fields to indicate error
                    new_passWrd.configure(highlightbackground=err_fG)
                    new_passWrdC.configure(highlightbackground=err_fG)

                    # Resetting the value of Confirm-Password Entry
                    new_passWrdC_var.set("")

                    # Showing a error message
                    settings_INFO.configure(
                        text="# Both fields must be filled to change password", foreground=err_fG)

            elif (updatePreference is False and updatePassword is False):

                # Showing a error message
                settings_INFO.configure(
                    text="# No Changes made on the preferences to Save", foreground=err_fG)

            # Calling the function to show the success message
            showSuccessMessage(updatePreference, updatePassword)

            # Hiding the INFO about the Save-Changes request and Re-enabling the Save-Changes Button again
            frame_S.after(2100, lambda: [
                settings_INFO.configure(foreground=settings_bG),
                saveChanges_btn.configure(state=NORMAL),

                # Re-settings the Highlighted password fields to normal
                new_passWrd.configure(highlightbackground="#9BA984"),
                new_passWrdC.configure(highlightbackground="#9BA984")
            ])

        # >>

        # Function for validating the value of TaxPercentage-Entry is Integer
        def validatingTaxEntry(var, index, mode):

            # Confirming the TaxPercentage-Entry is not empty
            if (taxEntry_S_Var.get() != ""):

                try:

                    # Converting the entry value to a Integer, if value not integer throws a exception
                    int(taxEntry_S_Var.get())

                    # Checking the tax entered is not exceed 100
                    if (len(taxEntry_S_Var.get()) > 2):

                        # Showing a error message
                        messagebox.showerror(
                            "in Voice", "Percentage value must be a integer less than 100")

                        # Re-setting the TaxPercentage-Entry to zero if value exceeds 100
                        taxEntry_S_Var.set(0)

                except ValueError:

                    # Re-setting the TaxPercentage-Entry to zero if is not a integer
                    taxEntry_S_Var.set(0)

        # >>

        # Function to populate the dropdowns in the Settings Panel with some predefined data from User's Database
        def populate_Boxes(object, widget, label):

            # Opening the User Preferences Table in the User's Database
            preferenceObj = UserPreference(loggedInUser)

            # Querying the 'userPreferences' table in the User's database and picking the record
            preferences = preferenceObj.all()

            if (object is None and label == "Tax" and preferences is not None):

                # Setting the default tax percentage as a value for Tax-Percentage Entry
                widget.set(preferences[2])

            else:

                # Opening the Table in the User's Database
                user_DataBase = object(loggedInUser)

                # Creating a empty List to append the queryed records from tables in User's database
                newList = []

                # Confirming the request is from Currency-Select Combobox
                if (label == "Pick your Currency"):

                    # Querying the 'currencyRates' table in the User's database and picking all the currencies
                    all_currencies = user_DataBase.all()

                    # Confirming the Currency Rates are not empty
                    if (all_currencies != []):

                        # Checking the User preference is empty or not
                        prefer = preferences[0] if (
                            preferences is not None) else "INR"

                        for item in all_currencies:

                            # Filling the new list with records from database tables
                            newList.append(f" {item[0]} {item[2]}" if (
                                item[0] != "CHF") else f" {item[0]}")

                        # Assigning the Currency Code and Symbol from the Database as values to the Currency-Select Combobox
                        widget.configure(values=newList)

                # Confirming the request is from DueDate-Select Combobox
                elif (label == "Pick a Due"):

                    # Querying the 'dueDates' table in the User's database and picking all the records
                    all_duedates = user_DataBase.all()

                    # Confirming the Due Dates are not empty
                    if (all_duedates != []):

                        for day in all_duedates:

                            if (day[0] != "Nil"):

                                newList.append(f" {day[0]} days")

                            else:
                                newList.append(f" {day[0]}")

                        # Assigning the Due Days from the Database as values to the DueDate-Select Combobox
                        widget.configure(values=newList)

                        # Checking the User preference is empty or not
                        prefer = preferences[1] if (
                            preferences is not None) else "Nil"

                # Closing the connection with the Database
                user_DataBase.closeDB()

                # Iterating through the List created and assigning the default option for the Combobox
                for item in newList:

                    if (item.find(prefer) == 1):

                        # Setting the default option for Combobox
                        widget.current(newList.index(item))

            # Closing the connection with the Database
            preferenceObj.closeDB()

        # >>

        # Assigning the common colors for Settings Panel
        settings_bG = "#F0EFF4"
        settings_fG = "#360015"
        err_fG = "#EF233C"

        # Dash-Separator label
        separator = 0.05
        while (separator <= 0.95):

            # Creating a label with Dashs and positioning it under the Preferences label on the Settings Panel
            preferences_separater = Label(frame_S, text="___", font=("Dodge", 10),
                                          background=settings_bG)
            preferences_separater.place(relx=separator, rely=0.185,
                                        anchor=CENTER)

            # Creating a label with Dashs and positioning it under the Credentials label on the Settings Panel
            credentials_separater = Label(frame_S, text="___", font=("Dodge", 10),
                                          background=settings_bG)
            credentials_separater.place(relx=separator, rely=0.62,
                                        anchor=CENTER)

            # Increasing the X axis value
            separator += 0.01

        #        ---------------------------------------
        # ----------------- User-Preferences ------------------
        #        ---------------------------------------

        # Creating a Preferences label for displaying the title for a set of options
        preferences_title = Label(frame_S, text="Preferences", font=("Dongle", 13, "bold"),
                                  background=settings_bG)
        preferences_title.place(relx=0.92, rely=0.155, anchor=NE)

        #    -------------------------------------
        #          Currency-Select Combobox
        #    -------------------------------------

        # Styling the Comboboxes in Settings Panel
        selectBox_S_style = Style(frame_S)
        selectBox_S_style.theme_use("default")
        selectBox_S_style.configure("Settings-Select.TCombobox", arrowsize=18,
                                    background="#9BA984")
        # Mouse Hovering style for Comboboxes in Settings Panel
        selectBox_S_style.map("Settings-Select.TCombobox", fieldbackground=[("readonly", "!focus", "#FFFFFF"), ("readonly", "focus", "#FFFFFF")], background=[("readonly", "focus", "#9BA984")],
                              selectbackground=[("readonly", "!focus", "none"), ("readonly", "focus", "none")], selectforeground=[("readonly", "focus", "#0A0908"), ("readonly", "!focus", settings_fG)])

        # Creating the Currency-Select Combobox to pick the default Currency
        currencySelect_S = Combobox(frame_S, font=("Dodge", 10, "bold"), style="Settings-Select.TCombobox",
                                    cursor="hand2", width=int(screen_width/40), state="readonly")
        currencySelect_S.place(relx=0.115, rely=0.32,
                               height=int(screen_height/30), anchor=W)

        # Currency-Combobox label
        currencySelect_S_label = Label(frame_S, text="Pick your Currency", font=("Dodge", 13),
                                       background=settings_bG, foreground=settings_fG)
        currencySelect_S_label.place(relx=0.12, rely=0.26,
                                     anchor=W)

        # Calling the function to populate and set the default option for Currency-Select Combobox
        populate_Boxes(
            object=CurrencyRate,
            widget=currencySelect_S,
            label=currencySelect_S_label["text"]
        )

        #    -------------------------------------
        #           DueDate-Select Combobox
        #    -------------------------------------

        # Creating a DueDate-Select Combobox to pick the default due-date in days
        dueSelect_S = Combobox(frame_S, font=("Dodge", 10, "bold"), style="Settings-Select.TCombobox",
                               cursor="hand2", width=int(screen_width/80), state="readonly")
        dueSelect_S.place(relx=0.116, rely=0.5,
                          height=int(screen_height/30), anchor=W)

        # DueDate-Combobox label
        dueSelect_S_label = Label(frame_S, text="Pick a Due", font=("Dodge", 13),
                                  background=settings_bG, foreground=settings_fG)
        dueSelect_S_label.place(relx=0.12, rely=0.44, anchor=W)

        # Calling the function to populate and set the default option for DueDate-Select Combobox
        populate_Boxes(
            object=DueDate,
            widget=dueSelect_S,
            label=dueSelect_S_label["text"]
        )

        #    -------------------------------------
        #            Tax-Percentage Entry
        #    -------------------------------------

        # Creating a Tax-Percentage Entry for setting the default Tax for User in percentage
        taxEntry_S_Var = StringVar(frame_S)
        taxEntry_S = tk.Entry(frame_S, textvariable=taxEntry_S_Var, font=("Dodge", 12, "bold"),
                              width=int(screen_width/260), borderwidth=2, justify=RIGHT)
        taxEntry_S.place(relx=0.83, rely=0.32,
                         height=int(screen_height/25), anchor=E)

        # TaxPercentage-Entry label
        taxEntry_S_label = Label(frame_S, text="Tax in (%)", font=("Dodge", 11),
                                 background=settings_bG, foreground=settings_fG)
        taxEntry_S_label.place(relx=0.83, rely=0.26, anchor=E)

        # Calling the function to populate and set the default value for Tax-Percentage Entry
        populate_Boxes(
            object=None,
            widget=taxEntry_S_Var,
            label="Tax"
        )

        # Assigning a function to validate the value in Tax-Percentage Entry
        taxEntry_S_Var.trace_add("write", validatingTaxEntry)

        #        ---------------------------------------
        # ----------------- User-Credentials ------------------
        #        ---------------------------------------

        # Creating a Credentials label for displaying the title for a set of options
        credentials_title = Label(frame_S, text="Credentials", font=("Dongle", 13, "bold"),
                                  background=settings_bG)
        credentials_title.place(relx=0.92, rely=0.59, anchor=NE)

        # Creating a New-Password Entry
        new_passWrd_var = StringVar(frame_S)
        new_passWrd = tk.Entry(frame_S, textvariable=new_passWrd_var, font=("Dodge", 14, "bold"),
                               highlightcolor="#0A0908", highlightbackground="#9BA984", highlightthickness=0.5, show="\u25CF", justify=RIGHT)
        new_passWrd.place(relx=0.117, rely=0.82,
                          height=int(screen_height/20), width=int(screen_width/6), anchor=W)

        # New-Password Entry label
        new_passWrd_label = Label(frame_S, text="New-Password", font=("Dodge", 13),
                                  background=settings_bG, foreground=settings_fG)
        new_passWrd_label.place(relx=0.119, rely=0.73, anchor=W)

        # Creating a New-Password Confirm Entry
        new_passWrdC_var = StringVar(frame_S)
        new_passWrdC = tk.Entry(frame_S, textvariable=new_passWrdC_var, font=("Dodge", 14, "bold"),
                                highlightcolor="#0A0908", highlightbackground="#9BA984", highlightthickness=0.5, show="\u25CF", justify=RIGHT)
        new_passWrdC.place(relx=0.52, rely=0.82,
                           height=int(screen_height/20), width=int(screen_width/6), anchor=W)

        # New-Password Confirm Entry label
        new_passWrdC_label = Label(frame_S, text="Confirm-Password", font=("Dodge", 13),
                                   background=settings_bG, foreground=settings_fG)
        new_passWrdC_label.place(relx=0.52, rely=0.73, anchor=W)

        # Creating a list of default values occupied on the Settings Panel before modifications
        oldDefaultValues = [
            (currencySelect_S, currencySelect_S.get()),
            (dueSelect_S, dueSelect_S.get()),
            (taxEntry_S_Var, taxEntry_S_Var.get())
        ]

        #       -----------------------------------
        # ------------- Save-Changes Button --------------
        #       -----------------------------------

        # Styling the Save-Changes Button on the Settings Panel
        saveChanges_btn_style = Style(frame_S)
        saveChanges_btn_style.theme_use("default")
        saveChanges_btn_style.configure("Save-Changes.TButton", font=("Dodge", 10, "bold"), background="#0CB0A9",
                                        borderwidth=3, focuscolor="none", anchor=CENTER)
        # Mouse Hovering style for Save-Changes Button
        saveChanges_btn_style.map("Save-Changes.TButton", foreground=[("active", "!disabled", "#000000")],
                                  background=[("active", "#61818D")])

        # Creating the Save-Changes Button to save the user modified values as their new defaults
        saveChanges_btn = Button(frame_S, text="Save Changes", style="Save-Changes.TButton",
                                 command=lambda: saveChangesMade(oldDefaultValues))
        saveChanges_btn.place(relx=0.93, rely=0.95, anchor=SE)

        # Creating a label to show INFO about the Save-Changes request
        settings_INFO = Label(frame_S, font=("Dodge", 11, "bold"), background=settings_bG,
                              foreground=settings_bG, justify=RIGHT)
        settings_INFO.place(relx=0.1, rely=0.95, anchor=SW)

    # >>

    # ------------------------------------- `(in Voice)` Home-Screen -StyleStarts----------------------------------------------------

    # Making the root-Window to fullscreen and non-resizable
    root.wm_state("zoomed")

    #     -----------------------------------------
    # -------------------- Title Bar ---------------------
    #     -----------------------------------------

    # Creating a frame for the title bar and positioning it on root-Window
    title_frame = Frame(root, width=screen_width, height=int(screen_height/24))
    title_frame.place(relx=0.5, rely=0, anchor=N)

    # Creating a label to set a background color for the title bar
    title_bgColor = Label(title_frame, width=screen_width,
                          background="#011932", borderwidth=1)
    title_bgColor.place(relx=0.5, rely=0.5,
                        height=int(screen_height/22), anchor=CENTER)

    #       -----------------------------------------
    # -------------------- Close(X) Button ---------------------
    #       -----------------------------------------

    # Styling the Close(X) Button
    close_X_btn_style = Style(title_frame)
    close_X_btn_style.theme_use("default")
    close_X_btn_style.configure("Close_X.TButton", font=("Dodge", 14, "bold"),
                                foreground="#B3C6E7", background="#011932", borderwidth=0, focuscolor="none")
    # Mouse Hovering style for Close(X) Button
    close_X_btn_style.map("Close_X.TButton", foreground=[("active", "!disabled", "#011932")],
                          background=[("active", "#EF233C")])

    # Creating the Close(X) Button to quit the Application and positioning it on the title bar
    close_X_btn = Button(title_frame, text="X", style="Close_X.TButton",
                         command=lambda: closeInVoiceAPP())
    close_X_btn.place(relx=0.998, rely=0.5, width=int(screen_width/27),
                      height=int(screen_height/28), anchor=E)

    # Assigning a function to show/hide Close(X) Button INFO while hovering
    close_X_btn.bind("<Enter>", titleBar_INFO)
    close_X_btn.bind("<Leave>", titleBar_INFO)

    #         -----------------------------------------
    # -------------------- Minimize Button ---------------------
    #         -----------------------------------------

    # Styling the Minimize Button
    minimize_btn_style = Style(title_frame)
    minimize_btn_style.theme_use("default")
    minimize_btn_style.configure("Minimize.TButton", foreground="#B3C6E7",
                                 background="#011932", borderwidth=0, focuscolor="none")
    # Mouse Hovering style for Minimize Button
    minimize_btn_style.map("Minimize.TButton", foreground=[("active", "!disabled", "#FF0000")],
                           background=[("active", "#01102E")])

    # Resizing the -- logo -- image and converting it into a object to display on a widget
    global logo_obj
    logo_obj = ImageTk.PhotoImage(logo.resize((33, 30), resampling_filter))

    # Creating a Minimize Button to minimize the Application and displaying it as a logo on the title bar
    minimize_btn = Button(title_frame, text="-",  style="Minimize.TButton", image=logo_obj,
                          command=lambda: minimizeInvoiceAPP())
    minimize_btn.place(relx=0.015, rely=0.5, width=int(screen_width/35),
                       height=int(screen_height/25), anchor=CENTER)

    # Assigning a function to show/hide Minimize Button INFO while hovering
    minimize_btn.bind("<Enter>", titleBar_INFO)
    minimize_btn.bind("<Leave>", titleBar_INFO)

    #         -----------------------------------------
    # -------------------- Main Panel (or) Home ---------------------
    #         -----------------------------------------

    # Creating a frame for the Main Panel and positioning it on root-Window
    home_frame = Frame(root, height=int(screen_height/1.035),
                       width=int(screen_width))
    home_frame.place(relx=0.5, rely=1, anchor=S)

    # Assigning a common background color for Main Panel
    main_bG = "#C8C8C8"

    # Creating a label to set a background color for the Main Panel
    main_bgColor = Label(home_frame, background=main_bG,
                         width=int(screen_width))
    main_bgColor.place(relx=0.5, rely=0.5,
                       height=int(screen_height), anchor=CENTER)

    # Styling the SignIn & AboutUs Button
    signIn_btn_style = Style(home_frame)
    signIn_btn_style.theme_use("default")
    signIn_btn_style.configure("SignInAbout.TButton", font=("Dodge", 16, "bold", "italic"),
                               foreground="#F0EFF4", background="#BF09D5", borderwidth=2, highlightthickness=0, focuscolor="none")
    # Mouse Hovering style for SignIn Button
    signIn_btn_style.map("SignInAbout.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                         background=[("active", "#DB12AF")])

    # Creating the SignIn Button
    signIn_btn = Button(home_frame, text="Sign In",
                        style="SignInAbout.TButton", command=lambda: signInPanel())
    signIn_btn.place(relx=0.9, rely=0.1, anchor=CENTER)

    # Creating the AboutUs Button
    aboutUs_btn = Button(home_frame, text="About Us",
                         style="SignInAbout.TButton", command=lambda: aboutUsPanel())
    aboutUs_btn.place(relx=0.1, rely=0.1, anchor=CENTER)

    # Creating labels for displaying the APP's name on the Main Panel
    appName_part1 = Label(home_frame, text="in", foreground="#000040",
                          background=main_bG, font=("Magneto", 100, "bold"))
    appName_part1.place(relx=0.5, rely=0.2, anchor=CENTER)

    appName_part2 = Label(home_frame, text="Voice", foreground="#464646",
                          background=main_bG, font=("Matura MT Script Capitals", 25, "bold"))
    appName_part2.place(relx=0.55, rely=0.3, anchor=CENTER)

    #         -----------------------------------------
    # -------------------- Tab-Buttons ---------------------
    #         -----------------------------------------

    # Styling the Tab-Buttons in the Main Panel
    TAB_btn_style = Style(home_frame)
    TAB_btn_style.theme_use("default")
    TAB_btn_style.configure("TAB.TButton", font=("Dodge", 30, "bold", "italic"),
                            foreground="#F0EFF4", background="#F72585", borderwidth=2, focuscolor="none", higlightthickness=0, anchor=N)

    # Blured styling for Tab-Buttons in the Main Panel
    TAB_btn_style.configure("TAB-Blur.TButton", font=("Dodge", 30, "bold", "italic"),
                            foreground="#E598AE", background="#B7094C", borderwidth=1, focuscolor="none", higlightthickness=0, anchor=N)
    # Mouse Hovering style for Tab-Buttons in the Main Panel
    TAB_btn_style.map("TAB.TButton", foreground=[("active", "!disabled", "#F0EFF4")],
                      background=[("active", "#F72585")])

    # Creating a InVoice Tab-Button for opening InVoices Tab
    inVoiceTAB_btn = Button(home_frame, text="\rInVoices",
                            style="TAB.TButton", command=lambda: signInPanel())
    inVoiceTAB_btn.place(relx=0.5, rely=0.7,
                         height=int(screen_height/2.7), width=int(screen_width/4.7), anchor=CENTER)

    # Assigning a function to change the style of InVoice Tab-Button while hovering
    inVoiceTAB_btn.bind("<Enter>", TAB_hoveringEffect)
    inVoiceTAB_btn.bind("<Leave>", TAB_hoveringEffect)

    # Creating a Client-Tab Button for opening Clients Tab
    clientTAB_btn = Button(home_frame, text="\rClients",
                           style="TAB.TButton", command=lambda: signInPanel())
    clientTAB_btn.place(relx=0.2, rely=0.7,
                        height=int(screen_height/3), width=int(screen_width/5), anchor=CENTER)

    # Assigning a function to change the style of Client-Tab Button while hovering
    clientTAB_btn.bind("<Enter>", TAB_hoveringEffect)
    clientTAB_btn.bind("<Leave>", TAB_hoveringEffect)

    # Creating a Stock-Tab Button for opening Stocks Tab
    stockTAB_btn = Button(home_frame, text="\rStocks",
                          style="TAB.TButton", command=lambda: signInPanel())
    stockTAB_btn.place(relx=0.8, rely=0.7,
                       height=int(screen_height/3), width=int(screen_width/5), anchor=CENTER)

    # Assigning a function to change the style of Stock Tab-Button while hovering
    stockTAB_btn.bind("<Enter>", TAB_hoveringEffect)
    stockTAB_btn.bind("<Leave>", TAB_hoveringEffect)

    # Styling the labels on the Tab-Buttons
    TAB_label_style = Style(home_frame)
    TAB_label_style.theme_use("default")
    TAB_label_style.configure("TAB.TLabel", font=("Dodge", 12, "bold", "italic"), foreground="#E598AE", background="#832161",
                              borderwidth=2, focuscolor="none", higlightthickness=0, relief=SUNKEN, justify=CENTER, anchor=CENTER)
    # Blur style
    TAB_label_style.configure("TAB-Blur.TLabel", font=("Dodge", 12, "bold", "italic"),
                              foreground="#E598AE", background="#602453", borderwidth=1, focuscolor="none", higlightthickness=0, relief=SUNKEN, justify=CENTER, anchor=CENTER)

    # Creating a label for placing on the InVoice Tab-Button
    inVoiceTAB_btnLabel = Label(inVoiceTAB_btn, text="\nCREATE,    VIEW   & \r\nMODIFY   inVoices\n",
                                style="TAB.TLabel")
    inVoiceTAB_btnLabel.place(relx=0.5, rely=0.7,
                              width=int(screen_width/5), anchor=CENTER)

    # Assigning a function to the InVoice Tab-Button's label for opening InVoices Tab
    inVoiceTAB_btnLabel.bind("<Button-1>", lambda *_: signInPanel())

    # Creating a label for placing on the Client Tab-Button
    clientTAB_btnLabel = Label(clientTAB_btn, text="\nADD,    VIEW   & \r\nEDIT   client's details\n",
                               style="TAB.TLabel")
    clientTAB_btnLabel.place(relx=0.5, rely=0.72,
                             width=int(screen_width/5.3), anchor=CENTER)

    # Assigning a function to the InVoice Tab-Button's label for opening InVoices Tab
    clientTAB_btnLabel.bind("<Button-1>", lambda *_: signInPanel())

    # Creating a label for placing on the Stock Tab-Button
    stockTAB_btnLabel = Label(stockTAB_btn, text="\n    ADD   & \r\nUPDATE   stocks \n",
                              style="TAB.TLabel")
    stockTAB_btnLabel.place(relx=0.5, rely=0.72,
                            width=int(screen_width/5.3), anchor=CENTER)

    # Assigning a function to the InVoice Tab-Button's label for opening InVoices Tab
    stockTAB_btnLabel.bind("<Button-1>", lambda *_: signInPanel())

    # Lifting these widgets on top of other widgets
    title_frame.lift()
    title_bgColor.lift()
    close_X_btn.lift()
    minimize_btn.lift()

    # -------------------------------------------------------------------------------------------- `(in Voice)` Home-Screen -StyleEnds----


# Function which creates the --- `(in Voice)` --- Launcher
def inVoice_Launcher():

    # Function which animates the dots in the launching countdown
    def launchingDotsAnimator(dots, timeInSEC, timer_widget):

        if (timeInSEC <= 5 and timeInSEC > 0.2):

            # Changing the dots according to the previous dot
            match dots:

                case "..." | ".. ":
                    dots = " .."

                case " ..":
                    dots = ". ."

                case ". .":
                    dots = ".. "

            # Changing the text of the launching timer over the Palette-Image
            launcher_palette.itemconfigure(timer_widget,
                                           text=txt1 + str(int(timeInSEC) if (int(timeInSEC) > 1) else 1) + txt2 + dots)

            # Calculating the time remaining to launch
            timeInSEC = float("%.1f" % (timeInSEC - 0.2))

            # Calling the function to animate the dots in the launching countdown
            root.after(200, lambda: launchingDotsAnimator(
                dots, timeInSEC, timer_widget))

    # >>

    # Function which creates and runs the launching countdown
    def launchingCountdown(timeRemaining, timer_widget=None):

        # Decreasing the time in seconds
        timeRemaining = timeRemaining - 1

        # Checking if the launching timer and text is created
        if (timer_widget is None):

            # Creating and Positioning the launching timer and text over the Palette-Image
            countdown_timer = launcher_palette.create_text(335, 245, text=txt1 + str(timeRemaining) + txt2 + initialdots,
                                                           font=("Dongle", 9), fill="#D6DDE8")

            # Calling the function to animate the dots in the launching countdown
            root.after(200, lambda: launchingDotsAnimator(
                initialdots, 5, countdown_timer))

            # Calling the function to countingdown the launching timer
            root.after(1000, lambda: launchingCountdown(
                timeRemaining, countdown_timer))

        # Checking if the launching timer is stopped
        elif (timeRemaining == 0 and timer_widget is not None):

            # Calling the function to create the structure of the --- `(in Voice)` --- Home-Screen
            root.after(110, lambda: inVoice_HomeScreen())

            # Destroying the --- `(in Voice)` --- Launcher's palette and its child widgets
            root.after(120, lambda: launcher_palette.destroy())

        else:

            # Calling the function to countingdown the launching timer
            root.after(1000, lambda: launchingCountdown(
                timeRemaining, timer_widget))

    # >>

    # Function which creates the APP's launching animation with the APP and developer name on it
    def initiate_Launcher(content):

        # Checking to create the next animation of the --- `(in Voice)` --- Launcher
        match content:

            # ------------------------------------- `(in Voice)` Launcher's Content -StyleStarts----------------------------------------------------

            case "in":

                # Creating and Positioning the first part of APP's name over the Palette-Image
                launcher_palette.create_text(250, 100, text=content,
                                             fill="#B3C6E7", font=("Magneto", 80, "bold"))

                # Calling the function to create the second part of APP's name
                root.after(400, lambda: initiate_Launcher("Voice"))

            case "Voice":

                # Creating and Positioning the second part of APP's name over the Palette-Image
                launcher_palette.create_text(260, 160, text=content,
                                             fill="#D6DDE8", font=("Matura MT Script Capitals", 18, "bold"))

                # Calling the function to create the designation
                root.after(800, lambda: initiate_Launcher("developed by"))

            case "developed by":

                # Creating and Positioning the designation over the Palette-Image
                launcher_palette.create_text(33, 232, text=content,
                                             fill="#00000E", font=("Dongle", 7))

                # Calling the function to create the name of the developer
                root.after(400, lambda: initiate_Launcher("Mahendra Kumara"))

            case "Mahendra Kumara":

                # Creating and Positioning the developer name over the Palette-Image
                launcher_palette.create_text(68, 247, text=content,
                                             fill="#01102E", font=("Playball", 8, "bold", "italic"))

                # Calling the function to create the launching timer
                root.after(800, lambda: launchingCountdown(6))

            # -------------------------------------------------------------------------------------------- `(in Voice)` Launcher's Content -StyleEnds----

    # >>

    # ------------------------------------- `(in Voice)` Launcher -StyleStarts----------------------------------------------------

    # Creating a palette for placing a background-image on the --- `(in Voice)` --- Launcher
    launcher_palette = Canvas(root, width=window_width,
                              height=window_height, highlightthickness=0)
    launcher_palette.grid()

    # Opening and resizing the Image to fit to the size of the palette, and also converting it into a PhotoImage object
    launcher_image = Image.open(f"{img_DIR}launcher.jpg")
    launcher_image = launcher_image.resize((window_width, window_height),
                                           resampling_filter)
    launcher_image = ImageTk.PhotoImage(launcher_image)

    # Placing the converted-image on the --- `(in Voice)` --- Launcher's palette
    launcher_palette.create_image(0, 0, anchor=NW, image=launcher_image)

    # Assigning the constant texts to the timer
    txt1 = "Starting in "
    txt2 = " s"
    initialdots = "..."

    # Calling the function to create the --- `(in Voice)` --- Launcher's animations
    root.after(500, lambda: initiate_Launcher("in"))

    # -------------------------------------------------------------------------------------------- `(in Voice)` Launcher -StyleEnds----

    # Continuously showing the root-Window
    root.mainloop()


if __name__ == "__main__":
    inVoice_Launcher()

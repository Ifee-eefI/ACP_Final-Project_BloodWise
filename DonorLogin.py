import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import font
from tkinter import PhotoImage
from DonorPanel import donor_panel


def donor_login():
    def create_user_table(username):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bloodbank_db"
            )

            cursor = connection.cursor()

            # Create a unique table for the user based on their username
            create_table_query = f"CREATE TABLE IF NOT EXISTS user_{username} (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), DonationType VARCHAR(255), password VARCHAR(255), phone VARCHAR(255), gender VARCHAR(255))"
            cursor.execute(create_table_query)

            connection.commit()
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def check_user_credentials(username, password):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bloodbank_db"
            )

            cursor = connection.cursor()

            # Query the user's specific table for login credentials
            query = f"SELECT * FROM user_{username} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            cursor.close()
            connection.close()

            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    root = tk.Tk()
    root.title("Donor Login")
    # width and height
    w = 450
    h = 535
    # bg color
    bgcolor = "#F4BF96"

    # center form
    root.overrideredirect()  # remove border
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws - w) / 2
    y = (hs - h) / 2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

    # top widgets
    top_custom_font = font.Font(family="Berlin Sans FB Demi", size=15, weight="bold")
    top_frame = tk.Frame(root,
                         borderwidth=3,
                         bg="black")
    top_frame.pack(anchor="n", fill="x", expand=True)

    top_canvas = tk.Canvas(top_frame,
                           bg="#FFF4E0")
    top_canvas.pack(fill="both", expand=True)

    top_label_image = PhotoImage(file="C:\\Users\\Jhun Harvey\\Pictures\\Logo.png")
    top_label_image = top_label_image.subsample(4)
    top_label = tk.Label(top_canvas,
                         bg="#FFF4E0",
                         image=top_label_image,
                         text=" BloodWise: Donor Login",
                         font=top_custom_font,
                         compound="left"
                         )
    top_label.pack(side="left")
    """end of top widgets"""
    # -----------------------------------START OF LOGIN GUI-----------------------------------------------------------#
    mainframe = tk.Frame(root, width=w, height=h)
    loginframe = tk.Frame(mainframe, width=500, height=400)
    login_contentframe = tk.Frame(loginframe, padx=30, pady=100, bg=bgcolor)

    username_label = tk.Label(login_contentframe, text='Username: ', font=('Verdana', 16), bg=bgcolor)
    password_label = tk.Label(login_contentframe, text='Password: ', font=('Verdana', 16), bg=bgcolor)

    username_entry = tk.Entry(login_contentframe, font=('Verdana', 16))
    password_entry = tk.Entry(login_contentframe, font=('Verdana', 16), show='*')

    login_button = tk.Button(login_contentframe, text='LOGIN', font=('Verdana', 16), bg='#CE5A67', fg='#fff', padx=25,
                             pady=10, width=25)

    login_label = tk.Button(login_contentframe, text='SIGN UP', font=('Verdana', 12), bg='#CE5A67', fg='#fff', padx=25,
                            pady=10, width=25)
    reminder_to_login = tk.Label(login_contentframe, text='No Existing Account? Click the Sign up Button to Register',
                                 font=('Verdana', 10), bg=bgcolor)
    mainframe.pack(fill='both', expand=1)
    loginframe.pack(fill='both', expand=1)
    login_contentframe.pack(fill='both', expand=1)

    username_label.grid(row=0, column=0, pady=10)
    username_entry.grid(row=0, column=1)

    password_label.grid(row=1, column=0, pady=10)
    password_entry.grid(row=1, column=1)

    login_button.grid(row=2, column=0, columnspan=2, pady=20)

    login_label.grid(row=3, column=0, columnspan=2, pady=10)

    error_label1 = tk.Label(login_contentframe, text='', font=('Verdana', 12), fg='red', bg='#F4BF96')
    error_label1.grid(row=5, column=0, columnspan=2, )
    success_label1 = tk.Label(login_contentframe, text='', font=('Verdana', 12), fg='green', bg='#F4BF96')
    success_label1.grid(row=6, column=0, columnspan=2, pady=10)

    reminder_to_login.grid(row=7, column=0, columnspan=2, pady=10)

    # -------------------------------------------END OF LOGIN GUI-----------------------------------------------------------#

    def go_to_register():
        loginframe.pack_forget()
        root.title("Donor Registration")
        registerframe.pack(fill='both', expand=1)

    login_label.config(command=go_to_register)

    def login_donor():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bloodbank_db"
                )

                cursor = connection.cursor()

                query = "SELECT * FROM `system_users` WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()

                if result:
                    success_label1.config(text="Login successful!")
                    create_user_table(username)
                    root.destroy()
                    donor_panel()
                else:
                    error_label1.config(text="Login failed. Invalid Username or password.")

                cursor.close()
                connection.close()
            except mysql.connector.Error as err:
                error_label1.config(text=f"Error: {err}")
        else:
            error_label1.config(text="Please enter Username and password.")

    login_button.config(command=login_donor)
    # ---------------------------------------------- START OF REGISTER GUI ----------------------------------------------------------------##

    registerframe = tk.Frame(mainframe, width=600, height=900)
    registerframe.pack(fill='both', expand=1)
    registerframe.pack_forget()

    register_contentframe = tk.Frame(registerframe, padx=15, pady=30, highlightcolor='yellow', bg='#F4BF96')
    register_contentframe.pack(fill='both', expand=1)

    fullname_label_rg = tk.Label(register_contentframe, text='Fullname: ', font=('Verdana', 14), bg='#F4BF96')
    username_label_rg = tk.Label(register_contentframe, text='Username: ', font=('Verdana', 14), bg='#F4BF96')
    password_label_rg = tk.Label(register_contentframe, text='Password: ', font=('Verdana', 14), bg='#F4BF96')
    confirmpass_label_rg = tk.Label(register_contentframe, text='Re-Password: ', font=('Verdana', 14), bg='#F4BF96')
    phone_label_rg = tk.Label(register_contentframe, text='Contact: ', font=('Verdana', 14), bg=bgcolor)
    gender_label_rg = tk.Label(register_contentframe, text='Sex: ', font=('Verdana', 14), bg=bgcolor)

    fullname_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 14), width=22)
    username_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 14), width=22)
    password_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 14), width=22, show='*')
    confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 14), width=22, show='*')
    phone_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 14), width=22)
    radiosframe = tk.Frame(register_contentframe)
    gender = StringVar()
    gender.set('Male')
    male_radiobutton = tk.Radiobutton(radiosframe, text='Male', font=('Verdana', 14), bg=bgcolor, variable=gender,
                                      value='Male')
    female_radiobutton = tk.Radiobutton(radiosframe, text='Female', font=('Verdana', 14), bg=bgcolor, variable=gender,
                                        value='Female')

    register_button = tk.Button(register_contentframe, text='REGISTER', font=('Verdana', 16), bg='#CE5A67', fg='#fff',
                                padx=25, pady=5, width=25)
    go_login_label = tk.Button(register_contentframe, text='LOG IN', font=('Verdana', 12), bg='#CE5A67', fg='#fff',
                               padx=25, pady=5, width=25)

    fullname_label_rg.grid(row=0, column=0, pady=5, sticky='e')
    fullname_entry_rg.grid(row=0, column=1)

    username_label_rg.grid(row=1, column=0, pady=5, sticky='e')
    username_entry_rg.grid(row=1, column=1)

    password_label_rg.grid(row=2, column=0, pady=5, sticky='e')
    password_entry_rg.grid(row=2, column=1)
    confirmpass_label_rg.grid(row=3, column=0, pady=5, sticky='e')
    confirmpass_entry_rg.grid(row=3, column=1)

    phone_label_rg.grid(row=4, column=0, pady=5, sticky='e')
    phone_entry_rg.grid(row=4, column=1)

    gender_label_rg.grid(row=5, column=0, pady=5, sticky='e')
    radiosframe.grid(row=5, column=1)
    male_radiobutton.grid(row=0, column=0)
    female_radiobutton.grid(row=0, column=1)

    register_button.grid(row=7, column=0, columnspan=2, pady=10)

    go_login_label.grid(row=8, column=0, columnspan=2, pady=10)

    error_label = tk.Label(register_contentframe, text='', font=('Verdana', 12), fg='red', bg='#F4BF96')
    error_label.grid(row=9, column=0, columnspan=2, pady=10)

    # Success message label
    success_label = tk.Label(register_contentframe, text='', font=('Verdana', 9), fg='green', bg='#F4BF96')
    success_label.grid(row=10, column=0, columnspan=2, pady=10)

    def save_user_registration():
        fullname = fullname_entry_rg.get()
        username = username_entry_rg.get()
        password = password_entry_rg.get()
        confirmpass = confirmpass_entry_rg.get()
        phone = phone_entry_rg.get()
        gdr = gender.get()

        if username and password and confirmpass:
            if password == confirmpass:
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bloodbank_db"  # pangalan nang database
                    )

                    cursor = connection.cursor()

                    insert_query = (
                        "INSERT INTO `system_users`(`fullname`, `username`, `password`, `phone`, `gender`) VALUES (%s,%s,%s,%s,%s)")

                    cursor.execute(insert_query, (fullname, username, password, phone, gdr))
                    connection.commit()
                    cursor.close()
                    connection.close()

                    success_label.config(text="User registration successful! Click the Login Button")
                    error_label.config(text='')

                    fullname_entry_rg.delete(0, tk.END)
                    username_entry_rg.delete(0, tk.END)
                    password_entry_rg.delete(0, tk.END)
                    confirmpass_entry_rg.delete(0, tk.END)
                    phone_entry_rg.delete(0, tk.END)
                except mysql.connector.Error as error:
                    print(f"Error: {error}")
            else:
                error_label.config(text="Password and Re-Password do not match.")

        else:
            error_label.config(text="Please fill up all the fields")

    register_button.config(command=save_user_registration)

    # ---------------------------------------------- END OF REGISTER GUI ----------------------------------------------------------------##

    def go_to_login_from_registration():
        registerframe.pack_forget()
        root.title("Donor Login")
        loginframe.pack(fill='both', expand=1)

    go_login_label.config(command=go_to_login_from_registration)

    def gobacktohomepage():
        root.destroy()
        from HomePage import homepage
        homepage()

    button = tk.Button(top_canvas, text="Homepage", bg='#CE5A67', command=gobacktohomepage)
    button.pack(side="right", anchor="e", padx=10)

    root.mainloop()

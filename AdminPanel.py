import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox


def admin_panel():
    """window designs================================================================================================"""
    window = tk.Tk()
    window.title("Admin Panel")
    window.attributes("-fullscreen", True)
    window_width = 1600  # Set your desired window width
    window_height = 780  # Set your desired window height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bloodbank_db"
    )

    def toggle_fullscreen(event):
        if window.attributes('-fullscreen'):
            window.attributes('-fullscreen', False)
        else:
            window.attributes('-fullscreen', True)

    window.bind("<F11>", toggle_fullscreen)
    window.bind("<Escape>", toggle_fullscreen)
    window_frame = tk.Frame(window)
    window_frame.pack(fill="both", expand=True)
    """end of window designs========================================================================================="""

    """top widgets==================================================================================================="""
    top_frame = tk.Frame(window_frame, borderwidth=2, bg="black")
    top_frame.pack(anchor="n", fill="x")

    top_frame_frame = tk.Frame(top_frame, bg="#D80032")
    top_frame_frame.pack(fill="both", expand=True)

    top_label_image = PhotoImage(file="C:\\Users\\Jhun Harvey\\Pictures\\Logo.png")
    top_label_image = top_label_image.subsample(4)
    top_label = tk.Label(top_frame_frame,
                         bg="#D80032",
                         image=top_label_image,
                         text=" BloodWise: A Blood Bank Management System",
                         font=("Arial", 15, "bold"),
                         compound="left")
    top_label.pack(side="left")
    """end of top widgets============================================================================================"""

    """manage schedule button function========================================================================="""
    def on_schedule_click():
        left_schedule_button.config(state="disabled", relief="sunken", disabledforeground="white")
        left_alldonor_button.config(state="normal", relief="raised")
        left_dashboard_button.config(state="normal", relief="raised")
        left_about_us_button.config(state="normal", relief="raised")
        left_help_button.config(state="normal", relief="raised")

        for widget in alldonor_frame.winfo_children():
            widget.pack_forget()
        alldonor_frame.forget()

        for widget in dashboard_frame.winfo_children():
            widget.pack_forget()
        dashboard_frame.forget()

        for widget in about_us_frame.winfo_children():
            widget.pack_forget()
        about_us_frame.forget()

        for widget in help_frame.winfo_children():
            widget.pack_forget()
        help_frame.forget()

        available_schedule_frame.pack(fill="both", expand=True)
        available_schedule_canvas.pack(fill="both", expand=True)
        for widget in available_schedule_frame.winfo_children():
            widget.pack(fill="both", expand=True)
    """end of manage schedule button function========================================================================"""

    """alldonor button function======================================================================================"""

    def on_alldonor_click():
        left_alldonor_button.config(state="disabled", relief="sunken", disabledforeground="white")
        left_schedule_button.config(state="normal", relief="raised")
        left_dashboard_button.config(state="normal", relief="raised")
        left_about_us_button.config(state="normal", relief="raised")
        left_help_button.config(state="normal", relief="raised")

        for widget in available_schedule_frame.winfo_children():
            widget.pack_forget()
        available_schedule_frame.forget()

        for widget in dashboard_frame.winfo_children():
            widget.pack_forget()
        dashboard_frame.forget()

        for widget in about_us_frame.winfo_children():
            widget.pack_forget()
        about_us_frame.forget()

        for widget in help_frame.winfo_children():
            widget.pack_forget()
        help_frame.forget()

        alldonor_frame.pack(fill="both", expand=True)
        alldonor_canvas.pack(fill="both", expand=True)
        for widget in alldonor_canvas.winfo_children():
            if widget == alldonor_searchandsort_frame:
                widget.pack(anchor="w", fill="x")
                for widget1 in alldonor_searchandsort_frame.winfo_children():
                    if widget1 == alldonor_search_entry or widget1 == alldonor_sort_entry:
                        widget1.pack(side="left", padx=(85, 0), pady=(10, 10))
                    elif widget1 == alldonor_search_button or widget1 == alldonor_sort_button:
                        widget1.pack(side="left", padx=(10, 0))
                    elif widget1 == alldonor_search_label:
                        widget1.pack(side="left", padx=(85, 0))
                    elif widget1 == alldonor_search_entry_label:
                        widget1.pack(side="left", padx=(10, 0), pady=(10, 10))
                    elif widget1 == alldonor_tree_refresh:
                        widget1.pack(side="left", padx=(145, 0))
            elif widget == tree:
                widget.pack()
            elif widget == alldonor_add_update_delete_button_frame:
                widget.pack(side="left", fill="y")
                for widget2 in alldonor_add_update_delete_button_frame.winfo_children():
                    widget2.pack(side="top", padx=(5, 5), pady=(20, 0))
            elif widget == alldonor_frame_of_each_button:
                widget.pack(side="top", pady=(20, 0), padx=(0, 40))
            else:
                widget.pack()
    """end of alldonor button function==============================================================================="""

    """dashboard button function======================================================================================="""
    def populate_dashboard():
        cursor = connection.cursor()
        blood_types = ['Blood(A+)', 'Blood(B+)', 'Blood(AB+)', 'Blood(O+)', 'Blood(A-)', 'Blood(B-)', 'Blood(AB-)',
                       'Blood(O-)', 'Power Red', 'Platelets', 'AB Plasma']
        total_amounts = {}
        for blood_type in blood_types:
            query = f"SELECT SUM(Donation_Amount) FROM admin_table WHERE Donation_Type = '{blood_type}'"
            cursor.execute(query)
            total_amount = cursor.fetchone()[0] or 0
            total_amounts[blood_type] = total_amount
            if blood_type == 'Blood(A+)':
                aplus = total_amount
                dashboard_button_in_frame_2_1.config(text=f"Blood(A+): {aplus}mL")
            elif blood_type == 'Blood(B+)':
                bplus = total_amount
                dashboard_button_in_frame_2_2.config(text=f"Blood(B+): {bplus}mL")
            elif blood_type == 'Blood(AB+)':
                abplus = total_amount
                dashboard_button_in_frame_2_3.config(text=f"Blood(AB+): {abplus}mL")
            elif blood_type == 'Blood(O+)':
                oplus = total_amount
                dashboard_button_in_frame_2_4.config(text=f"Blood(O+): {oplus}mL")
            elif blood_type == 'Blood(A-)':
                aminus = total_amount
                dashboard_button2_in_frame_2_1.config(text=f"Blood(A-): {aminus}mL")
            elif blood_type == 'Blood(B-)':
                bminus = total_amount
                dashboard_button2_in_frame_2_2.config(text=f"Blood(B-): {bminus}mL")
            elif blood_type == 'Blood(AB-)':
                abminus = total_amount
                dashboard_button2_in_frame_2_3.config(text=f"Blood(AB-): {abminus}mL")
            elif blood_type == 'Blood(O-)':
                ominus = total_amount
                dashboard_button2_in_frame_2_4.config(text=f"Blood(O-): {ominus}mL")
            elif blood_type == 'Power Red':
                powerred = total_amount
                dashboard_button3_in_frame_2_1.config(text=f"Power Red: {powerred}mL")
            elif blood_type == 'Platelets':
                platelets = total_amount
                dashboard_button3_in_frame_2_2.config(text=f"Platelets: {platelets}mL")
            elif blood_type == 'AB Plasma':
                abplasma = total_amount
                dashboard_button3_in_frame_2_3.config(text=f"AB Plasma: {abplasma}mL")
        query = f"SELECT COUNT(*) FROM admin_table"
        cursor.execute(query)
        count = cursor.fetchone()[0] or 0
        dashboard_button3_in_frame_2_4.config(text=f"Total Donors: {count}")

    def on_dashboard_click():
        left_dashboard_button.config(state="disabled", relief="sunken", disabledforeground="white")
        left_schedule_button.config(state="normal", relief="raised")
        left_alldonor_button.config(state="normal", relief="raised")
        left_about_us_button.config(state="normal", relief="raised")
        left_help_button.config(state="normal", relief="raised")

        for widget in available_schedule_frame.winfo_children():
            widget.pack_forget()
        available_schedule_frame.forget()

        for widget in alldonor_frame.winfo_children():
            widget.pack_forget()
        alldonor_frame.forget()

        for widget in about_us_frame.winfo_children():
            widget.pack_forget()
        about_us_frame.forget()

        for widget in help_frame.winfo_children():
            widget.pack_forget()
        help_frame.forget()

        dashboard_frame.pack(fill="both", expand=True)
        dashboard_canvas.pack(fill="both", expand=True)
        for widget in dashboard_canvas.winfo_children():
            if widget == dashboard_in_frame2:
                widget.pack(fill="x", pady=(80, 0), padx=(160, 160))
            else:
                widget.pack(fill="x")

        for widget in dashboard_in_frame1.winfo_children():
            if widget == dashboard_label1:
                widget.pack(side="top", pady=(20, 0))
        for widget in dashboard_in_frame2.winfo_children():
            widget.pack(fill="y", side="left", expand=True)

        for widget in dashboard_in_frame2_1.winfo_children():
            widget.pack(padx=10, pady=10, expand=True)
        for widget in dashboard_in_frame2_2.winfo_children():
            widget.pack(padx=10, pady=10, expand=True)
        for widget in dashboard_in_frame2_3.winfo_children():
            widget.pack(padx=10, pady=10, expand=True)
        for widget in dashboard_in_frame2_4.winfo_children():
            widget.pack(padx=10, pady=10, expand=True)
        populate_dashboard()
    """end of dashboard button function====================================================================================="""

    """start of about us button function===================================================================================="""
    def on_about_us_click():
        left_about_us_button.config(state="disabled", relief="sunken", disabledforeground="white")
        left_alldonor_button.config(state="normal", relief="raised")
        left_schedule_button.config(state="normal", relief="raised")
        left_dashboard_button.config(state="normal", relief="raised")
        left_help_button.config(state="normal", relief="raised")

        for widget in available_schedule_frame.winfo_children():
            widget.pack_forget()
        available_schedule_frame.forget()

        for widget in dashboard_frame.winfo_children():
            widget.pack_forget()
        dashboard_frame.forget()

        for widget in alldonor_frame.winfo_children():
            widget.pack_forget()
        alldonor_frame.forget()

        for widget in help_frame.winfo_children():
            widget.pack_forget()
        help_frame.forget()

        about_us_frame.pack(fill="both", expand=True)
        about_us_canvas.pack(fill="both", expand=True)
        for widget in about_us_canvas.winfo_children():
            if widget == about_us_pandg_title or widget == about_us_dev_team_title or widget == about_us_key_features_title\
                    or widget == about_us_acknowledgements_title:
                widget.pack(anchor="n", pady=(40, 10))
            elif widget == about_us_contact:
                widget.pack(anchor="sw", pady=(220, 0))
            else:
                widget.pack(anchor="n")
        for widget in dev_team_frame.winfo_children():
            widget.pack(side="left", padx=(10, 10))
    """end of about us button function==============================================================================="""

    """start of help button function============================================================================="""
    def on_help_click():
        left_help_button.config(state="disabled", relief="sunken", disabledforeground="white")
        left_about_us_button.config(state="normal", relief="raised")
        left_alldonor_button.config(state="normal", relief="raised")
        left_schedule_button.config(state="normal", relief="raised")
        left_dashboard_button.config(state="normal", relief="raised")

        for widget in available_schedule_frame.winfo_children():
            widget.pack_forget()
        available_schedule_frame.forget()

        for widget in dashboard_frame.winfo_children():
            widget.pack_forget()
        dashboard_frame.forget()

        for widget in alldonor_frame.winfo_children():
            widget.pack_forget()
        alldonor_frame.forget()

        for widget in about_us_frame.winfo_children():
            widget.pack_forget()
        about_us_frame.forget()

        help_frame.pack(fill="both", expand=True)
        help_canvas.pack(fill="both", expand=True)
        for widget in help_canvas.winfo_children():
            if widget == nextbutton:
                widget.pack(anchor="se", padx=(0, 20), pady=(20, 0))
            else:
                widget.pack(anchor="n", pady=(10, 0))
                for widget2 in helplabelframe1.winfo_children():
                    widget2.pack(anchor="n", fill="x")
                for widget3 in helplabelframe2.winfo_children():
                    widget3.pack(anchor="n", fill="x")
                for widget4 in helplabelframe3.winfo_children():
                    widget4.pack(anchor="n", fill="x")
                for widget5 in helplabelframe4.winfo_children():
                    widget5.pack(anchor="n", fill="x")
                for widget6 in helplabelframe5.winfo_children():
                    widget6.pack(anchor="n", fill="x")

    """Where the buttons of manage schedule, alldonor, and summary are stored========================================"""
    left_frame = tk.Frame(window_frame, borderwidth=2, bg="black")
    left_frame.pack(side="left", fill="y")

    left_frame_frame = tk.Frame(left_frame, bg="#FF6E7E")
    left_frame_frame.pack(fill="both", expand=True)

    left_dashboard_button = tk.Button(left_frame_frame,
                                      text="Dashboard",
                                      font=("", 15, "bold"),
                                      width=20,
                                      bg="#D80032",
                                      fg="white",
                                      activebackground="#E66371",
                                      activeforeground="white",
                                      relief="sunken",
                                      state="disabled",
                                      disabledforeground="white",
                                      command=on_dashboard_click)
    left_dashboard_button.pack(anchor="n", pady=(10, 0), padx=(5, 5))

    left_alldonor_button = tk.Button(left_frame_frame,
                                     text="All Donors",
                                     font=("", 15, "bold"),
                                     width=20,
                                     bg="#D80032",
                                     fg="white",
                                     activebackground="#E66371",
                                     activeforeground="white",
                                     relief="raised",
                                     command=on_alldonor_click)
    left_alldonor_button.pack(anchor="n", pady=(10, 0), padx=(5, 5))

    left_schedule_button = tk.Button(left_frame_frame,
                                     text="Manage Schedule's",
                                     font=("", 15, "bold"),
                                     width=20,
                                     bg="#D80032",
                                     fg="white",
                                     activebackground="#E66371",
                                     activeforeground="white",
                                     relief="raised",
                                     command=on_schedule_click)
    left_schedule_button.pack(anchor="n", pady=(10, 0), padx=(5, 5))

    left_about_us_button = tk.Button(left_frame_frame,
                                     text="About us",
                                     font=("", 15, "bold"),
                                     width=20,
                                     bg="#D80032",
                                     fg="white",
                                     activebackground="#E66371",
                                     activeforeground="white",
                                     relief="raised",
                                     command=on_about_us_click)
    left_about_us_button.pack(anchor="n", pady=(10, 0), padx=(5, 5))

    left_help_button = tk.Button(left_frame_frame,
                                 text="Help",
                                 font=("", 15, "bold"),
                                 width=20,
                                 bg="#D80032",
                                 fg="white",
                                 activebackground="#E66371",
                                 activeforeground="white",
                                 relief="raised",
                                 command=on_help_click)
    left_help_button.pack(anchor="n", pady=(10, 0), padx=(5, 5))
    """end of left widgets==========================================================================================="""

    """Inside the frame of manage schedule when you click the manage schedule button================================="""
    class EntryFrame(Frame):
        def __init__(self, parent, entry_data, entry_height):
            super().__init__(master=parent)
            self.pack(expand=True, fill="both")

            # widget data
            self.entry_data = entry_data
            self.entry_number = len(entry_data)
            self.table_height = self.entry_number * entry_height

            # canvas
            self.canvas = Canvas(self, background='#FFFFFF', scrollregion=(0, 0, 700, self.table_height))
            self.canvas.pack(expand=True, fill='both')

            # display frame
            self.frame = Frame(self)

            for index, entry in enumerate(self.entry_data):
                self.create_entry(index, entry).pack(expand=True, fill='both')

            # scrollbar
            self.scrollbar = Scrollbar(table_frame, orient='vertical', command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

            # events
            self.canvas.bind_all('<MouseWheel>',
                                 lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
            self.bind('<Configure>', self.update_size)

        def update_size(self, event):
            if self.table_height >= self.winfo_height():
                height = self.table_height
                self.canvas.bind_all('<MouseWheel>',
                                     lambda event1: self.canvas.yview_scroll(-int(event1.delta / 60), "units"))
                self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
            else:
                height = self.table_height
                self.canvas.unbind_all('<MouseWheel>')
                self.scrollbar.place_forget()

            self.canvas.create_window((0, 0),
                                      window=self.frame,
                                      anchor='nw',
                                      width=700,
                                      height=height)

        def create_entry(self, index, entry):
            def retrieve_schedule():
                entry_list.clear()

                con = mysql.connector.connect(host="localhost", user="root", password="", database="bloodbank_db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM AvailableSchedule")
                rows = cursor.fetchall()

                for row in rows:
                    entry_tuple = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
                    entry_list.append(entry_tuple)

                con.close()
            def delete_entry():
                con = mysql.connector.connect(host="localhost", user="root", password="", database="bloodbank_db")
                cursor = con.cursor()
                cursor.execute("DELETE FROM AvailableSchedule WHERE AppointmentID = '" + entry_list[index][0] + "'")
                cursor.execute("COMMIT")

                entry_name[0].destroy()
                retrieve_schedule()
                entry_name[1] = EntryFrame(table_frame, entry_list, 49)
                temp = entry_name[0]
                entry_name[0] = entry_name[1]
                entry_name[1] = temp

                messagebox.showinfo("Delete Schedule", "Schedule deleted successfully")
                con.close()

            frame = Frame(self.frame, bg="#F9DEC9")

            # grid layout
            frame.rowconfigure(0, weight=1)
            for i in [0, 1, 2, 3]:
                frame.columnconfigure(i, weight=1, uniform='a')

            # widgets
            id_frame = Frame(frame, width=175, height=49)
            id_frame.grid(row=0, column=0)
            id_frame.pack_propagate(False)
            id_label = Label(id_frame, text=f'{entry[0]}', bg="#FFFFFF", fg="#1F1717", font=('Berlin Sans FB Demi', 14))
            id_label.pack(fill=BOTH, expand=True)

            city_frame = Frame(frame, width=175, height=49)
            city_frame.grid(row=0, column=1)
            city_frame.pack_propagate(False)
            city_label = Label(city_frame, text=f'{entry[1]}', bg="#FFFFFF", fg="#1F1717",
                               font=('Berlin Sans FB Demi', 14))
            city_label.pack(fill=BOTH, expand=True)

            date_frame = Frame(frame, width=175, height=49)
            date_frame.grid(row=0, column=2)
            date_frame.pack_propagate(False)
            date_label = Label(date_frame, text=f'{entry[2]}', bg="#FFFFFF", fg="#1F1717",
                               font=('Berlin Sans FB Demi', 14))
            date_label.pack(fill=BOTH, expand=True)

            action_frame = Frame(frame, width=175, height=49, bg="#FFFFFF")
            action_frame.grid(row=0, column=3)
            action_frame.pack_propagate(False)
            action_button = Button(action_frame, text="Delete", bg="#D80032", fg="#FFFFFF",
                                   font=('Berlin Sans FB Demi', 10), command=delete_entry)
            action_button.pack(pady=10)

            return frame

    def insert():
        def retrieve_schedule():
            entry_list.clear()

            con = mysql.connector.connect(host="localhost", user="root", password="", database="bloodbank_db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM AvailableSchedule")
            rows = cursor.fetchall()

            for row in rows:
                entry_tuple = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
                entry_list.append(entry_tuple)

            con.close()
        municipality = city.get()
        dt = date.get_date()
        str_dt = dt.strftime("%Y-%m-%d")
        var = 0

        for entry in entry_list:
            if (entry[1] == municipality and entry[2] == str_dt):
                var += 1

        if (municipality == ""):
            messagebox.showinfo("Add Schedule", "All fields are required")
        elif (var == 1):
            messagebox.showinfo("Add Schedule", "Schedule already exists")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="bloodbank_db")
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO AvailableSchedule (CityMunicipality, Date) VALUES ('" + municipality + "','" + str_dt + "')")
            cursor.execute("COMMIT")

            entry_name[0].destroy()
            retrieve_schedule()
            entry_name[1] = EntryFrame(table_frame, entry_list, 49)
            temp = entry_name[0]
            entry_name[0] = entry_name[1]
            entry_name[1] = temp

            messagebox.showinfo("Add Schedule", "Schedule added successfully")
            con.close()

    available_schedule_frame = tk.Frame(window_frame,
                                        borderwidth=2,
                                        bg="black")

    available_schedule_canvas = tk.Canvas(available_schedule_frame,
                                          bg="#F9DEC9")

    available_schedule_label = Label(available_schedule_canvas, text="Available Schedule",
                                     font=('Berlin Sans FB Demi', 22),
                                     bg="#F9DEC9", fg="#0F0F0F")
    available_schedule_label.pack(pady=10)

    frame_for_all1 = Frame(available_schedule_canvas, bg="#F9DEC9")
    frame_for_all1.pack(fill="x", anchor="n")
    frame_for_all2 = Frame(available_schedule_canvas, bg="#F9DEC9")
    frame_for_all2.pack(fill="x", expand=True, anchor="n")

    label_date = Label(frame_for_all1, text="Date", font=('Berlin Sans FB Demi', 22), fg="#0F0F0F", bg="#F9DEC9")
    label_date.pack(side="left", pady=(10, 0), padx=10)

    label_add_schedule = Label(frame_for_all1, text="Add Schedule", font=('Berlin Sans FB Demi', 22),
                               bg="#F9DEC9", fg="#0F0F0F")
    label_add_schedule.pack(side="right", pady=(10, 0), padx=(0, 110))

    frame_for_all3 = Frame(frame_for_all2, bg="#F9DEC9")
    frame_for_all3.pack(side="right", pady=(0, 180))

    label_search = Label(frame_for_all3, text="City/Municipality", font=('Berlin Sans FB', 20), fg="#0F0F0F",
                         bg="#F9DEC9")
    label_search.pack(pady=(10, 0), padx=(0, 10), anchor="w")

    city = StringVar()
    search_combobox = ttk.Combobox(frame_for_all3, width=20, textvariable=city, font=('Berlin Sans FB', 16))

    search_combobox['values'] = (
        'Batangas City',
        'Bauan',
        'Taal'
    )

    search_combobox.pack(pady=(10, 0), padx=(0, 10), anchor="e")

    button_results = Button(frame_for_all3, text="Add", padx=30, bg="#D80032", fg="#FFFFFF",
                            font=('Berlin Sans FB Demi', 18), command=insert)
    button_results.pack(pady=(10, 0), padx=(0, 10), anchor="w")

    date = DateEntry(frame_for_all2, selectmode='day')
    date.pack(side="left", pady=(0, 280), padx=(10, 150))

    table_frame = Frame(frame_for_all2, height=320, width=700, bg="#FFFFFF")
    table_frame.pack(side="left", padx=(10, 10))
    table_frame.pack_propagate(False)

    attribute_frame = Frame(table_frame, bg="#F9DEC9")
    attribute_frame.pack(fill="both")

    id_frame = Frame(attribute_frame, width=175, height=49)
    id_frame.grid(row=0, column=0)
    id_frame.pack_propagate(False)
    id_label = Label(id_frame, text="Appointment ID", bg="#1F1717", fg="#FFFFFF", font=('Berlin Sans FB Demi', 14))
    id_label.pack(fill=BOTH, expand=True)

    city_frame = Frame(attribute_frame, width=175, height=49)
    city_frame.grid(row=0, column=1)
    city_frame.pack_propagate(False)
    city_label = Label(city_frame, text="City/Municipality", bg="#1F1717", fg="#FFFFFF",
                       font=('Berlin Sans FB Demi', 14))
    city_label.pack(fill=BOTH, expand=True)

    date_frame = Frame(attribute_frame, width=175, height=49)
    date_frame.grid(row=0, column=2)
    date_frame.pack_propagate(False)
    date_label = Label(date_frame, text="Date", bg="#1F1717", fg="#FFFFFF", font=('Berlin Sans FB Demi', 14))
    date_label.pack(fill=BOTH, expand=True)

    action_frame = Frame(attribute_frame, width=175, height=49)
    action_frame.grid(row=0, column=4)
    action_frame.pack_propagate(False)
    action_label = Label(action_frame, text="Action", bg="#1F1717", fg="#FFFFFF", font=('Berlin Sans FB Demi', 14))
    action_label.pack(fill=BOTH, expand=True)

    def retrieve_schedule():
        entry_list.clear()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="bloodbank_db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM AvailableSchedule")
        rows = cursor.fetchall()

        for row in rows:
            entry_tuple = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
            entry_list.append(entry_tuple)

        con.close()

    entry_list = list()
    retrieve_schedule()
    entry_name = ["entry_frame_1", "entry_frame_2"]
    entry_name[0] = EntryFrame(table_frame, entry_list, 49)

    """end of manage schedule widgets================================================================================"""

    """Inside the alldonor frame when you click the alldonor button=================================================="""
    alldonor_frame = tk.Frame(window_frame, borderwidth=2, bg="black")
    alldonor_canvas = tk.Canvas(alldonor_frame, bg="#F9DEC9")
    """functions for sql when you click search and sort=============================================================="""

    def search_data():
        def destroywindow4():
            search.destroy()
        if alldonor_search_entry.get() and alldonor_search_entry_label.get():
            try:
                search_column_name = alldonor_search_entry_label.get()
                search_column_data = alldonor_search_entry.get()
                search_query = f"SELECT * FROM admin_table WHERE {search_column_name} = '{search_column_data}'"
                for item in tree.get_children():
                    tree.delete(item)
                treecon.execute(search_query)
                rows = treecon.fetchall()
                for row in rows:
                    tree.insert("", "end", values=row)
                connection.commit()
                alldonor_search_entry.delete(0, "end")

            except Exception:
                print("catched exception")
        else:
            search = tk.Toplevel()
            search.title("Search entries not filled!")
            search_width = 300
            search_height = 100
            searchscreen_width = search.winfo_screenwidth()
            searchscreen_height = search.winfo_screenheight()
            searchx = (searchscreen_width - search_width) // 2
            searchy = (searchscreen_height - search_height) // 2
            search.geometry(f"{search_width}x{search_height}+{searchx}+{searchy}")
            search_label = tk.Label(search, text="Please fill the search entries.")
            search_label.pack(expand=True)
            search_button = tk.Button(search, text="Ok", command=destroywindow4)
            search_button.pack(expand=True)
            search.mainloop()

    def sort_data():
        def destroywindow5():
            sort.destroy()

        sort_column_names = ["Donor_ID", "Donor_FN", "Donor_LN", "Donor_Age", "Medical_Conditions", "Donation_Type",
                             "Donation_Amount"]
        if alldonor_sort_entry.get() and alldonor_search_entry_label.get():
            try:
                search_column_name = alldonor_search_entry_label.get()
                search_column_data = alldonor_sort_entry.get()
                search_query = f"SELECT * FROM admin_table ORDER BY {search_column_name} {search_column_data}"
                for item in tree.get_children():
                    tree.delete(item)
                treecon.execute(search_query)
                rows = treecon.fetchall()
                for row in rows:
                    tree.insert("", "end", values=row)
                connection.commit()
                alldonor_sort_entry.delete(0, "end")

            except Exception:
                print("catched exception")
        else:
            sort = tk.Toplevel()
            sort.title("Sort entries not filled!")
            sort_width = 300
            sort_height = 100
            sortscreen_width = sort.winfo_screenwidth()
            sortscreen_height = sort.winfo_screenheight()
            sortx = (sortscreen_width - sort_width) // 2
            sorty = (sortscreen_height - sort_height) // 2
            sort.geometry(f"{sort_width}x{sort_height}+{sortx}+{sorty}")
            sort_label = tk.Label(sort, text="Please fill the sort entries.")
            sort_label.pack(expand=True)
            sort_button = tk.Button(sort, text="Ok", command=destroywindow5)
            sort_button.pack(expand=True)
            sort.mainloop()
    """end of functions for search and sort=========================================================================="""
    """The frame used to contain the search and sort button and entry================================================"""
    alldonor_searchandsort_frame = tk.Frame(alldonor_canvas, borderwidth=2, bg="#F9DEC9")

    alldonor_search_label = tk.Label(alldonor_searchandsort_frame,
                                     text="Input column to search or sort: ",
                                     font=("", 10, "bold"),
                                     bg="#F9DEC9")
    alldonor_search_entry_label = ttk.Combobox(alldonor_searchandsort_frame)
    alldonor_search_entry_label['values'] = ('Donor_ID', 'Donor_FN', 'Donor_LN', 'Donor_Age', 'Medical_Conditions', 'Donation_Type',
                                             'Donation_Amount')

    alldonor_search_entry = tk.Entry(alldonor_searchandsort_frame)
    alldonor_search_button = tk.Button(alldonor_searchandsort_frame,
                                       text="Search",
                                       font=("", 7, "bold"),
                                       bg="#D80032",
                                       fg="white",
                                       activebackground="#E66371",
                                       activeforeground="white",
                                       command=search_data)

    def on_entry_click(event):
        if alldonor_sort_entry.get() == default_text:
            alldonor_sort_entry.delete(0, "end")
            alldonor_sort_entry.config(fg='black')

    def on_entry_leave(event):
        if not alldonor_sort_entry.get():
            alldonor_sort_entry.insert(0, default_text)
            alldonor_sort_entry.config(fg='grey')

    default_text = "Input if ASC or DESC"
    alldonor_sort_entry = tk.Entry(alldonor_searchandsort_frame)
    alldonor_sort_entry.insert(0, default_text)
    alldonor_sort_entry.bind('<FocusIn>', on_entry_click)
    alldonor_sort_entry.bind('<FocusOut>', on_entry_leave)
    alldonor_sort_button = tk.Button(alldonor_searchandsort_frame,
                                     text="Sort",
                                     font=("", 7, "bold"),
                                     bg="#D80032",
                                     fg="white",
                                     activebackground="#E66371",
                                     activeforeground="white",
                                     command=sort_data)
    treecon = connection.cursor()

    def populate_tree():
        for item in tree.get_children():
            tree.delete(item)
        treecon.execute("SELECT * FROM admin_table")
        rows = treecon.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)

    alldonor_tree_refresh = tk.Button(alldonor_searchandsort_frame,
                                      text="Refresh Table",
                                      width=12,
                                      font=("", 10, "bold"),
                                      bg="#D80032",
                                      fg="white",
                                      activebackground="#E66371",
                                      activeforeground="white",
                                      command=populate_tree)
    """end of search and sort, button and entry======================================================================"""

    """the table widget where you see all the donors================================================================="""

    def on_treeview_select(event):
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item, 'values')
            if values:
                alldonor_donorid_update_entry_var.set(values[0])
                alldonor_donorid_delete_entry_var.set(values[0])

    alldonor_donorid_update_entry_var = tk.StringVar()
    alldonor_donorid_delete_entry_var = tk.StringVar()

    tree = ttk.Treeview(alldonor_canvas,
                        height=25,
                        columns=("Donor_ID",
                                 "Donor_FN",
                                 "Donor_LN",
                                 "Donor_Age",
                                 "Medical_Conditions",
                                 "Donation_Type",
                                 "Donation_Amount(mL)"),
                        show="headings")
    tree.heading("Donor_ID", text="Donor_ID")
    tree.heading("Donor_FN", text="Donor_FN")
    tree.heading("Donor_LN", text="Donor_LN")
    tree.heading("Donor_Age", text="Donor_Age")
    tree.heading("Medical_Conditions", text="Medical_Conditions")
    tree.heading("Donation_Type", text="Donation_Type")
    tree.heading("Donation_Amount(mL)", text="Donation_Amount(mL)")
    tree.column("Donor_ID", width=100)
    tree.column("Donor_FN", width=150)
    tree.column("Donor_LN", width=150)
    tree.column("Donor_Age", width=100)

    tree.insert("", "end", values=("Row 1", "Value 1", "Value 2", "Value 1", "Value 2", "Value 1", "Value 2"))
    tree.bind("<<TreeviewSelect>>", on_treeview_select)
    populate_tree()

    """this is the frame where the add donor, update donor and delete donor button are stored in====================="""
    alldonor_add_update_delete_button_frame = tk.Frame(alldonor_canvas, borderwidth=1, bg="#F9DEC9")
    """when you click add donor, update donor and delete donor it uses this frame to switch canvas==================="""
    alldonor_frame_of_each_button = tk.Frame(alldonor_canvas, borderwidth=1, bg="white")

    """add donor button functions===================================================================================="""

    def add_gui():
        alldonor_frame_of_each_button.config(bg="black")
        alldonor_add_donor_button.config(state="disabled", relief="sunken", disabledforeground="white")
        alldonor_update_donor_button.config(state="normal", relief="raised")
        alldonor_delete_donor_button.config(state="normal", relief="raised")
        for widget in alldonor_canvas_of_update_donor_button.winfo_children():
            widget.pack_forget()
        alldonor_canvas_of_update_donor_button.forget()

        for widget in alldonor_canvas_of_delete_donor_button.winfo_children():
            widget.pack_forget()
        alldonor_canvas_of_delete_donor_button.forget()

        alldonor_canvas_of_add_donor_button.pack(fill="both", expand=True)
        for widget in alldonor_canvas_of_add_donor_button.winfo_children():
            if (widget == alldonor_firstname_add or widget == alldonor_lastname_add or widget == alldonor_age_add or
                    widget == alldonor_medicalconditions_add or widget == alldonor_donationtype_add or widget == alldonor_donationamount_add):
                widget.pack(side="left", fill="y")
                for widget2 in alldonor_firstname_add.winfo_children():
                    widget2.pack(anchor="n", padx=(15, 10), pady=(0, 10))
                for widget2 in alldonor_lastname_add.winfo_children():
                    widget2.pack(anchor="n", padx=(15, 10), pady=(0, 10))
                for widget2 in alldonor_age_add.winfo_children():
                    widget2.pack(anchor="n", padx=(15, 10), pady=(0, 10))
                for widget2 in alldonor_medicalconditions_add.winfo_children():
                    widget2.pack(anchor="n", padx=(15, 10), pady=(0, 10))
                for widget2 in alldonor_donationtype_add.winfo_children():
                    widget2.pack(anchor="n", padx=(15, 10), pady=(0, 10))
                for widget2 in alldonor_donationamount_add.winfo_children():
                    widget2.pack(anchor="n", padx=(15, 10), pady=(0, 10))
            elif widget == alldonor_add_button:
                widget.pack(anchor="ne", padx=(0, 40), pady=(20, 0))
    """end of add donor button functions============================================================================="""

    alldonor_add_donor_button = tk.Button(alldonor_add_update_delete_button_frame,
                                          text="Add donor",
                                          width=12,
                                          font=("", 10, "bold"),
                                          bg="#D80032",
                                          fg="white",
                                          activebackground="#E66371",
                                          activeforeground="white",
                                          command=add_gui)

    """the canvas of each frame for each button you click(add donor, update donor and delete donor==================="""
    alldonor_canvas_of_add_donor_button = tk.Canvas(alldonor_frame_of_each_button, bg="#F9DEC9")

    """these are the frames that the labels and entries of add donor are inside of==================================="""
    alldonor_firstname_add = tk.Frame(alldonor_canvas_of_add_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_lastname_add = tk.Frame(alldonor_canvas_of_add_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_age_add = tk.Frame(alldonor_canvas_of_add_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_medicalconditions_add = tk.Frame(alldonor_canvas_of_add_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_donationtype_add = tk.Frame(alldonor_canvas_of_add_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_donationamount_add = tk.Frame(alldonor_canvas_of_add_donor_button, borderwidth=2, bg="#F9DEC9")
    """end of label and entries frames==============================================================================="""

    """labels and entries for add donor=============================================================================="""
    alldonor_firstname_add_label = tk.Label(alldonor_firstname_add, text="First Name", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_firstname_add_entry = tk.Entry(alldonor_firstname_add)

    alldonor_lastname_add_label = tk.Label(alldonor_lastname_add, text="Last Name", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_lastname_add_entry = tk.Entry(alldonor_lastname_add)

    alldonor_age_add_label = tk.Label(alldonor_age_add, text="Age", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_age_add_entry = tk.Entry(alldonor_age_add)

    alldonor_medicalconditions_add_label = tk.Label(alldonor_medicalconditions_add, text="Medical Conditions", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_medicalconditions_add_entry = tk.Entry(alldonor_medicalconditions_add)

    alldonor_donationtype_add_label = tk.Label(alldonor_donationtype_add, text="Donation Type", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_donationtype_add_entry = ttk.Combobox(alldonor_donationtype_add)
    alldonor_donationtype_add_entry['values'] = ('Blood(A+)', 'Blood(B+)', 'Blood(AB+)', 'Blood(O+)',
                                                 'Blood(A-)', 'Blood(B-)', 'Blood(AB-)', 'Blood(O-)',
                                                 'Power Red', 'Platelets', 'AB Plasma')

    alldonor_donationamount_add_label = tk.Label(alldonor_donationamount_add, text="Donation Amount", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_donationamount_add_entry = tk.Entry(alldonor_donationamount_add)

    def add_data():
        def destroywindow1():
            added.destroy()
            populate_tree()
        if (alldonor_firstname_add_entry.get() and
                alldonor_lastname_add_entry.get() and
                alldonor_age_add_entry.get() and
                alldonor_medicalconditions_add_entry.get() and
                alldonor_donationtype_add_entry.get() and
                alldonor_donationamount_add_entry.get()):
            try:
                add_cursor = connection.cursor()
                add_query = "INSERT INTO admin_table (Donor_FN, Donor_LN, Donor_Age, Medical_Conditions, Donation_Type, Donation_Amount) VALUES (%s, %s, %s, %s, %s, %s)"
                data_to_add = (alldonor_firstname_add_entry.get(),
                               alldonor_lastname_add_entry.get(),
                               alldonor_age_add_entry.get(),
                               alldonor_medicalconditions_add_entry.get(),
                               alldonor_donationtype_add_entry.get(),
                               alldonor_donationamount_add_entry.get())
                add_cursor.execute(add_query, data_to_add)
                connection.commit()

                alldonor_firstname_add_entry.delete(0, "end")
                alldonor_lastname_add_entry.delete(0, "end")
                alldonor_age_add_entry.delete(0, "end")
                alldonor_medicalconditions_add_entry.delete(0, "end")
                alldonor_donationtype_add_entry.delete(0, "end")
                alldonor_donationamount_add_entry.delete(0, "end")

                added = tk.Toplevel()
                added.title("Successful!")
                added_width = 300
                added_height = 100
                addedscreen_width = added.winfo_screenwidth()
                addedscreen_height = added.winfo_screenheight()
                addx = (addedscreen_width - added_width) // 2
                addy = (addedscreen_height - added_height) // 2
                added.geometry(f"{added_width}x{added_height}+{addx}+{addy}")
                added_label = tk.Label(added, text="Donor successfully added!")
                added_label.pack(expand=True)
                added_button = tk.Button(added, text="Ok", command=destroywindow1)
                added_button.pack(expand=True)
                added.mainloop()
            except Exception:
                print("catched exception")
                age = int(alldonor_age_add_entry.get())
                donationamount = int(alldonor_donationamount_add_entry.get())
                if age < 18 or age > 65:
                    added = tk.Toplevel()
                    added.title("Error!")
                    added_width = 300
                    added_height = 100
                    addedscreen_width = added.winfo_screenwidth()
                    addedscreen_height = added.winfo_screenheight()
                    addx = (addedscreen_width - added_width) // 2
                    addy = (addedscreen_height - added_height) // 2
                    added.geometry(f"{added_width}x{added_height}+{addx}+{addy}")
                    added_label = tk.Label(added, text="Age should be between 18-65 only.")
                    added_label.pack(expand=True)
                    added_button = tk.Button(added, text="Ok", command=destroywindow1)
                    added_button.pack(expand=True)
                    added.mainloop()
                elif donationamount < 100 or donationamount > 450:
                    added = tk.Toplevel()
                    added.title("Error!")
                    added_width = 300
                    added_height = 100
                    addedscreen_width = added.winfo_screenwidth()
                    addedscreen_height = added.winfo_screenheight()
                    addx = (addedscreen_width - added_width) // 2
                    addy = (addedscreen_height - added_height) // 2
                    added.geometry(f"{added_width}x{added_height}+{addx}+{addy}")
                    added_label = tk.Label(added, text="Donation amount must be between 100mL and 450mL.")
                    added_label.pack(expand=True)
                    added_button = tk.Button(added, text="Ok", command=destroywindow1)
                    added_button.pack(expand=True)
                    added.mainloop()
        else:
            added = tk.Toplevel()
            added.title("Error")
            added_width = 300
            added_height = 100
            addedscreen_width = added.winfo_screenwidth()
            addedscreen_height = added.winfo_screenheight()
            addx = (addedscreen_width - added_width) // 2
            addy = (addedscreen_height - added_height) // 2
            added.geometry(f"{added_width}x{added_height}+{addx}+{addy}")
            added_label = tk.Label(added, text="Some field/s were not filled")
            added_label.pack(expand=True)
            added_button = tk.Button(added, text="Ok", command=destroywindow1)
            added_button.pack(expand=True)
            added.mainloop()

    alldonor_add_button = tk.Button(alldonor_canvas_of_add_donor_button,
                                    text="Add",
                                    width=12,
                                    font=("", 10, "bold"),
                                    bg="#D80032",
                                    fg="white",
                                    activebackground="#E66371",
                                    activeforeground="white",
                                    command=add_data)
    """end of add donor functions===================================================================================="""

    """update donor button functions================================================================================="""
    def update_gui():
        alldonor_canvas_of_add_donor_button.forget()
        alldonor_canvas_of_delete_donor_button.forget()
        alldonor_frame_of_each_button.config(bg="black")
        alldonor_canvas_of_update_donor_button.pack(fill="both", expand=True)
        alldonor_update_donor_button.config(state="disabled", relief="sunken", disabledforeground="white")
        alldonor_add_donor_button.config(state="normal", relief="raised")
        alldonor_delete_donor_button.config(state="normal", relief="raised")

        for widget in alldonor_canvas_of_update_donor_button.winfo_children():
            if (widget == alldonor_donorid_update or widget == alldonor_firstname_update or widget == alldonor_lastname_update or widget == alldonor_age_update or
                    widget == alldonor_medicalconditions_update or widget == alldonor_donationtype_update or widget == alldonor_donationamount_update):
                widget.pack(side="left", fill="y", expand=True)
                for widget2 in alldonor_donorid_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
                for widget2 in alldonor_firstname_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
                for widget2 in alldonor_lastname_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
                for widget2 in alldonor_age_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
                for widget2 in alldonor_medicalconditions_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
                for widget2 in alldonor_donationtype_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
                for widget2 in alldonor_donationamount_update.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
            elif widget == alldonor_update_button:
                widget.pack(anchor="ne", padx=(0, 30), pady=(20, 0))
    """end of update donor button functions=========================================================================="""

    alldonor_update_donor_button = tk.Button(alldonor_add_update_delete_button_frame,
                                             text="Update donor",
                                             width=12,
                                             font=("", 10, "bold"),
                                             bg="#D80032",
                                             fg="white",
                                             activebackground="#E66371",
                                             activeforeground="white",
                                             command=update_gui)
    """the canvas of each frame for each button you click(add donor, update donor and delete donor==================="""

    alldonor_canvas_of_update_donor_button = tk.Canvas(alldonor_frame_of_each_button, bg="#F9DEC9")

    alldonor_donorid_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_firstname_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_lastname_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_age_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_medicalconditions_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_donationtype_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")
    alldonor_donationamount_update = tk.Frame(alldonor_canvas_of_update_donor_button, borderwidth=2, bg="#F9DEC9")

    alldonor_donorid_update_label = tk.Label(alldonor_donorid_update, text="Donor ID", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_donorid_update_entry = tk.Entry(alldonor_donorid_update, textvariable=alldonor_donorid_update_entry_var)

    alldonor_firstname_update_label = tk.Label(alldonor_firstname_update, text="First Name", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_firstname_update_entry = tk.Entry(alldonor_firstname_update)

    alldonor_lastname_update_label = tk.Label(alldonor_lastname_update, text="Last Name", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_lastname_update_entry = tk.Entry(alldonor_lastname_update)

    alldonor_age_update_label = tk.Label(alldonor_age_update, text="Age", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_age_update_entry = tk.Entry(alldonor_age_update)

    alldonor_medicalconditions_update_label = tk.Label(alldonor_medicalconditions_update, text="Medical Conditions",
                                                       font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_medicalconditions_update_entry = tk.Entry(alldonor_medicalconditions_update)

    alldonor_donationtype_update_label = tk.Label(alldonor_donationtype_update, text="Donation Type",
                                                  font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_donationtype_update_entry = ttk.Combobox(alldonor_donationtype_update)
    alldonor_donationtype_update_entry['values'] = ('Blood(A+)', 'Blood(B+)', 'Blood(AB+)', 'Blood(O+)',
                                                    'Blood(A-)', 'Blood(B-)', 'Blood(AB-)', 'Blood(O-)',
                                                    'Power Red', 'Platelets', 'AB Plasma')

    alldonor_donationamount_update_label = tk.Label(alldonor_donationamount_update, text="Donation Amount",
                                                    font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_donationamount_update_entry = tk.Entry(alldonor_donationamount_update)

    def update_data():
        def destroywindow2():
            update.destroy()
            populate_tree()
        if alldonor_donorid_update_entry.get():
            if (alldonor_firstname_update_entry.get() or
                    alldonor_lastname_update_entry.get() or
                    alldonor_age_update_entry.get() or
                    alldonor_medicalconditions_update_entry.get() or
                    alldonor_donationtype_update_entry.get() or
                    alldonor_donationamount_update_entry.get()):
                try:
                    iddata = alldonor_donorid_update_entry.get()
                    column_names = ["Donor_FN", "Donor_LN", "Donor_Age", "Medical_Conditions", "Donation_Type", "Donation_Amount"]
                    data_to_get = (alldonor_firstname_update_entry,
                                   alldonor_lastname_update_entry,
                                   alldonor_age_update_entry,
                                   alldonor_medicalconditions_update_entry,
                                   alldonor_donationtype_update_entry,
                                   alldonor_donationamount_update_entry)
                    for item in data_to_get:
                        update_cursor = connection.cursor()
                        if item == alldonor_firstname_update_entry:
                            if item.get() != "":
                                column_name = column_names[0]
                                data = item.get()
                                update_query = f"UPDATE admin_table SET {column_name} = '{data}' WHERE Donor_ID = {iddata}"
                                update_cursor.execute(update_query)
                        elif item == alldonor_lastname_update_entry:
                            if item.get() != "":
                                column_name = column_names[1]
                                data = item.get()
                                update_query = f"UPDATE admin_table SET {column_name} = '{data}' WHERE Donor_ID = {iddata}"
                                update_cursor.execute(update_query)
                        elif item == alldonor_age_update_entry:
                            if item.get() != "" and (int(item.get()) > 18 or int(item.get()) < 65):
                                column_name = column_names[2]
                                data = int(item.get())
                                try:
                                    update_query = f"UPDATE admin_table SET {column_name} = '{data}' WHERE Donor_ID = {iddata}"
                                    update_cursor.execute(update_query)
                                except Exception:
                                    age = int(alldonor_age_update_entry.get())
                                    if age < 18 or age > 65:
                                        update = tk.Toplevel()
                                        update.title("Error!")
                                        update_width = 300
                                        update_height = 100
                                        update_screen_width = update.winfo_screenwidth()
                                        update_screen_height = update.winfo_screenheight()
                                        updatex = (update_screen_width - update_width) // 2
                                        updatey = (update_screen_height - update_height) // 2
                                        update.geometry(f"{update_width}x{update_height}+{updatex}+{updatey}")
                                        update_label = tk.Label(update, text="Age should be between 18-65 only.")
                                        update_label.pack(expand=True)
                                        update_button = tk.Button(update, text="Ok", command=destroywindow2)
                                        update_button.pack(expand=True)
                                        update.mainloop()
                        elif item == alldonor_medicalconditions_update_entry:
                            if item.get() != "":
                                column_name = column_names[3]
                                data = item.get()
                                update_query = f"UPDATE admin_table SET {column_name} = '{data}' WHERE Donor_ID = {iddata}"
                                update_cursor.execute(update_query)
                        elif item == alldonor_donationtype_update_entry:
                            if item.get() != "":
                                column_name = column_names[4]
                                data = item.get()
                                update_query = f"UPDATE admin_table SET {column_name} = '{data}' WHERE Donor_ID = {iddata}"
                                update_cursor.execute(update_query)
                        elif item == alldonor_donationamount_update_entry:
                            if item.get() != "" and (int(item.get()) > 350 or int(item.get()) < 450):
                                column_name = column_names[5]
                                data = int(item.get())
                                try:
                                    update_query = f"UPDATE admin_table SET {column_name} = '{data}' WHERE Donor_ID = {iddata}"
                                    update_cursor.execute(update_query)
                                except Exception:
                                    donationamount = int(alldonor_donationamount_update_entry.get())
                                    if donationamount < 100 or donationamount > 450:
                                        update = tk.Toplevel()
                                        update.title("Error!")
                                        update_width = 300
                                        update_height = 100
                                        update_screen_width = update.winfo_screenwidth()
                                        update_screen_height = update.winfo_screenheight()
                                        updatex = (update_screen_width - update_width) // 2
                                        updatey = (update_screen_height - update_height) // 2
                                        update.geometry(f"{update_width}x{update_height}+{updatex}+{updatey}")
                                        update_label = tk.Label(update, text="Donation amount must be between 100mL and 450mL.")
                                        update_label.pack(expand=True)
                                        update_button = tk.Button(update, text="Ok", command=destroywindow2)
                                        update_button.pack(expand=True)
                                        update.mainloop()
                        connection.commit()

                    alldonor_donorid_update_entry.delete(0, "end")
                    alldonor_firstname_update_entry.delete(0, "end")
                    alldonor_lastname_update_entry.delete(0, "end")
                    alldonor_age_update_entry.delete(0, "end")
                    alldonor_medicalconditions_update_entry.delete(0, "end")
                    alldonor_donationtype_update_entry.delete(0, "end")
                    alldonor_donationamount_update_entry.delete(0, "end")

                    update = tk.Toplevel()
                    update.title("Successful!")
                    update_width = 300
                    update_height = 100
                    updatescreen_width = update.winfo_screenwidth()
                    updatescreen_height = update.winfo_screenheight()
                    updatex = (updatescreen_width - update_width) // 2
                    updatey = (updatescreen_height - update_height) // 2
                    update.geometry(f"{update_width}x{update_height}+{updatex}+{updatey}")
                    update_label = tk.Label(update, text="Donor successfully updated!")
                    update_label.pack(expand=True)
                    update_button = tk.Button(update, text="Ok", command=destroywindow2)
                    update_button.pack(expand=True)
                    update.mainloop()
                except Exception:
                    print("catched exception")
            else:
                update = tk.Toplevel()
                update.title("Error!")
                update_width = 300
                update_height = 100
                updatescreen_width = update.winfo_screenwidth()
                updatescreen_height = update.winfo_screenheight()
                updatex = (updatescreen_width - update_width) // 2
                updatey = (updatescreen_height - update_height) // 2
                update.geometry(f"{update_width}x{update_height}+{updatex}+{updatey}")
                update_label = tk.Label(update, text="Column to update not filled!")
                update_label.pack(expand=True)
                update_button = tk.Button(update, text="Ok", command=destroywindow2)
                update_button.pack(expand=True)
                update.mainloop()
        else:
            update = tk.Toplevel()
            update.title("Donor id not filled")
            update_width = 300
            update_height = 100
            updatescreen_width = update.winfo_screenwidth()
            updatescreen_height = update.winfo_screenheight()
            updatex = (updatescreen_width - update_width) // 2
            updatey = (updatescreen_height - update_height) // 2
            update.geometry(f"{update_width}x{update_height}+{updatex}+{updatey}")
            update_label = tk.Label(update, text="Please input the Donor ID.")
            update_label.pack(expand=True)
            update_button = tk.Button(update, text="Ok", command=destroywindow2)
            update_button.pack(expand=True)
            update.mainloop()

    alldonor_update_button = tk.Button(alldonor_canvas_of_update_donor_button,
                                       text="Update",
                                       width=12,
                                       font=("", 10, "bold"),
                                       bg="#D80032",
                                       fg="white",
                                       activebackground="#E66371",
                                       activeforeground="white",
                                       command=update_data)
    """end of update donor functions================================================================================="""

    """delete donor button functions================================================================================="""
    def delete_gui():
        alldonor_canvas_of_add_donor_button.forget()
        alldonor_canvas_of_update_donor_button.forget()
        alldonor_frame_of_each_button.config(bg="black")
        alldonor_canvas_of_delete_donor_button.pack(fill="both", expand=True)
        alldonor_delete_donor_button.config(state="disabled", relief="sunken", disabledforeground="white")
        alldonor_add_donor_button.config(state="normal", relief="raised")
        alldonor_update_donor_button.config(state="normal", relief="raised")

        for widget in alldonor_canvas_of_delete_donor_button.winfo_children():
            if widget == alldonor_donorid_delete:
                widget.pack(side="left", fill="y", expand=True)
                for widget2 in alldonor_donorid_delete.winfo_children():
                    widget2.pack(anchor="n", padx=(5, 5), pady=(0, 10))
            elif widget == alldonor_delete_button:
                widget.pack(anchor="ne", padx=(0, 30), pady=(20, 0))

    alldonor_delete_donor_button = tk.Button(alldonor_add_update_delete_button_frame,
                                             text="Delete donor",
                                             width=12,
                                             font=("", 10, "bold"),
                                             bg="#D80032",
                                             fg="white",
                                             activebackground="#E66371",
                                             activeforeground="white",
                                             command=delete_gui)

    alldonor_canvas_of_delete_donor_button = tk.Canvas(alldonor_frame_of_each_button, bg="#F9DEC9")

    alldonor_donorid_delete = tk.Frame(alldonor_canvas_of_delete_donor_button, borderwidth=2, bg="#F9DEC9")

    alldonor_donorid_delete_label = tk.Label(alldonor_donorid_delete, text="Donor ID", font=("", 10, "bold"), bg="#F9DEC9")
    alldonor_donorid_delete_entry = tk.Entry(alldonor_donorid_delete, textvariable=alldonor_donorid_delete_entry_var)

    def delete_data():
        def destroywindow3():
            delete.destroy()
            populate_tree()

        if alldonor_donorid_delete_entry.get():
            try:
                iddata = alldonor_donorid_delete_entry.get()
                delete_cursor = connection.cursor()
                delete_query = f"DELETE FROM admin_table WHERE Donor_ID = {iddata}"
                delete_cursor.execute(delete_query)
                connection.commit()

                alldonor_donorid_delete_entry.delete(0, "end")

                delete = tk.Toplevel()
                delete.title("Success!")
                delete_width = 300
                delete_height = 100
                deletescreen_width = delete.winfo_screenwidth()
                deletescreen_height = delete.winfo_screenheight()
                deletex = (deletescreen_width - delete_width) // 2
                deletey = (deletescreen_height - delete_height) // 2
                delete.geometry(f"{delete_width}x{delete_height}+{deletex}+{deletey}")
                delete_label = tk.Label(delete, text="Donor successfully deleted!")
                delete_label.pack(expand=True)
                delete_button = tk.Button(delete, text="Ok", command=destroywindow3)
                delete_button.pack(expand=True)
                delete.mainloop()
            except Exception as e:
                print(e)
        else:
            delete = tk.Toplevel()
            delete.title("Donor id not filled")
            delete_width = 300
            delete_height = 100
            deletescreen_width = delete.winfo_screenwidth()
            deletescreen_height = delete.winfo_screenheight()
            deletex = (deletescreen_width - delete_width) // 2
            deletey = (deletescreen_height - delete_height) // 2
            delete.geometry(f"{delete_width}x{delete_height}+{deletex}+{deletey}")
            delete_label = tk.Label(delete, text="Please input the Donor ID.")
            delete_label.pack(expand=True)
            delete_button = tk.Button(delete, text="Ok", command=destroywindow3)
            delete_button.pack(expand=True)
            delete.mainloop()

    alldonor_delete_button = tk.Button(alldonor_canvas_of_delete_donor_button,
                                       text="Delete",
                                       width=12,
                                       font=("", 10, "bold"),
                                       bg="#D80032",
                                       fg="white",
                                       activebackground="#E66371",
                                       activeforeground="white",
                                       command=delete_data)

    """end of all donor widgets======================================================================================"""
    # dashboard widgets
    image_path = "C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\blood__1_-removebg-preview.png"
    image = PhotoImage(file=image_path)
    image = image.subsample(4)
    image_path2 = "C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\platelets.png"
    image2 = PhotoImage(file=image_path2)
    image2 = image2.subsample(5)
    image_path3 = "C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\plasma.png"
    image3 = PhotoImage(file=image_path3)
    image3 = image3.subsample(5)
    image_path4 = "C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\donors.png"
    image4 = PhotoImage(file=image_path4)
    image4 = image4.subsample(5)

    def dashboardbuttons(button):
        button_value = button.cget("text")
        button_value = button_value.split(":")[0]
        print(button_value)

        def populate_tree1():
            for item in tree1.get_children():
                tree1.delete(item)
            if button_value == "Total Donors":
                treecon.execute((f"SELECT * FROM admin_table"))
                rows = treecon.fetchall()
                for row in rows:
                    tree1.insert("", "end", values=row)
            else:
                treecon.execute(f"SELECT * FROM admin_table WHERE Donation_Type = '{button_value}'")
                rows = treecon.fetchall()
                for row in rows:
                    tree1.insert("", "end", values=row)

        window1 = tk.Toplevel()
        if button_value == "Total Donors":
            window1.title(f"{button_value}")
        else:
            window1.title(f"Blood donation type: {button_value}")
        window1_width = 1100
        window1_height = 390
        screen_width1 = window1.winfo_screenwidth()
        screen_height1 = window1.winfo_screenheight()
        x1 = (screen_width1 - window1_width) // 2
        y1 = (screen_height1 - window1_height) // 2
        window1.geometry(f"{window1_width}x{window1_height}+{x1}+{y1}")
        dashboard_canvas1 = tk.Canvas(window1, bg="#F9DEC9")
        dashboard_canvas1.pack(fill="both", expand=True)
        tree1 = ttk.Treeview(dashboard_canvas1,
                             height=25,
                             columns=("Donor_ID",
                                      "Donor_FN",
                                      "Donor_LN",
                                      "Donor_Age",
                                      "Medical_Conditions",
                                      "Donation_Type",
                                      "Donation_Amount(mL)"),
                             show="headings")
        tree1.heading("Donor_ID", text="Donor_ID")
        tree1.heading("Donor_FN", text="Donor_FN")
        tree1.heading("Donor_LN", text="Donor_LN")
        tree1.heading("Donor_Age", text="Donor_Age")
        tree1.heading("Medical_Conditions", text="Medical_Conditions")
        tree1.heading("Donation_Type", text="Donation_Type")
        tree1.heading("Donation_Amount(mL)", text="Donation_Amount(mL)")
        tree1.column("Donor_ID", width=100)
        tree1.column("Donor_FN", width=150)
        tree1.column("Donor_LN", width=150)
        tree1.column("Donor_Age", width=100)

        tree1.insert("", "end", values=("Row 1", "Value 1", "Value 2", "Value 1", "Value 2", "Value 1", "Value 2"))
        tree1.pack()
        populate_tree1()
        window1.mainloop()

    dashboard_frame = tk.Frame(window_frame, borderwidth=2, bg="black")
    dashboard_frame.pack(fill="both", expand=True)

    dashboard_canvas = tk.Canvas(dashboard_frame, bg="#F9DEC9")
    dashboard_canvas.pack(fill="both", expand=True)

    dashboard_in_frame1 = tk.Frame(dashboard_canvas, bg="#F9DEC9")
    dashboard_in_frame1.pack(fill="x")
    dashboard_label1 = tk.Label(dashboard_in_frame1, text="Blood Storage Dashboard", font=("", 20, "bold"), bg="#F9DEC9")
    dashboard_label1.pack(side="top", pady=(20, 0))

    dashboard_in_frame2 = tk.Frame(dashboard_canvas, bg="#F9DEC9")
    dashboard_in_frame2.pack(fill="x", pady=(80, 0), padx=(160, 160))
    dashboard_in_frame2_1 = tk.Frame(dashboard_in_frame2, bg="#F9DEC9")
    dashboard_in_frame2_1.pack(fill="y", side="left", expand=True)
    dashboard_button_in_frame_2_1 = tk.Button(dashboard_in_frame2_1, text=f"Blood(A+): ", width=213, height=125,
                                              font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                              compound="top", activebackground="#E66371", activeforeground="white",
                                              command=lambda: dashboardbuttons(dashboard_button_in_frame_2_1))
    dashboard_button_in_frame_2_1.pack(padx=10, pady=10, expand=True)
    dashboard_button2_in_frame_2_1 = tk.Button(dashboard_in_frame2_1, text=f"Blood(A-): ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button2_in_frame_2_1))
    dashboard_button2_in_frame_2_1.pack(padx=10, pady=10, expand=True)
    dashboard_button3_in_frame_2_1 = tk.Button(dashboard_in_frame2_1, text=f"Power Red: ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button3_in_frame_2_1))
    dashboard_button3_in_frame_2_1.pack(padx=10, pady=10, expand=True)

    dashboard_in_frame2_2 = tk.Frame(dashboard_in_frame2, bg="#F9DEC9")
    dashboard_in_frame2_2.pack(fill="y", side="left", expand=True)
    dashboard_button_in_frame_2_2 = tk.Button(dashboard_in_frame2_2, text=f"Blood(B+): ", width=213, height=125,
                                              font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                              compound="top", activebackground="#E66371", activeforeground="white",
                                              command=lambda: dashboardbuttons(dashboard_button_in_frame_2_2))
    dashboard_button_in_frame_2_2.pack(padx=10, pady=10, expand=True)
    dashboard_button2_in_frame_2_2 = tk.Button(dashboard_in_frame2_2, text=f"Blood(B-): ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button2_in_frame_2_2))
    dashboard_button2_in_frame_2_2.pack(padx=10, pady=10, expand=True)
    dashboard_button3_in_frame_2_2 = tk.Button(dashboard_in_frame2_2, text=f"Platelets: ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image2,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button3_in_frame_2_2))
    dashboard_button3_in_frame_2_2.pack(padx=10, pady=10, expand=True)

    dashboard_in_frame2_3 = tk.Frame(dashboard_in_frame2, bg="#F9DEC9")
    dashboard_in_frame2_3.pack(fill="y", side="left", expand=True)
    dashboard_button_in_frame_2_3 = tk.Button(dashboard_in_frame2_3, text=f"Blood(O+): ", width=213, height=125,
                                              font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                              compound="top", activebackground="#E66371", activeforeground="white",
                                              command=lambda: dashboardbuttons(dashboard_button_in_frame_2_3))
    dashboard_button_in_frame_2_3.pack(padx=10, pady=10, expand=True)
    dashboard_button2_in_frame_2_3 = tk.Button(dashboard_in_frame2_3, text=f"Blood(O-): ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button2_in_frame_2_3))
    dashboard_button2_in_frame_2_3.pack(padx=10, pady=10, expand=True)
    dashboard_button3_in_frame_2_3 = tk.Button(dashboard_in_frame2_3, text=f"AB Plasma: ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image3,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button3_in_frame_2_3))
    dashboard_button3_in_frame_2_3.pack(padx=10, pady=10, expand=True)

    dashboard_in_frame2_4 = tk.Frame(dashboard_in_frame2, bg="#F9DEC9")
    dashboard_in_frame2_4.pack(fill="y", side="left", expand=True)
    dashboard_button_in_frame_2_4 = tk.Button(dashboard_in_frame2_4, text=f"Blood(AB+): ", width=213, height=125,
                                              font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                              compound="top", activebackground="#E66371", activeforeground="white",
                                              command=lambda: dashboardbuttons(dashboard_button_in_frame_2_4))
    dashboard_button_in_frame_2_4.pack(padx=10, pady=10, expand=True)
    dashboard_button2_in_frame_2_4 = tk.Button(dashboard_in_frame2_4, text=f"Blood(AB-): ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button2_in_frame_2_4))
    dashboard_button2_in_frame_2_4.pack(padx=10, pady=10, expand=True)
    dashboard_button3_in_frame_2_4 = tk.Button(dashboard_in_frame2_4, text=f"Total Donors: ", width=213, height=125,
                                               font=("", 10, "bold"), bg="#ffbaba", fg="black", image=image4,
                                               compound="top", activebackground="#E66371", activeforeground="white",
                                               command=lambda: dashboardbuttons(dashboard_button3_in_frame_2_4))
    dashboard_button3_in_frame_2_4.pack(padx=10, pady=10, expand=True)
    populate_dashboard()
    """end of dashboard widgets======================================================================================"""
    """start of about us widgets====================================================================================="""
    about_us_frame = tk.Frame(window_frame, borderwidth=2, bg="black")
    about_us_canvas = tk.Canvas(about_us_frame, bg="#F9DEC9")

    about_us_pandg_title = tk.Label(about_us_canvas, text="Purpose and Goal", font=("", 30, "bold"), bg="#F9DEC9")
    about_us_pandg = tk.Label(about_us_canvas, text="Its purpose is to streamline and organize the process of scheduling and managing blood donation appointments. This system is designed to\nefficiently handle the logistics related to blood donation, ensuring a steady and reliable supply of blood for medical treatments.",
                              bg="#F9DEC9", font=("", 10))

    about_us_dev_team_title = tk.Label(about_us_canvas, text="Development Team", font=("", 30, "bold"), bg="#F9DEC9")
    dev_team_frame = tk.Frame(about_us_canvas)
    def contributionings(button):
        button_value = button.cget("text")
        if button_value == "Mark Justin Aguila":
            contribution = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\contribution1.png")
        elif button_value == "Jhun Harvey Cueto":
            contribution = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\contribution2.png")
        elif button_value == "Sean Angelo Gumba":
            contribution = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\contribution3.png")
        elif button_value == "Aron Joshua Holgado":
            contribution = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\contribution4.png")

        def contributions():
            delete = tk.Toplevel()
            delete.title("Contributions")
            delete_width = 800
            delete_height = 300
            deletescreen_width = delete.winfo_screenwidth()
            deletescreen_height = delete.winfo_screenheight()
            deletex = (deletescreen_width - delete_width) // 2
            deletey = (deletescreen_height - delete_height) // 2
            delete.geometry(f"{delete_width}x{delete_height}+{deletex}+{deletey}")
            delete_label = tk.Label(delete, image=contribution)
            delete_label.pack(expand=True)
            delete.mainloop()
        contributions()
    dev_team1 = tk.Button(dev_team_frame, text="Mark Justin Aguila", bg="#D80032", fg="black",
                          activebackground="#E66371", activeforeground="white", font=("", 10), width=15,
                          command=lambda: contributionings(dev_team1))
    dev_team2 = tk.Button(dev_team_frame, text="Jhun Harvey Cueto", bg="#D80032", fg="black",
                          activebackground="#E66371", activeforeground="white", font=("", 10), width=15,
                          command=lambda: contributionings(dev_team2))
    dev_team3 = tk.Button(dev_team_frame, text="Sean Angelo Gumba", bg="#D80032", fg="black",
                          activebackground="#E66371", activeforeground="white", font=("", 10), width=15,
                          command=lambda: contributionings(dev_team3))
    dev_team4 = tk.Button(dev_team_frame, text="Aron Joshua Holgado", bg="#D80032", fg="black",
                          activebackground="#E66371", activeforeground="white", font=("", 10), width=15,
                          command=lambda: contributionings(dev_team4))

    about_us_key_features_title = tk.Label(about_us_canvas, text="Key Features", font=("", 30, "bold"), bg="#F9DEC9")
    about_us_key_features = tk.Label(about_us_canvas, text="The key features of this system include, User Authentication and Authorization | Donor Management: add, edit, delete, search and sort donor records | Inventory Management: Monitor and manage the blood \n"
                                                           "inventory levels, Automatic updates of inventory after each donation or withdrawal. | Blood Donation Scheduling: The admin can add the available dates to donate blood and the donor can choose \n"
                                                           "among the available dates the admin has added | User-Friendly Interface.",
                                     bg="#F9DEC9", font=("", 10))

    about_us_acknowledgements_title = tk.Label(about_us_canvas, text="Acknowledgement", font=("", 30, "bold"),
                                               bg="#F9DEC9")
    about_us_acknowledgements = tk.Label(about_us_canvas, text="Teachers: Thank you for your guidance, support, and invaluable feedback throughout the project. Your expertise has been instrumental in shaping our work.\n"
                                                               "Group members: A special thanks to our dedicated team members who collaborated tirelessly to bring this project to fruition. Each contribution, big or small, has been essential to its success.",
                                         bg="#F9DEC9", font=("", 10))

    about_us_contact = tk.Label(about_us_canvas, text="Get in touch with us: 09123450400      example@gmail.com",
                                bg="#F9DEC9", font=("", 10))
    """end of about us widgets======================================================================================="""
    """start of help widgets========================================================================================="""
    help_frame = tk.Frame(window_frame, borderwidth=2, bg="black")
    help_canvas = tk.Canvas(help_frame, bg="#F9DEC9")

    helpimage1 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\searchandsort.png")
    helpimage2 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\leftbuttons.png")
    helpimage2 = helpimage2.subsample(3)
    helpimage3 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\adddonor.png")
    helpimage3 = helpimage3.subsample(2)
    helpimage4 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\updatedonor.png")
    helpimage4 = helpimage4.subsample(2)
    helpimage5 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\deletedonor.png")
    helpimage5 = helpimage5.subsample(2)
    helpimage6 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\dashboard.png")
    helpimage6 = helpimage6.subsample(3)
    helpimage7 = PhotoImage(file="C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\manageschedule.png")
    helpimage7 = helpimage7.subsample(3)

    helplabelframe1 = tk.Frame(help_canvas, borderwidth=1, bg="black")
    helplabel1 = tk.Label(helplabelframe1, image=helpimage2, compound="left",
                          text="   To the left of the admin panel is the tab section, just press the buttons there to go to your desired tab.",
                          font=("", 13), bg="#F9DEC9")

    helplabelframe2 = tk.Frame(help_canvas, borderwidth=1, bg="black")
    helplabel2 = tk.Label(helplabelframe2, image=helpimage1)
    helplabel2_1 = tk.Label(helplabelframe2, text="In the search and sort row you must first input the column the you want to search or sort. After that you need to type the data you want to search\n"
                                                   "in the search entry and click search to find the data you are looking for. As for the sort entry you need to put ASC for ascending or DESC for\n"
                                                   "descending and click the sort button to sort the column in that order.",
                            font=("", 13), bg="#F9DEC9")

    helplabelframe3 = tk.Frame(help_canvas, borderwidth=1, bg="black")
    helplabel3 = tk.Label(helplabelframe3, image=helpimage3)
    helplabel3_1 = tk.Label(helplabelframe3,
                            text="In the add donor section, the admin or staff must fill the following entries. all entries must be filled in order for it to add a new donor.",
                            font=("", 13), bg="#F9DEC9")

    helplabelframe4 = tk.Frame(help_canvas, borderwidth=1, bg="black")
    helplabel4 = tk.Label(helplabelframe4, image=helpimage4)
    helplabel4_1 = tk.Label(helplabelframe4,
                            text="In the update donor section, the admin or staff must fill the Donor_ID either by selecting it on the treeview or typing it on the Donor_ID entry before updating a column.",
                            font=("", 13), bg="#F9DEC9")

    helplabelframe5 = tk.Frame(help_canvas, borderwidth=1, bg="black")
    helplabel5 = tk.Label(helplabelframe5, image=helpimage5)
    helplabel5_1 = tk.Label(helplabelframe5,
                            text="In the delete donor section, the admin or staff must fill the Donor_ID either by selecting it on the treeview or typing it on the Donor_ID entry before deleting a row.",
                            font=("", 13), bg="#F9DEC9")

    def nextpage():
        help_canvas.pack_forget()
        help_canvas2.pack(fill="both", expand=True)
        for widget in help_canvas2.winfo_children():
            if widget == previousbutton:
                widget.pack(anchor="sw", padx=(20, 0), pady=(20, ))
            else:
                widget.pack(anchor="n", pady=(10, 0))
                for widget7 in helplabelframe6.winfo_children():
                    widget7.pack(anchor="n", fill="x")
                for widget8 in helplabelframe7.winfo_children():
                    widget8.pack(anchor="n", fill="x")


    def previous():
        help_canvas2.pack_forget()
        help_canvas.pack(fill="both", expand=True)

    help_canvas2 = tk.Canvas(help_frame, bg="#F9DEC9")
    nextbutton = tk.Button(help_canvas, text="Next", bg="#D80032", fg="black", activebackground="#E66371",
                           activeforeground="white", font=("", 10), width=10, command=nextpage)

    helplabelframe6 = tk.Frame(help_canvas2, borderwidth=1, bg="black")
    helplabel6 = tk.Label(helplabelframe6, image=helpimage6)
    helplabel6_1 = tk.Label(helplabelframe6,
                            text="In the dashboard section, the admin or staff can monitor the blood types and acquire data like how much is left and the total donors the hospital has had\n"
                                 "just by clicking the blood donation type a new window will pop up showing all the donors with that specific blood donation",
                            font=("", 13), bg="#F9DEC9")

    helplabelframe7 = tk.Frame(help_canvas2, borderwidth=1, bg="black")
    helplabel7 = tk.Label(helplabelframe7, image=helpimage7)
    helplabel7_1 = tk.Label(helplabelframe7,
                            text="In the manage schedule section the admin or staff can set a schedule in which the hospital is available for accepting blood donors which will then be\n"
                                 "available to select on the donor panel. All the user needs to do is select the date, pick the City/Municipality and press the add button all entries \n"
                                 "must be filled for it to work properly.",
                            font=("", 13), bg="#F9DEC9")

    previousbutton = tk.Button(help_canvas2, text="Previous", bg="#D80032", fg="black", activebackground="#E66371",
                               activeforeground="white", font=("", 10), width=10, command=previous)

    """end of help widgets==========================================================================================="""

    window.mainloop()
    connection.close()

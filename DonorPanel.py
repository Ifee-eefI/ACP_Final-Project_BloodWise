from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def donor_panel():
    def donation_type():
        MessageBox.showinfo(
            "Donation Type",
            "Blood: The most common type of donation,\nduring which approximately a pint of 'whole blood'\nis given. This type of blood donation usually takes\nabout an hour.\n\nPower Red: A Power Red donation collects the\nred cells but returns most of the plasma and\nplatelets to the donor. These donors must meet\nspecific eligibility requirements and have type A\nNeg, B Neg, or O blood.\n\nPlatelets: This type of donation collects the\nplatelets and some plasma and returns the red\ncells and most of the plasma back to the donor.\nThe donation takes approximately two to three\nhours.\n\nAB Plasma: This type of donation collects AB\nplasma, then safely and comfortably returns the\nred cells, platelets and some saline back to the\ndonor. It only takes a few minutes longer than\ndonating blood. Only donors with type AB blood\nare eligible for AB Elite plasma donation."
        )

    def schedule():
        for widgets in right_frame.winfo_children():
            widgets.destroy()

        root.title("Schedule an Appointment")

        button_schedule.config(bg="#D8D9DA", fg="#0F0F0F")
        button_manage.config(bg="#232D3F", fg="#FFFFFF")

        label_schedule = Label(right_frame, pady=30, text="Schedule an\nAppointment", font=('Berlin Sans FB', 40),
                               fg="#0F0F0F", bg="#FFF6E0")
        label_schedule.pack()

        search_frame = Frame(right_frame, bg="#FFF6E0")
        search_frame.place(x=150, y=220)

        label_search = Label(search_frame, text="Search by\nCity/Municipality", font=('Berlin Sans FB', 30),
                             fg="#0F0F0F", bg="#FFF6E0", justify="left")
        label_search.pack()

        city = StringVar()
        search_combobox = ttk.Combobox(search_frame, width=20, textvariable=city, font=('Berlin Sans FB', 16))

        search_combobox['values'] = (
            'Batangas City',
            'Bauan',
            'Taal'
        )

        search_combobox.pack(pady=20)

        date_frame = Frame(right_frame, bg="#FFF6E0")
        date_frame.place(x=150, y=400)

        label_date = Label(date_frame, text="Choose a Date", font=('Berlin Sans FB', 30), fg="#0F0F0F", bg="#FFF6E0")
        label_date.pack(anchor=W)

        date = DateEntry(date_frame, selectmode='day')
        date.pack(pady=20, anchor=W)

        type_frame = Frame(right_frame, bg="#FFF6E0")
        type_frame.place(x=750, y=220)

        type_label = Label(type_frame, text="Donation Type", font=('Berlin Sans FB', 40), fg="#0F0F0F", bg="#FFF6E0")
        type_label.pack(anchor=W)

        info_frame = Frame(right_frame, bg="#FFF6E0")
        info_frame.place(x=1090, y=230)

        info_button = Button(info_frame, borderwidth=0, bg="#FFF6E0", command=donation_type)
        info_button.pack()

        global donation_var
        donation_var = StringVar(value=0)

        blood_radio = Radiobutton(type_frame, text="Blood", variable=donation_var, value="Blood",
                                  font=('Berlin Sans FB', 20), fg="#0F0F0F", bg="#FFF6E0")
        blood_radio.pack(anchor=W, pady=10)
        power_red_radio = Radiobutton(type_frame, text="Power Red", variable=donation_var, value="Power Red",
                                      font=('Berlin Sans FB', 20), fg="#0F0F0F", bg="#FFF6E0")
        power_red_radio.pack(anchor=W, pady=10)
        platelets_radio = Radiobutton(type_frame, text="Platelets", variable=donation_var, value="Platelets",
                                      font=('Berlin Sans FB', 20), fg="#0F0F0F", bg="#FFF6E0")
        platelets_radio.pack(anchor=W, pady=10)
        ab_plasma_radio = Radiobutton(type_frame, text="AB Plasma", variable=donation_var, value="AB Plasma",
                                      font=('Berlin Sans FB', 20), fg="#0F0F0F", bg="#FFF6E0")
        ab_plasma_radio.pack(anchor=W, pady=10)

        def search():
            municipality = city.get()
            dt = date.get_date()
            donation = donation_var.get()
            str_dt = dt.strftime("%Y-%m-%d")
            var = 0

            for appointment in appointment_list:
                if (appointment[1] == municipality and appointment[2] == str_dt):
                    var += 1

            for entry in entry_list:
                if (entry[1] == municipality and entry[2] == str_dt):
                    var += 1

            if (municipality == ""):
                MessageBox.showinfo("Search Status", "All fields are required")
            elif (donation == "0"):
                MessageBox.showinfo("Search Status", "All fields are required")
            elif (var == 2):
                MessageBox.showinfo("Search Status", "Appointment already exists")
            elif (var == 1):
                con = mysql.connect(host="localhost", user="root", password="", database="bloodbank_db")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT * FROM AvailableSchedule WHERE CityMunicipality = '" + municipality + "' AND Date ='" + str_dt + "'")
                rows = cursor.fetchall()

                for row in rows:
                    cursor.execute(f"INSERT INTO Appointments VALUES ('{row[0]}','{row[1]}','{row[2]}','{donation}')")

                cursor.execute("COMMIT")
                con.close()
                MessageBox.showinfo("Search Status", "Appointment added successfully")
            else:
                MessageBox.showinfo("Search Status", "Schedule is not available")

        button_search = Button(type_frame, text="Search", padx=30, bg="#D80032", fg="#FFFFFF",
                               font=('Berlin Sans FB Demi', 18), command=search)
        button_search.pack(pady=30, anchor=W)

    def manage():
        class EntryFrame(Frame):
            def __init__(self, parent, entry_data, entry_height):
                super().__init__(master=parent)
                self.pack(expand=True, fill="both")

                # widget data
                self.entry_data = entry_data
                self.entry_number = len(entry_data)
                self.table_height = self.entry_number * entry_height

                # canvas
                self.canvas = Canvas(self, background='#FFFFFF', scrollregion=(0, 0, 1200, self.table_height))
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
                                         lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
                    self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
                else:
                    height = self.table_height
                    self.canvas.unbind_all('<MouseWheel>')
                    self.scrollbar.place_forget()

                self.canvas.create_window((0, 0),
                                          window=self.frame,
                                          anchor='nw',
                                          width=1200,
                                          height=height)

            def create_entry(self, index, entry):
                def delete_entry():
                    con = mysql.connect(host="localhost", user="root", password="", database="bloodbank_db")
                    cursor = con.cursor()
                    cursor.execute(
                        "DELETE FROM Appointments WHERE AppointmentID = '" + appointment_list[index][0] + "'")
                    cursor.execute("COMMIT")

                    entry_name[0].destroy()
                    retrieve_appointments()
                    entry_name[1] = EntryFrame(table_frame, appointment_list, 60)
                    temp = entry_name[0]
                    entry_name[0] = entry_name[1]
                    entry_name[1] = temp

                    MessageBox.showinfo("Delete Appointment", "Appointment deleted successfully")
                    con.close()

                frame = Frame(self.frame, bg="#F9DEC9")

                # grid layout
                frame.rowconfigure(0, weight=1)
                frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

                # widgets
                id_frame = Frame(frame, width=240, height=60)
                id_frame.grid(row=0, column=0)
                id_frame.pack_propagate(0)
                id_label = Label(id_frame, text=f'{entry[0]}', bg="#FFFFFF", fg="#1F1717",
                                 font=('Berlin Sans FB Demi', 16))
                id_label.pack(fill=BOTH, expand=True)

                city_frame = Frame(frame, width=240, height=60)
                city_frame.grid(row=0, column=1)
                city_frame.pack_propagate(0)
                city_label = Label(city_frame, text=f'{entry[1]}', bg="#FFFFFF", fg="#1F1717",
                                   font=('Berlin Sans FB Demi', 16))
                city_label.pack(fill=BOTH, expand=True)

                date_frame = Frame(frame, width=240, height=60)
                date_frame.grid(row=0, column=2)
                date_frame.pack_propagate(0)
                date_label = Label(date_frame, text=f'{entry[2]}', bg="#FFFFFF", fg="#1F1717",
                                   font=('Berlin Sans FB Demi', 16))
                date_label.pack(fill=BOTH, expand=True)

                type_frame = Frame(frame, width=240, height=60, bg="#FFFFFF")
                type_frame.grid(row=0, column=3)
                type_frame.pack_propagate(0)
                type_frame = Label(type_frame, text=f'{entry[3]}', bg="#FFFFFF", fg="#1F1717",
                                   font=('Berlin Sans FB Demi', 16))
                type_frame.pack(fill=BOTH, expand=True)

                action_frame = Frame(frame, width=240, height=60, bg="#FFFFFF")
                action_frame.grid(row=0, column=4)
                action_frame.pack_propagate(0)
                action_button = Button(action_frame, text="Delete", bg="#D80032", fg="#FFFFFF",
                                       font=('Berlin Sans FB Demi', 16), command=delete_entry)
                action_button.pack(pady=10)

                return frame

        def update():
            retrieve_appointments()

            if (len(entry_list) == 0):
                con = mysql.connect(host="localhost", user="root", password="", database="bloodbank_db")
                cursor = con.cursor()
                cursor.execute("DELETE FROM Appointments")
                cursor.execute("COMMIT")
                con.close()

            for appointment in appointment_list:
                for index, entry in enumerate(entry_list):
                    if (appointment[0] == entry[0]):
                        break
                    elif (index == len(entry_list) - 1):
                        con = mysql.connect(host="localhost", user="root", password="", database="bloodbank_db")
                        cursor = con.cursor()
                        cursor.execute("DELETE FROM Appointments WHERE AppointmentID = '" + appointment[0] + "'")
                        cursor.execute("COMMIT")
                        con.close()

            retrieve_appointments()

        for widgets in right_frame.winfo_children():
            widgets.destroy()

        root.title("Manage Existing Appointments")

        button_schedule.config(bg="#232D3F", fg="#FFFFFF")
        button_manage.config(bg="#D8D9DA", fg="#0F0F0F")

        label_manage = Label(right_frame, pady=30, text="Manage Existing\nAppointment", font=('Berlin Sans FB', 40),
                             fg="#0F0F0F", bg="#FFF6E0")
        label_manage.pack()

        table_frame = Frame(right_frame, width=1200, height=600, bg="#F9DEC9")
        table_frame.pack()
        table_frame.pack_propagate(0)

        attribute_frame = Frame(table_frame)
        attribute_frame.pack(fill=X)

        id_frame = Frame(attribute_frame, width=240, height=60)
        id_frame.grid(row=0, column=0)
        id_frame.pack_propagate(0)
        id_label = Label(id_frame, text="Appointment ID", bg="#1F1717", fg="#FFFFFF", font=('Berlin Sans FB Demi', 18))
        id_label.pack(fill=BOTH, expand=True)

        city_frame = Frame(attribute_frame, width=240, height=60)
        city_frame.grid(row=0, column=1)
        city_frame.pack_propagate(0)
        city_label = Label(city_frame, text="City/Municipality", bg="#1F1717", fg="#FFFFFF",
                           font=('Berlin Sans FB Demi', 18))
        city_label.pack(fill=BOTH, expand=True)

        date_frame = Frame(attribute_frame, width=240, height=60)
        date_frame.grid(row=0, column=2)
        date_frame.pack_propagate(0)
        date_label = Label(date_frame, text="Date", bg="#1F1717", fg="#FFFFFF", font=('Berlin Sans FB Demi', 18))
        date_label.pack(fill=BOTH, expand=True)

        donation_frame = Frame(attribute_frame, width=240, height=60)
        donation_frame.grid(row=0, column=3)
        donation_frame.pack_propagate(0)
        donation_label = Label(donation_frame, text="Donation Type", bg="#1F1717", fg="#FFFFFF",
                               font=('Berlin Sans FB Demi', 18))
        donation_label.pack(fill=BOTH, expand=True)

        action_frame = Frame(attribute_frame, width=240, height=60)
        action_frame.grid(row=0, column=4)
        action_frame.pack_propagate(0)
        action_label = Label(action_frame, text="Action", bg="#1F1717", fg="#FFFFFF", font=('Berlin Sans FB Demi', 18))
        action_label.pack(fill=BOTH, expand=True)

        update()

        entry_name = ["entry_frame_1", "entry_frame_2"]
        entry_name[0] = EntryFrame(table_frame, appointment_list, 60)

    def retrieve_schedule():
        entry_list.clear()

        con = mysql.connect(host="localhost", user="root", password="", database="bloodbank_db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM AvailableSchedule")
        rows = cursor.fetchall()

        for row in rows:
            entry_tuple = (f"{row[0]}", f"{row[1]}", f"{row[2]}")
            entry_list.append(entry_tuple)

        con.close()

    def retrieve_appointments():
        appointment_list.clear()

        con = mysql.connect(host="localhost", user="root", password="", database="bloodbank_db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Appointments")
        rows = cursor.fetchall()

        for row in rows:
            appointment_tuple = (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}")
            appointment_list.append(appointment_tuple)

        con.close()

    root = Tk()
    root.attributes("-fullscreen", True)
    root_width = 1600
    root_height = 780
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - root_width) // 2
    y = (screen_height - root_height) // 2
    root.geometry(f"{root_width}x{root_height}+{x}+{y}")

    def toggle_fullscreen(event):
        if root.attributes('-fullscreen'):
            root.attributes('-fullscreen', False)
        else:
            root.attributes('-fullscreen', True)

    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", toggle_fullscreen)
    root.title("Schedule an Appointment")
    root.iconbitmap("C:\\Users\\Jhun Harvey\\PycharmProjects\\images\\blood.ico")

    top_frame = Frame(root, pady=20, bg="#0F0F0F")
    top_frame.pack(fill=X)

    button_quit = Button(top_frame, text="Logout", padx=20, command=root.quit)
    button_quit.pack(side=RIGHT, padx=30)

    left_frame = Frame(root, bg="#232D3F")
    left_frame.pack(fill=Y, side=LEFT)

    button_schedule = Button(left_frame, text="Schedule an\nAppointment", padx=59, command=schedule,
                             font=('Berlin Sans FB Demi', 18), borderwidth=0)
    button_schedule.pack()
    button_manage = Button(left_frame, text="Manage Existing\nAppointment", command=manage, padx=40,
                           font=('Berlin Sans FB Demi', 19), borderwidth=0)
    button_manage.pack()

    right_frame = Frame(root, bg="#FFF6E0")
    right_frame.pack(fill=BOTH, expand=True, side=LEFT)

    entry_list = list()
    appointment_list = list()
    retrieve_schedule()
    retrieve_appointments()
    schedule()

    root.mainloop()
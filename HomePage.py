import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from DonorLogin import donor_login
from AdminLogin import admin_login



def homepage():
    # window designs
    window = tk.Tk()
    window.title("Home Page")
    window.attributes("-fullscreen", True)
    window_width = 1600
    window_height = 780
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def toggle_fullscreen(event):
        if window.attributes('-fullscreen'):
            window.attributes('-fullscreen', False)
        else:
            window.attributes('-fullscreen', True)

    window.bind("<F11>", toggle_fullscreen)
    window.bind("<Escape>", toggle_fullscreen)
    window_frame = tk.Frame(window)
    window_frame.pack(fill="both", expand=True)
    """end of window designs"""

    # top widgets
    top_frame = tk.Frame(window_frame,
                         borderwidth=2,
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
                         text=" BloodWise: A Blood Bank Management System",
                         font=("Arial", 15, "bold"),
                         compound="left"
                         )
    top_label.pack(side="left")
    """end of top widgets"""

    # left widgets
    left_frame = tk.Frame(window_frame,
                          borderwidth=1,
                          bg="black")
    left_frame.pack(side="left", fill="y")
    left_label_image = Image.open("C:\\Users\\Jhun Harvey\\Pictures\\Saved Pictures\\Hand.png")
    new_width = 680
    new_height = 800
    resized_left_label_image = left_label_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(resized_left_label_image)

    left_label = tk.Label(left_frame,
                          image=photo)
    left_label.pack(anchor="w")
    """end of left widgets"""

    # right button functions

    def onrdbtnclick():
        window.destroy()
        donor_login()

    def onrabtnclick():
        window.destroy()
        admin_login()

    # right widgets
    right_frame = tk.Frame(window_frame,
                           borderwidth=1,
                           bg="black")
    right_frame.pack(side="right", fill="both", expand=True)

    right_canvas = tk.Canvas(right_frame,
                             bg="#FFBF9B")
    right_canvas.pack(fill="both", expand=True)

    right_donor_button = tk.Button(right_canvas,
                                   text="DONOR",
                                   font=("", 40),
                                   width=12,
                                   bg="#CE5A67",
                                   fg="white",
                                   activebackground="#E66371",
                                   activeforeground="white",
                                   command=onrdbtnclick)
    right_donor_button.pack(anchor="s", expand=True)

    frame_spaces = tk.Frame(right_canvas,
                            height=50,
                            bg="#FFBf9B")
    frame_spaces.pack()

    right_admin_button = tk.Button(right_canvas,
                                   text="ADMIN",
                                   font=("", 40),
                                   width=12,
                                   bg="#CE5A67",
                                   fg="white",
                                   activebackground="#E66371",
                                   activeforeground="white",
                                   command=onrabtnclick)
    right_admin_button.pack(anchor="n", expand=True)
    window.mainloop()


functioncalled = False
if not functioncalled:
    homepage()
    functioncalled = True

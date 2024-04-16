import random as rnd
from datetime import date
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from module import *

# Connecting to the database
conn = None
cursor = None

connect()

year = date.today().year
random = rnd.randint(1000, 9999)

idNo = int(f"{year}{random}")

def submit():
    # Retrieve data from entry fields
    name = name_entry.get()
    dob = str(dob_calendar.get_date())
    gender = gender_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    pathway = path_entry.get()

    # Check if any field is empty
    if not (name and dob and gender and contact and email and pathway):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    # Storing data
    store(idNo, name, dob, gender, contact, email, pathway)

    # Display the submitted data
    messagebox.showinfo("Submission Successful", f"ID: {idNo}\nName: {name}\nDate of Birth: {dob}\nGender: {gender}\nContact: {contact}\nEmail: {email}\nPathway: {pathway}\n")

    # Closing the database
    commit()

# Create the main window
root = tk.Tk()
root.title("Zatabase")

# Create labels and entry fields for each input
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

dob_label = tk.Label(root, text="Date of Birth:")
dob_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
dob_calendar = DateEntry(root, selectmode="day", date_pattern="yyyy-mm-dd")
dob_calendar.grid(row=1, column=1, padx=10, pady=5)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
gender_entry = tk.Entry(root)
gender_entry.grid(row=2, column=1, padx=10, pady=5)

contact_label = tk.Label(root, text="Contact:")
contact_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
contact_entry = tk.Entry(root)
contact_entry.grid(row=3, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, padx=10, pady=5)

path_label = tk.Label(root, text="Pathway:")
path_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
path_entry = tk.Entry(root)
path_entry.grid(row=5, column=1, padx=10, pady=5)

id_label = tk.Label(root, text="Student ID:")
id_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
id_entry = tk.Label(root, text=idNo)
id_entry.grid(row=6, column=1, padx=10, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=7, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
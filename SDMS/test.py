import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

root = tk.Tk()

dob_label = tk.Label(root, text="Date of Birth:")
dob_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
dob_calendar = DateEntry(root, selectmode="day", date_pattern="yyyy-mm-dd")
dob_calendar.grid(row=0, column=1, padx=10, pady=5)

def submit():
    dob = dob_calendar.get_date()
    dob = str(dob)
    # Display the submitted data
    messagebox.showinfo("Submission Successful", f"{dob}\n")

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=7, columnspan=2, padx=10, pady=10)

root.mainloop()
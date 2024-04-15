import tkinter as tk
from tkinter import messagebox

def submit():
    # Retrieve data from entry fields
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    # Check if any field is empty
    if not (name and age and email):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Display the submitted data
    messagebox.showinfo("Submission Successful", f"Name: {name}\nAge: {age}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Zatabase")

# Create labels and entry fields for each input
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()

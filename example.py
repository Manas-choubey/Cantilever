import tkinter as tk
from tkinter import messagebox


contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        contacts.append((name, phone))
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def view_contacts():
    if contacts:
        contact_list.delete(0, tk.END)  # Clear existing items
        for name, phone in contacts:
            contact_list.insert(tk.END, f"{name}: {phone}")
    else:
        messagebox.showwarning("No Contacts", "There are no contacts to display.")

def delete_contact():
    try:
        index = contact_list.curselection()[0]
        contacts.pop(index)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete.")


root = tk.Tk()
root.title("Contact Book")


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=10)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=10)


btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

btn_view = tk.Button(root, text="View Contacts", command=view_contacts)
btn_view.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


contact_list = tk.Listbox(root, width=50, height=10)
contact_list.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()

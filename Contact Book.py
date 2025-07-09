import tkinter as tk
from tkinter import messagebox

# List to store contacts
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Input Error", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    update_contact_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully!")

def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showerror("Selection Error", "Please select a contact to update.")
        return

    index = selected[0]

    contacts[index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    update_contact_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact updated.")

def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showerror("Selection Error", "Please select a contact to delete.")
        return

    index = selected[0]
    del contacts[index]
    update_contact_list()
    clear_fields()
    messagebox.showinfo("Deleted", "Contact deleted.")

def search_contact():
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def show_selected_contact(event):
    selected = contact_listbox.curselection()
    if not selected:
        return

    index = selected[0]
    contact = contacts[index]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact['name'])

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact['phone'])

    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact['email'])

    address_entry.delete(0, tk.END)
    address_entry.insert(0, contact['address'])

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x550")

# Labels and Entry Fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", width=20, command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=20, command=delete_contact).pack(pady=5)

# Search
tk.Label(root, text="Search by name or phone:").pack()
search_entry = tk.Entry(root, width=50)
search_entry.pack()
tk.Button(root, text="Search", width=20, command=search_contact).pack(pady=5)

# Contact List Display
tk.Label(root, text="Contact List:").pack()
contact_listbox = tk.Listbox(root, width=60, height=10)
contact_listbox.pack()
contact_listbox.bind("<<ListboxSelect>>", show_selected_contact)

# Run the Application
root.mainloop()

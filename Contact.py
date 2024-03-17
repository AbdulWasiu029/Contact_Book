import tkinter as tk

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        update_contact_list()

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for idx, contact in enumerate(contacts, start=1):
        name = contact.get('Name', '')
        phone = contact.get('Phone', '')
        email = contact.get('Email', '')
        address = contact.get('Address', '')
        entry_text = f"{idx}. {name:<20} {phone:<15} {email:<30} {address}"
        contact_listbox.insert(tk.END, entry_text)
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['Name'].lower() or query in contact['Phone']:
            contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}")

def view_all_contacts():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def update_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone:
            contacts[selected_index[0]] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            update_contact_list()

def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        del contacts[selected_index[0]]
        update_contact_list()

root = tk.Tk()
root.geometry("1300x700")
root.title("Contact Book")
root.config(bg='LightGray')

title_label = tk.Label(root, text="Contact Book", font=("Arial", 30, "bold"),
                        border=7, relief=tk.GROOVE, bg="DimGray", fg="White")
title_label.pack(side="top", fill="x")

contact_frame = tk.Frame(root, border=7, relief=tk.GROOVE, bg="LightGrey")
contact_frame.place(x=40, y=100, width=1200, height=550)

name_label = tk.Label(contact_frame, text="Name:", font=("Arial", 15), bg="Gainsboro")
name_label.place(x=10, y=15)
name_entry = tk.Entry(contact_frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)
name_entry.place(x=120, y=15, width=350)

phone_label = tk.Label(contact_frame, text="Phone:", font=("Arial", 15), bg="Gainsboro")
phone_label.place(x=10, y=55)
phone_entry = tk.Entry(contact_frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)
phone_entry.place(x=120, y=55, width=350)

email_label = tk.Label(contact_frame, text="Email:", font=("Arial", 15), bg="Gainsboro")
email_label.place(x=10, y=95)
email_entry = tk.Entry(contact_frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)
email_entry.place(x=120, y=95, width=350)

address_label = tk.Label(contact_frame, text="Address:", font=("Arial", 15), bg="Gainsboro")
address_label.place(x=10, y=135)
address_entry = tk.Entry(contact_frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)
address_entry.place(x=120, y=135, width=350)

add_button = tk.Button(contact_frame, text="Add Contact", font=("Arial", 15, "bold"),
                       bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=add_contact)
add_button.place(x=490, y=20, width=180, height=40)

update_button = tk.Button(contact_frame, text="Update Contact", font=("Arial", 15, "bold"),
                          bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=update_contact)
update_button.place(x=490, y=70, width=180, height=40)

delete_button = tk.Button(contact_frame, text="Delete Contact", font=("Arial", 15, "bold"),
                          bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=delete_contact)
delete_button.place(x=490, y=120, width=180, height=40)

search_label = tk.Label(contact_frame, text="Search:", font=("Arial", 18), bg="Gainsboro")
search_label.place(x=680, y=14)
search_entry = tk.Entry(contact_frame, font=("Arial", 15), bd=5, relief=tk.GROOVE)
search_entry.place(x=770, y=13, width=250, height=35)

search_button = tk.Button(contact_frame, text="Search", font=("Arial", 15, "bold"),
                          bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=search_contact)
search_button.place(x=1040, y=10, width=130, height=40)

view_all_button = tk.Button(contact_frame, text="View All", font=("Arial", 15, "bold"),
                            bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=view_all_contacts)
view_all_button.place(x=1040, y=55, width=130, height=40)

contact_listbox = tk.Listbox(contact_frame, font=("Arial", 15), bg="Gainsboro", bd=5, relief=tk.GROOVE)
contact_listbox.place(x=0, y=183, width=1188, height=355)

scrollbar = tk.Scrollbar(contact_frame, orient=tk.VERTICAL)
scrollbar.place(x=1195, y=230, height=310)

scrollbar.config(command=contact_listbox.yview)

root.mainloop()
import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
        "email": email,
        "password": password
        }
    }
    # confirm_data = messagebox.askokcancel(title="ENTRY", message=f"CONFIRM YOUR DATA\nWEBSITE: {website}\n"
                                                                 # f"EMAIL: {email}\nPASSWORD: {password}")

    # empty_data = messagebox.showwarning(title="Oops", message="Your entries are empty")

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Make sure you haven't left any field emplty")


    else:
        # messagebox.askokcancel(title="ENTRY", message=f"CONFIRM YOUR DATA\nWEBSITE: {website}\n"
        # f"EMAIL: {email}\nPASSWORD: {password}")
        # with open("data.txt", "a") as data_file:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                """write json"""
                # json.dump(new_data, data_file, indent=4)
                """read json"""
                # data = json.load(data_file)
                # print(data)
                """update json"""
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            search_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="There's no data file")

    else:
        if len(website) == 0:
            messagebox.showwarning(title="Oops", message="There's nothing to search")

        elif website in search_data:
            email = search_data[website]["email"]
            password = search_data[website]["password"]
            messagebox.showinfo(title=website, message=f"EMAIL: {email}\nPASSWORD: {password}")

        else:
            messagebox.showwarning(title="Oops", message="There's no such website saved in your data file")

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=150, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(90, 100, image=logo)
canvas.grid(row=0, column=1)
"""Lable"""
website_lable = Label(text="Website:")
website_lable.grid(row=1, column=0)

email_lable = Label(text="Email/Username:")
email_lable.grid(row=2, column=0)

password_lable = Label(text="Password:")
password_lable.grid(row=3, column=0)

"""Entry"""
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=44)
email_entry.insert(0, "xzy@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

"""Button"""
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

"""collecting info"""
# password_entry.get()

window.mainloop()
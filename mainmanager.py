from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_entry.delete(0, END)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = web_entry.get()
    email = email_entry.get()
    password1 = pass_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password1,
        }
    }

    if len(website) == 0 or len(password1) == 0:
        messagebox.showerror(title="Oops", message="Dont leave any fields empty!")
    else:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

        with open("passwords.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(height=200, width=200)
window.config(pady=50, padx=50, bg="white")

lock_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
web_text = Label(text="Website:", bg="white")
email_text = Label(text="Email/Username:", bg="white")
pass_text = Label(text="Password:", bg="white")

# Entry
web_entry = Entry(width=35)
email_entry = Entry(width=35)
pass_entry = Entry(width=35)

# Text Grid
web_text.grid(column=0, row=1)
email_text.grid(column=0, row=2)
pass_text.grid(column=0, row=3)

# Buttons
generate_button = Button(text="Generate Password", highlightthickness=0, bg="white", command=generate)
search_button = Button(text="Search", highlightthickness=0, bg="white")
add_button = Button(text="Add", width=30, highlightthickness=0, bg="white", command=save)

# Entry grid
web_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry.grid(column=1, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=3, row=1)
generate_button.grid(column=3, row=3)

web_entry.focus()
email_entry.insert(0, "frank@silva.com")

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Remember to fill all entries.")
    else:
        check = messagebox.askokcancel(title=website, message=f"These are the information entered: "
                                                              f"\nWebsite: {website}"
                                                              f"\nEmail: {email}"
                                                              f"\nPassword: {password}\n"
                                                              f"Is it okay to save?")

        if check:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

#Image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

#Entries
website_input = Entry(bg="white", width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(bg="white", width=52)
email_input.insert(0, "") #Insert your own email
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(bg="white", width=32)
password_input.grid(column=1, row=3, sticky="w")

#Buttons
password_generator_button = Button(text="Generate Password", bg="white", width=15, command=password_generator)
password_generator_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=44, bg="white", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

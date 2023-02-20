from tkinter import *
from tkinter import messagebox
import random
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0,password)


def save():

    website_input = website_entry.get()
    mail_input = email_entry.get()
    password_input = password_entry.get()
    new_dict = {
        website_input: {
            "email": mail_input,
            "password": password_input,
        }
    }

    if website_input == "" or mail_input == "" or password_input == "" :
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_dict, file, indent=4)
        else:
            data.update(new_dict)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = website_entry.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]
            password = data[website]["password"]
            mail = data[website]["email"]
            email_entry.delete(0,END)
            email_entry.insert(0,mail)
            password_entry.insert(0,password)


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width = 200)
image = PhotoImage(file="logo.png")
canvas.create_image(125,100,image = image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1,column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry = Entry(width=38)
email_entry.insert(0, "david@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=13,command=search)
search_button.grid(row=1,column=2)

window.mainloop()
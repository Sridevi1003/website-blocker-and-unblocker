import os
from tkinter import *
from tkinter.messagebox import *

# Setting localhost IP address for GUI
localhost = '127.0.0.1'
hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"


def block_website(website):
    try:
        with open(hosts_file_path, 'a') as hostfile:
            hostfile.write(f'{localhost}\t{website}\n')
        showinfo('Website Blocked!', f'{website} has been blocked!')
    except Exception as e:
        showerror('Error', f'An error occurred: {e}')


def unblock_website(website):
    try:
        with open(hosts_file_path, 'r') as hostfile:
            lines = hostfile.readlines()

        with open(hosts_file_path, 'w') as hostfile:
            for line in lines:
                if website not in line:
                    hostfile.write(line)

        showinfo('Website Unblocked!', f'{website} has been unblocked.')
    except Exception as e:
        showerror('Error', f'An error occurred: {e}')


# Creating a GUI master window
root = Tk()
root.title("Website Blocker")
root.geometry('400x300')
root.wm_resizable(False, False)

# Set background color
root.configure(bg='#E6E6FA')

Label(root, text='Website Blocker', font=("Comic Sans MS", 16), bg='#E6E6FA').place(x=120, y=1)
Label(root, text='Enter website to block/unblock:', font=("Helvetica", 14), bg='#E6E6FA').place(x=50, y=80)

# Increased width of the Entry widget
website_entry = Entry(root, width=50)
website_entry.place(x=50, y=120)

block_button = Button(root, text='Block Website', font=('Times', 16), bg='purple',
                      command=lambda: block_website(website_entry.get()))
block_button.place(x=120, y=170)

unblock_button = Button(root, text='Unblock Website', font=('Times', 16), bg='#FF6347',
                        command=lambda: unblock_website(website_entry.get()))
unblock_button.place(x=110, y=220)

root.mainloop()

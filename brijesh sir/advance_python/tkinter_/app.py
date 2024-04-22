import tkinter as tk

screen = tk.Tk()

screen.geometry('400x400')

screen.title("Witzcode Management")

screen.iconbitmap(r'images\Logo_Favicon.ico')

screen.configure(bg='#78b846')

# Load the image file
image_path = r"images\Logo_Name_Slogan.png"  # Replace "image.png" with the path to your image file
image = tk.PhotoImage(file=image_path)

image = image.subsample(2) 
# Create a label to display the image
label = tk.Label(screen, image=image, bg="#78b846")
label.pack(pady=16)

tk.Label(screen, text="Welcome to witzcode", font=("Helvetica", 24), fg="#092d1f",  bg="#78b846").pack(pady=16)


def register_page():  
    register_screen = tk.Toplevel(screen)  
    register_screen.geometry('400x400')

    register_screen.title("Witzcode Management - Register")

    register_screen.iconbitmap(r'images\Logo_Favicon.ico')

    register_screen.configure(bg='blue')

    def on_entry_click(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')  # Change text color to black when the Entry is clicked

    def on_focusout(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='grey')  # Change text color to grey when the Entry is not focused and is empty


    entry = tk.Entry(register_screen)
    placeholder = "Enter your fullname"
    entry.insert(0, placeholder)  # Insert placeholder text
    entry.bind("<FocusIn>", on_entry_click)  # Bind on_entry_click function to <FocusIn> event
    entry.bind("<FocusOut>", on_focusout)  # Bind on_focusout function to <FocusOut> event
    entry.pack(padx=10, pady=10)
    register_screen.mainloop()  

def login_page():  
    login_screen = tk.Toplevel(screen)   
    login_screen.geometry('400x400')

    login_screen.title("Witzcode Management - Login")

    login_screen.iconbitmap(r'images\Logo_Favicon.ico')

    login_screen.configure(bg='#78b846')

    def get_data():
        Username = user.get()
        Password = password.get()
        tk.Label(login_screen, text=f"Username:, {Username}, Password:, {Password}").grid(row=3, column=1)
        print("Username:", Username, "Password", Password)

    userLable = tk.Label(login_screen, text="Email/Username: ").grid(row=0, column=0)
    user = tk.Entry(login_screen)
    user.grid(row=0, column=1)
    passwordLable = tk.Label(login_screen, text="password: ").grid(row=1, column=0)
    password = tk.Entry(login_screen)
    password.grid(row=1, column=1)

    tk.Button(login_screen, text="Login", command=get_data).grid(row=2, column=1)
    login_screen.mainloop()  
  


# Create and pack the "Register" button
register_btn = tk.Button(screen, text="Register", font=("Helvetica", 14), bg="#092d1f", fg="white", padx=10, pady=5, bd=0, relief=tk.FLAT, command=register_page)
register_btn.pack(pady=10)
# Adjust button width
register_btn.config(width=10)  # Adjust as needed

# Create and pack the "Login" button
login_btn = tk.Button(screen, text="Login", font=("Helvetica", 14), bg="#092d1f", fg="white", padx=10, pady=5, bd=0, relief=tk.FLAT, command=login_page)
login_btn.pack(pady=10)
# Adjust button width
login_btn.config(width=10)  # Adjust as needed


# tk.Label(screen, text="Welcome to witzcode").grid(row=0, column=5)
# tk.Label(screen, text="Welcome to witzcode").place(x=150, y=50)


screen.mainloop()
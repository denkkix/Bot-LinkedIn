import customtkinter as ctkr

def submitar():
    username = entry_username.get()
    password = entry_password.get()
    iniciar_auto_linkedin(username, password) # proximo arquivo...

app = ctkr.CTk()
app.geometry("500x350")
app.title("Bot Networking Linkedin")

label_username = ctkr.CTkLabel(app, text="User:")
label_username.pack(pady=10)
entry_username = ctkr.CTkEntry(app)
entry_username.pack(pady=5)

label_password = ctkr.CTkLabel(app, text="Password:")
label_password.pack(pady=10)
entry_password = ctkr.CTkEntry(app, show="#")
entry_password.pack(pady=5)

submit_button = ctkr.CTkButton(app, text="Start", command=submitar)
submit_button.pack(pady=20)

app.mainloop()
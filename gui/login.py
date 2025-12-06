import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
import os
# ------------------------
# Configuration
# -------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -------------------------
#  UPDATED DATABASE (Stores Password & Real Name)
# -------------------------
def load_users_from_csv(filename="assets/people_2025_50.csv"):
    users = {}
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Now we use 'id' as the key, but the CSV starts with name first
            users[row["ID"]] = {
                "password": row["Password"],
                "name": row["Name"]
            }
    return users

TEST_USERS = load_users_from_csv()


class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("FindMe - Secure Login")
        self.geometry("900x600")
        self.resizable(False, False)
        
        self._center_window(900, 600)

        # Layout columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT SIDE: Image/Branding ---
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#000000")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self._load_sidebar_image()

        # --- RIGHT SIDE: Login Form ---
        self.login_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#2b2b2b")
        self.login_frame.grid(row=0, column=1, sticky="nsew")
        self._create_login_widgets()

    def _center_window(self, width, height):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def _load_sidebar_image(self):
        image_path = "assets/login.png" 
        try:
            img_data = Image.open(image_path)
            side_img = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(450, 600))
            lbl_img = ctk.CTkLabel(self.sidebar_frame, text="", image=side_img)
            lbl_img.pack(expand=True, fill="both")
        except Exception:
            self.sidebar_frame.configure(fg_color="#1a1a1a")
            lbl_fallback = ctk.CTkLabel(
                self.sidebar_frame, text="FindMe\nSystem", 
                font=("Roboto", 40, "bold"), text_color="white"
            )
            lbl_fallback.pack(expand=True)

    def _create_login_widgets(self):
        form_inner = ctk.CTkFrame(self.login_frame, fg_color="transparent")
        form_inner.pack(expand=True, fill="both", padx=40)

        ctk.CTkLabel(form_inner, text="", height=50).pack()

        # Header
        welcome_label = ctk.CTkLabel(
            form_inner, text="Welcome Back", 
            font=("Roboto Medium", 30), text_color="white"
        )
        welcome_label.pack(anchor="w", pady=(0, 5))

        sub_label = ctk.CTkLabel(
            form_inner, text="Please enter your details to sign in.", 
            font=("Roboto", 14), text_color="#a3a3a3"
        )
        sub_label.pack(anchor="w", pady=(0, 30))

        # ID Entry
        self.user_entry = ctk.CTkEntry(
            form_inner, width=300, height=40,
            placeholder_text="Student / Staff ID",
            font=("Roboto", 14), border_width=1, corner_radius=8
        )
        self.user_entry.pack(fill="x", pady=(0, 15))

        # Password Entry
        self.pass_entry = ctk.CTkEntry(
            form_inner, width=300, height=40,
            placeholder_text="Password", show="*",
            font=("Roboto", 14), border_width=1, corner_radius=8
        )
        self.pass_entry.pack(fill="x", pady=(0, 10))

        # Forgot Password (Moved to right since "Remember me" is gone)
        forgot_btn = ctk.CTkButton(
            form_inner, text="Forgot Password?", 
            font=("Roboto", 12, "underline"), text_color="#a3a3a3",
            fg_color="transparent", hover=False, 
            anchor="e", command=self.forgot_password_dummy
        )
        forgot_btn.pack(fill="x", pady=(0, 20))

        # Login Button
        login_btn = ctk.CTkButton(
            form_inner, text="Sign In", height=45,
            font=("Roboto", 15, "bold"), corner_radius=8,
            fg_color="#1f6aa5", hover_color="#144870",
            command=self.check_login
        )
        login_btn.pack(fill="x", pady=(0, 20))
        
        # Footer
        footer_frame = ctk.CTkFrame(form_inner, fg_color="transparent")
        footer_frame.pack(fill="x")
        
        ctk.CTkLabel(footer_frame, text="Don't have an account?", font=("Roboto", 12), text_color="#a3a3a3").pack(side="left")
        ctk.CTkButton(
            footer_frame, text="Contact Admin", 
            font=("Roboto", 12, "bold"), fg_color="transparent", 
            text_color="#1f6aa5", hover=False, width=80,
            command=lambda: messagebox.showinfo("Info", "Please visit the IT department.")
        ).pack(side="left", padx=5)

    def check_login(self):
        user_id = self.user_entry.get()
        password = self.pass_entry.get()

        # 1. Check if ID exists in database
        if user_id in TEST_USERS:
            user_data = TEST_USERS[user_id]
            
            # 2. Check if password matches
            if user_data["password"] == password:
                real_name = user_data["name"]
                messagebox.showinfo("Success", f"Welcome back, {real_name}!")
                # Next step: self.open_dashboard()
            else:
                messagebox.showerror("Access Denied", "Incorrect Password.")
        else:
            messagebox.showerror("Access Denied", "ID not found. Please check your id or password")

    def forgot_password_dummy(self):
        messagebox.showinfo("Forgot Password", "Feature coming soon!")

# ---------------------------------------------------------
#  LINKING FUNCTION for startup.py
# ---------------------------------------------------------
def launch_login_page():
    app = LoginApp()
    app.mainloop()

if __name__ == "__main__":
    launch_login_page()
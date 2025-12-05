import customtkinter as ctk
from PIL import Image, ImageDraw

def launch_login_page():
    # Create CustomTkinter window
    login = ctk.CTk()
    login.title("FindMe - Login")

    # Window size & center
    width, height = 1280, 720
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    login.geometry(f"{width}x{height}+{x}+{y}")

    # Set background color
    login.configure(fg_color="#2e2e2e")  # dark gray background

    # CustomTkinter appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # --- Content: logo + login form ---
    content = ctk.CTkFrame(login, fg_color="#2e2e2e", border_width=0)
    content.pack(expand=True, fill="both")

    # --- Function to make circular logo ---
    def make_circle_image(path, size):
        img = Image.open(path).resize((size, size), Image.Resampling.LANCZOS).convert("RGBA")
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        img.putalpha(mask)
        return ctk.CTkImage(light_image=img, size=(size, size))

    # Load circular logo
    logo_image = make_circle_image("assets/login.png", 200)
    ctk.CTkLabel(content, image=logo_image, text="", fg_color="#2e2e2e").pack(pady=30)

    # Login form
    form_frame = ctk.CTkFrame(content, fg_color="#2e2e2e", border_width=0)
    form_frame.pack(pady=20)

    ctk.CTkLabel(form_frame, text="ID", fg_color="#2e2e2e").pack(pady=5)
    username_entry = ctk.CTkEntry(form_frame, width=300, placeholder_text="Enter your ID")
    username_entry.pack(pady=5)

    ctk.CTkLabel(form_frame, text="Password", fg_color="#2e2e2e").pack(pady=5)
    password_entry = ctk.CTkEntry(form_frame, show="*", width=300, placeholder_text="Enter your password")
    password_entry.pack(pady=5)

    ctk.CTkButton(form_frame, text="Login", width=300).pack(pady=20)

    login.mainloop()

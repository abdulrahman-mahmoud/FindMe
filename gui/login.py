import customtkinter as ctk
from PIL import Image

def launch_login_page(root=None):
    login = root if root else ctk.CTk()
    login.title("FindMe - Login")

    width, height = 1280, 720
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    login.geometry(f"{width}x{height}+{x}+{y}")

    login.overrideredirect(True)  # remove OS title bar
    login.configure(fg_color="#d9d9d9")  # grey background

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # --- Top bar with Mac-style buttons on the RIGHT ---
    top_bar = ctk.CTkFrame(login, height=40, fg_color="#d9d9d9", border_width=0)
    top_bar.pack(fill="x")

    # Enable window dragging
    def start_move(event):
        login.x = event.x
        login.y = event.y

    def stop_move(event):
        login.x = None
        login.y = None

    def do_move(event):
        x = event.x_root - login.x
        y = event.y_root - login.y
        login.geometry(f"+{x}+{y}")

    top_bar.bind("<Button-1>", start_move)
    top_bar.bind("<ButtonRelease-1>", stop_move)
    top_bar.bind("<B1-Motion>", do_move)

    # Buttons frame on the right
    buttons_frame = ctk.CTkFrame(top_bar, fg_color="#d9d9d9", border_width=0)
    buttons_frame.pack(side="right", padx=10, pady=10)

    is_maximized = {"state": False, "geom": f"{width}x{height}+{x}+{y}"}

    def close(): login.destroy()

    # Simulate minimize (hide and restore)
    def minimize():
        login.withdraw()
        login.after(100, lambda: login.deiconify())

    # Maximize toggle
    def maximize():
        if not is_maximized["state"]:
            is_maximized["geom"] = login.geometry()
            login.geometry(f"{login.winfo_screenwidth()}x{login.winfo_screenheight()}+0+0")
            is_maximized["state"] = True
        else:
            login.geometry(is_maximized["geom"])
            is_maximized["state"] = False

    # Mac-style buttons with requested colors
    ctk.CTkButton(buttons_frame, width=15, height=15, corner_radius=8,
                  fg_color="#FF605C", hover_color="#ff4d4d", command=close, text="").pack(side="left", padx=5)
    ctk.CTkButton(buttons_frame, width=15, height=15, corner_radius=8,
                  fg_color="#FFBD44", hover_color="#ffd966", command=minimize, text="").pack(side="left", padx=5)
    ctk.CTkButton(buttons_frame, width=15, height=15, corner_radius=8,
                  fg_color="#00CA4E", hover_color="#00e66e", command=maximize, text="").pack(side="left", padx=5)

    # --- Content: logo + login form ---
    content = ctk.CTkFrame(login, fg_color="#d9d9d9", border_width=0)
    content.pack(expand=True, fill="both")

    # Logo
    logo_image = ctk.CTkImage(light_image=Image.open("assets/login.png"), size=(200,200))
    ctk.CTkLabel(content, image=logo_image, text="", fg_color="#d9d9d9").pack(pady=30)

    # Login form
    form_frame = ctk.CTkFrame(content, fg_color="#d9d9d9", border_width=0)
    form_frame.pack(pady=20)

    ctk.CTkLabel(form_frame, text="Username", fg_color="#d9d9d9").pack(pady=5)
    username_entry = ctk.CTkEntry(form_frame, width=300)
    username_entry.pack(pady=5)

    ctk.CTkLabel(form_frame, text="Password", fg_color="#d9d9d9").pack(pady=5)
    password_entry = ctk.CTkEntry(form_frame, show="*", width=300)
    password_entry.pack(pady=5)

    ctk.CTkButton(form_frame, text="Login", width=300).pack(pady=20)

    if root is None:
        login.mainloop()

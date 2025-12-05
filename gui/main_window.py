import customtkinter as ctk

def launch_main_app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("FindMe")

    # --- Match the size of the intro video ---
    width = 1280
    height = 720

    # Get screen size to center the window
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate x and y coordinates to center
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set geometry
    app.geometry(f"{width}x{height}+{x}+{y}")

    # Example content
    label = ctk.CTkLabel(app, text="Welcome to FindMe", font=ctk.CTkFont(size=24, weight="bold"))
    label.pack(pady=50)

    app.mainloop()

if __name__ == "__main__":
    launch_main_app()

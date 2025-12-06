import tkinter as tk
from tkvideo import tkvideo
import sys
import os

# Ensure Python can find the gui folder
sys.path.append(os.path.join(os.path.dirname(__file__), 'gui'))

# Now import the function we created in Step 1
from gui.login import launch_login_page

VIDEO_PATH = "assets/intro.mp4"
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720
VIDEO_DURATION_MS = 5000  # 5 seconds

def show_splash_then_login():
    root = tk.Tk()
    root.overrideredirect(True)  # remove title bar
    root.attributes("-topmost", True)

    # Center splash window
    x = (root.winfo_screenwidth() - VIDEO_WIDTH) // 2
    y = (root.winfo_screenheight() - VIDEO_HEIGHT) // 2
    root.geometry(f"{VIDEO_WIDTH}x{VIDEO_HEIGHT}+{x}+{y}")

    splash_label = tk.Label(root)
    splash_label.pack(expand=True, fill="both")

    # Make window modal / freeze user input
    root.grab_set()
    root.focus_force()

    # Play video once
    # Note: Ensure assets/intro.mp4 actually exists!
    player = tkvideo(VIDEO_PATH, splash_label, loop=0, size=(VIDEO_WIDTH, VIDEO_HEIGHT))
    player.play()

    # Switch to login after video
    def switch_to_login():
        root.grab_release()  # release modal grab
        root.destroy()       # Close the splash screen
        launch_login_page()  # Open the login screen

    root.after(VIDEO_DURATION_MS, switch_to_login)
    root.mainloop()

if __name__ == "__main__":
    show_splash_then_login()
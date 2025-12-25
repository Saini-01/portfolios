import tkinter as tk

root = tk.Tk()
root.title("Asset Tracker")
root.geometry("525x325")
root.configure(bg="#2b2b2b")

label = tk.Label(
    root,
    text="Hello, Tkinter!\nThis is a test",
    fg="white",
    bg="#2b2b2b"
)

label.pack(padx=20, pady=20)

root.mainloop()
import tkinter as tk
import main
import time

root = tk.Tk()
root.title("Asset Tracker")
root.geometry("525x325")
root.configure(bg="#2b2b2b")

kalshi_values = main.values()

label = tk.Label(
    root,
    text="",
    fg="white",
    bg="#2b2b2b"
)
label.pack(anchor='nw', padx=20, pady=10)

button_frame = tk.Frame(root, bg="#2b2b2b")
button_frame.pack(anchor='nw', padx=20)

kalshi_label = tk.Label(
    root,
    text="",
    fg="white",
    bg="#2b2b2b",
    justify="left"
)

kalshi_label.pack(anchor='nw', padx = 20, pady = 5)

def kalshi_button_clicked():
    template = template = f"Cash: ${kalshi_values['cash']}\nInvested: ${kalshi_values['invested']}\nTransferred: ${kalshi_values['transferred']}"
    kalshi_label.config(text=template)

def coinbase_button_clicked():
    print("Coinbase was clicked")

kalshi_button = tk.Button(button_frame, text="Kalshi", command=kalshi_button_clicked)
kalshi_button.pack(side=tk.LEFT, anchor='nw')

coinbase_button = tk.Button(button_frame, text="Coinbase", command=coinbase_button_clicked)
coinbase_button.pack(side=tk.LEFT, anchor='nw', padx = 5)

def updateWelcome():
    now = time.localtime()
    hour = now.tm_hour
    current = ""
    if 0 <= hour < 12:
        current = "morning"
    elif 12 <= hour < 17:
        current = "afternoon"
    else:
        current = "evening"
    label.config(text="Good " + current + "!")
    root.after(1000, updateWelcome)

root.after(0, updateWelcome)
root.mainloop()
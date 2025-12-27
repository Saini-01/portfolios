import tkinter as tk
import main
import time

root = tk.Tk()
root.title("Asset Tracker")
root.geometry("525x325")
root.configure(bg="#2b2b2b")
root.resizable(False, False)

label = tk.Label(
    root,
    text="",
    fg="white",
    bg="#2b2b2b",
    font=('Courier', 15)
)
label.pack(anchor='nw', padx=20, pady=10)

button_frame = tk.Frame(root, bg="#2b2b2b")
button_frame.pack(anchor='nw', padx=20)

info_frame = tk.Frame(root, bg="#2b2b2b")
info_frame.pack(anchor='nw', padx=20, pady=0)

kalshi_label = tk.Label(
    info_frame, 
    text="",
    fg="white",
    bg="#2b2b2b",
    justify="left",
    font=('Courier', 11)
)

kalshi_logo = tk.Label(
    root,  
    text="",
    fg="#4DE4B2",
    bg="#2b2b2b",
    justify="right",
    font=('Courier', 11)
)

kalshi_label.pack(side=tk.LEFT, padx=0, pady=0)
kalshi_logo.place(x=300, y=35)

def kalshi_button_clicked():
    if main.values()['transferred'] > (main.values()['cash'] + main.values()['invested']):
        signToUse = "-"
    else:
        signToUse = "+"
    updown = main.values()['transferred'] - (main.values()['cash'] + main.values()['invested'])
    template = f"Cash: ${main.values()['cash']}\nInvested: ${main.values()['invested']}\nTransferred: ${main.values()['transferred']}\n\nTotal Change: {signToUse}${updown:.2f}"
    kalshi_label.config(text=template)
    kalshi_logo.config(text="""██╗  ██╗
██║ ██╔╝
█████╔╝ 
██╔═██╗ 
██║  ██╗
╚═╝  ╚═╝""")
    root.after(0, update_kalshi_data)

def coinbase_button_clicked():
    print("Coinbase was clicked")

kalshi_button = tk.Button(
    button_frame, 
    text="Kalshi", 
    command=kalshi_button_clicked,
    font=('Courier', 10)
)
kalshi_button.pack(side=tk.LEFT, anchor='nw')

coinbase_button = tk.Button(
    button_frame, 
    text="Coinbase", 
    command=coinbase_button_clicked,
    font=('Courier', 10)
)
coinbase_button.pack(side=tk.LEFT, anchor='nw', padx=5)

def updateWelcome():
    now = time.localtime()
    hour = now.tm_hour
    current = ""
    if 0 <= hour < 12:
        current = "Morning"
    elif 12 <= hour < 17:
        current = "Afternoon"
    else:
        current = "Evening"
    label.config(text="Good " + current + "!")
    root.after(1000, updateWelcome)

def update_kalshi_data():
    data = main.values()
    if main.values()['transferred'] > (main.values()['cash'] + main.values()['invested']):
        signToUse = "-"
    else:
        signToUse = "+"
    updown = main.values()['transferred'] - (main.values()['cash'] + main.values()['invested'])
    template = f"Cash: ${data['cash']}\nInvested: ${data['invested']}\nTransferred: ${data['transferred']}\n\nTotal Change: {signToUse}${updown:.2f}"
    kalshi_label.config(text=template)
    root.after(5000, update_kalshi_data)

root.after(0, updateWelcome)
root.mainloop()
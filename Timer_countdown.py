import time
import tkinter as tk
from datetime import datetime
from win10toast import ToastNotifier
import winsound

# Create window
window = tk.Tk()
window.geometry('600x600')
window.title('Countdown Timer')

head = tk.Label(window, text="Countdown Clock and Timer", font=('Calibri', 15))
head.pack(pady=20)

# Variables
hours = tk.StringVar()
minutes = tk.StringVar()
seconds = tk.StringVar()
check_music = tk.BooleanVar()

# Inputs
tk.Label(window, text="Enter time in HH:MM:SS", font=('bold')).pack()
tk.Entry(window, textvariable=hours, width=10).pack()
tk.Entry(window, textvariable=minutes, width=10).pack()
tk.Entry(window, textvariable=seconds, width=10).pack()

tk.Checkbutton(text='Check for Music', onvalue=True, offvalue=False, variable=check_music).pack()

# Current time display
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
tk.Label(window, text=current_time).pack()

# Countdown label
countdown_label = tk.Label(window, text="", font=('bold', 20))
countdown_label.pack(pady=20)

# Countdown logic
def start_countdown():
    try:
        total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except ValueError:
        countdown_label.config(text="Invalid input!")
        return
    update_timer(total_seconds)

def update_timer(t):
    if t >= 0:
        mins, secs = divmod(t, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        countdown_label.config(text=time_str)
        window.after(1000, update_timer, t - 1)
    else:
        countdown_label.config(text="Time-Up")
        ToastNotifier().show_toast("Notification", "Timer is Off", duration=5)
        if check_music.get():
            winsound.Beep(440, 1000)

# Button
tk.Button(window, text="Set Countdown", command=start_countdown, bg='yellow').place(x=260, y=230)

window.mainloop()

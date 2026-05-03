import tkinter as tk
from time import strftime
import datetime
import threading
import time

# ----------- MAIN WINDOW -----------
root = tk.Tk()
root.title("Advanced Digital Clock")
root.geometry("600x300")
root.configure(bg="black")

# ----------- ALARM VARIABLES -----------
alarm_time = ""
alarm_running = False

# ----------- TIME FUNCTION -----------
def update_time():
    now = datetime.datetime.now()

    current_time = now.strftime('%I:%M:%S %p')
    current_date = now.strftime('%d/%m/%Y')
    current_day = now.strftime('%A')

    display = f"{current_time}\n{current_day}, {current_date}"

    label.config(text=display)

    check_alarm(current_time)

    label.after(1000, update_time)

# ----------- NEON EFFECT -----------
def neon_effect():
    colors = ["#00FFFF", "#00FFAA", "#00FF00", "#00FFAA"]
    for color in colors:
        label.config(fg=color)
        root.update()
        time.sleep(0.1)

# ----------- ALARM CHECK -----------
def check_alarm(current_time):
    global alarm_time, alarm_running
    if alarm_time == current_time and not alarm_running:
        alarm_running = True
        threading.Thread(target=trigger_alarm).start()

# ----------- ALARM FUNCTION -----------
def trigger_alarm():
    for _ in range(10):
        neon_effect()
        print("ALARM! Wake up!")
        time.sleep(1)
    stop_alarm()

def set_alarm():
    global alarm_time
    alarm_time = entry.get()
    status_label.config(text=f"Alarm set for: {alarm_time}")

def stop_alarm():
    global alarm_running
    alarm_running = False
    status_label.config(text="Alarm stopped")

# ----------- UI ELEMENTS -----------

label = tk.Label(
    root,
    font=("Calibri", 40, "bold"),
    bg="black",
    fg="#00FFFF",
    justify="center"
)
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)
entry.insert(0, "HH:MM:SS AM/PM")

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=5)

set_btn = tk.Button(btn_frame, text="Set Alarm", command=set_alarm, bg="#222", fg="white")
set_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop Alarm", command=stop_alarm, bg="#222", fg="white")
stop_btn.grid(row=0, column=1, padx=5)

status_label = tk.Label(root, text="", bg="black", fg="white", font=("Arial", 12))
status_label.pack()

update_time()

root.mainloop()

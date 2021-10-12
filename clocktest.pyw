import tkinter as tk
import subprocess as sp
import time


root = tk.Tk()
screenwidth = root.winfo_screenwidth()
rightside = str(screenwidth*2-250)
root.overrideredirect(True)
root.attributes("-transparentcolor", "black")
root.geometry("+{}+0".format(rightside))
root.config(background="black")
root.attributes("-topmost", True)
root.attributes("-alpha", 0.5)
clock = tk.Label()
clock.configure(font=("Arial", 64, "bold"))
clock.configure(bg="black", fg="white", pady=20)

while True:
    timenow = sp.Popen("time /t", stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    clock.configure(text="{}".format(timenow.stdout.read().decode("utf-8")))
    clock.pack()
    clock.update()
    time.sleep(0.01)

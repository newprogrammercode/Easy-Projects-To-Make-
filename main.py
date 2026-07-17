
import time
from tkinter import *


class Main:

    def stars_time(self):
        self.time += 1
        self.label.configure(text=self.time)
        self.timer_id = self.root.after(1000, self.stars_time)

    def reset_time(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        self.time = 0
        self.label.configure(text=self.time)

    def __init__(self):
        self.root = Tk()
        self.root.title("Timer")
        self.root.geometry("300x150")
        self.time = 0
        self.timer_id = None

        self.label = Label(
            self.root, text=0, font=("Courier", 20, "bold"), fg="black"
        )
        self.root.config(bg="white")

        self.start = Button(
            self.root,
            text="Start",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            bd=0,
            command=self.stars_time,
        )
        self.reset = Button(
            self.root,
            text="Reset",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            bd=0,
            command=self.reset_time,
        )

        self.label.pack(fill="both", expand=True)
        self.start.pack(fill="both")
        self.reset.pack(fill="both")

    def run(self):
        self.root.mainloop()


m = Main()
m.run()

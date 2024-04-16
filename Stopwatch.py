import tkinter as tk
from datetime import timedelta
import time


class Stopwatch:
    def __init__(self, _root):
        self.root = _root
        self.root.title("Stopwatch")
        self.root.minsize(width=350, height=70)

        self.label = tk.Label(
            self.root, text="0:00:00.000", fg="black", font="Verdana 30 bold"
        )
        self.label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(anchor="center", pady=5)

        self.start_button = tk.Button(
            self.frame, text="Start", width=6, command=self.start_timer
        )
        self.stop_button = tk.Button(
            self.frame, text="Stop", width=6, state="disabled", command=self.stop_timer
        )
        self.reset_button = tk.Button(
            self.frame,
            text="Reset",
            width=6,
            state="disabled",
            command=self.reset_timer,
        )

        self.start_button.pack(side="left")
        self.stop_button.pack(side="left")
        self.reset_button.pack(side="left")

        self.running = False
        self.start_time = 0
        self.elapsed_time = timedelta(seconds=0)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.monotonic() - self.elapsed_time.total_seconds()
            self.update_timer()
            self.set_button_states()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.set_button_states()

    def reset_timer(self):
        if not self.running:
            self.elapsed_time = timedelta(seconds=0)
            self.update_label("0:00:00.000")
            self.set_button_states()

    def update_timer(self):
        if self.running:
            self.elapsed_time = timedelta(seconds=time.monotonic() - self.start_time)
            self.update_label(str(self.elapsed_time)[:-3])
            self.root.after(10, self.update_timer)

    def update_label(self, text):
        self.label["text"] = text

    def set_button_states(self):
        self.start_button["state"] = "disabled" if self.running else "normal"
        self.stop_button["state"] = "disabled" if not self.running else "normal"
        self.reset_button["state"] = "disabled" if self.running else "normal"


if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
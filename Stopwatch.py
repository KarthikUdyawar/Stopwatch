"""
A simple stopwatch application using Tkinter.

This application displays a stopwatch with start, stop, and reset buttons.
"""

import time
import tkinter as tk
from datetime import timedelta
from tkinter import Tk


class Stopwatch:
    """
    A simple stopwatch class.

    This class creates a stopwatch GUI with start, stop, and reset buttons.
    """

    def __init__(self, _root: Tk):
        """Initialize the Stopwatch class.

        Args:
            root (Tk): The Tkinter root window.
        """
        self.root = _root
        self.root.title("Stopwatch")
        self.root.minsize(width=350, height=70)
        self.root.iconbitmap("./img/stopwatch.ico")

        self.ui_elements: dict = {}
        self.ui_elements["label"] = tk.Label(
            self.root, text="0:00:00.000", fg="black", font="Verdana 30 bold"
        )
        self.ui_elements["label"].pack()

        self.ui_elements["frame"] = tk.Frame(self.root)
        self.ui_elements["frame"].pack(anchor="center", pady=5)

        self.ui_elements["start_button"] = tk.Button(
            self.ui_elements["frame"], text="Start", width=6, command=self.start_timer
        )
        self.ui_elements["start_button"].pack(side="left")

        self.ui_elements["stop_button"] = tk.Button(
            self.ui_elements["frame"],
            text="Stop",
            width=6,
            state="disabled",
            command=self.stop_timer,
        )
        self.ui_elements["stop_button"].pack(side="left")

        self.ui_elements["reset_button"] = tk.Button(
            self.ui_elements["frame"],
            text="Reset",
            width=6,
            state="disabled",
            command=self.reset_timer,
        )
        self.ui_elements["reset_button"].pack(side="left")

        self.running: bool = False
        self.start_time: float = 0
        self.elapsed_time: timedelta = timedelta(seconds=0)

    def start_timer(self):
        """Start the stopwatch."""
        if not self.running:
            self.running = True
            self.start_time = time.monotonic() - self.elapsed_time.total_seconds()
            self.update_timer()
            self.set_button_states()

    def stop_timer(self):
        """Stop the stopwatch."""
        if self.running:
            self.running = False
            self.set_button_states()

    def reset_timer(self):
        """Reset the stopwatch."""
        if not self.running:
            self.elapsed_time = timedelta(seconds=0)
            self.update_label("0:00:00.000")
            self.set_button_states()

    def update_timer(self):
        """Update the stopwatch timer."""
        if self.running:
            self.elapsed_time = timedelta(seconds=time.monotonic() - self.start_time)
            self.update_label(str(self.elapsed_time)[:-3])
            self.root.after(10, self.update_timer)

    def update_label(self, text: str):
        """Update the stopwatch label text.

        Args:
            text (str): The new text for the label.
        """
        self.ui_elements["label"]["text"] = text

    def set_button_states(self):
        """Set the state of the stopwatch buttons based on the stopwatch state."""
        state = "disabled" if self.running else "normal"
        self.ui_elements["start_button"]["state"] = state
        self.ui_elements["stop_button"]["state"] = (
            "disabled" if not self.running else "normal"
        )
        self.ui_elements["reset_button"]["state"] = state


if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()

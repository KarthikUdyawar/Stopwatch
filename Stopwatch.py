# Import
from tkinter import Frame, Button, Tk, Label
from datetime import datetime

# Variables
counter = 66600
running = False

# Main function
def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S.%f")[:-3]
                display = string

            label['text'] = display
            label.after(1,count)
            counter += 0.001

    count()

# Start function
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

# Stop function
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False

# Reset function
def Reset(label):
    global counter
    counter = 66600
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'

# GUI
root = Tk()
root.title("Stopwatch")
root.minsize(width=350,height=70)
label = Label(root, text="Welcome!",fg='black',font="Verdana 30 bold")
label.pack()
f = Frame(root)
start = Button(f,text='Start',width=6,command=lambda:Start(label))
stop = Button(f,text='Stop',width=6,state='disabled',command=Stop)
reset = Button(f,text='Reset',width=6,state='disabled',command=lambda:Reset(label))
f.pack(anchor='center',pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()

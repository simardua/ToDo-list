import tkinter
import threading
from tkinter import messagebox
import sys
import datetime

tasks = []
ok_thread = True


def getting_tasks(event=""):
    work = todo.get()
    day = int(date_d.get())
    month = int(date_m.get())
    hour = int(time_hrs.get())
    min = int(time_min.get())
    # if month==1:
    #     day==31
    # elif month==2:
    #     day==28 or 29
    if day>31 or month>12 or hour>24 or min>59:
        messagebox.showinfo("ERROR", "Invalid Input")
    else:
        now = datetime.datetime.now()
        day_sec = (day - now.day) * 86400
        month_sec = (month - now.month) * 2628288
        hour_sec = (hour - now.hour) * 3600
        min_sec = (min - now.minute) * 60
        total_time = day_sec + month_sec + hour_sec + min_sec - now.second
        if total_time <= -1:
            tkinter.messagebox.showinfo("ERROR","Time cannot be of Past")
        todo.delete(0, tkinter.END)
        date_m.delete(0, tkinter.END)
        date_d.delete(0, tkinter.END)
        time_hrs.delete(0, tkinter.END)
        time_min.delete(0, tkinter.END)
        todo.focus_set()
        if total_time > -1:
            adding_record(work, total_time)
        if 0 < total_time < 99999:
            updating_record()


def adding_record(work, time):
    tasks.append([work, time])
    clock = threading.Timer(time, notification, [work])
    clock.start()


def updating_record():
    if WorkingList.size() > 0:
        WorkingList.delete(0, "end")
    for task in tasks:
        WorkingList.insert("end", "" + task[0] + "=======>>> Time left: " + str(task[1]) + " seconds")


def notification(task):
    tkinter.messagebox.showinfo("Notification", "Its Now the Time for : " + task)


def actual_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, actual_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    updating_record()


# gui application
root = tkinter.Tk()
root.geometry("643x480")
root.title("ToDo List Reminder")
root.rowconfigure(0, weight=1)
root.config(bg="#304aa1")
root.resizable(False, False)

frame = tkinter.Frame(root)
frame.pack()

# widgets
lbl = tkinter.Label(root, text="Enter Tasks To Do:", fg="white", bg="grey", font=('Arial', 14), wraplength=0)
date = tkinter.Label(root, text="Date(dd-mm):", fg="white", bg="grey", font=('Arial', 14), wraplength=150)
date_m = tkinter.Entry(root, width=15, font=('Arial', 14))
date_d = tkinter.Entry(root, width=15, font=('Arial', 14))
lbl_time = tkinter.Label(root, text="Enter Time(hh:mm):", fg="white", bg="grey", font=('Arial', 14), wraplength=200)
todo = tkinter.Entry(root, width=30, font=('Arial', 14))
time_hrs = tkinter.Entry(root, width=15, font=('Arial', 14))
time_min = tkinter.Entry(root, width=15, font=('Arial', 14))
post = tkinter.Button(root, text='Add task', fg="white", bg='green', font=('Arial', 16), relief="ridge", bd=5, height=3, width=30, command=getting_tasks)
Exit = tkinter.Button(root, text='Exit', fg="white", bg='red', height=3, font=('Arial Bold', 14), relief="ridge", bd=5, width=30, command=root.destroy)
WorkingList = tkinter.Listbox(root,bg="black", font=('Arial', 18), fg="white")
if tasks != "":
    actual_time()


# binding
root.bind('<Return>', getting_tasks)

# widgets placement
lbl.place(x=0, y=10, width=200, height=25)
date.place(x=230, y=10, width=200, height=25)
date_m.place(x=330, y=40, width=50, height=25)
date_d.place(x=270, y=40, width=50, height=25)
lbl_time.place(x=460, y=10, width=200, height=25)
todo.place(x=20, y=40, width=160, height=25)
time_hrs.place(x=505, y=40, width=40, height=25)
time_min.place(x=555, y=40, width=40, height=25)
post.place(x=62, y=80, width=100, height=25)
Exit.place(x=520, y=80, width=50, height=25)
WorkingList.place(x=20, y=120, width=585, height=300)

root.mainloop()
ok_thread = False
sys.exit("FINISHED")
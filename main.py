import tkinter as tk
import time


def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def remove_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        tasks_listbox.delete(selected_task)


def start_timer():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        task_name = tasks_listbox.get(selected_task)
        timer_label.config(text=f"Timer for '{task_name}':")
        start_time = time.time()
        update_timer(start_time)
        timer_label.pack()  # Show the timer label
        timer_display.pack()  # Show the timer display
    else:
        timer_label.pack_forget()  # Hide the timer label
        timer_display.pack_forget()  # Hide the timer display


def update_timer(start_time):
    elapsed_time = time.time() - start_time
    timer_var.set(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    root.after(1000, lambda: update_timer(start_time))


root = tk.Tk()
root.title("To-Do List with Timer")
root.configure(bg="pink")  # Set background color to pink

root.geometry("400x400")  # Adjusted root window size

tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
tasks_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

task_entry = tk.Entry(root)
task_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

timer_label = tk.Label(root, text="Timer:")
timer_var = tk.StringVar()
timer_display = tk.Label(root, textvariable=timer_var, font=("Helvetica", 20))

root.mainloop()

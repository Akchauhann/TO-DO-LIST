import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("To-Do List Application")

# Task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=13)

# Buttons frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=13)

add_task_button = tk.Button(buttons_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=10)

delete_task_button = tk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)

clear_tasks_button = tk.Button(buttons_frame, text="Clear All Tasks", command=clear_tasks)
clear_tasks_button.pack(side=tk.LEFT, padx=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=60, height=15)
tasks_listbox.pack(pady=20)

root.mainloop()
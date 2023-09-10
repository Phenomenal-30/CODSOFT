from tkinter import *
import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def update_task():
    selected_task_index = tasks_listbox.curselection()
    updated_task = task_entry.get()
    if selected_task_index and updated_task:
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, updated_task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task and enter an updated task.")


root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

add_button.pack()
update_button.pack()
remove_button.pack()

tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
tasks_listbox.pack(pady=10)

root.mainloop()

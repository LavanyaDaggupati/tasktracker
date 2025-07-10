import tkinter as tk
from tkinter import messagebox

class TaskTrackr:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskTrackr - To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.tasks = []

        self.title_label = tk.Label(root, text="📝 TaskTrackr", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=22)
        self.task_entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_btn.pack(pady=5)

        self.task_frame = tk.Frame(root, bg="#f0f0f0")
        self.task_frame.pack(pady=10)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return
        task_var = tk.StringVar(value=task_text)
        task_check = tk.Checkbutton(self.task_frame, textvariable=task_var, font=("Helvetica", 12), bg="#f0f0f0", anchor="w")
        task_check.pack(fill='x', padx=10, pady=2)
        self.tasks.append((task_var, task_check))
        self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTrackr(root)
    root.mainloop()
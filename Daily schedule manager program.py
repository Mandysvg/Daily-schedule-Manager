import tkinter as tk
from tkinter import messagebox, ttk

# Dictionary to store schedules with the time as key and activity as value
tasks = {
    "08:00": "Wake up",
    "09:00": "Eat breakfast", 
    "10:00": "Go to the pool",
    "11:00": "Go to the store"
}

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Schedule Manager")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Title Label
        title_label = tk.Label(
            root, 
            text="Welcome to Your Daily Schedule",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Frame for schedule display
        schedule_frame = tk.LabelFrame(
            root,
            text="Current Schedule",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        schedule_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Treeview for displaying schedule
        self.schedule_tree = ttk.Treeview(
            schedule_frame,
            columns=("Time", "Task"),
            show="headings",
            height=10
        )
        self.schedule_tree.heading("Time", text="Time")
        self.schedule_tree.heading("Task", text="Task")
        self.schedule_tree.column("Time", width=100)
        self.schedule_tree.column("Task", width=400)
        self.schedule_tree.pack(fill="both", expand=True)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(schedule_frame, orient="vertical", command=self.schedule_tree.yview)
        self.schedule_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        # Frame for adding new tasks
        add_frame = tk.LabelFrame(
            root,
            text="Add New Task",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        add_frame.pack(padx=20, pady=10, fill="x")
        
        # Time input
        tk.Label(add_frame, text="Time (HH:MM):", bg="#ffffff", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.time_entry = tk.Entry(add_frame, font=("Arial", 10), width=15)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Task input
        tk.Label(add_frame, text="Task:", bg="#ffffff", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.task_entry = tk.Entry(add_frame, font=("Arial", 10), width=40)
        self.task_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Button frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        # Add Task Button
        add_button = tk.Button(
            button_frame,
            text="Add Task",
            command=self.add_task,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=5,
            cursor="hand2"
        )
        add_button.grid(row=0, column=0, padx=10)
        
        # Remove Task Button
        remove_button = tk.Button(
            button_frame,
            text="Remove Selected",
            command=self.remove_task,
            bg="#f44336",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=5,
            cursor="hand2"
        )
        remove_button.grid(row=0, column=1, padx=10)
        
        # Refresh Schedule Button
        refresh_button = tk.Button(
            button_frame,
            text="Refresh Schedule",
            command=self.display_schedule,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=5,
            cursor="hand2"
        )
        refresh_button.grid(row=0, column=2, padx=10)
        
        # Display initial schedule
        self.display_schedule()
    
    def display_schedule(self):
        """Display the current schedule in the treeview"""
        # Clear existing items
        for item in self.schedule_tree.get_children():
            self.schedule_tree.delete(item)
        
        # Sort tasks by time and display
        sorted_tasks = sorted(tasks.items())
        for time, task in sorted_tasks:
            self.schedule_tree.insert("", "end", values=(time, task))
    
    def add_task(self):
        """Add a new task to the schedule"""
        time = self.time_entry.get().strip()
        task = self.task_entry.get().strip()
        
        # Validate inputs
        if not time or not task:
            messagebox.showwarning("Input Error", "Please enter both time and task!")
            return
        
        # Add to dictionary
        tasks[time] = task
        
        # Clear entry fields
        self.time_entry.delete(0, tk.END)
        self.task_entry.delete(0, tk.END)
        
        # Refresh display
        self.display_schedule()
        
        messagebox.showinfo("Success", f"Task '{task}' added at {time}!")
    
    def remove_task(self):
        """Remove selected task from the schedule"""
        selected_item = self.schedule_tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a task to remove!")
            return
        
        # Get the time value from selected item
        item_values = self.schedule_tree.item(selected_item[0])['values']
        time = item_values[0]
        
        # Remove from dictionary
        if time in tasks:
            task_name = tasks[time]
            del tasks[time]
            self.display_schedule()
            messagebox.showinfo("Success", f"Task '{task_name}' at {time} removed!")
        else:
            messagebox.showerror("Error", "Task not found!")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
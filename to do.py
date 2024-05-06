import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog 
class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_list_frame = tk.Frame(master)
        self.task_list_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.populate_task_list()

    def populate_task_list(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            task_label = tk.Label(self.task_list_frame, text=task["description"])
            task_label.grid(row=i, column=0, sticky="w", padx=5)

            
            delete_button = tk.Button(self.task_list_frame, text="Delete", command=lambda index=i: self.delete_task(index))
            delete_button.grid(row=i, column=2, padx=5)

            update_button = tk.Button(self.task_list_frame, text="Update", command=lambda index=i: self.update_task(index))
            update_button.grid(row=i, column=3, padx=5)

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.tasks.append({"description": description, "completed": False})
            self.populate_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

  

    def delete_task(self, index):
        del self.tasks[index]
        self.populate_task_list()

    def update_task(self, index):
        description = self.tasks[index]["description"]
        updated_description = simpledialog.askstring("Update Task", f"Update task '{description}' to:")
        if updated_description:
            self.tasks[index]["description"] = updated_description
            self.populate_task_list()
def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

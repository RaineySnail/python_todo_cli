import json
import os

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
        
    def mark_done(self):
        self.completed = True
        
    def to_dict(self):
        return{"title": self.title, "completed": self.completed}
    

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        
    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Добавлено: {title}")
        
    def show_tasks(self):
        if not self.tasks:
            print("\n Задач нет!")
            return
        
        print("\n ---To-Do List---")
        for i, task in enumerate(self.tasks, start=1):
            status = "[x]" if task.completed else "[ ]"
            print(f"{i}. {status} {task.title}")
            
    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.mark_done()
            self.save_tasks()
            print(f"Выполнено: {task.title}")
        else:
            print("Неверный номер задачи!")
            
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Удалено: {removed.title}")
        else:
            print("Неверный номер задачи!")
            
    def save_tasks(self):
        data = []
        for task in self.tasks:
            data.append(task.to_dict())
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
            
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    task = Task(item["title"], item["completed"])
                    self.tasks.append(task)
                    
def main():
    todo_list = TodoList()
    
    while True:
        print("\n [1] Просмотреть  [2] Добавить  [3] Выполнено  [4] Удалить  [5] Выйти")
        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            title = input("Введите название задачи: ").strip()
            if title:
                todo_list.add_task(title)
        elif choice == "3":
            todo_list.show_tasks()
            number = int(input("Введите номер задачи: "))
            todo_list.complete_task(number)
        elif choice == "4":
            todo_list.show_tasks()
            number = int(input("Введите номер задачи: "))
            todo_list.delete_task(number)
        elif choice == "5":
            print("Пака пака!")
            break
        else:
            print('Неверное действие!')
            
if __name__ == "__main__":
    main()
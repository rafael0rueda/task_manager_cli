import os
import json
from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def add_task(file_path, new_task):
    # Load existing data
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    tasks = json.load(file)
                except json.JSONDecodeError:
                    tasks = {}
        else:
            tasks = {}
        
        # Create new id
        new_id = len(tasks) + 1
        new_task_id = f"task{new_id}"

        # Create new tasks
        data = {
            "id": new_id,
            "task": new_task["task"],
            "due": new_task["due"],
            "priority":new_task["priority"],
            "complete": new_task["complete"]
        }
         
        tasks[new_task_id] = data

        # Save all task back to the file
        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)
        console.print(f"{new_task_id} add to the list ✅", style="green")  


def list_tasks(file_path):
     with open(file_path, "r") as file:
          data = json.load(file)
     
     table = Table(title="🌟 Task Manager", box=box.SIMPLE_HEAD, border_style="bright_blue")
     table.add_column("Id", style="cyan", justify="center", header_style="bold cyan")
     table.add_column("Task", style="magenta", header_style="bold magenta")
     table.add_column("Date", style="green", header_style="bold green")
     table.add_column("Priority", style="purple", header_style="bold purple")
     table.add_column("Complete", style="Orange1", header_style="bold Orange1")

     for task, task_info in data.items():
          # print(task)       
          table.add_row(f"{task_info["id"]}", task_info["task"], task_info["due"], task_info["priority"], f"{task_info["complete"]}")
     console.print(table)
        
def done_task(file_path, task_id):
    task_id = f"task{task_id}"

    if os.path.exists(file_path): 
         with open(file_path, "r") as file:
               try:
                    tasks = json.load(file)
               except json.JSONDecodeError:
                    tasks = {}
    else:
         tasks = {}
    tasks[task_id]['complete'] = True
    print(tasks[task_id])

    with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)

def delete_task(file_path, task_id):
    task_id = f"task{task_id}"

    if os.path.exists(file_path): 
         with open(file_path, "r") as file:
               try:
                    tasks = json.load(file)
               except json.JSONDecodeError:
                    tasks = {}
    else:
         tasks = {}
    
    del tasks[task_id]
    console.print(f"{task_id} deleted ❌", style="red")

    with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)
    

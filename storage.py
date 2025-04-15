import os
import json

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
            "complete": new_task["done"]
        }
         
        tasks[new_task_id] = data

        # Save all task back to the file
        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)


def list_tasks(file_path):
     with open(file_path, "r") as file:
          data = json.load(file)
    
     for task, task_info in data.items():
          print(task)
          for k, v in task_info.items():
               print(f"{k}: {v}")
        
def task_done(file_path, task_id):
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
    

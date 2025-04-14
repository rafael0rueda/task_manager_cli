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
            "done": False
        }
         
        tasks[new_task_id] = data

        # Save all task back to the file
        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)
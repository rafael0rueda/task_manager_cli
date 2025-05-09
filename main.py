from datetime import datetime
from argparse import ArgumentParser, Namespace, ArgumentTypeError
from storage import add_task, list_tasks, done_task, delete_task

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ArgumentTypeError(f"Ivalid date: {date_str}. Use format YYYY-MM-DD.")

parser = ArgumentParser(description="Task Manager CLI")

# Create new tasks
parser.usage = '--add "{task}" --due {date} --priority {low | normal | high}'

add_group = parser.add_argument_group('Add Task Options')
add_group.add_argument('--add', type=str, help='Task description in quotes')
add_group.add_argument('--due', type=validate_date, help='Due date (e.g., 2025-04-15)')
add_group.add_argument('--priority', type=str, choices=['low', 'normal', 'high'], help='Priority: low, normal, or high')

# List tasks
parser.add_argument('--list', action='store_true', help='List the task')

# Change the list to complete
parser.add_argument('--complete',type=int, help='Change the state to complete, --complete {id task}')

# Delete task from the list
parser.add_argument('--delete', type=int, help='Delete Task from the list, --delete {id task}')

args: Namespace = parser.parse_args()
file_path = "tasks.json"

# add a new task require due and priority flags
if args.add:
    if not args.due or not args.priority:
        parser.error("--due and --priority are required when using --add")
    else:
          task ={
                "id": 0,
                "task": args.add,
                "due": args.due.strftime("%Y-%m-%d"),
                "priority": args.priority.capitalize(),
                "complete": False
            }
          add_task(file_path, task)

if args.list:
    list_tasks(file_path)

if args.complete:
    done_task(file_path, args.complete)

if args.delete:
    delete_task(file_path, args.delete)


from datetime import datetime
from argparse import ArgumentParser, Namespace, ArgumentTypeError
from storage import add_task, list_tasks

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ArgumentTypeError(f"Ivalid date: {date_str}. Use format YYYY-MM-DD.")

parser = ArgumentParser(description="Task Manager CLI")

# Create new tasks
parser.usage = '--add "{task}" --due {date} --priority {low | normal | high}'

parser.add_argument('--add', type=str, help='Task description in quotes')
parser.add_argument('--due', type=validate_date, help='Due date (e.g., 2025-04-15)')
parser.add_argument('--priority', type=str, choices=['low', 'normal', 'high'], help='Priority: low, normal, or high')

# List tasks
parser.add_argument('--list', action='store_true')

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
                "priority": args.priority,
                "done": False
            }
          add_task(file_path, task)

if args.list:
    list_tasks(file_path)

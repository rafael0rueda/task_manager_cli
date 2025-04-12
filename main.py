from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.usage = '--add "{task}" --due {date} --priority {low | normal | high}'

parser.add_argument('task', type=str, help='The task')
parser.add_argument('date', type=int, help='The due date of the task')
parser.add_argument('priority', type=str, help='Priority of the task')
parser.add_argument('-a','--add', help='Add new task', action="store_true")
parser.add_argument('-l','--list', help='Show all task', action="store_true")
parser.add_argument('-d','--done', help='Mark task as completed', action="store_true")

args: Namespace = parser.parse_args()

print(f"{args.task} due {args.date} with {args.priority}")

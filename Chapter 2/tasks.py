from argparse import ArgumentParser
from add_task import add
from list_tasks import list
from update_task import update
from remove_task import remove

parser = ArgumentParser()
parser.add_argument('function', nargs='?', choices=['add', 'list', 'update', 'remove'], default='list')
args, sub_args = parser.parse_known_args()

if args.function == 'add':
    parser.add_argument('--name', metavar='', required=True, help='Name of the task')
    parser.add_argument('--deadline', metavar='', required=True, help='Deadline for the task')
    parser.add_argument('--description', metavar='', required=True, help='Description of the task')
    args = parser.parse_args(sub_args)
    add(args.name, args.deadline, args.description)

elif args.function == 'list':
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--all', action='store_true', help='Print all tasks')
    group.add_argument('--today', action='store_true', help='Print tasks for today')
    args = parser.parse_args(sub_args)
    list(all=args.all, today=args.today)

elif args.function == 'update':
    parser.add_argument('--name', metavar='', required=False, help='Name of the task')
    parser.add_argument('--deadline', metavar='', required=False, help='Deadline for the task')
    parser.add_argument('--description', metavar='', required=False, help='Description of the task')
    parser.add_argument('--hash', metavar='', required=True, help='Hash value of the task')
    args = parser.parse_args(sub_args)
    update(name=args.name, deadline=args.deadline, description=args.description, hash=args.hash)

elif args.function == 'remove':
    parser.add_argument('--hash', metavar='', required=True, help='Hash value of the task')
    args = parser.parse_args(sub_args)
    remove(args.hash)

from models import Task, Session
from datetime import datetime


def list(**kwargs):
    """
    Since this function is called 'list' in a given example for Chapter 2, I also named it 'list'.
    In other scenario I wouldn't do that.
    """
    session = Session()
    tasks = session.query(Task).all()

    if kwargs['all']:
        [print(f"{task.id} | {task.name} | {task.deadline} | {task.description} | {task.hash}") for task in tasks]

    elif kwargs['today']:
        [print(f"{task.id} | {task.name} | {task.deadline} | {task.description} | {task.hash}")
         for task in tasks if task.deadline.date() == datetime.now().date()]

    session.close()

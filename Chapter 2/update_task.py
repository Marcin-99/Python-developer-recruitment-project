from models import Task, Session
from datetime import datetime


def update(**kwargs):
    session = Session()
    task = session.query(Task).filter(Task.hash == kwargs['hash']).first()

    if task:
        deadline_time_object = datetime.strptime(kwargs['deadline'], '%Y-%m-%d,%H:%M') if kwargs['deadline'] else None

        task.name = kwargs['name'] if kwargs['name'] else task.name
        task.deadline = deadline_time_object if kwargs['deadline'] else task.deadline
        task.description = kwargs['description'] if kwargs['description'] else task.description
        session.commit()
        print("Task updated successfully.")

    else:
        print("There is no task with such a hash value. Please, try again.")

    session.close()

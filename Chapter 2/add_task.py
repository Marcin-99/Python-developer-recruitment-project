from models import Task, Session
from datetime import datetime


def add(**kwargs):
    deadline_time_object = datetime.strptime(kwargs['deadline'], '%Y-%m-%d,%H:%M')

    session = Session()
    task = Task(name=kwargs['name'],
                deadline=deadline_time_object,
                description=kwargs['description'],
                hash=hash(str(kwargs['name']) + str(kwargs['deadline']) + str(kwargs['description']))
                )

    session.add(task)
    session.commit()
    print('Task added successfully.')
    session.close()

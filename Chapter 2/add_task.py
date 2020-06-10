from models import Task, Session
from datetime import datetime


def add(name, deadline, description):
    deadline_time_object = datetime.strptime(deadline, '%Y-%m-%d,%H:%M')

    session = Session()
    task = Task(name=name,
                deadline=deadline_time_object,
                description=description,
                hash = hash(str(name) + str(deadline) + str(description)))

    session.add(task)
    session.commit()
    session.close()


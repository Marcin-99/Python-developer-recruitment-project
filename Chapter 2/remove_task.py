from models import Task, Session


def remove(hash_value):
    session = Session()
    task = session.query(Task).filter(Task.hash == hash_value).first()

    if task:
        session.delete(task)
        session.commit()
        print("Task deleted successfully.")

    else:
        print("There is no task with such a hash value. Please, try again.")

    session.close()

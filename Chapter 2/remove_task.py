from models import Task, Session


def remove(hash_value):
    session = Session()

    task = session.query(Task).filter(Task.hash == hash_value).first()
    session.delete(task)
    session.commit()
    print("Task deleted successfully.")

    session.close()


import time
from celery.task import Task


class Course(Task):
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start...')
        time.sleep(3)
        print(f'args={args},kwargs={kwargs}')
        print('end task....')
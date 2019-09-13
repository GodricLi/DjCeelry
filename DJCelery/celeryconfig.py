import djcelery
from datetime import timedelta

djcelery.setup_loader()
CELERY_IMPORTS = [
    'celeryapp.tasks'
]

CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }
}
CELERY_DEFAULT_QUEUE = 'work_queue'
# 有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发数量
CELERYD_CONCURRENCY = 4

# 每个worker最多执行100个任务，防止泄露内存
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务最多执行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

CELERYBAET_SCHEDULE = {
    'task1': {
        'task': 'course-task',
        'schedule': timedelta(seconds=5),
        'options': {
            'queue': 'beat_tasks'
        }
    }
}

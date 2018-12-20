# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kombu import Exchange, Queue


class CeleryConfig(object):
    BROKER_URL = 'amqp://han:haner27@localhost:5672/hnf'  # 中间人
    CELERY_RESULT_BACKEND = 'amqp'  # 结果存放地址
    CELERYD_PREFETCH_MULTIPLIER = 4  # celery worker 每次去rabbitmq取任务的数量
    CELERYD_MAX_TASKS_PER_CHILD = 200  # 每个worker执行了多少任务就会死掉
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
    CELERY_ENABLE_UTC = True

    CELERY_QUEUES = (
        Queue('common', exchange=Exchange('common'), routing_key='common', consumer_arguments={'x-priority': 10}),
        Queue('email', exchange=Exchange('email'), routing_key='email', consumer_arguments={'x-priority': 5}),
        Queue('file', exchange=Exchange('file'), routing_key='file', consumer_arguments={'x-priority': 1}),
        Queue('transient', exchange=Exchange('transient'), routing_key='transient', delivery_mode=1),  # 阅后即焚模式
        Queue('schedule', exchange=Exchange('schedule'), routing_key='schedule')  # 定时任务
    )
    CELERY_DEFAULT_QUEUE = 'common'
    CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
    CELERY_DEFAULT_ROUTING_KEY = 'common'


celery_config = CeleryConfig()
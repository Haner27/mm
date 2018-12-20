# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mq.celery_worker import celery_app
from mq.tasks import CallbackTask
from time import sleep


@celery_app.task(bind=True, base=CallbackTask)
def add(self, x, y):
    """
    当使用 bind=True 参数之后, 函数的参数发生变化, 多出了参数 self, 这这相当于把 div 编程了一个已绑定的方法,
    通过 self 可以获得任务的上下文.
    """
    sleep(3)
    return x + y


@celery_app.task(bind=True, base=CallbackTask)
def subtract(self, x, y):
    sleep(3)
    return x - y

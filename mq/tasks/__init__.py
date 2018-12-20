# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import wraps
from celery import Task


class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print("----%s is done" % task_id)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass


def task_status(task_func, task_id):
    # 获取celery之中 task_id的状态信息
    the_task = task_func.AsyncResult(task_id)   # 获取状态信息
    if  the_task.state=='PROGRESS':
        resp = 'progress', the_task.info
    elif  the_task.state=='SUCCESS':
        resp = 'success', the_task.info
    elif the_task.state == 'PENDING':   # 任务处于排队之中
        resp = 'waitting', the_task.info
    else:
        resp = the_task.state, the_task.info
    return resp
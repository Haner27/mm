# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import glob
import os
import sys

from celery.utils.imports import instantiate
from mq.tasks.celery_tasks import add, subtract
from mq.celery_worker import celery_app
from celery.app.control import Control


def chain_task():
    """
    链式任务，前一个的结果作为第二个任务的参数
    :return:
    """
    chain = add.s(6, 4) | subtract.s(3)
    res = chain()
    print(res.get())


def main_task():
    print(add(7, 4))  # 同步执行
    add.apply_async(args=[7, 4], queue='email')  # 异步执行，指定队列


def schedule_task():
    pass


if __name__ == '__main__':
    # chain_task()
    main_task()







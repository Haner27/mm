# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import glob
import os
import sys


from mq.tasks import task_status
from mq.tasks.celery_tasks import add, subtract, write_to_file, read_from_file, send_email_to_mine


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


def test():
    task = write_to_file.apply_async(args=('test.log',), queue='file')
    task_id = task.id
    while True:
        state, info = task_status(write_to_file, task_id)
        print(info)
        print('任务：{0} 当前的 state 为：{1}'.format(task_id, state), end='')

        if state == 'success':
            print('(100%)')
            break
        elif state == 'waitting':
            print('(0%)')
        else:
            print('({})'.format(info.get('percent', '100%')))
    print('done')


def test2():
    task = read_from_file.apply_async(args=('test.log',), queue='email')
    task_id = task.id
    while True:
        state, info = task_status(read_from_file, task_id)
        print('任务：{0} 当前的 state 为：{1}'.format(task_id, state), end='')
        print(info)
        if state == 'success':
            break
    print('done')


def test3():
    chain = write_to_file.s('test.log') | send_email_to_mine.s()
    res = chain()
    print('done')


def schedule_task():
    pass


if __name__ == '__main__':
    # chain_task()
    # main_task()
    test()
    # test2()
    # test3()





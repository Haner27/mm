# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import sleep
from io import StringIO

from mq.tasks import CallbackTask
from mq.celery_worker import celery_app
from utils.mail_utils import Email


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


@celery_app.task(bind=True, base=CallbackTask)
def write_to_file(self, file_name):
    totol = 10
    with open(file_name, 'w') as f:
        for i in range(1, totol + 1):
            sleep(1)
            percent = (i / totol) * 100
            self.update_state(state='PROGRESS', meta={'percent': '{}%'.format(percent)})  # 更新任务状态，保存到任务上下文中
            f.write('{}\n'.format(i))
    return file_name


@celery_app.task(bind=True, base=CallbackTask)
def read_from_file(self, file_name):
    l = ''
    with open(file_name) as f:
        line_no = 0
        for line in f.readlines():
            sleep(1)
            line_no += 1
            self.update_state(state='PROGRESS', meta={'line_no': '{}'.format(line_no)})
            l += line


@celery_app.task(bind=True, base=CallbackTask)
def send_email_to_mine(self, file_name):
    sender = 'sender@126.com'
    receivers = ['receiver@qq.com']
    mails_bcc = []
    subject = 'test-mail-utils'
    EMAIL_HOST = ('smtp.126.com', 25)
    body = 'test test test'
    email = Email(sender=sender, receivers=receivers, subject=subject, mails_bcc=mails_bcc, smtp_sever=EMAIL_HOST[0],
                  body=body, username='username', password='password')

    with open(file_name) as f:
        io = StringIO(f.read())
        io.seek(0)
    email.build_email()
    email.add_attachment(io, 'llll.txt')
    email.send_email()
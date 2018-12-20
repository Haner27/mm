# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import glob

from celery import Celery

from mq.celery_config import celery_config


def get_tasks_module_path_list():
    path_list = []
    mq_work_dir = os.path.dirname(__file__)
    mq_work_dir_name = os.path.basename(mq_work_dir)
    tasks_dir_name = 'tasks'
    for tasks_file in glob.glob(os.path.join(mq_work_dir, tasks_dir_name, '*.py')):
        basename = os.path.basename(tasks_file)
        if basename == '__init__.py':
            continue

        tasks_module_name = basename[:basename.rindex('.')]
        path_list.append('{0}.{1}.{2}'.format(mq_work_dir_name, tasks_dir_name, tasks_module_name))
    return path_list


celery_app = Celery('hnf', include=get_tasks_module_path_list())
celery_app.config_from_object(celery_config)


# if __name__ == '__main__':
#     celery_app.start()

# 重启celery
celery multi restart common_worker email_worker file_worker transient_worker -A mq.celery_worker -l INFO -c 2 -Q:common_worker common -Q:email_worker email -Q:file_worker file -Q:transient_worker transient --pidfile=mq/pids/%n.pid -l info --logfile=mq/logs/%n.log

# 查看命令
# celery multi show common_worker email_worker ls -lfile_worker transient_worker -A mq.celery_worker -l INFO -c 2 -Q:common_worker common -Q:email_worker email -Q:file_worker file -Q:transient_worker transient --pidfile=mq/pids/%n.pid -l info --logfile=mq/logs/%n.log
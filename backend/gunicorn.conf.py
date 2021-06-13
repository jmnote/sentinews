import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1

bind = 'unix:/tmp/gunicorn.sock'
errorlog = '/var/log/gunicorn_error.log'
accesslog = '/var/log/gunicron_access.log'
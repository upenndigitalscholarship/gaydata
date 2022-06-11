from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/srv/gaydata/gaydata.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/srv/gaydata/access.log'
errorlog =  '/srv/gaydata/error.log'

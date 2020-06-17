from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from love import send_love, send_love_captain

sched = BlockingScheduler()

# Schedule job_function to be called every 160 sec
sched.add_job(send_love, 'interval', seconds=3600)
# Schedule job_function to be called every 160 sec
sched.add_job(send_love_captain, 'interval', seconds=3600)

sched.start()
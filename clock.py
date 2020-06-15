from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from love import send_love

sched = BlockingScheduler()

# Schedule job_function to be called every 5 sec
sched.add_job(send_love, 'interval', seconds=5)

sched.start()
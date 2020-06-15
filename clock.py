from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from love import send_love, send_love_captain

sched = BlockingScheduler()

# Schedule job_function to be called every 60 sec
sched.add_job(send_love, 'interval', seconds=60)
# Schedule job_function to be called every 1 hr
sched.add_job(send_love_captain, 'interval', hours=1)

sched.start()
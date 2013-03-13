# -*- coding: gbk -*-
"""
@brief: main methods
@author:chenlianchang
@qiyingjita@126.com
@log:2012-09-18:create
"""

from apscheduler.scheduler import Scheduler
from datetime import datetime, timedelta

import daemon
from email import process_mail

if __name__ == '__main__':
    daemon.daemonize(noClose=False)
    sched = Scheduler()
    sched.daemonic = False
    sched.start()
    start_process_time = datetime.now() + timedelta(seconds=5)
    sched.add_interval_job(process_mail, hours = 1, start_date = start_process_time)

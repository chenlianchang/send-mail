send-mail
=========

功能：定时发邮件
通过 调整main.py里的 sched.add_interval_job(process_mail, hours = 1, start_date = start_process_time)， hours=1表示一个小时候跑一次程序

执行： python main.py

如果发送没成功，请确认25端口是否可用，打开25端口：service sendmail start

#encoding=utf8

"""
@author:zhengyi.clc
@brief:send email for kingbaboon
@log:create at 2013-01-30:14:50
"""

import os
from datetime import datetime

MALL_TO = ['qiyigjita@126.com', qiyingjita@163.com]

def process_mail():
    mydatetime = datetime.now()
    if int((mydatetime.isoformat().split(':')[0]).split('T')[1]) == 10:
        subject = "标题".decode('utf8').encode('gbk')
        msg = "邮件内容"
        sendmail_linux_command(subject, msg, MALL_TO)

def sendmail_linux_command(subject, msg, mail_to_list):
    assert type(mail_to_list) == type([])
    if 'LISTEN' not in os.popen('netstat -tuln | grep :25').read():
        return False
    command = 'echo "%s"|mail -s "%s" %s' % (msg, subject, ','.join(mail_to_list))
    os.system(command)
    if os.popen("echo $?").read().strip() == '0':
        return True
    else:
        return False

if __name__ == "__main__":
    process_mail()

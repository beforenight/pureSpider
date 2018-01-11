# !/usr/bin/python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText
import sys

# 邮箱服务器地址
mail_host = 'smtp.qq.com'
# 邮箱用户名
mail_user = 'XXX'
# 邮箱密码
mail_pass = 'XXX'
mail_postfix = 'qq.com'


def send_mail(to_list, subject, content):
    format = 'plain'
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, format, 'gbk')
    reload(sys)
    sys.setdefaultencoding('gb18030')
    if not isinstance(subject, unicode):
        subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    msg['Accept-Language'] = 'zh-CN'
    msg['Accept-Charset'] = 'ISO-8859-1,utf-8'

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == "__main__":
    result = send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
    if result:
        print "发送到 %s 成功！" % sys.argv[1]
    else:
        print "发送到 %s 失败！" % sys.argv[1]

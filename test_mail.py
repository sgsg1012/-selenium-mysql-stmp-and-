import smtplib
from email.mime.text import MIMEText

# 设置服务器所需信息
# 163邮箱服务器地址
from config import mail_host, mail_pass, mail_user, sender, receivers, path


def mail(content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = '成绩通知'
    message['From'] = sender
    message['To'] = receivers[0]
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(
        sender, receivers, message.as_string())
    smtpObj.quit()
    print('成功发送邮件')


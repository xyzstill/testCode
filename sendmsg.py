import os.path
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class ErrorLogAlert:
    def check_log(self):
        pass

    def send_email(self):
        mail_host="smtp.qq.com"           # 设置服务器
        mail_user="?@qq.com"     # 用户名
        mail_pass=""           # 口令(qq邮箱非密码)

        sender = '?@qq.com'
        receivers = ['?']   # 接收邮箱，可设置为你的QQ邮箱或者其他邮箱

        subject = 'test错误日志变动提醒！'               							# 邮件标题
        message = MIMEText('您的日志中出现错误，请查看：{0}', 'plain', 'utf-8')   # 邮件正文内容
        message['From'] = '2325227059@qq.com'                         # 邮件头信息
        message['To'] = 'zhang.xiao.yi@foxmail.com'                   # 邮件头信息
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.send_message(message)
            print("邮件发送成功")
            
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)
        
        
notice = ErrorLogAlert()
notice.send_email()

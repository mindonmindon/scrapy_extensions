# -*- coding: utf-8 -*-
# @Time    : 2022/10/17 14:40
# @Author  : LinMD
# @File    : email_client.py
# @Desc    :
from typing import Optional
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from scrapy.utils.project import get_project_settings


class EmailClient:
    EMAIL_SMTP_SERVER = 'EMAIL_SMTP_SERVER'
    EMAIL_SENDER = 'EMAIL_SENDER'
    EMAIL_SENDER_PASSWORD = 'EMAIL_SENDER_PASSWORD'
    EMAIL_RECEIVER = 'EMAIL_RECEIVER'

    def __init__(self):
        # 发件人邮箱的SMTP服务器（即sender的SMTP服务器）
        settings = get_project_settings()
        self.smtp_server = settings[self.EMAIL_SMTP_SERVER]
        # 发件人邮箱的用户名和授权码（不是登陆邮箱的密码）
        self.sender = settings[self.EMAIL_SENDER]
        self.password = settings[self.EMAIL_SENDER_PASSWORD]
        self.receiver = settings[self.EMAIL_RECEIVER]
        self.smtp: Optional[smtplib.SMTP] = None

    def connect(self):
        self.smtp = smtplib.SMTP()  # 创建一个连接
        self.smtp.connect(self.smtp_server)  # 连接发送邮件的服务器
        self.smtp.login(self.sender, self.password)  # 登录服务器

    def close(self):
        self.smtp.quit()

    def send(self, title: str, body: str):

        self.connect()
        try:
            # 创建一个实例
            message = MIMEText(body, 'plain', 'utf-8')  # 邮件正文
            # (plain表示mail_body的内容直接显示，也可以用text，则mail_body的内容在正文中以文本的形式显示，需要下载）
            message['From'] = self.sender  # 邮件上显示的发件人
            message['To'] = self.receiver  # 邮件上显示的收件人
            message['Subject'] = Header(title, 'utf-8')  # 邮件主题

            self.smtp.sendmail(self.sender, self.receiver, message.as_string())  # 填入邮件的相关信息并发送
        finally:
            self.close()

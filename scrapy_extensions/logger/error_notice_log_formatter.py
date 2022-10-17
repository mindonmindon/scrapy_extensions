# -*- coding: utf-8 -*-
# @Time    : 2022/10/17 14:14
# @Author  : LinMD
# @File    : logFormatter.py
# @Desc    :
import logging

from scrapy import logformatter
from scrapy_expand.email.email_client import EmailClient
from scrapy.utils.project import get_project_settings


class ErrorNoticeLogFormatter(logformatter.LogFormatter):
    """
    https://docs.scrapy.org/en/latest/topics/logging.html?highlight=LogFormatter#scrapy.logformatter.LogFormatter
    usage: LOG_FORMATTER = "zggw.log_formatter.PoliteLogFormatter"
    """

    def __init__(self):
        super(ErrorNoticeLogFormatter, self).__init__()
        self.has_occurred_error = False
        self.project = get_project_settings()['NEWSPIDER_MODULE']

    def send_email_with_once(self, title, body):
        if not self.has_occurred_error:
            try:
                print("occur error, send email")
                EmailClient().send(title, body)
                self.has_occurred_error = True
            except:
                logging.error("email server occur error")

    def item_error(self, item, exception, response, spider):
        self.send_email_with_once(f"{self.project} ITEM ERROR", exception)
        return super(ErrorNoticeLogFormatter, self).item_error(item, exception, response, spider)

    def spider_error(self, failure, request, response, spider):
        self.send_email_with_once(f"{self.project}  SPIDER ERROR", failure)
        return super(ErrorNoticeLogFormatter, self).spider_error(failure, request, response, spider)

    def download_error(self, failure, request, spider, errmsg=None):
        self.send_email_with_once(f"{self.project}  DOWNLOAD ERROR", failure)
        return super(ErrorNoticeLogFormatter, self).download_error(failure, request, spider, errmsg)

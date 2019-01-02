import sys
sys.path.append('/Users/tangxiao/文件/practice/New_API')
import smtplib
from email.mime.text import MIMEText
from util.operation_config import OperationConfig

class SendEmail():
    def __init__(self):
        oper_conf = OperationConfig()
        self.host = oper_conf.get_email('host')
        self.user = oper_conf.get_email('user')
        self.password = oper_conf.get_email('password')
        self.content = oper_conf.get_email('content')
        self.subject = oper_conf.get_email('subject')
        self.port = oper_conf.get_email('port')

    def send_email(self,send_list):
        message = MIMEText(self.content,_subtype='plain',_charset='utf-8')
        print(self.content)
        message['Subject'] = self.subject
        message['To'] = ';'.join(send_list)
        message['From'] = self.user
        server = smtplib.SMTP()
        server.connect(self.host)
        server.login(self.user,self.password)
        # server.sendmail(self.user,send_list,message.as_string())
        # server.close()
if __name__ == '__main__':
    send_list = ['18602804663@163.com','1374265193@qq.com','xiao.tang@downjoy.com']
    SendEmail().send_email(send_list)
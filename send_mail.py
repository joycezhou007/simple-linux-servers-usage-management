import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender =  'xxx@xxxx.com'
send_pwd = 'xxxxxxxxxx' #email authorization code
smtp_server = 'smtp.exmail.qq.com'


def send_mail(receiver,ip,pwd,new_expire_date):
    default_receivers = ['default1@xxxxx.com','default2@xxxxx.com']
    default_receivers.append(receiver)
    print (default_receivers)

    subject = '[Server Notification] ' + ip
    body = '[Server Notification] \n\n' + ip + ' is updated for you, its password is: ' + pwd + '\n\nPlease arrange your work before it expiration date: ' + new_expire_date
    message = MIMEText(body, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = sender
    message['To'] = ",".join(default_receivers)


    try:
        smtpObj = smtplib.SMTP_SSL(smtp_server)
        smtpObj.connect(smtp_server, 465)
        #smtpObj.set_debuglevel(1)
        smtpObj.login(sender,send_pwd)
        smtpObj.sendmail(sender,default_receivers, message.as_string(),subject)
        print('send mail successfully')
        return True
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print('error',e)
        return False



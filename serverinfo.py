#!/usr/bin/env python
from flask import Flask, render_template,request,url_for,redirect
from send_mail import *
import datetime
from func import *

serverInfo = Flask(__name__)
ip = get_server_ip()
new_user = {}
file = './log/server_account_history.json'
account = 'test'
host = 'http://' + ip +':8888'

@serverInfo.route("/")
def index():
    new_expire_date = get_expired_change_date(account)
    new_update_date = get_last_change_date(account)
    last_user = get_server_account_history(file)
    email = last_user['email']
    task = last_user['task']
    return render_template('index.html',email=email, task=task, update_date=new_update_date, expire_date=new_expire_date, ip=ip)


@serverInfo.route('/update_user', methods=['POST','GET'])
def update_user():
    if request.method == 'POST':
        email = request.form['email']
        task = request.form['task']
        expire_date = request.form['expire_date']
        pwd = generate_pwd()
        if pwd is None or pwd.strip() == '':
           pwd = datetime.date.today().strftime('%Y-%m-%d')

        failed_info = ''
        new_expire_date_status = set_expire_date(account, expire_date)
        if new_expire_date_status is not True:
            failed_info = 'Account expiration date was not updated,error: ' + new_expire_date_status +'\n'
            last_user = get_server_account_history(file)
            email = last_user['email']
            task = last_user['task']
            expire_date = get_expired_change_date(account)
        else:
            update_date = get_last_change_date(account)
            new_pwd_status = set_password(account, pwd)
            if new_pwd_status is False:
                failed_info = failed_info + 'Account password was not updated' + '\n'
            else:
                mail_status = send_mail(email, ip, pwd, expire_date)
                if mail_status is False:
                    failed_info = failed_info + 'if you cannot get mail, please check if your email-address is correct'
                    update_info = 'Please check with admin. \n' + failed_info
                else:
                    update_info = 'Server account was updated successfully, you can get password in your mail after a few mins.'
                    new_user['email'] = email
                    new_user['task'] = task
                    set_server_account_history(file, new_user)

        return redirect(url_for('user_info', email=email, task=task, update_date=update_date, expire_date=expire_date, update_info=update_info))

    return render_template('update_user.html')


@serverInfo.route('/user_info', methods=['GET'])
def user_info():
    if request.method == 'GET':
        email = request.args.get('email')
        task = request.args.get('task')
        new_expire_date = request.args.get('expire_date')
        new_update_date = request.values.get('update_date')
        update_info = request.values.get('update_info')

        return render_template('index.html', email=email, task=task, update_date=new_update_date, expire_date=new_expire_date, update_info=update_info,ip=ip)


if __name__ == "__main__":
    serverInfo.run(debug=True, host=ip, port=8888)

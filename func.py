#!/usr/bin/env python

import commands
import random
import string
import json

def get_server_ip():
    return commands.getoutput('''ip addr | grep eno3|grep inet|grep brd|awk '{print $2}'|sed -e 's#/24##' ''')


def get_last_change_date(account):
    return commands.getoutput(''' echo '(echo "encrypted-passwords" | base64 -d)' | sudo chage -l ''' + account + ''' |awk 'NR==1 {print}'|cut -f2 -d":" ''')
    # s,p = commands.getstatusoutput(''' echo 'echo "encrypted-passwords" | base64 -d' | sudo chage -l test ''')

def get_expired_change_date(account):
    return commands.getoutput(''' echo '(echo "encrypted-passwords" | base64 -d)' | sudo chage -l ''' + account + ''' |awk 'NR==4 {print}'|cut -f2 -d":" ''')


def set_expire_date(account,expire_date):
    #dates, datep = commands.getstatusoutput(''' echo '(echo "encrypted-passwords" | base64 -d)' | sudo usermod -e ''' + expire_date + ' ' + account)
    s_cmd = "sudo usermod -e {0} {1}".format(expire_date,account)
    dates, datep = commands.getstatusoutput(''' echo '(echo "encrypted-passwords" | base64 -d)' | ''' + s_cmd)
    if dates == 0:
        return True
    else:
        return datep

def set_password(account,pwd):
    output = commands.getoutput(''' (echo ''' + pwd +''';sleep 1;echo '''+ pwd + ''') | sudo passwd ''' + account + '''> /home/assets-servers/log/set_pwd_log.txt ''')
    if output.find('password updated successfully') != -1:
        return True
    else:
        return False


def generate_pwd():
    new_pwd = []
    for i in range(10):
        one_pwd = random.choice(string.ascii_letters + string.digits)
        new_pwd.append(one_pwd)
        pwd_result = ''.join(new_pwd)

    return pwd_result


def get_server_account_history(file):

    with open(file, 'r') as f:
        contents = f.read()
        last_update = json.loads(contents)
        f.close
    return last_update


def set_server_account_history(file, update_dict):
    json_str = json.dumps(update_dict)
    with open(file, 'w') as f:
        f.write(json_str)
        f.close()


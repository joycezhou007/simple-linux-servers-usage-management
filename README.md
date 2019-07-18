# simple-linux-servers-usage-management

implemented functions & specification：

1. linux 服务器上任意目录存放脚本
2. 进入脚本目录，运行serverinfo.py, 这里设置的服务端口是8888
3. 浏览器打开linux服务器IP+端口88888， 如http://10.xxx.xxx.xxx:8888
4. 默认主页展示的是服务器用户test当前状态，点击update user 更新使用情况
     ![images](https://raw.githubusercontent.com/joycezhou007/simple-linux-servers-usage-management/master/images/index.png)
  
5. 使用者可填写自己的邮箱，使用截止日期，使用的任务描述
      ![images](https://raw.githubusercontent.com/joycezhou007/simple-linux-servers-usage-management/master/images/update_user.jpg)
  
6. 提交后，脚本会自行更改服务器已有的sudo用户test的过期时间 & 密码
7. 将test用户新的过期时间和密码发送至新的使用者邮箱，示例如下 
      ![images](https://raw.githubusercontent.com/joycezhou007/simple-linux-servers-usage-management/master/images/email.png)

to be continued：
1. 脚本服务加入服务器启动命令
2. 多台linux服务器，无需每个服务器单独部署脚本，集中管理

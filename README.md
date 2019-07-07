#基于Flask实现后台权限管理系统

基于Python的Flask WEB框架实现后台权限管理系统，内容包含：用户管理、角色管理、资源管理和机构管理。前端页面参考了@sypro。

**系统已经切换python 3，我的是在python 3.7.0下测试的，理论上Python 3版本应该都是可以运行的。需要Python 2版本的朋友可以checkout到python2分支。**


**完整设计文档**
[参考百度阅读](https://yuedu.baidu.com/ebook/8e8853732e60ddccda38376baf1ffc4fff47e278)

**前端依赖插件**

 1. My97DatePicker
 2. jQuery
 3. Bootstrap
 4. jQuery EasyUI
 5. jQuery Portal
 

**后端依赖插件**

 1. Flask
 2. Flask-Migrate
 3. Flask-Script
 4. Flask-SQLAlchemy
 5. Flask-Login
 6. itsdangerous
 7. Jinja2
 8. Werkzeug
 9. mysql-python

**使用方法**

1. 导入根目录下db.sql数据库脚本到mysql数据库
2. pip install -r requirements.txt。本项目下的flask是下载好的依赖，在python环境下可以直接运行。
3. python manager.py runserver
 
**讨论群**

欢迎加入python技术爱好者，群号码：297690915，内有福利！

**效果图**

![机构管理](doc/机构管理.png)

![角色管理](doc/角色管理.png)

![用户管理](doc/用户管理.png)

![资源管理](doc/资源管理.png)

**图书资源推荐**

![小程序](doc/扫码_搜索联合传播样式-标准色版.png)
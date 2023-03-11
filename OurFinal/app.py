from flask import Flask, render_template, request, session, Response
from service.UserService import UserService
from controller.JobController import jobController
# from controller.UserController import userController


app = Flask(__name__)
app.config["SECRET_KEY"] = "SESSIONKEYAAAABBBXXXYYYYY" # 给session加密用的(要使用session的必备项）
app.register_blueprint(jobController)   #注册Bluprint 否则无法使用
# app.register_blueprint(userController)
userService = UserService()

@app.route('/')  #定义路由:将url和处理函数进行绑定
def hello_world():  # put application's code here
    print("===================helloworld======================")
    return render_template("hello_world.html")

#登录
@app.route("/login", methods=['post'])
def login():
    # 接收表单数据
    print("===================login======================")
    userName = request.form.get("userName")
    userPwd = request.form.get("userPwd")
    if userName and userPwd:
        user = userService.getUserByUserName(userName)  #基于数据库用户表验证登录
        print(user)
        if user and user['userPwd'] == userPwd:
            session['userName'] = userName
            session['user'] = user
            return render_template("main.html")
            pass
        pass
    else:
        return render_template("hello_world.html")
        pass
    pass

#退出
@app.route("/logout", methods=['get'])
def logout():
    print("===================logout======================")
    session.clear()
    return render_template("hello_world.html")
    pass

@app.route('/main')  # url
def main():   #在进入的网址后加上\main 即可显示出“Flask page！”
    print("===================main======================")
    return render_template("main.html")
    pass



#数据的列表呈现



if __name__ == '__main__':  #在run()函数里可以修改端口，默认端口是5000
    app.run()

# MVC:  model view controller
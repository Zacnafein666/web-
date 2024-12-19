from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')#主页面
def zhuyemian():  # put application's code here
    return render_template('zhuyemian.html')

@app.route('/biaoge')#表格
def biaoge():  # put application's code here
    return render_template('biaoge.html')

@app.route('/liebiao')#列表
def liebiao():  # put application's code here
    return render_template('liebiao.html')

@app.route('/zhuce')#注册
def zhuce():  # put application's code here
    return render_template('zhuce.html')



if __name__ == '__main__':
    app.run()

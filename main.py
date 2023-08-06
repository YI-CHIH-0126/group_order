# -*- coding: utf-8 -*-
from flask import Flask,request,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("./templates/home.html")

@app.route("/order",methods=['POST','GET'])
def order():
    if request.method=='POST':
        html='''
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="UTF-8">
                        <title>order</title>
                        <link rel="stylesheet" href="{\{url_for('static',filename='template.css')}}">
                    </head>
                    <body class="background">
                        <form method="POST" action="/check_order">
                            <label for="phone">座號:</label><input type="text" name="phone" id="phone" class="enter"><br><br>
                            <label for="option">今天我想來點 </label><select id="option" name="meals">
            '''
        menulist=request.form['menu'].split("\n")
        for i in menulist:
            html+="<option value={}>{}</option>".format(i,i)
        html+='''
                                </select>
                                <input type="submit" value="送出訂單">
                            </form>
                        </body>
                    </html>
                '''
        f=open("./templates/order.html",'w',encoding="utf-8")
        f.write(html)
        f.close()
        return render_template('./templates/order.html')
    else:
        return render_template("./templates/order.html")

@app.route("/check_order",methods=['POST','GET'])
def check():
    if request.method =='POST':
        file=open("./static/list.txt",mode='a')
        print("{}:{}".format(request.form['phone'],request.form['meals']),file=file)
        file.close()
        file=open('./static/list.txt',mode='r')
        olist=file.readlines()
        html='''
                <h1>完成點餐</h1>
                <table border>
            '''
        for i in olist:
            html+='<tr><td>{}</td></tr>'.format(i)
        html+='</table>'
        file.close()
        return html
    else:
        html='''
                <h1>完成點餐</h1>
                <table border>
            '''
        file=open("./static/list.txt","r")
        olist=file.readlines()
        for i in olist:
            html+="<tr><td>{}</td></tr>".format(i)
        html+='</table>'
        file.close()
        return html
@app.route("/log_in",methods=['POST','GET'])
def log_in():
    if request.method=="POST":
        if request.form['account']=="king" and request.form['pwd']=="0126":
            return render_template("./templates/edit.html")
        else:
            return "密碼錯誤"
    else:
        return render_template("login.html")
    
if __name__ == '__main__':
    app.run()
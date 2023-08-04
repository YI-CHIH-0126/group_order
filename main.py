from flask import Flask,request,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/check_order",methods=['POST','GET'])
def check():
    if request.method =='POST':
        file=open("static/list.txt",mode='a')
        print("{}:{}".format(request.form['phone'],request.form['item']),file=file)
        file.close()
        file=open('static/list.txt',mode='r')
        olist=file.readlines()
        html='''
                <h1>order list</h1>
                <table border>
            '''
        for i in olist:
            html+='<tr><td>{}</td></tr>'.format(i)
        html+='</table>'
        file.close()
        return html
    else:
        html='''
                <h1>order list</h1>
                <table border>
            '''
        file=open("static/list.txt","r")
        olist=file.readlines()
        for i in olist:
            html+="<tr><td>{}</td></tr>".format(i)
        html+='</table>'
        file.close()
        return html
@app.route("/log_in")
def log_in():
    return render_template("login.html")
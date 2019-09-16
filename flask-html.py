from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

path = 'filestudents.txt'


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/show', methods =['POST', 'GET'])
def show():
    f = open(path, 'r',encoding='utf-8')
    content = f.read()
    f.close()
    return render_template("show.html", f= content)

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/save', methods =['POST', 'GET'])
def save():
    if request.method == 'POST':
        f = open(path, 'a', encoding='utf-8')
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        classroom = request.form['classroom']
        line = id +','+name +','+address+','+classroom
        f.writelines(str(line)+'\n')
        f.close()
    return redirect("http://127.0.0.1:5000/show")

@app.route('/id')
def id():
    return render_template("id.html")

@app.route('/delete', methods =['POST', 'GET'])
def delete():
    if request.method == 'POST':
        f = open(path,'r', encoding='utf-8')
        lis = []
        for line in f:
            data = line.strip(",")
            lis.append(data.split(","))
        k = 0
        id = request.form['id']
        while k < len(lis):
            if lis[k][0] == id:
                lis.remove(lis[k])
            k += 1

        i = 0
        lines = ''
        while i < len(lis):
            line = ','.join(lis[i]).strip("\n")
            i += 1
            lines += line + '\n'
        f = open(path, 'w', encoding='utf-8')
        f.writelines(lines)
        f.close()
    return redirect('http://127.0.0.1:5000/show')

@app.route('/name')
def name():
    return render_template("name.html")

@app.route('/classroom', methods=['POST','GET'])
def id_show():
    str=""
    if request.method == 'POST':

        f = open(path,'r', encoding='utf-8')
        lis = []

        for line in f:
            data = line.strip(",")
            lis.append(data.split(","))
        k = 0
        name = request.form['name']
        while k < len(lis):
            if lis[k][1] == name:
                str = ",".join(lis[k])
            k+=1
    return render_template('classroom.html', f=str)

@app.route('/edit')
def edit():
    return render_template("edit.html")

@app.route('/saveEdit', methods = ['POST','GET'])
def save_edit():
    if request.method == 'POST':
        f = open(path, 'r', encoding='utf-8')
        lis = []
        for line in f:
            data = line.strip(",")
            lis.append(data.split(","))
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        classroom = request.form['classroom']
        k = 0
        while k < len(lis):
            if lis[k][0]==id:
                lis[k][1]= name
                lis[k][2]=  address
                lis[k][3]=  classroom
            k+=1

        l = 0
        lines = ''
        while l < len(lis):
            line = ','.join(lis[l]).strip("\n")
            l += 1
            lines += line + '\n'
        f = open(path, 'w', encoding='utf-8')
        f.writelines(lines)
        f.close()
    return redirect('http://127.0.0.1:5000/show')

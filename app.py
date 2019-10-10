from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)


class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(100))
    address = db.Column(db.String(100))

    def __init__(self,  name, age, address):
        self.name = name
        self.age = age
        self.address = address

@app.route('/')
def list_employees():
    return render_template('list_employees.html', Employees=Employees.query.all())


@app.route('/add', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['age']:
            flash('Please enter all the fields', 'error')
        else:
            employee = Employees(request.form['name'], request.form['age'], request.form['address'])

            db.session.add(employee)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('list_employees'))
    return render_template('add.html')

@app.route('/delete', methods =['GET', 'POST'])
def del_employee():
    if request.method== 'POST':
        Employees.query.filter_by(id=request.form['id']).delete()
        db.session.commit()
        flash('Employee was successfully deleted')
        return redirect(url_for("list_employees"))
    return render_template('delete.html')


@app.route('/edit', methods=['POST','GET'])
def edit_employee():
    if request.method == 'POST':
        employee = Employees.query.filter_by(id=request.form['id'])
        employee.update({Employees.name:request.form['name']})
        employee.update({Employees.age:request.form['age']})
        employee.update({Employees.address:request.form['address']})

        db.session.commit()
        return redirect(url_for('list_employees'))
    return render_template('edit.html')


@app.route('/showinfo', methods = ['POST', 'GET'])
def show_info():
    if request.method== 'POST':
        employee = request.form['id']
        return render_template('show_info.html', Employees=Employees.query.filter_by(id=employee))
    return render_template('id.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
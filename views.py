from flask import render_template, request, flash, url_for
from werkzeug.utils import redirect

from models import Employees
from webapp import app, db


@app.route('/')
def list_employees():
    return render_template('list_employees.html', Employees = Employees.query.all())

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['age'] or not request.form['address']:
            flash('Please enter all the fields', 'error')
        else:
            employee = Employees(request.form['name'], request.form['age'], request.form['address'])
            db.session.add(employee)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('list_employees'))
    return render_template('add.html')

@app.route('/delete', methods=['GET', 'POST'])
def del_employee():
    if request.method == 'POST':
        Employees.query.filter_by(id=request.form['id']).delete()
        db.session.commit()
        flash('Employee was successfully deleted')
        return redirect(url_for('list_employees'))
    return render_template('delete.html')

@app.route('/edit', methods=['GeT', 'POST'])
def edit_employee():
    if request.method == 'POST':
        employee = Employees.query.filter_by(id=request.form['id'])
        employee.update({Employees.name:request.form['name']})
        employee.update({Employees.age: request.form['age']})
        employee.update({Employees.address: request.form['address']})

        db.session.commit()
        flash('Employee was successfully edited')
        return redirect(url_for('list_employees'))
    return render_template('edit.html')

@app.route('/idshow', methods=['POST','GET'])
def id_search():
    if request.method == 'POST':
        employee = request.form['id']
        return render_template('show_info.html', Employees=Employees.query.filter_by(id=employee))
    return render_template('id.html')

from webapp import db

class Employees(db.Model):
    id = db.Column('employee.id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    address = db.Column(db.String(100))

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

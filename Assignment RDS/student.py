
import os
from flask import Flask, flash, render_template, redirect, url_for, request, session
from database import Database


app = Flask(__name__)
app.secret_key = os.urandom(12)
db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Student Record Added Successfully")
        else:
            flash("Record cannot be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updaterec', methods = ['POST'])
def updaterec():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Record has been updated')

        else:
            flash('Record cannot be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deleterec', methods = ['POST'])
def deleterec():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Student Record Deleted Successfully')

        else:
            flash('Record cannot be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

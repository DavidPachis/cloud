from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Contact, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@views.route('/register', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # receive data from the form
        name = request.form['name']
        category = request.form['category']
        place = request.form['place']
        start = request.form['start']
        end = request.form['end']
        mode = request.form['mode']

        # create a new Contact object
        new_contact = Contact(name, category, place, start, end, mode, user_id=current_user.id)

        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')
    return render_template("taskform.html", user=current_user)


@views.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.name = request.form['name']
        contact.category = request.form['category']
        contact.place = request.form['place']
        contact.start = request.form['start']
        contact.end = request.form['end']
        contact.mode = request.form['mode']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('views.index'))

    return render_template("update.html", contact=contact, user=current_user)


@views.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return render_template('index.html', user=current_user)


@views.route('/events')
@login_required
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts, user=current_user)


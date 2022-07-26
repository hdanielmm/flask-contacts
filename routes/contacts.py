from flask import Blueprint, redirect, render_template, request, url_for, flash
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def index():
    contacts = Contact.query.all()

    return render_template('index.html', contacts=contacts)


@contacts.route('/about')
def about():
    return render_template('about.html')


@contacts.route('/new', methods=['POST'])
def add_contact():

    fullname = request.form['fullname'],
    phone = request.form['phone'],
    email = request.form['email'],

    new_contact = Contact(fullname, phone, email)

    db.session.add(new_contact)
    db.session.commit()

    flash('Contact created successfully', 'info')

    return redirect(url_for('contacts.index'))


@contacts.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)

    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.phone = request.form['phone']
        contact.email = request.form['email']

        db.session.commit()

        flash('Contact updated successfully', 'info')

        return redirect(url_for('contacts.index', contact=contact))

    return render_template('update.html', contact=contact)


@contacts.route('/delete/<int:id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully', 'info')

    return redirect(url_for('contacts.index'))

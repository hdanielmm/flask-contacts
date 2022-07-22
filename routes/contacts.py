from flask import Blueprint, redirect, render_template, request
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    contacts = Contact.query.all()
    print(contacts)
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
def add_contact():

    fullname = request.form['fullname'],
    phone = request.form['phone'],
    email = request.form['email'],

    new_contact = Contact(fullname, phone, email)

    db.session.add(new_contact)
    db.session.commit()

    return redirect('/')


@contacts.route('/update')
def update():
    return 'Update contact'


@contacts.route('/delete/<int:id>')
def delete(id):
    return 'Delete contact'

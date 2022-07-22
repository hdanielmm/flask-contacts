from flask import Blueprint, redirect, render_template, request
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    return render_template('index.html')


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
def update_contacts():
    pass


@contacts.route('/delete/<int:id>')
def delete(id):
    pass

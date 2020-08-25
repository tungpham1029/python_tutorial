from flask import Flask, jsonify, request, session, url_for, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address
        if db.users.find_one({'email': user['email']}):
            return jsonify({"error":"Email address already exists"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error":"Signup Failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user:
            return self.start_session(user)
        if not user:
            return jsonify({ "error" : "Invalid login credentials" }), 401
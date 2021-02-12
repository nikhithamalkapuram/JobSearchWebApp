from flask import Flask, jsonify, request, session, redirect,url_for,render_template
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
from datetime import date
from bson.json_util import dumps
class Emp:
  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('empname'),
      "phonenumber": request.form.get('empphonenumber'),
      "password": request.form.get('emppassword'),
      "email":request.form.get('empemail')
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.employer.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.employer.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.employer.find_one({
      "email": request.form.get('empemail')
    })

    if user and pbkdf2_sha256.verify(request.form.get('emppassword'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401

class Jobseeker:
  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('jobseekername'),
      "phonenumber": request.form.get('jobseekerphonenumber'),
      "password": request.form.get('jobseekerpassword')
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.jobseeker.find_one({ "phonenumber": user['phonenumber'] }):
      return jsonify({ "error": "phonenumber already in use" }), 400

    if db.jobseeker.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.jobseeker.find_one({
      "phonenumber": request.form.get('jobseekerphonenumber')
    })

    if user and pbkdf2_sha256.verify(request.form.get('jobseekerpassword'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401

class Job:
  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def postjob(self):
    print(request.form)

    # Create the job object
    job = {
      "_id": uuid.uuid4().hex,
      "jobcategory": request.form.get('jobcategory'),
      "joblocation": request.form.get('joblocation'),
      "jobtype": request.form.get('jobtype'),
      "jobcount":  request.form.get('jobcount'),
      "posted_on": date.today().isoformat(),
      "posted by": session['user']
    }
    db.jobs.insert_one(job)
    session['postmessage'] = "posted succesfully"
    return redirect(url_for('postjobs'))

  #searching jobs by category
  def searchbycategory(self,category):
    course_list = list(db.jobs.find({"jobcategory": category}))
    #print(course_list)
    return course_list

#searching jobs by location
  def searchbylocation(self,location):
    course_list = list(db.jobs.find({"joblocation": location}))
    print(course_list)
    return course_list
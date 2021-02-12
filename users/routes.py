from flask import Flask,request,render_template
from app import app
from users.models import Emp
from users.models import Jobseeker
from users.models import Job
from bson.json_util import dumps
@app.route('/emp/signup', methods=['POST'])
def empdbsignup():
  return Emp().signup()

@app.route('/emp/signout')
def empdbsignout():
  return Emp().signout()

@app.route('/emp/login', methods=['POST'])
def empdblogin():
  return Emp().login()

@app.route('/jobseeker/signup', methods=['POST'])
def jobseekdbsignup():
  return Jobseeker().signup()

@app.route('/jobseeker/signout')
def jobseekdbsignout():
  return Jobseeker().signout()

@app.route('/jobseeker/login', methods=['POST'])
def jobseekdblogin():
  return Jobseeker().login()

@app.route('/postjobs/jobpost', methods=['POST','GET'])
def jobpost():
  return Job().postjob()


@app.route('/searchjobcat/cat', methods=['GET'])
def bycategory():
  jobslist = Job().searchbycategory(request.args.get('jobcategory'))
  return render_template("searchjobcat.html",catjobs = jobslist)


@app.route('/searchjobloc/loc', methods=['GET'])
def bylocation():
  jobslist = Job().searchbylocation(request.args.get('joblocation'))
  return render_template("searchjobloc.html",locjobs = jobslist)
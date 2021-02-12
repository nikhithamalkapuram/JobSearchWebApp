from flask import Flask,render_template,session
from functools import wraps
import pymongo


app = Flask(__name__)

app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.jobsearch

from users import routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emp/',methods = ['POST','GET'])
def emp():
    return render_template('emp.html')

@app.route('/jobseeker/',methods = ['POST','GET'])
def jobseeker():
    return render_template('jobseeker.html')

@app.route('/jobseeker/jobseekerlogin/')
def jobseekerlogin():
    return render_template('jobseekerlogin.html')

@app.route('/emp/emplogin/')
def emplogin():
    return render_template('emplogin.html')

#jobseekerwelcome page
@app.route('/jobseekerwelcome/',methods=['POST','GET'])
def jobseekerwelcome():
    return render_template('jobseekerwelcome.html')

#employer welcome page
@app.route('/empwelcome/',methods=['POST','GET'])
def empwelcome():
    return render_template('empwelcome.html',emp = session['user'])

#posting jobs
@app.route('/postjobs/',methods=['POST','GET'])
def postjobs():
    return render_template('postjobs.html')

#search jobs by category
@app.route('/searchjobcat/',methods=['GET'])
def searchjobcat():
    return render_template('searchjobcat.html')
    
#search jobs by location
@app.route('/searchjobloc/',methods=['GET'])
def searchjobloc():
    return render_template('searchjobloc.html')

#search jobs first by category then by location
@app.route('/searchjobcattheloc/',methods=['GET'])
def searchjobcat_loc():
    return render_template('catthenloc.html')

#search jobs first by location and then by category
@app.route('/searchjoblocthencat/',methods=['GET'])
def searchjobloc_cat():
    return render_template('locthencat.html')



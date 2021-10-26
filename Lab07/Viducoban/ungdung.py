from flask import Flask, render_template, abort, redirect, url_for, request,make_response
from flask import session

ungdung = Flask(__name__, static_folder="D:\VanLang\AdvancedPythonProgramming\Lab07\Viducoban\static")

@ungdung.route('/')
def hello():
  return render_template("index.html")

@ungdung.route('/monhoc')
def learn():
    return ('Day la mon hoc')

@ungdung.route('/dinhtuyen')
def dinhtuyen():
  return redirect(url_for('login'))

@ungdung.route('/login')
def login():
  abort (401)clear_session_cookies()

#Bai 12
# https://pythonbasics.org/flask-http-methods/
@ungdung.route('/bai12',methods = ['POST', 'GET'])
def bai12():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@ungdung.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

#Bai13
@ungdung.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nmsetcookie']
      session['username']= user
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@ungdung.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   if name in session:
         name = name + ': ' + name
   return '<h1>welcome ' + str(name) + '</h1>'

@ungdung.errorhandler(404)
def page_not_found(error):
   return render_template('page_not_found.html'), 404

if __name__ == "__main__":
  ungdung.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/ ,?RT'
  ungdung.run(port = 5050)
  #from waitress import serve
  #serve(ungdung, port=5050)

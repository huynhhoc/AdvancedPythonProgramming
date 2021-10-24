from flask import Flask, render_template, abort, redirect, url_for

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
  abort (401)
  
if __name__ == "__main__":
  ungdung.run(port = 5050)

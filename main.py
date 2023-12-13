from flask import Flask
app = Flask('app')

@app.route('/hello')
def hello_world():
  return 'Hello, World!'
  
@app.route('/admin')
def admin_page():
  return 'Hello Admin'

@app.route('/login.portal')
def login_portal():
  return 'This is the login Portal'

app.run(host='0.0.0.0', port=8080)

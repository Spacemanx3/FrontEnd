from flask import Flask
app = Flask('app')

@app.route('/hello')
def hello_world():
  return 'Hello, World!'
  
@app.route('/admin')
def admin_page():
  return 'Hello Admin'

app.run(host='0.0.0.0', port=8080)

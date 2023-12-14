from flask import Flask, redirect, url_for
app = Flask('app')

@app.route('/hello')
def hello_world():
  return 'Hello, World!'
  
@app.route('/guest/<guest>')
def hello_guest(guest):
  return 'Hello, %s!' % guest
  
@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % username
  
@app.route('/post/<int:post_id>')
def show_post(post_id):
  # show the post with the given id, the id is an integer
  return 'Post %d' % post_id
  
@app.route('/admin')
def admin_page():
  return 'Hello Admin'


app.run(host='0.0.0.0', port=8080)

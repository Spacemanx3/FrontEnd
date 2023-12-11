//Before running this code, make sure you have Flask installed. If not, run the command pip install Flask

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True)

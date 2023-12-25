from flask import Flask

app = Flask(__name__)

# Prompt the user for the host and port to run the server
host = input("Enter the host (default is 127.0.0.1): ") or '127.0.0.1'
port = input("Enter the port (default is 5000): ") or 5000

@app.route('/')
def hello_world():
    return 'Hello, World! This is a basic Flask application.'

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)

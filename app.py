from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Cloud DevOps Automation!"

if __name__ == '__main__':
    app.run(debug=True)

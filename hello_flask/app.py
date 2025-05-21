from flask import Flask



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world.. Al hamdulilah I have just created my first docker based project where I'm using docker container to run my web application of hello-flask which is scripted in Python!'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

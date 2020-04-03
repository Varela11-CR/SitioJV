from flask import Flask, render_template
from flask_socketio import SocketIO, send

#   An instance of the Flask class is created
app = Flask(__name__)
#   Flask-SocketIO is added to the application
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


#   Route creation
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')


#   Creating the event handler
@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)


if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)

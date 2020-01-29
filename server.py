import requests,threading
from flask import Flask
from flask import request

message = ''
users = ["http://localhost:9000"]
app = Flask(__name__)


@app.route('/logon')
def logon():
  #users.append(request.remote_addr)
  return ''

@app.route('/logoff')
def logoff():
  users.remove(request.remote_addr)
  return ''

@app.route('/post_message/<text>')
def post_message(text):
    print(text)
    for user in users:
      requests.get(user + "/new_message/"+text)
    return ''

app.use_reloader=False
threading.Thread(app.run(host='127.0.0.1', port=5000, debug=False)).start()


  

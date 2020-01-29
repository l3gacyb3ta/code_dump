import requests,threading
from flask import Flask

app = Flask(__name__)

@app.route('/new_message/<text>')
def print_message(text):
  print(text)
  return ''


if __name__ == '__main__':
  #server_url = str(input("URL> "))
  requests.get("http://127.0.0.1:5000/logon")

threading.Thread(app.run(host='localhost', port=9000, debug=True)).start()

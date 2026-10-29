from Flask import Flask

app = Flask(__name__)

@app.route ('/')
def homepage():
  return "oi"

app.run()

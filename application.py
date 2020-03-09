from flask import Flask,render_template

app = Flask(__name__)

# Load config
app.config.from_pyfile('config.cfg', silent=True)  # load settings from config.cfg
#Session(app)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="lazzi`")

@app.route('/login')
def login():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True) 
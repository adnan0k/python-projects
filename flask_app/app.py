from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world rerun debug true"

if __name__ == "__main__":
    app.run(debug=True)
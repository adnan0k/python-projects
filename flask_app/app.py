from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="lazzi`")

@app.route('/login', methods=['GET','POST'] )
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        print(email,password)
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True) 
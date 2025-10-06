from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class User(db.Model):
    sr_no = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    dateTime = db.Column(db.DateTime, default=datetime.utcnow) 



with app.app_context():
    db.create_all()



@app.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route('/register', methods=['GET','POST'] )
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        new_user = User(
            user_email = email,
            password = password
            )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('form.html')


@app.route('/update/<sr>', methods=['GET','POST'] )
def update(sr):
    user = User.query.get(sr)
    if request.method == "POST":
        user.user_email = request.form['email']
        user.password = request.form['password']
        db.session.add(user)
        db.session.commit()
        return redirect("/")

    return render_template("updateForm.html", user=user)


@app.route("/delete/<sr_no>")
def delete(sr_no):
    user = User.query.get(sr_no)
    db.session.delete(user)
    db.session.commit()
        
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True) 